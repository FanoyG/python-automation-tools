import shutil
from pathlib import Path


# Define the mapping of file ext to folder names.
EXTENSION_FOLDER = {
    ".txt": "Text_Files",
    ".pdf": "PDF_Files",
    ".log": "LOG_Files"
}

def sort_file_type(dirctory: Path):

    # Define the source directory user want to organize.
    source = Path(dirctory)

    num_of_files_moved = 0

    for file_path in source.iterdir():
        if file_path.is_dir():
            continue

        # check if the item is file and not dir.
        if file_path.is_file():
            #Get the lower case ext.
            file_ext = file_path.suffix.lower()

            # check if the ext is in our defiend mapping.
            if file_ext in EXTENSION_FOLDER:
                destination_folder_name = EXTENSION_FOLDER[file_ext]

                destination_folder = source / destination_folder_name
                destination_folder.mkdir(parents=True, exist_ok=True)

                destinatoin_file_path = destination_folder / file_path.name
            
                #Move the file
                try:
                    shutil.move(str(file_path), str(destinatoin_file_path))
                    num_of_files_moved += 1
                    print(f"Moved: {file_path.name} --> {destination_folder_name}")
                except shutil.Error as e:
                    print(f"Could not move {file_path.name}: {e}")
            
            else:
                print(f"Skipping: {file_path.name} --> unknown-extension")
    
    print(f"\nFile Organizatoin Completed. \nNo of Files Sorted --> {num_of_files_moved}")

if __name__ == "__main__":
    dir = input("Enter the directory path to Organized: ")
    sort_file_type(dir)