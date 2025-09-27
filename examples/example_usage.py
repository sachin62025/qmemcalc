from qmemcalc import estimate_memory

result = estimate_memory(
    model_name="NousResearch/Llama-2-7b-chat-hf",
    batch_size=16,
    seq_len=512,
    lora_r=64,
    precision="fp32",
    quantization="4bit",
    optimizer="AdamW",
    gradient_checkpointing=True
)

print("Estimated GPU memory usage:")
for k, v in result.items():
    print(f"{k:<20}: {v}")
