import streamlit as st

st.title("أهلاً بك يا أميرتي")

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    password = st.text_input("كلمة السر لفتح قلب مهووسك:", type="password")
    if st.button("دخول"):
        if password == "63951":
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("كلمة المرور خاطئة")
else:
    st.write("أهلاً بكِ في عالمك الخاص!")
