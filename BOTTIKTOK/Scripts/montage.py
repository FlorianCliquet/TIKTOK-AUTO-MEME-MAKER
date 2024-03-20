from moviepy.editor import VideoFileClip, CompositeVideoClip
import os
import random

def create_composite_video_9_16(main_video_path, spam_folder, subtitles):
    width = 720
    height = 1280

    main_video = VideoFileClip(main_video_path).resize(height=int(0.45*height))
    main_video_duration = main_video.duration
    main_video = main_video.set_position(("center", "top"))

    spam_videos = [f for f in os.listdir(spam_folder) if f.endswith(('.mp4', '.avi', '.mov'))]
    random_spam_video = random.choice(spam_videos)
    spam_video_path = os.path.join(spam_folder, random_spam_video)
    spam_video = VideoFileClip(spam_video_path).resize(height=int(0.55*height))
    spam_video = spam_video.set_position(("center", "bottom")).set_duration(main_video_duration)

    subtitle_clip = main_video.text_clip(subtitles, fontsize=24, color='white').set_duration(main_video_duration)
    subtitle_clip = subtitle_clip.set_position(("center", "bottom"))

    final_video = CompositeVideoClip([main_video, spam_video, subtitle_clip], size=(width, height))

    final_video_path = "composite_video_9_16.mp4"
    final_video.write_videofile(final_video_path, codec='libx264', fps=24)

    return final_video_path