# PhotoBooth
A fully functional, frontend-focused photobooth application built with Python, Streamlit, and Pillow. Featuring a retro-glitch aesthetic and custom framing.

# Features
- Sequential Capture: Takes 4 distinct photos using session state management.
-  Auto-Crop: Uses ImageOps.fit to ensure a consistent 1:1 aspect ratio for all shots.
-  Funky UI: Black background with neon pink and cyan accents, using Google Fonts (Monoton and Bungee).
- Framing Options: Choose between a classic vertical strip or a 2x2 party grid.
- JPG Export: High-quality download button for the final composition.

# Quick Start
1. Save ![[app.py]] in a virtual environment.
2. Install dependencies:
```Bash
pip install streamlit Pillow
```
3. Run the app:
```Bash
streamlit run app.py
```
