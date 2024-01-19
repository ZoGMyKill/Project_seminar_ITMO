# fastapi_app.py
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
from io import BytesIO
import numpy as np
from PIL import Image

app = FastAPI()

# Это заглушка для модели сегментации, замените её своей моделью
def segment_image(image):
    # Здесь должна быть логика модели машинного обучения
    # Для примера просто возвращаем загруженное изображение
    return image

@app.post("/predict/")
async def create_upload_file(file: UploadFile = File(...)):
    image = Image.open(BytesIO(await file.read()))
    segmented_image = segment_image(image)
    img_byte_arr = BytesIO()
    segmented_image.save(img_byte_arr, format='JPEG')
    return StreamingResponse(BytesIO(img_byte_arr.getvalue()), media_type='image/jpeg')
