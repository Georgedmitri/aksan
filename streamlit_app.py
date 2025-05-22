import streamlit as st

st.title("🎈Mauricitarumboys")
st.write(
    "Kenapa rambut mauri kayak jamur busuk"
)
st.image("ebe378cc-d715-4ffe-84b2-ad19d7205c54.jpeg")
st.header("Aplikasi Mengecek Nilai Genap/Ganjil")
angka = st.number_input("Tulis sebuah Angka:", value=0, step=1)

if (angka %2) == 0:
    st.write(f"{angka} adalah Bilangan Genap")
else:
    st.write(f"{angka} adalah Bilangan Ganjil")
