# Video to MP3 Audio Extractor 🎵

A simple yet powerful Python script to automatically extract audio from multiple video files and save them as high-quality MP3s.

<!-- A generic GIF showing a command-line script running -->

## 📝 Overview

This script uses the `moviepy` library to process a list of video files (`.mp4`, `.mov`, `.avi`, etc.) and extracts their audio tracks, saving each one as a separate `.mp3` file in a designated output folder. It's designed to be easy to configure and run, even for users with minimal programming experience.

## ✨ Features

* **Batch Processing**: Convert multiple videos in a single run.
* **Simple Configuration**: Just paste your video file paths into a list.
* **Organized Output**: All extracted MP3 files are saved in a clean, separate directory.
* **Error Handling**: Gracefully skips missing files and handles videos that have no audio track.
* **Cross-Platform**: Works on Windows, macOS, and Linux.

---

## 🚀 Getting Started

Follow these instructions to get the project up and running on your local machine.

### ✅ Prerequisites

Make sure you have Python 3 installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

You will also need `pip`, the Python package installer, which is usually included with Python installations.

### ⚙️ Installation & Setup

1.  **Clone the Repository**
    Open your terminal or Git Bash and clone this repository to your local machine:
    ```bash
    git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git)
    cd YOUR_REPOSITORY_NAME
    ```

2.  **Install Required Libraries**
    The script depends on the `moviepy` library. Install it using `pip`:
    ```bash
    pip install moviepy
    ```

---

## USAGE

1.  **Add Your Video Files**
    Open the `app.py` file in a text editor. Locate the `video_paths` list and replace the placeholder paths with the full paths to your video files.

    ```python
    # --- User Configuration ---

    # 1. Add the full paths to your video files here.
    video_paths = [
        r"C:\Users\YourUser\Videos\video1.mp4",
        r"D:\Family\Vacation\IMG_1234.mov",
        r"/home/user/media/another_video.avi"
    ]

    # 2. Specify the folder where the converted MP3 files will be saved.
    output_directory = "extracted_audio"
    ```
    > **💡 Tip:** On Windows, you can right-click a file, select "Copy as path," and paste it directly. Remember to keep the `r` before the quotes to handle backslashes correctly.

2.  **Run the Script**
    Open a terminal or command prompt, navigate to the project directory (where `app.py` is located), and run the script with the following command:
    ```bash
    python app.py
    ```

3.  **Find Your Audio Files**
    The script will create a new folder named `extracted_audio` (or whatever you named it in `output_directory`). Inside this folder, you will find all your converted `.mp3` files.

    ```
    Your-Project-Folder/
    ├── extracted_audio/
    │   ├── video1.mp3
    │   ├── IMG_1234.mp3
    │   └── another_video.mp3
    └── app.py
    ```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME/issues).

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.
