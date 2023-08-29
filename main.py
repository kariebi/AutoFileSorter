import os
import shutil
import time

def organize_file(file_path):
    filename, extension = os.path.splitext(file_path)
    extension = extension.lower()

    video_extensions = ['.mp4', '.avi', '.mkv']
    music_extensions = ['.mp3', '.wav']
    photo_extensions = ['.jpg', '.jpeg', '.png']

    if extension in video_extensions:
        destination_folder = 'videos'
    elif extension in music_extensions:
        destination_folder = 'music'
    elif extension in photo_extensions:
        destination_folder = 'photos'
    else:
        destination_folder = 'downloads'

    destination_path = os.path.join(download_folder, destination_folder, os.path.basename(file_path))
    shutil.move(file_path, destination_path)
    print(f"Moved {file_path} to {destination_path}")

if __name__ == "__main__":
    download_folder = "/home/soroh/Downloads/"

    video_folder = os.path.join(download_folder, "videos")
    music_folder = os.path.join(download_folder, "music")
    photo_folder = os.path.join(download_folder, "photos")
    downloads_folder = os.path.join(download_folder, "downloads")

    # Create subfolders if they don't exist
    for folder in [video_folder, music_folder, photo_folder, downloads_folder]:
        os.makedirs(folder, exist_ok=True)

    while True:
        for filename in os.listdir(download_folder):
            file_path = os.path.join(download_folder, filename)
            if os.path.isfile(file_path):
                organize_file(file_path)
        time.sleep(60)  # Check for new files every 60 seconds
