# This script will backup a directory to a specified location older than 30 days
import os
import shutil
from datetime import datetime, timedelta, timezone
def backup_old_files(source_dir, backup_dir):
    # Get the current time in UTC
    current_time = datetime.now(timezone.utc)
    
    # Ensure the backup directory exists
    os.makedirs(backup_dir, exist_ok=True)
    
    # Iterate through all files in the source directory
    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)
        
        # Check if it is a file and not a directory
        if os.path.isfile(file_path):
            # Get the last modified time of the file
            file_mtime = datetime.fromtimestamp(os.path.getmtime(file_path), timezone.utc)
            
            # Check if the file is older than 30 days
            if current_time - file_mtime > timedelta(days=30):
                # Copy the file to the backup directory
                shutil.copy2(file_path, backup_dir)
                print(f"Backed up: {filename}")
    
    print("Backup completed.")