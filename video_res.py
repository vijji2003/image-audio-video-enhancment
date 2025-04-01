from moviepy.editor import VideoFileClip

def enhance_video(video_path, scale_factor=2):
    clip = VideoFileClip(video_path)
    upscaled_clip = clip.resize(scale_factor)
    upscaled_clip.write_videofile("upscaled_video.mp4", codec='libx264')
    return "upscaled_video.mp4"
