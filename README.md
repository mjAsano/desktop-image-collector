# Organizing Image Files on Your Desktop
Hello, my name is mjasano.
I recently created a program to help me organize the many sketches and psd files that had been scattered on my desktop. As I draw more illustrations, I found it increasingly uncomfortable to have these files scattered across my desktop. With this program, I am able to keep my desktop organized and clutter-free. Therefore, I'd like to share this toy-project.

In this tutorial, we will create a Python script that organizes the image files on your desktop by creating folders for each type of image file, and moving the files into the corresponding folders. The script will also create a log file that records the time and date when the image files were organized, as well as the names of the files that were collected and moved.

## Prerequisites
Before we begin, make sure you have the following installed on your system:

- Python 3

- The shutil module, which provides functions for copying and moving files. To install this module, run the following command:
```
pip install shutil
```
## Creating the Script
1. Open your favorite text editor and create a new file named image_organizer.py.

2. Import the following modules at the top of the file:

```python
import os
import shutil
import datetime
```
3. Add the following code to set the path to the desktop, and get a list of all the files on the desktop:
```python
# Set the path to the desktop
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')

# Get a list of all files on the desktop
desktop_files = os.listdir(desktop_path)
```
4. Create a dictionary to store the file extension and corresponding folder, and a list to store the collected files:
```python
# Create a dictionary to store the file extension and corresponding folder
file_folders = {}

# Create a list to store the collected files
collected_files = []
```
5. Add the following code to loop through the list of files on the desktop, and move the image files into the corresponding folders:
```python
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
```
6. Add the following code to write a log message to the log file:
```python
# Get the current date and time
now = datetime.datetime.now()

# Format the date and time for the log file
log_time = now.strftime('%Y-%m-%d %H:%M:%S')

# Write a log message to the log file
log_message = 'Finished organizing images on {}\n'.format(log_time)
```
7. Add the collected files to the log message:
```python
# Add the collected files to the log message
log_message += 'Collected files: \n'
for file in collected_files:
    log_message += '- {}\n'.format(file)
```
9. Write the log message to the log file:
```python
    # Write the log message to the file
    f.write(log_message)

```
10. Save the file and run the script to organize the image files on your desktop:

```
python image_organizer.py
```
After running the script, the image files on your desktop will be organized into folders named folder_<file_extension>, where <file_extension> is the file extension of the image files (e.g. folder_.png for PNG files). A log file named image_organizer.txt will also be created on your desktop, which will contain a log message with the time and date when the image files were organized, as well as the names of the files that were collected and moved.

## Conclusion
In this tutorial, we learned how to create a Python script that organizes the image files on your desktop by creating folders for each type of image file, and moving the files into the corresponding folders. We also learned how to create a log file that records the time and date when the image files were organized, as well as the names of the files that were collected and moved.