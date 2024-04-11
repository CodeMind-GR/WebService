import os

import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = "google/gemma-2b-it"
HUGGINGFACE_READ_TOKEN = os.getenv('HUGGINGFACE_READ_TOKEN')


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
