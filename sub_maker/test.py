import io

audio_stream, _ = (
    ffmpeg
    .input(file_path)
    .audio
    .output('-', format='wav')
    .run(capture_stdout=True)
)
audio_bytes = io.BytesIO(audio_stream)
file_size = audio_bytes.getbuffer().nbytes/1000000

temp = tempfile.NamedTemporaryFile()
temp.close()