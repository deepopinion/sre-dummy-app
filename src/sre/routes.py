import hashlib
import io
import os
import time

import requests
from fastapi import APIRouter


IMAGE_URL = (
    "https://www.nasa.gov/wp-content/uploads/2024/10/iss072e034554orig.jpg")
ITERATIONS = 1000


router = APIRouter()


@router.get("/health")
def health() -> dict[str, bool]:
    return {"ok": True}


@router.get("/image-hasher")
def image_hasher() -> dict[str, str]:
    response = requests.get(IMAGE_URL)
    response.raise_for_status()

    buffer = io.BytesIO()

    for i in range(ITERATIONS):
        buffer.write(response.content + os.getrandom(i))

    result = hashlib.sha512(buffer.getvalue()).hexdigest()

    time.sleep(10)

    return {"result": result}
