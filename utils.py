def clean_output(response_text):
    # Remove special tokens
    cleaned_text = response_text.replace("<bos>", "").replace("<start_of_turn>", "").replace("<end_of_turn>",
                                                                                             "").replace("<eos>", "")

    # Split the text into user and model parts
    user_text, model_text = cleaned_text.split("model")

    return model_text
