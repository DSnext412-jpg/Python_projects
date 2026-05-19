import os
import shutil

folder_path=input("Enter folder path: ")

file_types={
    "Images":[".jpg",".png",".jpeg",".gif"],
    "Documents":[".pdf",".docx",".txt"],
    "Videos":[".mp4",".mkv",".avi"],
    "Music":[".mp3",".wav"],
    "Programs":[".py",".java",".cpp",".c"]
}

for file_name in os.listdir(folder_path):
    file_path=os.path.join(folder_path,file_name)

    if os.path.isdir(file_path):
        continue

    _, extension=os.path.splitext(file_name)
    moved=False

    for folder,extensions in file_types.items():
        if extension.lower() in extensions:
            target_folder=os.path.join(folder_path, folder)
            os.makedirs(target_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(target_folder,file_name))
            print(f"Moved: {file_name} → {folder}")
            moved=True
            break

    if not moved:
        other_folder = os.path.join(folder_path, "Others")
        os.makedirs(other_folder, exist_ok=True)
        shutil.move(file_path, os.path.join(other_folder, file_name))
        print(f"Moved: {file_name} → Others")

print("\nfiles organized successfully")
