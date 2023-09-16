from pytube import YouTube

# Replace 'VIDEO_URL' with the URL of the YouTube video you want to download.
video_url = 'VIDEO_URL'

# Create a YouTube object
yt = YouTube(video_url)

# Select the best audio stream
audio_stream = yt.streams.filter(only_audio=True).first()

# Define the output file path
output_path = '/path/to/save/audio.mp3'

# Download the audio stream
audio_stream.download(output_path=output_path)

print(f"Audio downloaded to {output_path}")
