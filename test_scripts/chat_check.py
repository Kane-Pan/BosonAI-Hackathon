from client import client

resp = client.chat.completions.create(
    model="Qwen3-14B-Hackathon",
    messages=[
        {"role":"system","content":"You are a helpful assistant."},
        {"role":"user","content":"Reply with exactly: READY"}
    ],
    max_tokens=8,
    temperature=0
)

print(resp.choices[0].message.content)
