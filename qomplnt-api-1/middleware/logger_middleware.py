# middleware.py
from fastapi import Request

from logger import logger
import time

async def measure_time(request: Request, call_next):
    start_time = time.time()

    response = await call_next(request)

    end_time = time.time()
    elapsed_time = end_time - start_time

    logger.info(f"Endpoint {request.url.path} executed in {elapsed_time:.5f} seconds")

    return response
