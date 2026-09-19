import numpy as np
import pandas as pd

class Model:
    def __init__ (self, learning_rate: float, values: pd.DataFrame, answers: pd.Series | pd.DataFrame):
        self.values = values
        self.answers = answers

        values_raw = values.to_numpy(dtype=np.float64)
        answers_raw = answers.to_numpy(dtype=np.float64).ravel()

        self.x_min = values_raw.min(axis=0)
        self.x_max = values_raw.max(axis=0)
        self.range_x = np.where(self.x_max - self.x_min == 0, 1.0, self.x_max - self.x_min)
        self.values = (values_raw - self.x_min) / self.range_x

        self.y_min = answers_raw.min(axis=0)
        self.y_max = answers_raw.max(axis=0)
        range_y = 1.0 if self.y_max == self.y_min else (self.y_max - self.y_min)
        self.answers = (answers_raw - self.y_min) / range_y

        self.bias = 0
        self.learning_rate = learning_rate
        self.weights = np.random.uniform(low=0.0, high=0.1, size=self.values.shape[1])

    def forward (self, values = None) -> np.ndarray:
        values = values if values is not None else self.values
        return np.dot(values, self.weights) + self.bias

    def get_loss (self, predictions) -> float:
        return np.mean((self.answers - predictions) ** 2)

    def update_weights (self, predictions):
        error = predictions - self.answers

        gradient_weights = np.dot(self.values.T, error) / len(self.values)
        gradient_bias = np.mean(error)

        self.weights -= self.learning_rate * gradient_weights
        self.bias -= self.learning_rate * gradient_bias

    def fit(self, iterations):
        for i in range(iterations):
            predictions = self.forward()
            loss = self.get_loss(predictions)

            if (i + 1) % 100 == 0 or i == 0:
                print(f"Iteration {i+1}, loss: {loss}")

            self.update_weights(predictions)

    def denormalize_y (self, y: np.ndarray) -> np.ndarray:
        return y * (self.y_max - self.y_min) + self.y_min

    def predict(self, values: pd.DataFrame) -> np.ndarray:
        values_raw = values.to_numpy(dtype=np.float64)
        values_norm = (values_raw - self.x_min) / self.range_x

        y_pred_norm = self.forward(values_norm)
        return self.denormalize_y(y_pred_norm)