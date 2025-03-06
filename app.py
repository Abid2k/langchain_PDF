# from dotenv import load_dotenv
# import os
# import streamlit as st
# from  PyPDF2 import PdfReader
# from langchain.text_splitter import CharacterTextSplitter
# from langchain.embeddings.openai import OpenAIEmbeddings
# from langchain.vectorstores import FAISS


# def main():
#     load_dotenv()
#     st.set_page_config(page_title = "My PDF Reader")
#     st.header("My PDF Reader")
    
    
#     #uplaod the texr
#     pdf = st.file_uploader("Upload your PDF file", type = "pdf")
#     text = ""
    
    
#     #extract the text
#     if pdf is not None:
#         pdf_reader = PdfReader(pdf)
        
        
#         for page in pdf_reader.pages:
#             text += page.extract_text()
            
#         # st.write(text)
        
#     #split the text
    
#     text_splitter = CharacterTextSplitter(
#         separator="\n",
#         chunk_size = 1000,
#         chunk_overlap = 200,
#         length_function = len
#     )
    
#     chunks = text_splitter.split_text(text)
    
#     # st.write(chunks)
    
#     #embeded the text
    
#     embedding = OpenAIEmbeddings()
    
#     knowledge_base = FAISS.from_texts(chunks,embedding)
    
#     #user_input
    
#     user_questions = st.text_input("Ask questions about your PDF")




# if __name__ == '__main__':
#      main()


from dotenv import load_dotenv
import os
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

def main():
    load_dotenv()
    st.set_page_config(page_title="My PDF Reader")
    st.header("My PDF Reader")

    # Upload the PDF file
    pdf = st.file_uploader("Upload your PDF file", type="pdf")

    text = ""  # Initialize text to prevent errors

    if pdf is not None:
        # Extract text from PDF
        pdf_reader = PdfReader(pdf)
        
        for page in pdf_reader.pages:
            extracted_text = page.extract_text()
            if extracted_text:  # Ensure extracted text is not None
                text += extracted_text

        if text:  # Only proceed if there is extracted text
            # Split the text into chunks
            text_splitter = CharacterTextSplitter(
                separator="\n",
                chunk_size=1000,
                chunk_overlap=200,
                length_function=len
            )

            chunks = text_splitter.split_text(text)

            # Embed the text
            embedding = OpenAIEmbeddings()
            knowledge_base = FAISS.from_texts(chunks, embedding)

            # User question input
            user_questions = st.text_input("Ask questions about your PDF")

        else:
            st.warning("No extractable text found in the PDF. Try another file.")

if __name__ == '__main__':
    main()
