import os
import subprocess

def convert_heic_to_jpg_in_folder(input_folder):
    # Check if the input folder exists
    if not os.path.isdir(input_folder):
        print(f"The folder {input_folder} does not exist.")
        return

    # Iterate over all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".heic"):
            # Construct full file path for input and output
            heic_file_path = os.path.join(input_folder, filename)
            jpg_filename = filename.rsplit(".", 1)[0] + ".jpg"
            jpg_file_path = os.path.join(input_folder, jpg_filename)

            # Convert HEIC to JPG using ImageMagick's magick command
            try:
                subprocess.run(["magick", "convert", heic_file_path, jpg_file_path], check=True)
                print(f"Converted {filename} to {jpg_filename}")
            except subprocess.CalledProcessError as e:
                print(f"Failed to convert {filename}. Error: {e}")

input_folder = "path"
convert_heic_to_jpg_in_folder(input_folder)
