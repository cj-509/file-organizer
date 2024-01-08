import os
import shutil
#======== a script that manage files


audio = (".3ga", ".aac", ".ac3", ".aif", ".aiff",
         ".alac", ".amr", ".ape", ".au", ".dss",
         ".flac", ".flv", ".m4a", ".m4b", ".m4p",
         ".mp3", ".mpga", ".ogg", ".oga", ".mogg",
         ".opus", ".qcp", ".tta", ".voc", ".wav",
         ".wma", ".wv")

video = (".webm", ".MTS", ".M2TS", ".TS", ".mov",
         ".mp4", ".m4p", ".m4v", ".mxf")

img = (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png",
       ".gif", ".webp", ".svg", ".apng", ".avif")

doc = (".epub", ".mobi", ".pdf", ".azw", ".txt", 
       ".html", ".htm",".fb2", ".cbz", ".cbr", 
       ".lit", ".iba")  #document files

data = (".csv", ".xlsx", ".xls", ".json", ".xml", 
        ".sql", ".tsv", ".h5", ".hdf5", ".yaml", 
        ".yml", ".feather", ".parquet", ".avro", 
        ".sqlite", ".db")

def is_audio(file):
    return os.path.splitext(file)[1] in audio

def is_video(file):
    return os.path.splitext(file)[1] in video

def is_image(file):
    return os.path.splitext(file)[1] in img

def is_screenshot(file):
    name, ext = os.path.splitext(file)
    return (ext in img) and "screenshot" in name.lower()

def is_document(file):
    return os.path.splitext(file)[1] in doc

def is_data(file):
    return os.path.splitext(file)[1] in data 

input_path = input("Enter files location: ")


if not input_path:
    curent_user = os.environ.get('USER') or os.environ.get('LOGNAME')
    change_to_dir = f"/home/{curent_user}/Downloads"
    os.chdir(change_to_dir)
    #print(os.getcwd())
    for file in os.listdir():
        if is_data(file):
            dataPath = f"/home/{curent_user}/Data"
            if not os.path.exists(dataPath):
                os.mkdir(dataPath)
            shutil.move(file, dataPath)

        elif is_Document(file):
            path_to_document = f"/home/{curent_user}/Document"
            shutil.move(file, path_to_document)

        elif is_screenshot(file):
            path_to_screen_shot = f"~/Screenshots"
            if not os.path.exists(path_to_screenshot):
                os.mkdir(path_to_screenshot)
            shutil.move(file, path_to_screenshot)

        elif
else:
    try:
        os.path.isdir(input_path)
    except OSError as e:
        print("Error")
