import yt_dlp
import cv2
import subprocess
from openai import OpenAI
import json
import math
import re
import os
from os import listdir
import random
from youtube_transcript_api import YouTubeTranscriptApi
from os.path import isfile, join
from moviepy.editor import VideoFileClip, clips_array

api_key = 'YOUR API KEY'  
client = OpenAI(api_key=api_key)

def download_video(url, filename, output_folder):
    ydl_opts = {
        'format': 'best',
        'outtmpl': f'{output_folder}/{filename}.%(ext)s'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def segment_video(response,file_name,video_directory,output_folder):
  response = json.loads(response)
  custom_name = f'{video_directory}/{file_name}.mp4'
  for i, segment in enumerate(response):
        start_time = math.floor(float(segment.get("start_time", 0)))
        end_time = math.ceil(float(segment.get("end_time", 0))) + 2
        output_file = f"{output_folder}/output{str(i).zfill(3)}.mp4"
        command = f"ffmpeg -i {custom_name} -ss {start_time} -to {end_time} -c copy {output_file}"
        subprocess.call(command, shell=True)

def create_spam_video(main_video_path, spam_folder_path, output_path):
    
    main_video = VideoFileClip(main_video_path)
    main_video_width = main_video.size[0]
    main_video_height = main_video.size[1]
    
    
    spam_videos = [f for f in listdir(spam_folder_path) if isfile(join(spam_folder_path, f))]
    
    
    spam_video_path = join(spam_folder_path, random.choice(spam_videos))
    spam_video = VideoFileClip(spam_video_path)
    resized_spam_video = spam_video.resize(newsize=(main_video_width, main_video_height))

    
    combined_clip = clips_array([[main_video], [resized_spam_video]])
    final_aspect_ratio = 9/16
    final_video = combined_clip.resize(height=combined_clip.h)
    final_width = int(final_video.h * final_aspect_ratio)
    final_video = final_video.resize(width=final_width)
    
    final_video = final_video.set_duration(main_video.duration).set_audio(main_video.audio)

    
    final_video.write_videofile(output_path, codec='libx264')


def adjust_video_dimensions(input_file, output_file, new_width, new_height,spam_folder):
    
    cap = cv2.VideoCapture(input_file)

    
    original_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    original_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_file, fourcc, 30, (new_width, new_height))

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        
        resized_frame = cv2.resize(frame, (new_width, new_height))

        
        out.write(resized_frame)

    
    cap.release()
    out.release()

def get_transcript(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    formatted_transcript = ''
    for entry in transcript:
        start_time = "{:.2f}".format(entry['start'])
        end_time = "{:.2f}".format(entry['start'] + entry['duration'])
        text = entry['text']
        formatted_transcript += f"{start_time} --> {end_time} : {text}\n"
    return transcript

response_obj='''[
  {
    "start_time": 97.19, 
    "end_time": 127.43,
    "duration":36 
  },
  {
    "start_time": 169.58,
    "end_time": 199.10,
    "duration":33 
  },
]'''
import re

def extract_json_from_text(text):
    pattern = r"```json(.*?)```"

    
    matches = re.search(pattern, text, re.DOTALL)

    
    if matches:
        return matches.group(1).strip()
    return text

def analyze_transcript(transcript,duration):
    prompt = f"This is a transcript of a video. Please identify the 5 most viral sections from the whole to TIKTOK, make sure they are more than {duration} seconds in duration,Make Sure you provide extremely accurate timestamps respond only in this format {response_obj} without any other comments \n Here is the Transcription:\n{transcript}"
    messages = [
        {"role": "system", "content": "You are a helpful assistant. Identify the most interesting and viral content from YouTube transcripts."},
        {"role": "user", "content": prompt}
    ]
    response = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=messages,
        max_tokens=512,
        n=1,
        stop=None

    )
    return response.choices[0].message.content

def cropper(video_directory,output_folder,duration,current_directory):
    with open('ytb_vid_to_dl.txt', 'r') as file:
        lines = file.readlines()

    try:
        print('Téléchargement en cours')
        random_line = random.choice(lines).strip().split(' ')
        video_url = random_line[0]  
        filename = ' '.join(random_line[1:])  

        lines.remove(' '.join(random_line) + '\n')
        with open('ytb_vid_to_dl.txt', 'w') as file:
            file.writelines(lines)

        video_id_match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11})", video_url)
        if video_id_match:
            video_id = video_id_match.group(1)

            url = f"https://www.youtube.com/watch?v={video_id}"
    except Exception as e:
        print(f"Une erreur s'est produite lors du téléchargement de la vidéo : {e}")
    download_video(url,filename,video_directory)
    transcript = get_transcript(video_id)
    print('Analyzing the transcript')
    interesting_segments_v1 = analyze_transcript(transcript,duration)
    interesting_segments = extract_json_from_text(interesting_segments_v1)
    print('Finished')
    print(interesting_segments)
    print('Starting to segment_video')
    segment_video((interesting_segments),filename,video_directory,output_folder)
    for i, segment in enumerate(json.loads(interesting_segments)):
            input_file = f'{output_folder}/output{str(i).zfill(3)}.mp4'
            output_file = f'{output_folder}/cropped/output_cropped{str(i).zfill(3)}.mp4'
            spam_folder = current_directory+"/SPAMVIDEO"
            create_spam_video(input_file,spam_folder,output_file)
            os.remove(input_file)

