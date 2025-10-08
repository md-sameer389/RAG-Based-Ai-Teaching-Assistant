

import whisper

print("📥 Loading model...")
model = whisper.load_model("large-v2")   # try "base" first, much faster than large-v2

print("🎵 Transcribing...")
result = model.transcribe(audio="audio/12.mp3",
                          language="hi",
                          task="translate")

print("✅ Done!")
print(result["text"])
