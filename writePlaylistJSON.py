import os
import json

# Directory path where your music files are located
music_dir = dir+'/media/music'

# Get a list of music file names in the directory
music_files = [file for file in os.listdir(music_dir) if file.endswith(('.mp3', '.wav', '.flac'))]

# Create a dictionary to store the music file names
music_data = {
    'allMusics': music_files
}

# Define the path for the JSON file
json_file_path = dir+'/settings/playlist.json'

# Write the data to the JSON file
with open(json_file_path, 'w') as json_file:
    json.dump(music_data, json_file, indent=4)

print(f"JSON file with music names saved at {json_file_path}")
