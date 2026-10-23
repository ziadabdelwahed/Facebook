import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="تسجيل الدخول",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown(
    """
    <style>
        .stApp > header {display: none;}
        .block-container {padding: 0 !important; max-width: 100% !important;}
        iframe {width: 100% !important; height: 100vh !important; border: none;}
    </style>
    """,
    unsafe_allow_html=True
)

html_file = Path("index.html")
if html_file.exists():
    st.iframe(html_file, height="stretch", width="stretch")
else:
    st.error("ملف index.html غير موجود. تأكد من وجوده في نفس مجلد app.py.")