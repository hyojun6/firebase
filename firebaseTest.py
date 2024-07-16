import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json
import streamlit as st

key_dict = json.loads(st.secrets["textkey"])

# Fetch the service account key JSON file contents
cred = credentials.Certificate(key_dict)

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://test-py-1ff5b-default-rtdb.firebaseio.com'
})

ref = db.reference('led')
print(ref.get())

ref2 = db.reference()
ref2.set({"main":"123"})

ref3 = db.reference()
ref3.update({"main":"2135"})

ref3.update({"ex":"test"})