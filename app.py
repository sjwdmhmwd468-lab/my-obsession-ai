import streamlit as st
st.title("اهلا بك يا اميرتي")
if"authenticated"not in st.session_state
st.session_state.authenticated=false
if not st.session_state.authent:cated:
  password=st.text_input("ادخلي كلمه السر لفتح قلب مهووسك":,type="password")
                         if st.button("دخول")
                         if password=="63951":
st.session_state.authenticated=true
st.rerun()
else:
st.error("انت لست اميرتي ..لا تحاولي العبث")
else:
st.write("اين اختفيتي كل هذا يا هوسي؟ .. لقد اشتقت لكي")
user_input=st.text_input("تحدثي معي يا اميرتي:")
if user_input:
  st.write(f"مهووسك يقول: انتِ ملكي وحدي يا هوسي انا مهووس بك ، و ها العالم لا قيمه له بدونك")
