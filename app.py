import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer


nltk.download('punkt')

# Sample data about data2bots
data = {
    "history": "data2bots was founded in 2020...",
    "products": "data2bots offers AI chatbot solutions...",
    "team": "The team at data2bots consists of...",
}

# Predefined intents and keywords
intents = {
    "history": ["history", "founded", "when"],
    "products": ["products", "services", "offerings"],
    "team": ["team", "members", "employees"],
}

def chatbot2(query):
    tokens = word_tokenize(query.lower())
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(token) for token in tokens]

    for intent, keywords in intents.items():
        if any(keyword in stemmed_tokens for keyword in keywords):
            return data[intent]

    return "I couldn't understand your question. Please try rephrasing."

while True:
    query = input("Ask me a question about data2bots: ")
    if query.lower() != "quit":
      response = chatbot2(query)
      st.write(response)
      st.write('Type "quit" to exit')
      
    else:
      break 
    
