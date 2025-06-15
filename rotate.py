import sys
import os
from moviepy import VideoFileClip

def rotate_video(video_path, angle):
    """
    Rotates a video by a specified angle and saves it.

    Args:
        video_path (str): The full path to the video file.
        angle (int): The angle (in degrees) to rotate the video. 
                     Positive values rotate counter-clockwise.
    """
    if not os.path.exists(video_path):
        print(f"Error: Video file not found at '{video_path}'")
        return

    try:
        angle = int(angle)
        
        print(f"Loading video: {video_path}")
        clip = VideoFileClip(video_path)
        
        print(f"Rotating video by {angle} degrees...")
        rotated_clip = clip.rotated(angle, expand=True)
        
        # Define the output filename
        file_directory, original_filename = os.path.split(video_path)
        filename, file_extension = os.path.splitext(original_filename)
        output_filename = f"{filename}_rotated_{angle}{file_extension}"
        output_path = os.path.join(file_directory, output_filename)
        
        print(f"Saving rotated video to: {output_path}")
        # Write the result to a new file
        rotated_clip.write_videofile(output_path, codec='libx264')
        
        print("Rotation complete!")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage  : python rotate.py <path_to_video> <degrees_to_rotate>")
        print("Example: python rotate.py video.mp4 90")
        sys.exit(1)

    video_file_path = sys.argv[1]
    rotation_angle = sys.argv[2]
    
    rotate_video(video_file_path, rotation_angle)