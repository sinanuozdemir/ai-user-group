# The Fine-tuning notebook

We have two Jupyrer notebooks:

1. [Fine-tuning BERT](notebooks/fine_tuning_bert.ipynb) to see how to fine-tune a BERT model to perform QNLI - Question Natural Language Inference
2. [Using T5 off the shelf](notebooks/t5.ipynb) to see how we can use even a 3 year old open source model to solve tasks for us (for free!)

# Streamlit App

This streamlit allows users to input a pair of text inputs - a question and a statement - and uses the model to infer whether the statement is an answer to the question.

## Requirements

You can install required packages using pip:

```bash
pip install -r requirements.txt
```

## Usage
To run the streamlit application:

1. Clone this repository or download the Streamlit app script.
2. In the terminal, navigate to the directory containing the script.
3. Run the command `streamlit run app.py`, replacing app.py with the name of the script if necessary. 

This will start the Streamlit server and open the application in your default web browser.

In the app, you will find two text input fields. Enter your question in the first field and the corresponding statement in the second field, then click the 'Run Model' button to see the model's inference. There are also example buttons which automatically populate the text fields with example question-statement pairs.

### Note
This application uses a fine-tuned BERT model for sequence classification trained in the notebook in the same directory. The model must be loaded from a local directory. Please replace 'ai_user_grp_tmp' in the code with the actual path to your trained model directory.
