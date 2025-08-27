import os
from moviepy.editor import VideoFileClip

# --- User Configuration ---

# 1. Add the full paths to your video files here.
video_paths = [
    r"E:\D\Arpita\V5\VID20250626152545.mp4",
    r"E:\D\Arpita\V5\VID20250626153723.mp4",
    r"E:\D\Arpita\V5\VID20250626154627.mp4"
]

# 2. Specify the folder where the converted MP3 files will be saved.
output_directory = "extracted_audio"


# --- Extraction Logic ---

def extract_audio_to_mp3(video_list, output_folder):
    """
    Extracts audio from a list of videos and saves them as MP3 files.

    Args:
        video_list (list): A list of full paths to the video files.
        output_folder (str): The path to the folder for saving extracted MP3 files.
    """
    if not os.path.exists(output_folder):
        print(f"Creating output directory: {output_folder}")
        os.makedirs(output_folder)

    if not video_list:
        print("The video_paths list is empty. Please add video paths to process.")
        return

    print(f"\nStarting audio extraction process...")
    print(f"Number of files to process: {len(video_list)}")
    print("-" * 30)

    for video_path in video_list:
        if not os.path.isfile(video_path):
            print(f"⚠️  Warning: File not found at '{video_path}'. Skipping.")
            continue

        try:
            base_filename = os.path.basename(video_path)
            filename_without_ext = os.path.splitext(base_filename)[0]

            # --- CHANGE #1: Define the output path with an .mp3 extension ---
            output_filepath = os.path.join(output_folder, f"{filename_without_ext}.mp3")

            print(f"▶️  Extracting audio from '{base_filename}'...")

            clip = VideoFileClip(video_path)

            # --- CHANGE #2: Isolate the audio and use write_audiofile ---
            # We access the clip's audio with 'clip.audio'
            # Then we write it to an audio file.
            clip.audio.write_audiofile(output_filepath)

            clip.close()

            print(f"✅  Successfully extracted and saved to '{output_filepath}'")

        except Exception as e:
            # If a video has no audio track, it will raise an error.
            if "NoneType" in str(e):
                 print(f"❌  Error: Video '{base_filename}' might not have an audio track.")
            else:
                 print(f"❌  Error processing '{video_path}': {e}")


        print("-" * 30)

    print("All files have been processed.")


# --- Run the Script ---
if __name__ == "__main__":
    extract_audio_to_mp3(video_paths, output_directory)