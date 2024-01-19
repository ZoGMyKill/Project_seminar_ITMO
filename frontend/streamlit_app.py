# streamlit_app.py
import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# Путь к изображению внутри вашей папки проекта
header_image_path = "/home/aat71/Desktop/Proj_sem/frontend/header.png"

# Вставьте изображение как шапку сайта
st.image(header_image_path, use_column_width=True)

st.title('Загрузка изображения для обработки')

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

