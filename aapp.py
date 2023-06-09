import streamlit as st

import joblib

model_nb = joblib.load('Project')
vect = joblib.load('vect.pkl')

def main():
  st.title('Real Time Facial Emotion Detection') #creates a title in web app
  ip = st.text_input('Enter Input') #creates a text box in web app
  if st.button('Check'):
    data=[ip]
    cv=vect.transform(data).toarray()
    prediction=model_nb.predict(cv)
    result=prediction[0]
    if result=='Happy':
      st.success("Happy")
    else:
      st.error("sad")
   
main()  
