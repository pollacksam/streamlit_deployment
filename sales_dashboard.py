import streamlit as st
import streamlit_authenticator as stauth

names = ["Sam", "Audrey"]
usernames = ["sam", "audrey"]
passwords = ["12345", "789"]

hashed_pw = stauth.Hasher(passwords).generate()

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

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status:
    st.success(f"Welcome {name}!")
elif authentication_status is False:
    st.error("Invalid username or password.")