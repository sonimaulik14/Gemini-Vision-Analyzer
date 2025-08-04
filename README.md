# Gemini Vision Analyzer 🖼️🔍

This project uses Google's **Gemini Pro Vision API** to analyze images and return intelligent, AI-generated insights. It's a simple Python script that demonstrates how to integrate image understanding capabilities using the `google-generativeai` library.

---

## 🚀 Features

- Upload any image and receive detailed analysis
- Uses Gemini Pro Vision for generative image interpretation
- Simple CLI-based input
- Secure key management with `.env` support

---

## 🧰 Tech Stack

- Python 3.8+
- [Google Generative AI](https://ai.google.dev/)
- `google-generativeai`
- `Pillow` (image processing)
- `python-dotenv`

---

## 🔧 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/gemini-vision-analyzer.git
cd gemini-vision-analyzer
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Create `.env` File

Create a `.env` file and add your Gemini API key:

```env
GOOGLE_API_KEY=your_api_key_here
```

---

## 🖼️ Run the Script

```bash
python vision.py
```

Then, enter the full path of the image you want to analyze.

---

## 📂 Project Structure

```
gemini-vision-analyzer/
├── vision.py          # Main script
├── requirements.txt   # Dependencies
├── .env.example       # Sample environment variable
├── .gitignore         # Ignored files
└── README.md          # This file
```

---

## ✅ Example Use Case

```bash
Enter the image file path: /Users/maulik/Desktop/cat.png

🔍 Gemini Vision Output:

This image shows a cat sitting on a wooden bench with trees in the background...
```

