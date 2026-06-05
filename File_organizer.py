# Code using Os and Shutil libraries:
import os
import shutil
# import time


My_Files = os.listdir("My_Files")
'''
  instead of adding file names manually os library give us a tool
   -which is function listdir()- it automatically reads all files
   from a given folder and returns them as a list
    '''


extentions_dictionary = {  # This is a dictionary where the keys are the file extentions, and the value is in which category this extention belongs
                           # As we explained before chosing dictionary method is because the constant time :O(1) 
    # Images        
    "jpg": "Images", "jpeg": "Images", "png": "Images", "gif": "Images",
    "bmp": "Images", "svg": "Images", "ico": "Images", "tif": "Images",
    "raw": "Images", "psd": "Images", "webp": "Images", "heif": "Images",
    # Videos
    "mp4": "Videos", "avi": "Videos", "mov": "Videos", "mkv": "Videos",
    "wmv": "Videos", "flv": "Videos", "webm": "Videos", "mpeg": "Videos",
    "3gpp": "Videos",
    # Documents
    "pdf": "Document", "doc": "Document", "docx": "Document", "xls": "Document",
    "xlsx": "Document", "ppt": "Document", "pptx": "Document", "txt": "Document",
    "csv": "Document", "rtf": "Document",
    # Code
    "py": "Code", "js": "Code", "html": "Code", "css": "Code", "json": "Code",
    "java": "Code", "cpp": "Code", "php": "Code", "ts": "Code", "jsx": "Code",
    "swift": "Code", "dart": "Code", "cs": "Code", "vb": "Code", "yaml": "Code",
    # Audio
    "mp3": "Audio", "wav": "Audio", "aac": "Audio", "flac": "Audio",
    "ogg": "Audio", "m4a": "Audio", "wma": "Audio", "opus": "Audio", "aiff": "Audio",
    # Archives
    "zip": "Archives", "rar": "Archives", "tar": "Archives", "gz": "Archives",
    "7z": "Archives", "bz2": "Archives", "cab": "Archives",
    # Executables
    "exe": "Executables", "msi": "Executables", "apk": "Executables",
    "deb": "Executables", "rpm": "Executables",
    # Fonts
    "ttf": "Fonts", "otf": "Fonts", "woff": "Fonts", "woff2": "Fonts",
    # Database
    "sqlite": "Database", "sql": "Database", "db": "Database", "mdb": "Database",
    # Ebooks
    "epub": "Ebooks", "mobi": "Ebooks", "cbr": "Ebooks", "azw3": "Ebooks",
    # Disk Images
    "iso": "DiskImages", "img": "DiskImages", "bin": "DiskImages", "vmdk": "DiskImages",
    # Backup
    "bak": "Backup", "bkp": "Backup", "tmp": "Backup",
    # System
    "dll": "System", "sys": "System", "ini": "System", "cfg": "System",
    "bat": "System", "log": "System", "reg": "System", "conf": "System",
}

'''
  Here we iterate for each item in the My_Files list and 
  we start to chek the item extention using split and move
  it to its type folder

'''

for file in My_Files:
  if os.path.isfile(os.path.join("My_Files/",file)) :
  
    ext = file.split(".")[-1]  
    file_type = extentions_dictionary.get(ext, "Others")  
    # time.sleep(0.5)
    os.makedirs(os.path.join("My_Files", file_type), exist_ok= True) # once the file type is identified (image or video or audio); create a folder of this certain type


    
    shutil.move(os.path.join("My_Files", file)  , os.path.join("My_Files", file_type))  # now we can move the file -which we verify its extension- to  its category folder 
#we move the file in the first argument   (source)  to the second argument (destination) which is file_type 
                           # Source           --,-->           Destination
