from transformers import pipeline, AutoTokenizer

model_path = "models/hospital-chatbot-model"

tokenizer = AutoTokenizer.from_pretrained(model_path)

pipe = pipeline(
    "text-generation",
    model=model_path,
    tokenizer=tokenizer
)

prompt = """### Question:
What are hospital visiting hours?

### Answer:
"""
result = pipe(
    prompt,
    max_new_tokens=40,
    temperature=0.2
)
print(result[0]["generated_text"])