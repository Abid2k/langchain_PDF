from dotenv import load_dotenv
import os
import streamlit as st

def main():
    load_dotenv()
    st.set_page_config(page_title = "My PDF Reader")
    st.header("My PDF Reader")
    
    pdf = st.file_uploader("Upload your PDF file", type = "pdf")




if __name__ == '__main__':
     main()