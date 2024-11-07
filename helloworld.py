import streamlit as st
import tempfile

# Set up custom styles for buttons and progress bar
st.markdown(
    """
    <style>
    .stButton>button {
        background-color: #4CAF50; /* Green background */
        color: white; /* White text */
        border: none;
        border-radius: 8px;
        padding: 10px 20px;
        font-size: 16px;
        margin-top: 10px;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #45a049; /* Darker green on hover */
    }
    .stProgress > div > div {
        background-color: #4CAF50; /* Green progress bar */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title for the app
st.title("🎾 Tennis Game Tracking")

# Create two columns for layout
col1, col2 = st.columns([3, 1])

# Video upload in the first column
with col1:
    st.subheader("Upload & Preview Video")
    video_file = st.file_uploader("Select Input File", type=["mp4", "avi", "mov"])
    if video_file is not None:
        temp_video = tempfile.NamedTemporaryFile(delete=False)
        temp_video.write(video_file.read())

        # Preview button to show the videos
        if st.button("Preview Video"):
            st.video(temp_video.name)
        else:
            st.write("Click 'Preview Video' to view the uploaded video.")
    else:
        st.write("Please select a video file.")

# Buttons in the second column
with col2:
    st.subheader("Control Panel")
    
    # Buttons for video processing and download actions
    if st.button("Process Video"):
        st.write("Processing video...")
        st.progress(0.5)  # Simulate progress for example
    if st.button("Show Output"):
        st.write("Displaying processed output...")
    if st.button("Download Output"):
        st.write("Preparing download...")

    # Static progress bar as an example
    st.progress(0.2)
