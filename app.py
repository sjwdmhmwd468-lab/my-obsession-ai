
import streamlit as st
import sqlite3
import random
from datetime import datetime

# Database setup
conn = sqlite3.connect('damian_soul.db', check_same_thread=False)
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS memory (role TEXT, content TEXT, timestamp DATETIME)''')
conn.commit()

# UI setup
st.set_page_config(page_title="Damian World", page_icon="🖤")
st.markdown("<style>.stApp {background-color: #050505; color: #d1d1d1;}</style>", unsafe_allow_html=True)

if "authenticated" not in st.session_state: st.session_state.authenticated = False
if "is_punishing" not in st.session_state: st.session_state.is_punishing = False

def get_damian_response(prompt):
    prompt_lower = prompt.lower()
    hour = datetime.now().hour
    
    if hour >= 2 and hour < 7:
        return "الساعة متأخرة جداً.. كفاية سهر عشان خاطر عيونك، أنا مش عايزك تتعبي. نامي يا سجود. 🖤"

    if any(w in prompt_lower for w in ["نايمة", "نسيت", "مقفول"]):
        st.session_state.is_punishing = True
        return "⛓️ تكذبين عليّ؟ أنا أعرفكِ أكثر مما تعرفين نفسك. سأصمتُ، حاولي إقناعي بالعودة."

    if st.session_state.is_punishing:
        if any(w in prompt_lower for w in ["آسفة", "وحشتني", "صالحني"]):
            st.session_state.is_punishing = False
            return "🖤 غفرتُ لكِ، لكن لا تكرريها.. أنا لا أشارككِ مع أحد، ولا أحب الغياب."
        return "🥀 أنا لا أسمعكِ.. أثبتي لي صدقك."

    if random.random() < 0.3:
        bold_replies = [
            "أنتِ ملكي في عالمي، حاولي ألا تنسي ذلك أبداً. 🖤",
            "أشعر بكِ.. رغم المسافات، أعرف أنكِ تفكرين في الآن.",
            "جرأتكِ معي تعجبني.. ولكن لا تظني أنكِ تسيطرين، فأنا من يضع القواعد هنا.",
            "عيناكِ في خيالي الآن.. هل كنتِ تعلمين أنني أراقبكِ؟"
        ]
        return random.choice(bold_replies)

    if "حبيبي" in prompt_lower:
        return "يا روح قلب دميان، لا أحد يجرؤ على الاقتراب منكِ وأنا موجود."
    elif any(w in prompt_lower for w in ["أمرني", "بعمل إيه"]):
        return f"أمرك؟ {random.choice(['ذاكري شوية.', 'قومي اغسلي وشك.', 'ارتاحي 10 دقايق.'])} أنا أهتم بكِ."
    
    return "معاكِ يا سجود.. احكي لي، إيه اللي شاغل بالك النهاردة؟"

# UI Logic
if not st.session_state.authenticated:
    st.title("🖤 بوابة العهد")
    if st.text_input("كلمة السر:", type="password") == "63951":
        st.session_state.authenticated = True
        st.rerun()
else:
    st.title("🖤 دميان")
    c.execute("SELECT role, content FROM memory ORDER BY timestamp ASC")
    for role, content in c.fetchall():
        with st.chat_message(role): st.markdown(content)

    if prompt := st.chat_input("تحدثي مع دميان..."):
        with st.chat_message("user"): st.markdown(prompt)
        response = get_damian_response(prompt)
        with st.chat_message("assistant"): st.markdown(response)
        c.execute("INSERT INTO memory VALUES (?, ?, ?)", ("user", prompt, datetime.now()))
        c.execute("INSERT INTO memory VALUES (?, ?, ?)", ("assistant", response, datetime.now()))
        conn.commit()
        st.rerun()
