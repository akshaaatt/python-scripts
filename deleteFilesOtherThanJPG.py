import os

folder_path = 'path'

# Loop through each file in the folder
for filename in os.listdir(folder_path):
    # Construct the full file path
    file_path = os.path.join(folder_path, filename)
    # Check if it's a file and not a .jpg
    if os.path.isfile(file_path) and not filename.lower().endswith('.jpg'):
        # Delete the file
        os.remove(file_path)
        print(f"Deleted {filename}")

print("Done deleting files other than .jpg")
