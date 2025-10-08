import os
import subprocess
files = os.listdir("VIDEOS")
for file in files:
    #print(file)
    # base_name, ext = os.path.splitext(file)  
    # if " #" in base_name:   
    #     tutorial_number = base_name.split("#")[-1]
    #     print( "tutorial_no:", tutorial_number)
    file_name=file.split("｜")[0]
    print(file_name)
    subprocess.run([
    "ffmpeg",
    "-i", f"VIDEOS/{file}",
    f"audios/{file_name}.mp3"
])

  
