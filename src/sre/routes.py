import hashlib
import io
import logging
import os
import time
from typing import Any

import pandas as pd
import requests
from fastapi import APIRouter


IMAGE_URL = (
    "https://www.nasa.gov/wp-content/uploads/2024/10/iss072e034554orig.jpg")
ITERATIONS = 500


router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/health")
def health() -> dict[str, bool]:
    return {"ok": True}


@router.get("/image-hasher")
def image_hasher() -> dict[str, Any]:
    logger.info("Starting to hash stuff")
    response = requests.get(IMAGE_URL)
    response.raise_for_status()

    buffer = io.BytesIO()
    randomized: list[bytes] = []

    for i in range(ITERATIONS):
        iteration_random = response.content + os.getrandom(i)
        buffer.write(iteration_random)
        randomized.append(iteration_random)

    overall_hash = hashlib.md5(buffer.getvalue()).hexdigest()
    df = pd.DataFrame({
        "randomized": [hash(r) for r in randomized],
    })

    time.sleep(5)

    logger.info("Hashed all the stuff")

    return {
        "overall_hash": overall_hash,
        "dataframe": df.to_dict(),
    }
