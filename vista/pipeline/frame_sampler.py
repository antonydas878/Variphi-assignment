# pipeline/frame_sampler.py

import cv2
import os

def sample_frames(video_path, output_dir, sample_rate=1):
    cap = cv2.VideoCapture(video_path)
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    frame_interval = int(fps * sample_rate)
    count = 0
    saved = 0

    os.makedirs(output_dir, exist_ok=True)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if count % frame_interval == 0:
            filename = f"{output_dir}/frame_{saved}.jpg"
            cv2.imwrite(filename, frame)
            saved += 1

        count += 1

    cap.release()