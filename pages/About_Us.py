import streamlit as st
from helper_functions.utility import check_password

# Do not continue if check_password is not True.  
if not check_password():  
    st.stop()

st.title("About this App")
st.write("This is a Streamlit App that demonstrates how to use the OpenAI API to generate text completions.")
with st.expander(label="How to use this App", expanded=False):
    st.markdown("1. Enter your prompt in the text area.")
    st.markdown("2. Click the Submit button...")
    st.markdown("3. The app will generate a text completion based on your prompt.")
    