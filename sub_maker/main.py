import os
import pathlib
import openai
import ffmpeg

from codetiming import Timer


# CONFIG
PROMPT = 'The transcript is about firm BTL Medical Technologies and machines EMSCULPT NEO, EXILIS'
file_path = pathlib.Path(r'C:\Users\Martin\source\repos\sub_maker\data\out.mov')



# Load OpenAi key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Extract audio from video
output_audio = pathlib.Path(r'audio.mp3')
data = ffmpeg.input(file_path)

(
    ffmpeg
    .input(file_path)
    .audio
    .output(str(output_audio), format='mp3', **{'ac': 1, 'q:a': 6})
    .run(overwrite_output=True, quiet=False)
)

# Check for max audio size
file_size = os.path.getsize(output_audio)/1000000
print("File Size is :", file_size, "MB")
assert file_size < 24, 'Too big file !'


# Call Whisper and create subtitles
audio_file = open(output_audio, "rb")

with Timer(name='Whisper', initial_text='Whisper started!'):
    transcript = openai.Audio.transcribe(model="whisper-1",
                                         file=audio_file,
                                         prompt=PROMPT*10,
                                         response_format='srt',
                                         language='en')

# Save subtitles
f = open(file_path.parent / (file_path.stem + '.srt'), "w")
f.write(transcript)
f.close()

# print(transcript)

pass

# Hi, I'm from BTL medical technologies firm. Our main machines are BTL AmpSculpt Neo, Exilis 2.
# Hi, I'm from BTL Medical Technologies firm. Our main machines are BTL EMSCULPT NEO, EXILIS 2.
