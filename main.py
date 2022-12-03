import os
import shutil
import datetime
# Set the path to the desktop
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')

# Get a list of all files on the desktop
desktop_files = os.listdir(desktop_path)

# Create a dictionary to store the file extension and corresponding folder
file_folders = {}

# Create a list to store the collected files
collected_files = []

# Loop through the list of files on the desktop
for file in desktop_files:
    # Get the file extension
    file_ext = os.path.splitext(file)[1]

    # Check if the file is an image file
    if file_ext in ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.psd']:
        # Check if a folder for the file extension exists
        folder_name = 'folder_{}'.format(file_ext)
        folder_path = os.path.join(desktop_path, folder_name)
        if not os.path.exists(folder_path):
            # Create a new folder for the file extension
            os.mkdir(folder_path)

        # Move the file into the corresponding folder
        file_path = os.path.join(desktop_path, file)
        shutil.move(file_path, folder_path)

        # Add the file name to the list of collected files
        collected_files.append(file)

# Get the current date and time
now = datetime.datetime.now()

# Format the date and time for the log file
log_time = now.strftime('%Y-%m-%d %H:%M:%S')

# Write a log message to the log file
log_message = 'Finished organizing images on {}\n'.format(log_time)

# Add the collected files to the log message
log_message += 'Collected files: \n'
for file in collected_files:
    log_message += '- {}\n'.format(file)

# Set the path to the log file
log_file = os.path.join(desktop_path, 'image_organizer.txt')

# Open the log file in append mode
with open(log_file, 'a') as f:
    # Write the log message to the file
    f.write(log_message)
