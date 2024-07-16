import streamlit as st

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db



# Fetch the service account key JSON file contents
cred = credentials.Certificate('secrets.json')

# Initialize the app with a service account, granting admin privileges
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://test-py-1ff5b-default-rtdb.firebaseio.com'
})

score=0
if st.button("결과 확인"):
    if st.session_state.result1 == 50:
        st.write("첫 번째 답이 맞습니다!")
        score += 50
    else:
        st.write("첫 번째 답이 틀렸습니다!")

    if st.session_state.result2 == 50:
        st.write("두 번째 답이 맞습니다!")
        score += 50
    else:
        st.write("두 번째 답이 틀렸습니다!")
    st.write(f"{score}점 입니다")  