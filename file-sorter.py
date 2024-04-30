# Import statements
import os, shutil, time
from PIL import Image, ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True

rootLocation = r'C:\\Users\\yourUsername\\Unsorted' # where you want to sort from
backupLocation = r'C:\\Users\\yourUsername\\Sorted' # where you want to sort to
sourceLocations = []
sourceLocations.append(rootLocation)

# Set extensions you want to accept here (files not of these types will be deleted)
photoExtensions = ['.jpg', '.jpeg', '.png', '.JPG', '.HEIC']
videoExtensions = ['.mp4', '.avi', '.AVI', '.MOV']
otherExtensions = []
acceptedExtensions = photoExtensions + videoExtensions + otherExtensions

# Create the backup location if it does not already exist
if not os.path.exists(backupLocation):
    os.mkdir(backupLocation)

# Compares files to see if the file is already at the backup location
def CompareFiles(fileToCopy, fileAtDestination):

    # the file is not at the backup location, we want to move the file there
    if not os.path.exists(fileAtDestination):
        return 1
    
    sourceFile = Image.open(fileToCopy)
    destinationFile = Image.open(fileAtDestination)

    # do nothing if our source file is the same as the destination file (file is skipped over)
    if sourceFile == destinationFile:
        return 2
    
    else:
        return 3

# Gets the month when the photo was taken
def GetMonth(numMonth):
    if numMonth == 1:
        return "January"
    if numMonth == 2:
        return "February"
    if numMonth == 3:
        return "March"
    if numMonth == 4:
        return "April"
    if numMonth == 5:
        return "May"
    if numMonth == 6:
        return "June"
    if numMonth == 7:
        return "July"
    if numMonth == 8:
        return "August"
    if numMonth == 9:
        return "September"
    if numMonth == 10:
        return "October"
    if numMonth == 11:
        return "November"
    if numMonth == 12:
        return "December"

# Gets the date when the photo was taken
def GetDate(filePath):
    temp = time.gmtime(os.path.getmtime(filePath))
    day = time.strftime("%d", temp)
    month = time.strftime("%B", temp)
    year = time.strftime("%G", temp)

    out = '\\' + year + '\\' + month + '\\' + day + '\\'
    return out

# Compares the files using CompareFiles function and deals with it accordingly
def FileChecker(sourceFile, backupFile, backupLocation):
    temp = CompareFiles(sourceFile , backupFile)
    if temp == 1:
        if not os.path.exists(backupLocation):
            os.makedirs(backupLocation)
        shutil.move(sourceFile, backupFile, copy_function = shutil.copy2)
    elif temp == 2:
        os.remove(sourceFile)

# Cleanup when the code is finished running, discards of the unsorted folder and all subdirectories
def FolderRemover(locations):
    for location in locations:
        rootFolder = location
        folders = list(os.walk(rootFolder))
        for folder in folders:
            if len(folder) > 1 and not '.' in folder:
                rootFolder = folder[0]
                for root, dirs, files in os.walk(rootFolder):
                    for file in files:
                        if os.path.exists(folder[0] + '\\' + file):
                            os.remove(folder[0] + '\\' + file)
                if len(list(os.scandir(folder[0]))) == 0:
                    try:
                        os.rmdir(folder[0])
                    except:
                        print("Access was denied to: " + folder[0])

# Start of program
print("Starting file-sorter")

# Adds all subfolders to the sourceLocations list
for root, subdirectories, files in os.walk(rootLocation):
    for subdirectory in subdirectories:
        if subdirectory is not []:
            sourceLocations.append(rootLocation + '\\' + subdirectory)

# Iterates through each folder and goes through all of its files
for location in sourceLocations:
    print(location)
    for root, dirs, files in os.walk(location):
        for file in files:
            for extension in acceptedExtensions:
                if file.endswith(extension):
                    fileDirectory = root
                    sourceFile = fileDirectory + '\\' + file
                    backupFileLocation = backupLocation + GetDate(sourceFile)
                    backupfile = backupFileLocation + file
                    FileChecker(sourceFile, backupfile, backupFileLocation)

# Cleanup of unsorted folder
time.sleep(3)
for i in range(len(sourceLocations)):
    FolderRemover(sourceLocations)
    time.sleep(0.2)

# Program end
print("Finished sorting")