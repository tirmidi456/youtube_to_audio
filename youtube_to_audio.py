from pytube import YouTube
from moviepy.video.io.VideoFileClip import VideoFileClip
import re

# Ask the user to input a YouTube link
youtube_link = input("Enter the YouTube video link: ")

try:
    # Create a YouTube object for the provided link
    yt = YouTube(youtube_link)

    # Get the highest resolution video stream available
    video_stream = yt.streams.get_highest_resolution()

    # Download the video
    video_filename = re.sub(r'[^\w\s-]', '', yt.title) + ".mp4"
    video_stream.download(filename=video_filename)

    # Convert video to audio
    audio_filename = re.sub(r'[^\w\s-]', '', yt.title) + ".mp3"
    video_clip = VideoFileClip(video_filename)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(audio_filename)

    print(f"Audio file '{audio_filename}' created successfully.")

except Exception as e:
    print(f"An error occurred: {e}")
