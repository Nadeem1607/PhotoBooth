import streamlit as st
from PIL import Image, ImageOps
import io

# Page configuration
st.set_page_config(page_title =  "PhotoBooth", layout = "centered")
st.markdown('''
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Bungee&family=Monoton&display=swap');
        /* Main Background */
        .stApp {
            background-color: #000000;
            background-image: radial-gradient(#1a1a1a 1px, transparent 1px);
            background-size: 20px 20px;
            color: #ffffff;
        }
        /* Headers */
        h1 {
            font-family: 'Monoton', cursive;
            color: #ff00ff;
            text-align: center;
            font-size: 4rem !important;
            text-shadow: 0 0 10px #ff00ff, 0 0 20px #00ffff;
            margin-bottom: 0;
        }
        .status-text {
            font-family: 'Bungee', cursive;
            text-align: center;
            color: #00ffff;
            letter-spacing: 2px;
        }
        /* Target camera input containers */
        [data-testid="stCameraInput"] {
            border: 5px solid #00ffff;
            border-radius: 15px;
            box-shadow: 0 0 20px #00ffff;
        }
        /* Buttons */
        .stButton>button {
            font-family: 'Bungee', cursive;
            border: 3px solid #ff00ff;
            padding: 15px 30px;
            font-size: 20px;
            background: transparent;
            color: #ff00ff;
            transition: 0.3s;
            text-transform: uppercase;
        }
        .stButton>button:hover {
            background: #ff00ff;
            color: white;
            box-shadow: 0 0 30px #ff00ff;
        }
    </style>
''', unsafe_allow_html = True)
st.title("PhotoBooth")

# State management for images
if 'photos' not in st.session_state:
    st.session_state.photos = []

# Capture photos
if len(st.session_state.photos) < 4:
    st.markdown(f"<p class ='status-text'>Get Ready for Photo #{len(st.session_state.photos) + 1} of 4</p>", unsafe_allow_html = True)
    cam_photo = st.camera_input("Smile!", key = f"cam_input_{len(st.session_state.photos)}")
    if cam_photo:
        img = Image.open(cam_photo)
        img = ImageOps.fit(img, (600, 600), Image.Resampling.LANCZOS)
        st.session_state.photos.append(img)
        st.rerun()

else:
    st.markdown("<p class ='status-text'>All photos captured! Choose your vibe.</p>", unsafe_allow_html = True)
    layout = st.radio("Frame Style:", ["Vertical Strip", "PARTY Grid"], horizontal = True)
    border_size = 40
    img_w, img_h = st.session_state.photos[0].size
    # Vertical Strip
    if layout == "Vertical Strip":
        canvas_w = img_w + (2 * border_size)
        canvas_h = (img_h * 4) + (5 * border_size)
        final_img = Image.new('RGB', (canvas_w, canvas_h), (255, 255, 255))
        for i, img in enumerate(st.session_state.photos):
            final_img.paste(img, (border_size, border_size +i * (img_h + border_size)))
    # Party Grid
    else:
        canvas_w = (img_w * 2) + (3 * border_size)
        canvas_h = (img_h * 2) + (3 * border_size)
        final_img = Image.new('RGB', (canvas_w, canvas_h), (255, 255, 255))
        final_img.paste(st.session_state.photos[0], (border_size, border_size))
        final_img.paste(st.session_state.photos[1], (img_w + border_size * 2, border_size))
        final_img.paste(st.session_state.photos[2], (border_size, img_h + border_size * 2))
        final_img.paste(st.session_state.photos[3], (img_w + border_size * 2, img_h + border_size * 2))
    # Display
    st.image(final_img, caption = "Preview", use_container_width = True)

    # Download
    buf = io.BytesIO()
    final_img.save(buf, format = "JPEG")
    col1, col2 = st.columns(2)
    with col1:
        st.download_button("Save Photo", buf.getvalue(), "photobooth.jpg", "image/jpeg")
    with col2:
     if st.button("Restart"):
            st.session_state.photos = []
            st.rerun()