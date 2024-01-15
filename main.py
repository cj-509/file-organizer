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

curent_user = os.environ.get('USER') or os.environ.get('LOGNAME') #get the user's using the system

if not input_path:
    change_to_dir = f"/home/{curent_user}/Downloads"
    os.chdir(change_to_dir)
    #print(os.getcwd())
    for file in os.listdir():
        if is_data(file):
            dataPath = f"/home/{curent_user}/Data"
            if not os.path.exists(dataPath):
                os.mkdir(dataPath)
            shutil.move(file, dataPath)

        elif is_document(file):
            path_to_document = f"/home/{curent_user}/Document"
            shutil.move(file, path_to_document)

        elif is_screenshot(file):
            path_to_screenshot = f"/home/{curent_user}/Screenshots"
            if not os.path.exists(path_to_screenshot):
                os.mkdir(path_to_screenshot)
            shutil.move(file, path_to_screenshot)

        elif is_image(file):
            image_path = f"/home/{curent_user}/Image"
            if not os.path.exists(image_path):
                os.mkdir(image_path)
            shutil.move(file, image_path)
        elif is_video(file):
            vid_path = f"/home/{curent_user}/Videos"
            shutil.move(file, vid_path)
        elif is_audio(file):
            audio_path = f"/home/{curent_user}/Music"
            shutil.move(file, audio_path)
else:
    try:
        os.chdir(input_path)
        #print(os.getcwd())
        #print(os.listdir())
        for file in os.listdir(): 
            if is_audio(file):
                 audio_p = f"/home/{curent_user}/Music"
                 shutil.move(file, audio_p)
            elif is_video(file):
                video_path = f"/home/{curent_user}/Videos"
                shutil.move(file, video_path)

            elif is_image(file):
                img_path = f"/home/{curent_user}/Pictures"
                shutil.move(file, img_path)

            elif is_screenshot(file):
                scrn_shot = f"/home/{curent_user}/Screenhot"
                if not os.path.exists(scrn_shot):
                    os.mkdir(scrn_shot)
                shutil.move(file, scrn_shot)

            elif is_document(file):
                doc_path = f"/home/{curent_user}/Document"
                shutil.move(file, doc_path)

            elif is_data(file):
                data_path = f"/home/{curent_user}/Data"
                if not os.path.exists(data_path):
                    os.mkdir(data_path)
                shutil.move(file, data_path)

    except OSError as e:
        print("Error: ", e)
