import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from model import Model

model = Model(0.01)
model.load_weights()