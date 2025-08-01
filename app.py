import streamlit as st
from PIL import Image

st.set_page_config(page_title="Muffinie.ia", layout="centered")

st.title("🧁 Muffinie.ia - Demo de prueba")

st.write("Bienvenida a la versión demo de Muffinie.ia. Sube tu imagen para probar el análisis visual.")

uploaded_file = st.file_uploader("📸 Sube tu foto aquí", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Tu imagen subida", use_column_width=True)
    st.success("Imagen cargada correctamente. Aquí es donde aparecería el análisis 👀.")
else:
    st.info("Aún no has subido ninguna imagen.")