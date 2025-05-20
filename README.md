# 🎨 Color Detection from Images

A lightweight Streamlit web app that lets you upload an image, pick any pixel, and instantly see the closest named color and its RGB values. Perfect for designers, developers, and accessibility checks.

---

## 📂 Project Structure
├── app.py             # Streamlit application ├── colors.csv         # Dataset of color names and RGB values ├── requirements.txt   # Python dependencies ├── assets/ │   └── screenshot.png # Demo screenshot for this README └── README.md

## 🚀 Quick Start
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the app locally
streamlit run app.py
🖥️ How It Works
1. Upload an image (JPEG or PNG).


2. Select a pixel by clicking the image or adjusting X/Y sliders.


3. The app converts the image to RGB and computes Manhattan distance between the pixel’s RGB and every entry in colors.csv to find the nearest color name.


4. It displays:

Color name

Exact RGB tuple

A swatch filled with that color

---

📊 Dataset (colors.csv)

The CSV ships with 865 common color names and their R,G,B triples. You can expand or replace this palette—just keep the column headers: color_name,R,G,B.
