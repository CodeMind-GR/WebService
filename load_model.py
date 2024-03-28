import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM

import os

model_id = "roberta-base"
HUGGINGFACE_READ_TOKEN = os.getenv('HUGGINGFACE_READ_TOKEN')

@st.cache(allow_output_mutation=True, show_spinner=True)
def load_LLM_model():
    tokenizer = AutoTokenizer.from_pretrained(model_id, use_auth_token=HUGGINGFACE_READ_TOKEN)
    model = AutoModelForCausalLM.from_pretrained(model_id, use_auth_token=HUGGINGFACE_READ_TOKEN)

    return model, tokenizer
