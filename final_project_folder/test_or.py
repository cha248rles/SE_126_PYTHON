import base64
import csv

# Encode WAV file to base64
def encode_wav(wav_file_path):
    with open(wav_file_path, 'rb') as f:
        return base64.b64encode(f.read()).decode('utf-8')

# Write to CSV
with open('audio_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'audio'])  # Header
    writer.writerow([1, encode_wav('path/to/your/file.wav')])

# Decode base64 back to WAV
def decode_wav(base64_string, output_path):
    with open(output_path, 'wb') as f:
        f.write(base64.b64decode(base64_string))

# Read from CSV and decode
with open('audio_data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip header
    for row in reader:
        decode_wav(row[1], 'output.wav')  # Decode the audio
from playsound import playsound

# Play the audio file
playsound('output.wav')
