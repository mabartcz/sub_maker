import os
import pathlib
import tempfile
import openai
import ffmpeg
import requests
from requests.structures import CaseInsensitiveDict


openai.api_key = os.getenv("OPENAI_API_KEY")

# file_path = pathlib.Path(r'C:\Users\Martin\source\repos\sub_maker\data\1.wav')
file_path = pathlib.Path(r'C:\Users\Martin\source\repos\sub_maker\data\out.MOV')

output_audio = pathlib.Path(r'C:\Users\Martin\source\repos\sub_maker\sub_maker\audio.wav')

data = ffmpeg.input(file_path)

(
    ffmpeg
    .input(file_path)
    .audio
    .output(str(output_audio), format='wav', **{'ar': '16000'})
    .run(overwrite_output=True, quiet=False)
)

file_size = os.path.getsize(output_audio)/1000000

print("File Size is :", file_size, "MB")
assert file_size < 5, 'Too big file !'


PROMPT = 'The transcript is about firm BTL Medical Technologies and machines EMSCULPT NEO, EXILIS'
audio_file = open(output_audio, "rb")
transcript = openai.Audio.transcribe(model="whisper-1",
                                     file=audio_file,
                                     prompt=PROMPT,
                                     response_format='srt',
                                     language='en')
print(transcript)

pass

