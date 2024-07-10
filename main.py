import streamlit as st
import cv2

def main():
    st.title("Video Streaming with Streamlit")

    # Sidebar selection for camera or file upload
    streaming_option = st.sidebar.radio("Choose Streaming Option", ("Camera", "Upload Video"))

    if streaming_option == "Camera":
        show_camera_stream()
    elif streaming_option == "Upload Video":
        show_uploaded_video()

def show_camera_stream():
    st.subheader("Camera Streaming")

    # Start capturing from the camera
    cap = cv2.VideoCapture(0)

    stframe = st.empty()
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        stframe.image(frame, channels="RGB", use_column_width=True)

    cap.release()

def show_uploaded_video():
    st.subheader("Upload Video")

    # File uploader for video files
    video_file = st.file_uploader("Upload a Video File", type=["mp4", "avi", "mov", "mkv"])

    if video_file is not None:
        # Start capturing from the uploaded video file
        cap = cv2.VideoCapture(video_file)

        stframe = st.empty()
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            stframe.image(frame, channels="RGB", use_column_width=True)

        cap.release()
    else:
        st.warning("Please upload a video file.")

if __name__ == "__main__":
    main()
