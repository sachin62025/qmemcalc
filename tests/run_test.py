from qmemcalc import estimate_memory

result = estimate_memory(
    model_name="sshleifer/tiny-gpt2",
    batch_size=2,
    seq_len=16,
    lora_r=4,
    precision="fp16",
    quantization="none",
    optimizer="adamw",
    gradient_checkpointing=True,
    gpu_vram_MB=4096
)

print("Test Memory Estimation:")
for k, v in result.items():
    print(f"{k:<30}: {v}")
