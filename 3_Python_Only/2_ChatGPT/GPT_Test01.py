from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch

# Load the pre-trained model
model = GPT2LMHeadModel.from_pretrained("gpt2")
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")


# Fine-tune on your dataset
for i in range(num_epochs):
    for j in range(0, len(text_data), batch_size):
        # Prepare input and target
        input_ids = tokenizer.batch_encode_plus(text_data[j:j+batch_size], return_tensors="pt")["input_ids"]
        labels = input_ids.clone()
        labels[:, :-1] = input_ids[:, 1:]

        # Forward pass
        outputs = model(input_ids=input_ids, labels=labels)
        loss = outputs[0]

        # Backward pass and optimization
        loss.backward()
        optimizer.step()

# Save the fine-tuned model
model.save_pretrained("finetuned_gpt2")

