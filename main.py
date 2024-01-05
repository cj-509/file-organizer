import os
#======== a script that manage files

input_path = input("Enter files location: ")


if not input_path:
    curent_user = os.environ.get('USER') or os.environ.get('LOGNAME')
    change_to_dir = f"/home/{curent_user}/Downloads"
    os.chdir(change_to_dir)
    print(os.getcwd())    

else:
    print(input_path)