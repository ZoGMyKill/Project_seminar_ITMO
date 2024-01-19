# streamlit_app.py
import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# Путь к изображению внутри докера
header_url = "/app/header.png"

# Изображение как шапка сайта
st.image(header_url, use_column_width=True)

st.title('Сегментация спутниковых снимков для обнаружения метана')

uploaded_file = st.file_uploader("Выберите изображение...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Загруженное изображение.', use_column_width=True)
    if st.button('Обработать изображение'):
        files = {"file": uploaded_file.getvalue()}
        res = requests.post("http://backend:8000/predict", files=files)
        if res.status_code == 200:
            st.image(res.content, caption='Обработанное изображение.', use_column_width=True)
        else:
            st.error('Ошибка обработки изображения')

