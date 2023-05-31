import streamlit as st
from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer

# Load the fine-tuned model and tokenizer
fine_tuned_model = AutoModelForSequenceClassification.from_pretrained('notebooks/ai_user_grp_tmp')
tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')

# Create a pipeline for text classification
pipe = pipeline("text-classification", model=fine_tuned_model, tokenizer=tokenizer)

# Set up the Streamlit app title and user input fields
st.title("BERT Cross Encoding App for QNLI")
text1 = st.text_input("Enter your question:", "What is the Capital of France?")
text2 = st.text_input("Enter your statement:", "Paris is the capital of France.")

# Run the model when the user clicks the button
if st.button('Run Model'):
    # Pass the user inputs to the pipeline for classification
    result = pipe([{"text": text1, "text_pair": text2}])
    # Display the result and score
    st.write(f"Result: {result[0]['label']}")
    st.write(f"Score: {result[0]['score']}")
