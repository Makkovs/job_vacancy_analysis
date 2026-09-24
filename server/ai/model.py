import os
import json
import numpy as np
import pandas as pd

class Model:
    def __init__ (self, weights_num: int = 1): 
        self.bias = 0
        self.weights = np.random.uniform(low=0.0, high=0.1, size=weights_num)

        self.X_min = None
        self.X_range = None
        self.Y_min = None
        self.Y_range = None
        self.feature_columns = []

    def normalize (self, values: np.ndarray) -> np.ndarray:
        values_min = values.min(axis=0)
        values_max = values.max(axis=0)
        values_range = np.where(values_max - values_min == 0, 1.0, values_max - values_min)
        values_norm = (values - values_min) / values_range

        return values_min, values_range, values_norm

    def denormalize (
            self, values: np.ndarray, 
            values_max: float | np.ndarray, values_min: float | np.ndarray
        ) -> np.ndarray:
        return values * (values_max - values_min) + values_min
        
    def forward (self, values: np.ndarray) -> np.ndarray:
        return np.dot(values, self.weights) + self.bias

    def get_loss (self, answers: np.ndarray, predictions: np.ndarray) -> float:
        return np.mean((answers - predictions) ** 2)

    def update_weights (
            self, answers: np.ndarray, values: np.ndarray, 
            predictions: np.ndarray, learning_rate: float
        ):
        error = predictions - answers

        gradient_weights = np.dot(values.T, error) / len(values)
        gradient_bias = np.mean(error)

        self.weights -= learning_rate * gradient_weights
        self.bias -= learning_rate * gradient_bias

    def fit(self, X: pd.DataFrame, Y: pd.Series, iterations: int, learning_rate: float):
        X_raw = X.to_numpy(dtype=np.float64)
        Y_raw = Y.to_numpy(dtype=np.float64).ravel()

        self.X_min, self.X_range, X_norm = self.normalize(X_raw)
        self.Y_min, self.Y_range, Y_norm = self.normalize(Y_raw)

        for i in range(iterations):
            predictions = self.forward(X_norm)    
            loss = self.get_loss(Y_norm, predictions)

            if (i + 1) % 100 == 0 or i == 0:
                print(f"Iteration {i+1}, loss: {loss}")

            self.update_weights(Y_norm, X_norm, predictions, learning_rate)

        self.feature_columns = list(X.columns)

    def predict(self, values: pd.DataFrame) -> np.ndarray:
        values_norm = (values - self.X_min) / self.X_range
        pred_norm = self.forward(values_norm)
        return self.denormalize(pred_norm, self.Y_range, self.Y_min)

    def save_weights(self, filename: str = "weights.json"):
        if self.X_min is None:
            raise ValueError("There is nothing to save! Call fit to train model!")

        data = {
            "weights" : self.weights.tolist(),
            "bias" : self.bias,
            "X_min" : self.X_min.tolist(),
            "X_range" : self.X_range.tolist(),
            "Y_min" : self.Y_min.tolist(),
            "Y_range" : self.Y_range.tolist(),
            "feature_columns" : self.feature_columns
        }

        base_dir = os.path.dirname(os.path.abspath(__file__))
        filepath = os.path.join(base_dir, filename)

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        print("Model was saved")


    def load_weights(self, filename: str = "weights.json"):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        filepath = os.path.join(base_dir, filename)

        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.weights = np.array(data["weights"], dtype=np.float64)
        self.bias = data["bias"]
        self.X_min = np.array(data["X_min"], dtype=np.float64)
        self.X_range = np.array(data["X_range"], dtype=np.float64)
        self.Y_min = data["Y_min"]
        self.Y_range = data["Y_range"]
        self.feature_columns = data["feature_columns"]
