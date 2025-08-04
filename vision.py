from dotenv import load_dotenv
load_dotenv()  # Load environment variables

import streamlit as st
import os
import google.generativeai as genai

# ✅ Configure Gemini API with your API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# ✅ Use a supported Gemini model (multimodal)
model = genai.GenerativeModel("gemini-2.5-flash")  # or use "gemini-2.5-pro" if needed

def get_gemini_response(input_text, uploaded_file):
    uploaded_file.seek(0)
    image_bytes = uploaded_file.read()

    # Detect MIME type
    if uploaded_file.name.endswith(("jpg", "jpeg")):
        mime_type = "image/jpeg"
    elif uploaded_file.name.endswith("png"):
        mime_type = "image/png"
    else:
        raise ValueError("Unsupported image type.")

    # Gemini expects a list with dict format for image
    image_part = {
        "mime_type": mime_type,
        "data": image_bytes
    }

    # Prompt with or without text
    if input_text:
        response = model.generate_content([input_text, image_part])
    else:
        response = model.generate_content([image_part])

    return response.text

# ✅ Streamlit UI
st.set_page_config(page_title="Gemini Vision App")
st.header("🔍 Gemini 2.5 Multimodal Demo")

input_text = st.text_input("Enter a prompt (optional):")
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

if st.button("Analyze Image"):
    if uploaded_file:
        try:
            response = get_gemini_response(input_text, uploaded_file)
            st.subheader("🧠 Gemini Response:")
            st.write(response)
        except Exception as e:
            st.error(f"❌ Error: {e}")
    else:
        st.warning("⚠️ Please upload an image before submitting.")
