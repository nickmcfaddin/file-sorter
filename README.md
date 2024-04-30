# file-sorter
Sorts files (tailored to images &amp; videos) into folders by year, month and day.

## Purpose
If you have a lot of images and videos, but not the time to sort them, this script is perfect for you. It will organize all of your files within a folder and all of its subfolders into new folders by year, month and day, as well as clean up your old folder directory in the process. Originally, I built this for my mom who had tens of thousands of photos all in different directories that would have taken quite a few hours to deal with.

## Running the Program
Modify the rootLocation and backupLocation from within the file as shown below.

```python
rootLocation = r'C:\\Users\\yourUsername\\Unsorted' # where you want to sort from
backupLocation = r'C:\\Users\\yourUsername\\Sorted' # where you want to sort to
```

If you are wanting to accept other types of extensions, modify the video, photo and other extensions as shown below.

```python
# Set extensions you want to accept here (files not of these types will be deleted)
photoExtensions = ['.jpg', '.jpeg', '.png', '.JPG', '.HEIC']
videoExtensions = ['.mp4', '.avi', '.AVI', '.MOV']
otherExtensions = []
acceptedExtensions = photoExtensions + videoExtensions + otherExtensions
```

Now that you have made all the modifications, you can run the program!
