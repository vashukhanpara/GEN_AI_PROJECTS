import streamlit as st
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel

model_path = "models/hospital-chatbot-model"

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_path)

# Load base model
base_model = AutoModelForCausalLM.from_pretrained("distilgpt2")

# Load LoRA adapter
model = PeftModel.from_pretrained(base_model, model_path)

# Merge LoRA into base model
model = model.merge_and_unload()

# Create pipeline
pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer
)

# UI
st.title("🏥 Hospital AI Chatbot")

user_question = st.text_input("Ask a question:")

if st.button("Ask"):

    prompt = f"""You are a hospital assistant.

Answer the question in a helpful and complete sentence.
If you don't know the answer, say: "Please contact the hospital reception."

### Question:
{user_question}

### Answer:"""

    result = pipe(
        prompt,
        max_new_tokens=60,
        temperature=0.3,
        do_sample=True,
        top_p=0.9
    )

    output = result[0]["generated_text"]

    # ✅ FIX: keep inside if block
    answer = output.split("### Answer:")[-1].strip()

    st.write(answer)