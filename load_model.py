from os import environ as env

import streamlit as st
import torch
from dotenv import find_dotenv, load_dotenv
from transformers import AutoTokenizer, AutoModelForCausalLM

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

model_id = "google/gemma-2b-it"
HUGGINGFACE_READ_TOKEN = env.get('HUGGINGFACE_READ_TOKEN')


@st.cache_resource
def load_llm_model():
    tokenizer = AutoTokenizer.from_pretrained(model_id, use_auth_token=HUGGINGFACE_READ_TOKEN)
    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        use_auth_token=HUGGINGFACE_READ_TOKEN,
        torch_dtype=torch.bfloat16,
        revision="float16",
    )

    return model, tokenizer
