import whisper
import json
import os
print("📥 Loading model...")
model=whisper.load_model("large-v2")
audios=os.listdir("audios")

for audio in audios:
    #print(audio)
    number=audio.split("-")[0]
    title=audio.split("-")[1][:-4]
    # print(number,title)
    print("🎵 Transcribing...")
    result=model.transcribe(audio=f"audios/{audio}",
                            language="hi",
                            task="translate",
                            word_timestamps=False)

    chunks=[]
    for segment in result["segments"]:
        chunks.append({"number":number,"title":title,"start":segment["start"],"end":segment["end"],"text":segment["text"]})
        chunks_with_metadata={"chunks":chunks,"text":result["text"]}
    
    with open(f"jsons/{audio}.json","w") as f:
        json.dump(chunks_with_metadata,f)    