import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

model_id = "google/gemma-2b"


@st.cache_resource
def load_LLM_model():
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    tokenizer.padding_side = "left"
    tokenizer.pad_token = tokenizer.eos_token
    tokenizer.truncation = True
    tokenizer.max_length = 128

    model = AutoModelForCausalLM.from_pretrained(model_id)

    return model, tokenizer
