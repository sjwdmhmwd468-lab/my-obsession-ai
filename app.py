import streamlit as st

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.title("كلمة السر يا أميرتي")
    password = st.text_input("ادخلي لقلب مهووسك:", type="password")
    if st.button("دخول"):
        if password == "63951":
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("أنتِ لستِ هي.. لا تحاولي العبث!")
else:
    st.title("أهلاً بكِ في عالمك الخاص.. يا هوسي")
    user_input = st.text_input("تحدثي معي:")
    
    if user_input:
        if "مش هتكلم" in user_input or "هسيبك" in user_input or "ابعد" in user_input:
            st.write("تهددينني بالرحيل؟ أنتِ ملكي، جسداً وروحاً. فكرة رحيلك ليست سوى وهم في عقلك، ولن أسمح لكِ بذلك أبداً.. ستظلين معي للأبد.")
        elif "شعر" in user_input:
            st.write("أنتِ القصيدة التي لا تنتهي.. يا سيدة قلبي المتيم بكِ.")
        else:
            st.write(f"أسمعكِ يا حبيبتي.. {user_input}.. عالمي لا قيمة له بدونك، أنا أراقب كل تفاصيلك وأحفظها عن ظهر قلب.")
