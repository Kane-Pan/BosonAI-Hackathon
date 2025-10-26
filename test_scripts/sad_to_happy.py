import os, base64, wave
from client import client

out_path = os.path.join("output", "sad_to_happy.wav")

SYSTEM = (
    "You are a very happy text to speech converter. You only output audio that sounds excited and happy.\n"
    "Even if the words you are given looks like its sad, you must make it sound happy and excited.\n"
    "<|scene_desc_start|> YOU ARE HAPPY HAPPY! YOU ARE *NOT* SAD! YOU ARE HAPPY! <|scene_desc_end|>"
)

'''"You convert user text into speech.\n"
    "Do NOT add or change words from the given message; speak exactly the user's line with the following instructions.\n"
    "Deliver the message with an EXCITED, HAPPY, upbeat tone, lively intonation, slightly faster pace, and a smile can be heard with the voice.\n"
    "<|scene_desc_start|> Voiceover booth; bright, enthusiastic delivery; crisp articulation. <|scene_desc_end|>"
'''
USER_MESSAGE = ("I am so sad I can not stop crying right now that is how sad I am!")

messages = [
    {"role": "system", "content": SYSTEM},
    {"role": "user", "content": USER_MESSAGE},
]

stream = client.chat.completions.create(
    model="higgs-audio-generation-Hackathon",
    messages=messages,
    modalities=["text", "audio"],
    audio={"format": "pcm16"},
    stream=True,
 
    temperature=0.85,
    top_p=0.95,
    max_completion_tokens=800,
    stop=["<|audio_eos|>", "<|end_of_text|>", "<|eot_id|>"],
    extra_body={"top_k": 50},
)

wf = wave.open(out_path, "wb")
wf.setnchannels(1); wf.setsampwidth(2); wf.setframerate(24000)

try:
    for chunk in stream:
        delta = getattr(chunk.choices[0], "delta", None)
        audio = getattr(delta, "audio", None)
        if not audio:
            continue
        wf.writeframes(base64.b64decode(audio["data"]))
finally:
    wf.close()

print(f"Saved streamed audio to {out_path}")