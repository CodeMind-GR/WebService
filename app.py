import streamlit as st

from load_model import load_LLM_model, model_id

# Streamlit 페이지 설정
st.set_page_config(page_title='chatGPT-like Interface', layout='wide')

model, tokenizer = load_LLM_model()


# Generate response from the model
def generate_response(prompt):
    input_ids = tokenizer.encode(prompt, return_tensors="pt")

    # Generate text using the model
    output_sequences = model.generate(
        input_ids=input_ids,
        max_length=1000,  # Adjust max response length as needed
        pad_token_id=tokenizer.eos_token_id
    )

    # Decode the generated text
    response = tokenizer.decode(output_sequences[0], skip_special_tokens=True)
    return response


st.session_state["model"] = model_id

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = generate_response(prompt)
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
