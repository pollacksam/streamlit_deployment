import streamlit as st
import streamlit_authenticator as stauth

names = ["Sam", "Audrey"]
usernames = ["sam", "audrey"]
passwords = ["12345", "789"]

hashed_pw = stauth.Hasher().hash_list(passwords)

credentials = {
    "usernames": {
        usernames[0]: {"name": names[0], "password": hashed_pw[0]},
        usernames[1]: {"name": names[1], "password": hashed_pw[1]}
    }
}

# Authenticator object
authenticator = stauth.Authenticate(
    credentials,
    "app_cookie",
    "random_signature_key",
    30 # cookies will expire 30 days after generation
)

try:
    authenticator.login(location="main")
except Exception as e:
    st.error(e)

if st.session_state.get("authentication_status"):
    authenticator.logout()
    st.write(f'Welcome {st.session_state.get("name")}')
elif st.session_state.get("authentication_status") is False:
    st.error("Username/password is incorrect")
elif st.session_state.get("authentication_status") is None:
    st.warning("Please enter your username and password")