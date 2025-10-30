import requests,ssl
import streamlit as st

url = "https://api.nasa.gov/planetary/apod?api_key="

responce = requests.get(url)

cont = responce.json()

image_url = cont["url"]
image_data = requests.get(image_url).content

with open("image.png","wb")as f:
    f.write(image_data)

st.title("NASA's Astronomy Picture of the Day")
st.image("image.png")
st.caption(cont["explanation"])



st.markdown(f"Photo by NASA | Date: {cont['date']}")
st.markdown(f"[Source]({cont['hdurl']})")
st.markdown("Developed by Your Name")
st.markdown(f"© {cont['date']}{cont['copyright']}")

