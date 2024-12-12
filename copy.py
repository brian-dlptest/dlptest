import os
import shutil
def move_files(src_directory, dest_directory):
    # Check if source directory exists
    if not os.path.exists(src_directory):
        print(f"Source directory '{src_directory}' does not exist.")
        return
    # Create destination directory if it doesn't exist
    if not os.path.exists(dest_directory):
        os.makedirs(dest_directory)
        print(f"Destination directory '{dest_directory}' created.")
    # Iterate over the files in the source directory
    for file_name in os.listdir(src_directory):
        # Build the full file path
        src_file_path = os.path.join(src_directory, file_name)
        dest_file_path = os.path.join(dest_directory, file_name)
        # Check if it is a file (not a subdirectory)
        if os.path.isfile(src_file_path):
            try:
                # Move the file
                shutil.move(src_file_path, dest_file_path)
                print(f"Moved: {file_name}")
            except Exception as e:
                print(f"Error moving {file_name}: {e}")
        else:
            print(f"Skipping directory: {file_name}")
# Set your source and destination directories
src_directory = '/path/to/source/directory'
dest_directory = '/path/to/destination/directory'
# Call the function to move files
move_files(src_directory, dest_directory)
