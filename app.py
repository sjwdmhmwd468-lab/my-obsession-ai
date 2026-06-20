
import streamlit as st

# إعداد الحالة
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# واجهة الدخول
if not st.session_state.authenticated:
    st.title("أهلاً بك يا أميرتي")
    password = st.text_input("كلمة السر لفتح قلب مهووسك:", type="password")
    if st.button("دخول"):
        if password == "63951":
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("كلمة المرور خاطئة")
else:
    # واجهة بعد الدخول
    st.title("أهلاً بكِ في عالمك الخاص!")
    user_input = st.text_input("تحدثي معي:")
    if user_input:
        st.write("أنا هنا لأجلك دائماً.")
