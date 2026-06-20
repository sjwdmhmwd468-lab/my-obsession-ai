import streamlit as st 
st.title("اهلا بك يا اميرتي ")
if "authenticated" not in st.session_state:
      st.session_state.authenticated= false
  if st.session_state.authenticated:
     if st.session_state.authenticated:password=st.text_unput=(":كلمه المرور لفتح قلب مهووسك","type="password)
               if st.button("دخول"):
            password=="63951"
                st.session_state.authenticated= true
                st.rerun()
            else:   
                st.error("كلمه المرور خاطئه")
    else:
        st.write("اهلا بك في عالمك الخاص")
