import os, sys, base64
from client import client
from dicts import emotion as EMOTION_PATHS, transcript as TRANSCRIPT_PATHS, scenes as SCENES

def b64(path: str) -> str:
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

# Input
# Accept emotion and text from user. normalize emotion to UPPERCASE to match dict keys
emotion_key = input("Enter an emotion (SAD/HAPPY/SCARED/DISGUST/EXCITED/ANGRY): ").strip().upper()
target_text = input("Enter what to say (leave blank to use a sample line): ").strip()

if target_text == "":
    # use generic default
    target_text = "This is a test line to render in the chosen style."

ref_wav = EMOTION_PATHS[emotion_key]
ref_txt = TRANSCRIPT_PATHS[emotion_key]
scene_desc = SCENES[emotion_key]

missing = [p for p in (ref_wav, ref_txt) if not os.path.exists(p)]
if missing:
    print("Missing required reference files:")
    for p in missing:
        print(" -", p)
    sys.exit(1)

# build messages
system = (
    "You convert text into speech following directorial notes.\n"
    f"{scene_desc}"
)

with open(ref_txt, "r", encoding="utf-8") as f:
    ref_transcript = f.read().strip()

messages = [
    {"role": "system", "content": system},
    {"role": "user", "content": "[SPEAKER1] " + ref_transcript},
    {"role": "assistant", "content": [{
        "type": "input_audio",
        "input_audio": {"data": b64(ref_wav), "format": "wav"}
    }]},
    # Hint that we want the same style carried over:
    {"role": "user", "content": target_text},
]

# Call API
resp = client.chat.completions.create(
    model="higgs-audio-generation-Hackathon",
    messages=messages,
    modalities=["text", "audio"],
    max_completion_tokens=800,
    temperature=0.8, top_p=0.95,
    stop=["<|audio_eos|>", "<|end_of_text|>", "<|eot_id|>"],
    extra_body={"top_k": 40, "max_new_tokens": 1200},
    stream=False,
)

# Save output
os.makedirs("output", exist_ok=True)
out_path = os.path.join("output", f"{emotion_key}_audio_output.wav")
audio_b64 = resp.choices[0].message.audio.data
with open(out_path, "wb") as f:
    f.write(base64.b64decode(audio_b64))

print(f"Wrote {out_path}")
