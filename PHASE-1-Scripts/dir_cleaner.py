import datetime
from pathlib import Path


def clean_old_files(directory: Path, min: int) -> None:
    """Delete files older than 'min' minutes in the specified directory."""

    file_path = Path(directory)
    if not file_path.is_dir():
        print(f"The provided path {directory} is not a valid directory.")
        return
    
    if not file_path.exists():
        print(f"The directory {directory} does not exist.")
        return
    
    now = datetime.datetime.now()
    cutoff = now - datetime.timedelta(minutes=min)

    files_deleted = 0

    for item in file_path.iterdir():
        if item.is_file():
            file_modified = datetime.datetime.fromtimestamp(item.stat().st_mtime)
            if file_modified < cutoff:
                try:
                    item.unlink()
                    files_deleted += 1
                    print(f"Deleted file: {item}")
                except Exception as e:
                    print(f"Error deleting file {item}: {e}")
    
    print(f"Total files deleted: {files_deleted}")


if __name__ == "__main__":
    dir_to_clean = input("Enter the directory path to clean: ")
    minutes_threshold = input("Enter the age threshold in minutes: ")

    if minutes_threshold.strip() == "":
        minutes_threshold = 2
    minutes_threshold = int(minutes_threshold)

    clean_old_files(dir_to_clean, minutes_threshold)