import streamlit as st
import tempfile

# Title for the app
st.title("Tennis Game Tracking")

# Create two columns for layout
col1, col2 = st.columns([3, 1])

# Video upload in the first column
with col1:
    video_file = st.file_uploader("Select Input File", type=["mp4", "avi", "mov"])
    if video_file is not None:
        temp_video = tempfile.NamedTemporaryFile(delete=False)
        temp_video.write(video_file.read())

        # Preview button to show the video
        if st.button("Preview Video"):
            st.video(temp_video.name)
        else:
            st.write("Click 'Preview Video' to view the uploaded video.")
    else:
        st.write("Please select a video file.")

# Buttons in the second column
with col2:
    st.button("Select Input File")  # This can be handled by file uploader
    st.button("Preview Video")  # This can be handled in the code above
    st.progress(0.2)  # Display progress as an example (20%)

    # Additional buttons for process control
    st.button("Process Video")
    st.button("Show Output")
    st.button("Download Output")

