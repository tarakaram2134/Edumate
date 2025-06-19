from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

model_name = "google/flan-t5-large"

print("⏳ Loading FLAN-T5 large...")
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name).to("cuda" if torch.cuda.is_available() else "cpu")

def generate_answer(context, question):
    context = context[:700]
    if "." in context:
        context = context[:context.rfind(".") + 1]

    prompt = f"""You are a helpful teaching assistant. Using the lecture notes below, answer the question in your own words.
Avoid copying sentences directly. Be concise, clear, and include an example if appropriate.
Explain it like you're teaching a student.

### Example:
Question: What is a stack?
Answer: A stack is a linear data structure that follows Last In First Out (LIFO). It's like a stack of plates — you add and remove from the top. The main operations are push (add) and pop (remove).

### Context:
{context}

### Question:
{question}

### Detailed Answer:"""

    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(
        **inputs,
        max_new_tokens=200,           # Increased length for full answers
        do_sample=True,               # Enable some creativity
        temperature=0.8,              # Encourages elaboration
        top_p=0.95,
        pad_token_id=tokenizer.eos_token_id
    )

    output = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return output.strip()

