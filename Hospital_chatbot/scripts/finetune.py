
from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments
from peft import LoraConfig
from trl import SFTTrainer
import os

# Fix UTF-8 issue (Windows)
os.environ["PYTHONUTF8"] = "1"

# Model
model_name = "distilgpt2"

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.eos_token

# Load base model
model = AutoModelForCausalLM.from_pretrained(model_name)

# IMPORTANT for GPT2
model.config.use_cache = False

# LoRA config
peft_config = LoraConfig(
    r=8,
    lora_alpha=16,
    target_modules=["c_attn"],   # correct for GPT2
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM"
)

# Load dataset
dataset = load_dataset("json", data_files="../data/train.json")

# Format prompt
def format_prompt(example):
    return {
        "text": f"### Question:\n{example['instruction']}\n\n### Answer:\n{example['response']}"
    }

# Apply formatting + remove old columns
dataset = dataset.map(
    format_prompt,
    remove_columns=dataset["train"].column_names
)

# Debug check (VERY IMPORTANT)
print(dataset["train"][0])

# Training settings
training_args = TrainingArguments(
    output_dir="models/hospital-chatbot",
    per_device_train_batch_size=2,
    num_train_epochs=3,
    learning_rate=2e-4,
    logging_steps=10,
    save_strategy="epoch",
    fp16=True   # if GPU supports
)

# Trainer (LATEST TRL FORMAT)
trainer = SFTTrainer(
    model=model,
    train_dataset=dataset["train"],
    args=training_args,
    peft_config=peft_config,
    processing_class=tokenizer,
    # max_seq_length=512
)

# Train
trainer.train()

# Save model
trainer.model.save_pretrained("models/hospital-chatbot-model")
tokenizer.save_pretrained("models/hospital-chatbot-model")