import os, shutil
import customtkinter as Tk

Tk.set_appearance_mode("dark")
Tk.set_default_color_theme("dark-blue")

TK = Tk.CTk()
TK.geometry("500x400")
TK.title("File Sorter")

frame = Tk.CTkFrame(master=TK)
frame.pack(pady=20, padx=90, fill="both", expand=True)

TextBox = Tk.CTkLabel(master=frame, text="Input Path")
TextBox.pack(pady=12, padx=20)

EntryBox = Tk.CTkEntry(master=frame)
EntryBox.pack(pady=12, padx=20)

UserPath = f'{EntryBox.get()}'
path1 = f'{UserPath}/PDF'
path2 = f'{UserPath}/PNG JPEG'
path3 = f'{UserPath}/DOCX'
path4 = f'{UserPath}/OBJ MTL'
path5 = f'{UserPath}/APPS'
path6 = f'{UserPath}/BLEND'
path7 = f'{UserPath}/AUDIO'
path8 = f'{UserPath}/VIDEO'

paths = [path1, path2, path3, path4, path5, path6, path7, path8]

def SortObjects():
    UserPath = f'{EntryBox.get()}'
    Items = os.listdir(UserPath)
    for items in Items:
        Split_Text = os.path.splitext(items)

        File_extension = Split_Text[1]
        print(File_extension)

        if File_extension == ".png":
            src_path = os.path.join(UserPath, items)
            dst_path = os.path.join(f'{UserPath}/PNG JPEG', items)
            shutil.move(src_path, dst_path)
        elif File_extension == ".jpg":
            src_path = os.path.join(UserPath, items)
            dst_path = os.path.join(f'{UserPath}/PNG JPEG', items)
            shutil.move(src_path, dst_path)
        elif File_extension == ".pdf":
            src_path = os.path.join(UserPath, items)
            dst_path = os.path.join(f'{UserPath}/PDF', items)
            shutil.move(src_path, dst_path)
        elif File_extension == ".docx":
            src_path = os.path.join(UserPath, items)
            dst_path = os.path.join(f'{UserPath}/DOCX', items)
            shutil.move(src_path, dst_path)
        elif File_extension == ".obj":
            src_path = os.path.join(UserPath, items)
            dst_path = os.path.join(f'{UserPath}/OBJ MTL', items)
            shutil.move(src_path, dst_path)
        elif File_extension == ".mtl":
            src_path = os.path.join(UserPath, items)
            dst_path = os.path.join(f'{UserPath}/OBJ MTL', items)
            shutil.move(src_path, dst_path)
        elif File_extension == ".exe":
            src_path = os.path.join(UserPath, items)
            dst_path = os.path.join(f'{UserPath}/APPS', items)
            shutil.move(src_path, dst_path)
        elif File_extension == ".blend":
            src_path = os.path.join(UserPath, items)
            dst_path = os.path.join(f'{UserPath}/BLEND', items)
            shutil.move(src_path, dst_path)
        elif File_extension == ".mp3":
            src_path = os.path.join(UserPath, items)
            dst_path = os.path.join(f'{UserPath}/AUDIO', items)
            shutil.move(src_path, dst_path)
        elif File_extension == ".m4a":
            src_path = os.path.join(UserPath, items)
            dst_path = os.path.join(f'{UserPath}/AUDIO', items)
            shutil.move(src_path, dst_path)
        elif File_extension == ".mp4":
            src_path = os.path.join(UserPath, items)
            dst_path = os.path.join(f'{UserPath}/VIDEO', items)
            shutil.move(src_path, dst_path)
        elif File_extension == ".wmv":
            src_path = os.path.join(UserPath, items)
            dst_path = os.path.join(f'{UserPath}/VIDEO', items)
            shutil.move(src_path, dst_path)
        


def FolderCreation():

    for path in paths:
        try:
            os.makedirs(path)
        except FileExistsError:
            TextBox1.configure(text="A Folder Already Exists")
        except:
            TextBox1.configure(text="Something is wrong with your Input")
        else:
            E = 0
    
def SettingsWindow():
    Case = Tk.CTk()
    Case.title("Settings")
    Case.geometry("700x400")

    frame1 = Tk.CTkFrame(master=Case)
    frame1.pack(pady=20, padx=90, fill="both", expand=True)

    TextBox1 = Tk.CTkLabel(master=frame1, text="Add New Directory To List")
    TextBox1.pack(pady=12, padx=20)

    EntryBox = Tk.CTkEntry(master=frame1)
    EntryBox.pack(pady=12, padx=20)

    def appendObject():
        paths.append("/"+EntryBox.get())
        print(paths)
        TextBox2.configure(text=paths)

    ButtonBox1 = Tk.CTkButton(master=frame1, text="AddObject", command=appendObject)
    ButtonBox1.pack(pady=12, padx=20)

    TextBox2 = Tk.CTkLabel(master=frame1, text="Input Path")
    TextBox2.pack(pady=12, padx=20)

    

    




    Case.mainloop()

ButtonBox1 = Tk.CTkButton(master=frame, text="Convert", command=SortObjects)
ButtonBox1.pack(pady=12, padx=20)

ButtonBox2 = Tk.CTkButton(master=frame, text="Create Folders", command=FolderCreation)
ButtonBox2.pack(pady=12, padx=20)

ButtonBox2 = Tk.CTkButton(master=frame, text="Settings", command=SettingsWindow)
ButtonBox2.pack(pady=12, padx=20)

TextBox1 = Tk.CTkLabel(master=frame, text="")
TextBox1.pack(pady=12, padx=20)

TK.mainloop()





