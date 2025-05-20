import streamlit as st
import pandas as pd
import cv2
from PIL import Image
import numpy as np

# Load color dataset
df = pd.read_csv("colors.csv")

# Function to get closest color name
def get_color_name(R, G, B):
    minimum = float("inf")
    cname = "Unknown"
    for i in range(len(df)):
        d = abs(R - int(df.loc[i, "R"])) + abs(G - int(df.loc[i, "G"])) + abs(B - int(df.loc[i, "B"]))
        if d < minimum:
            minimum = d
            cname = df.loc[i, "color_name"]
    return cname

st.title("🎨 Color Detection from Image")

# Upload image
uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Display image
    st.image(img_rgb, caption="Uploaded Image", use_container_width=True)

    st.markdown("📌 Select a point on the image (use sliders below):")
    
    # Use sliders for selecting pixel coordinates
    x = st.slider("X-coordinate", 0, img.shape[1] - 1, img.shape[1] // 2)
    y = st.slider("Y-coordinate", 0, img.shape[0] - 1, img.shape[0] // 2)

    # Get color at selected pixel
    b, g, r = img[y, x]
    r, g, b = int(r), int(g), int(b)
    color_name = get_color_name(r, g, b)

    # Show result
    st.markdown(f"### 🎯 Detected Color: {color_name}")
    st.markdown(f"**RGB Values:** ({r}, {g}, {b})")
    st.markdown(
        f"<div style='width:100px;height:50px;border:1px solid #000;background-color:rgb({r},{g},{b});'></div>",
        unsafe_allow_html=True
    )
