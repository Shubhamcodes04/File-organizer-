import os
import shutil

# Folder path (change this to your folder)
folder_path = r"D:\ayush college video"

# File type categories
file_types = {
    "Images": [".jpg", ".png", ".jpeg"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
    "Music": [".mp3"],
    "Others": []
}

# Organize files
for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)

    if os.path.isfile(file_path):
        moved = False

        for category, extensions in file_types.items():
            if any(file.endswith(ext) for ext in extensions):
                category_folder = os.path.join(folder_path, category)

                if not os.path.exists(category_folder):
                    os.makedirs(category_folder)

                destination = os.path.join(category_folder, file)

                # Handle duplicate file names
                count = 1
                file_name, file_ext = os.path.splitext(file)

                while os.path.exists(destination):
                    new_name = f"{file_name}_{count}{file_ext}"
                    destination = os.path.join(category_folder, new_name)
                    count += 1

                shutil.move(file_path, destination)

                print(f"Moved: {file} → {category}")
                moved = True
                print(f"Moved: {file} → {category}")   
                break
            
        if not moved:
            other_folder = os.path.join(folder_path, "Others")

            if not os.path.exists(other_folder):
                os.makedirs(other_folder)

            shutil.move(file_path, os.path.join(other_folder, file))

print("Files organized successfully!")