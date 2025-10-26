emotion = {
    "SAD": "sample/ref-sad.wav",
    "HAPPY": "sample/ref-happy.wav",
    "SCARED": "sample/ref-scared.wav",
    "DISGUST": "sample/ref-disgust.wav",
    "EXCITED": "sample/ref-excited.wav",
    "ANGRY": "sample/ref-angry.wav",
}  # dict map user input to sound

transcript = {
    "SAD": "sample/ref-sad.txt",
    "HAPPY": "sample/ref-happy.txt",
    "SCARED": "sample/ref-scared.txt",
    "DISGUST": "sample/ref-disgust.txt",
    "EXCITED": "sample/ref-excited.txt",
    "ANGRY": "sample/ref-angry.txt",
}  # dict map input to transcript

scenes = {
    "SAD": (
        "<|scene_desc_start|> "
        "Voiceover booth; low energy; slower pace; softer volume; lower pitch; sad, mournful tone; "
        "<|scene_desc_end|>"
    ),

    "DISGUST": (
        "<|scene_desc_start|> "
        "Voiceover booth; tight, nasal resonance; shortened vowels; disgust; grossed out; subtle exhalations; "
        "<|scene_desc_end|>"
    ),

    "EXCITED": (
        "<|scene_desc_start|> "
        "Voiceover booth; high energy; faster pace; wide pitch variability; bright, smiling tone; "
        "<|scene_desc_end|>"
    ),

    "SCARED": (
        "<|scene_desc_start|> "
        "Voiceover booth; trembling, frightened delivery; hushed volume; tense; irregular, shallow breathing; jittery pace; "
        "cautious"
        "<|scene_desc_end|>"
    ),

    "ANGRY": (
        "<|scene_desc_start|> "
        "Voiceover booth; strong, firm; elevated intensity; forceful emphasis; hard consonants; "
        "short, decisive pauses; downward, final phrase endings. "
        "<|scene_desc_end|>"
    ),

    "HAPPY": (
        "<|scene_desc_start|> "
        "Voiceover booth; warm, cheerful tone; moderately quick pace;"
        "gentle smile audible; light;"
        "subtle upward cadences at phrase ends. "
        "<|scene_desc_end|>"
    ),
}