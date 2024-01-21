import cv2
import numpy as np
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get configuration from environment variables
video_path = os.getenv("VIDEO_PATH", "demovideo.mp4")
output_path = os.getenv("OUTPUT_PATH", "demovideo_blurred_exact.mp4")
top_left_x = int(os.getenv("TOP_LEFT_X", 527))
top_left_y = int(os.getenv("TOP_LEFT_Y", 103))
bottom_right_x = int(os.getenv("BOTTOM_RIGHT_X", 901))
bottom_right_y = int(os.getenv("BOTTOM_RIGHT_Y", 151))

def blur_rectangle(video_path, output_path, top_left, bottom_right):
    cap = cv2.VideoCapture(video_path)

    # Get video properties
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    frames_per_second = cap.get(5)

    # Create VideoWriter object with codec -1 (choose codec dialog)
    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), frames_per_second, (frame_width, frame_height))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Apply blur to the specified rectangle
        frame[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]] = cv2.GaussianBlur(frame[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]], (51, 51), 0)

        # Write the frame to the output video
        out.write(frame)

    cap.release()
    out.release()
    cv2.destroyAllWindows()

# Example usage with environment variables
top_left = (top_left_x, top_left_y)
bottom_right = (bottom_right_x, bottom_right_y)

blur_rectangle(video_path, output_path, top_left, bottom_right)

