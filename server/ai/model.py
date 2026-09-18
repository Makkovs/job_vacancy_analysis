import numpy as np
import pandas as pd

class Model:
    def __init__ (self, learning_rate: int, values: pd.DataFrame, answers: pd.Series | pd.DataFrame):
        self.values = values
        self.answers = answers

        self.bias = 5
        self.learning_rate = learning_rate
        self.weights = np.random.uniform(low=0.5, high=1, size=self.values.shape[1])

    def forward (self):
        return np.dot(self.values, self.weights) + self.bias