import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

# إعدادات الصفحة (إخفاء القوائم الجانبية)
st.set_page_config(
    page_title="تسجيل الدخول",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# إخفاء واجهة Streamlit الافتراضية (الهيدر والبادينج) عشان الصفحة تظهر كاملة
st.markdown(
    """
    <style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        .block-container {padding: 0 !important; max-width: 100% !important;}
    </style>
    """,
    unsafe_allow_html=True
)

# البحث عن ملف الـ HTML وقراءته
html_file = Path("index.html")

if html_file.exists():
    # قراءة محتوى الملف
    html_content = html_file.read_text(encoding="utf-8")
    
    # عرض المحتوى داخل iframe مع تحديد الارتفاع والعرض
    components.html(html_content, height=900, scrolling=True)
else:
    st.error("خطأ: ملف index.html غير موجود! تأكد من رفعه بجانب app.py")
