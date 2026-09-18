import os
import sys
import asyncio
import numpy as np
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from data_format import get_formatted_jobs
from model import Model

answers, values = asyncio.run(get_formatted_jobs())

model = Model(0.01, values, answers)

