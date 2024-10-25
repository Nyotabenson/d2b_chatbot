import streamlit as st
import tensorflow
import transformers
from transformers import pipeline
chatbot = pipeline("question-answering")


info = '''Data2Bots is an IT consulting company committed to providing our clients with cutting-edge and effective data solutions and strategies 
to improve client's business productivity. Through a fusion of technological innovation, we foster lasting impact and sustainable growth.'''

def chatbots():
    while True:
      quiz = str(input("Ask a question: "))
      result = chatbot(question=quiz, context=info)
      print(result['answer'])
      print('Type "quit" to exit')
      if quiz == "quit":
        break

    else :
      print("Hello! I be back soon") 