import streamlit as st
import cv2

def main():
    st.title("Video Streaming with Streamlit")

    # Use the camera if you have a webcam
    use_camera = st.checkbox("Use Camera")
    
    # If not using camera, ask for a video file
    if not use_camera:
        video_file = st.file_uploader("Upload a Video", type=["mp4", "avi", "mov", "mkv"])
    
    if use_camera:
        # Start capturing from the camera
        cap = cv2.VideoCapture(0)
    else:
        if video_file is not None:
            # Start capturing from the uploaded video file
            cap = cv2.VideoCapture(video_file.name)
        else:
            st.text("Please upload a video file or select to use the camera.")
            return

    stframe = st.empty()
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        stframe.image(frame, channels="RGB", use_column_width=True)

    cap.release()

if __name__ == "__main__":
    main()
