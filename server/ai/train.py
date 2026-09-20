import asyncio

from model import Model
from data_format import get_formatted_jobs

answers, values = asyncio.run(get_formatted_jobs())

model = Model(0.01, values.shape[1])

model.fit(values, answers, 1000)
model.save_weights()