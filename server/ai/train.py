import asyncio

from model import Model
from data_format import get_formatted_jobs

answers, values = asyncio.run(get_formatted_jobs())

model = Model(values.shape[1])

model.fit(values, answers, 1000, 0.01)
model.save_weights()