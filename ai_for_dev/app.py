import streamlit as st
from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer

fine_tuned_model = AutoModelForSequenceClassification.from_pretrained('notebooks/ai_user_grp_tmp')
tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
pipe = pipeline("text-classification", model=fine_tuned_model, tokenizer=tokenizer)

st.title("BERT Cross Encoding App for QNLI")

text1 = st.text_input("Enter your question:", "What is the Capital of France?")
text2 = st.text_input("Enter your statement:", "Paris is the capital of France.")

if st.button('Run Model'):

    result = pipe([{"text": text1, "text_pair": text2}])
    st.write(f"Result: {result[0]['label']}")
    st.write(f"Score: {result[0]['score']}")
