from transformers import AutoModelForCausalLM, AutoTokenizer

def initialize_chatbot(data):
    # Load a pre-trained language model (e.g., GPT-2)
    model_name = "gpt2"
    model = AutoModelForCausalLM.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Fine-tune the model on the GitLab data (simplified example)
    # In practice, you'd need more sophisticated fine-tuning
    for chunk in data:
        inputs = tokenizer(chunk, return_tensors="pt", truncation=True, max_length=512)
        model(**inputs)

    return model, tokenizer

def get_response(model, tokenizer, user_input):
    # Generate a response based on user input
    inputs = tokenizer.encode(user_input, return_tensors="pt")
    outputs = model.generate(inputs, max_length=100, num_return_sequences=1)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response
