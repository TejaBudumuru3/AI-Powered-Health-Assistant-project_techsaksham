import streamlit as st
import nltk
from transformers import pipeline
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


chatbot = pipeline("text-generation", model="distilgpt2")


def bot(userinput):
    response = chatbot(userinput, max_length=500, num_return_sequences=1, truncation=True)
    print(response)
    return response[0]["generated_text"]


def main():
    st.title("Healthcare Chatbot")
    userInput = st.text_input("how may I assisst you?")
    if st.button("Submit"):
        if userInput:
            st.write("User:  ",userInput)
            with st.spinner("please wait..."):
                response = bot(userInput)
            st.write("bot:  ",response)
        else:
            st.write("please enter a messege")

main()#streamlit run ./app.py