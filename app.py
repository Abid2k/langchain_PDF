from dotenv import load_dotenv
import os
import streamlit as st
from  PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
# from langchain_openai import OpenAI
from langchain_google_genai import ChatGoogleGenerativeAI



def main():
    load_dotenv()
    
    google_api_key = os.getenv("GEMENI_API_KEY")
    if not google_api_key:
      st.error("API KEY NOT FOUND")
      return

    
    st.set_page_config(page_title="Ask your PDF")
    st.header("Ask your PDF ")
    
    # upload file
    pdf = st.file_uploader("Upload your PDF", type="pdf")
    
    # extract the text
    if pdf is not None:
      pdf_reader = PdfReader(pdf)
      text = ""
      for page in pdf_reader.pages:
        text += page.extract_text()
        
      # split into chunks
      text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
      )
      chunks = text_splitter.split_text(text)
      
      # create embeddings
      # embeddings = OpenAIEmbeddings()
      embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001",api_key=google_api_key)
      knowledge_base = FAISS.from_texts(chunks, embeddings)

      user_question = st.text_input("Ask question about your pdf here")
      
      if user_question:
        docs = knowledge_base.similarity_search(user_question)
        # st.write(docs)
        
        # llm = OpenAi()
        llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=google_api_key)
        chain = load_qa_chain(llm, chain_type="stuff")
        responce = chain.run(input_documents=docs, questions=user_question)
        
        st.write(responce)
      
if __name__ == '__main__':
     main()



