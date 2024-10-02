# filename: utility.py
import streamlit as st  
import random  
import hmac  
import os
from dotenv import load_dotenv
  
# """  
# This file contains the common components used in the Streamlit App.  
# This includes the sidebar, the title, the footer, and the password check.  
# """  

# if load_dotenv('.env'):
#   app_password = os.getenv('password')
#else:
#   app_password = st.secrets['password']

app_password = st.secrets.get('password',False)
if not app_password:
   app_password = os.getenv('password')
  

def check_password():  
    """Returns `True` if the user had the correct password."""  
    def password_entered():  
        """Checks whether a password entered by the user is correct."""  
        if hmac.compare_digest(st.session_state["password"], app_password):  
            st.session_state["password_correct"] = True  
            del st.session_state["password"]  # Don't store the password.  
        else:  
            st.session_state["password_correct"] = False  
    # Return True if the passward is validated.  
    if st.session_state.get("password_correct", False):  
        return True  
    # Show input for password.  
    st.text_input(  
        "Password", type="password", on_change=password_entered, key="password"  
    )  
    if "password_correct" in st.session_state:
        st.error("😕 Password incorrect")  
    return False
