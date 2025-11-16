import shutil
import zipfile
import questionary
from pathlib import Path
from datetime import datetime
from questionary import Separator


# ======================================================
# INTERNAL DIRECTORY HANDLER (single core function)
# ======================================================

def _ask_dir_core(prompt, must_exist=False, allow_create=False):
    """
    Core directory selection logic.

    must_exist=True  -> directory MUST already exist 
    allow_create=True -> if directory missing, ask user to create it
    """
    while True:
        path_str = questionary.path(
            message=prompt,
            only_directories=True
        ).ask()

        if path_str is None:
            print("\n❌ Operation cancelled.\n")
            return None

        path = Path(path_str)

        # Case 1: Path exists
        if path.exists():
            if path.is_dir():
                return path
            else:
                print("❌ This is not a directory.\n")
                continue

        # Case 2: Must exist → reject if missing
        if must_exist:
            print(f"❌ ERROR: Directory '{path}' does NOT exist.\n")
            continue

        # Case 3: Allow creation → ask user
        if allow_create:
            create = questionary.confirm(
                f"Directory '{path}' does not exist. Create it?"
            ).ask()
            if create:
                path.mkdir(parents=True, exist_ok=True)
                print(f"📁 Created directory: {path}")
                return path
            else:
                print("❌ Please select a valid existing directory.\n")
                continue

        # If neither exists nor allowed → reject
        print("❌ Invalid directory.\n")


# ======================================================
# PUBLIC FUNCTIONS FOR SPECIFIC BEHAVIOR
# ======================================================

def ask_existing_directory(prompt):
    """Directory MUST exist."""
    return _ask_dir_core(prompt, must_exist=True)


def ask_or_create_directory(prompt):
    """Directory may be created."""
    return _ask_dir_core(prompt, allow_create=True)


# ======================================================
# BACKUP FUNCTIONS
# ======================================================

def full_backup(src: Path, dest: Path):
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    archive_name = f"{src.name}-backup-{timestamp}"

    base_path = dest / archive_name

    archive_path = shutil.make_archive(
        base_name=str(base_path),
        format='zip',
        root_dir=str(src)
    )

    print(f"✅ Full backup created → {archive_path}\n")


def custom_backup(src: Path, dest: Path):
    files = [f for f in src.iterdir() if f.is_file()]
    if not files:
        print("⚠️ No files in source directory.\n")
        return

    selected_files = questionary.checkbox(
        "Select files to include in backup:",
        choices=[f.name for f in files]
    ).ask()

    if not selected_files:
        print("⚠️ No files selected.\n")
        return

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    zip_path = dest / f"custom-backup-{timestamp}.zip"

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for fname in selected_files:
            z.write(src / fname, arcname=fname)

    print(f"✅ Custom backup created → {zip_path}\n")


# ======================================================
# REMOVE BACKUP
# ======================================================

def remove_backup():
    backup_dir = ask_existing_directory("Select BACKUP directory (must exist):")
    if backup_dir is None:
        return

    action = questionary.select(
        "What do you want to delete?",
        choices=[
            {"name": "🗂️ Entire Backup Folder", "value": "folder"},
            {"name": "📄 Specific ZIP Files", "value": "files"},
            {"name": "❌ Cancel", "value": "cancel"}
        ]
    ).ask()

    if action == "cancel":
        print("❌ Deletion cancelled.\n")
        return

    if action == "folder":
        confirm = questionary.confirm(
            f"⚠️ Delete entire folder? → {backup_dir}"
        ).ask()

        if confirm:
            shutil.rmtree(backup_dir)
            print(f"🗑️ Folder deleted: {backup_dir}\n")
        else:
            print("❌ Cancelled.\n")

        return

    if action == "files":
        zip_files = [f for f in backup_dir.iterdir() if f.suffix == ".zip"]

        if not zip_files:
            print("⚠️ No zip files.\n")
            return

        selected = questionary.checkbox(
            "Select ZIPs to delete:",
            choices=[f.name for f in zip_files]
        ).ask()

        if not selected:
            print("⚠️ Nothing selected.\n")
            return

        if not questionary.confirm(
            f"Delete {len(selected)} files?"
        ).ask():
            print("❌ Cancelled.\n")
            return

        for name in selected:
            (backup_dir / name).unlink()
            print(f"🗑️ Deleted {name}")

        print("\n✅ Done!\n")


# ======================================================
# MAIN PROGRAM
# ======================================================

if __name__ == "__main__":
    try:
        choice = questionary.select(
            "Choose backup mode:",
            choices=[
                Separator("=== BACKUP OPTIONS ==="),
                {"name": "📁  Full Backup", "value": "full"},
                {"name": "📄  File Backup", "value": "files"},
                {"name": "🗑️  Remove Backup", "value": "remove"},
                Separator("=== EXIT ==="),
                {"name": "❌ Cancel", "value": "exit"},
            ]
        ).ask()

        if choice in ("exit", None):
            print("Goodbye!")
            exit()

        if choice == "remove":
            remove_backup()
            exit()

        # Source must exist
        src = ask_existing_directory("Enter Source Directory (must exist):")

        # Destination can be created
        dest = ask_or_create_directory("Enter Destination Directory:")

        if src is None or dest is None:
            print("❌ Operation cancelled.\n")
            exit()

        if choice == "full":
            full_backup(src, dest)
        elif choice == "files":
            custom_backup(src, dest)

    except KeyboardInterrupt:
        print("\n❌ Interrupted by user.\n")
