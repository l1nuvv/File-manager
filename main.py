from tkinter import *
import shutil
import os
import easygui
from tkinter import filedialog
from tkinter import messagebox as mb


def open_window():
    read = easygui.fileopenbox()
    return read


def open_file():
    string = open_window()
    try:
        os.startfile(string)
    except FileNotFoundError:
        mb.showinfo('confirmation', 'File not found!')


def copy_file():
    source1 = open_window()
    destination1 = filedialog.askdirectory()
    shutil.copy(source1, destination1)
    mb.showinfo('confirmation', "File Copied !")


def delete_file():
    del_file = open_window()
    if os.path.exists(del_file):
        os.remove(del_file)
    else:
        mb.showinfo('confirmation', 'File not found!')


def rename_file():
    chosenFile = open_window()
    path1 = os.path.dirname(chosenFile)
    extension = os.path.splitext(chosenFile)[1]
    print("Enter new name for the chosen file")
    newName = input()
    path = os.path.join(path1, newName + extension)
    print(path)
    os.rename(chosenFile, path)
    mb.showinfo('confirmation', "File Renamed!")


def move_file():
    source = open_window()
    destination = filedialog.askdirectory()
    if source == destination:
        mb.showinfo('confirmation', "Source and destination are same")
    else:
        shutil.move(source, destination)
        mb.showinfo('confirmation', "File Moved!")


def make_folder():
    newFolderPath = filedialog.askdirectory()
    print('Enter name of new folder')
    newFolder = input()
    path = os.path.join(newFolderPath, newFolder)
    os.mkdir(path)
    mb.showinfo('confirmation', "Folder created!")


def remove_folder():
    delFolder = filedialog.askdirectory()
    os.rmdir(delFolder)
    mb.showinfo('confirmation', "Folder Deleted!")


def list_files():
    folderList = filedialog.askdirectory()
    sortList = sorted(os.listdir(folderList))
    i = 0
    print("Files in", folderList, "folder are:")
    while i < len(sortList):
        print(sortList[i] + '\n')
        i += 1


# Tkinter GUI

root = Tk()

Label(root, text='l1nuvv File Manager', font=('Helvetica', 16), fg='blue').grid(row=5, column=2)

Button(root, text="Open a file", command=open_file).grid(row=15, column=2)

Button(root, text="Copy a file", command=copy_file).grid(row=25, column=2)

Button(root, text="Delete a file", command=delete_file).grid(row=35, column=2)

Button(root, text="Rename a file", command=rename_file).grid(row=45, column=2)

Button(root, text="Move a file", command=move_file).grid(row=55, column=2)

Button(root, text="Create a folder", command=make_folder).grid(row=75, column=2)

Button(root, text="Delete a folder", command=remove_folder).grid(row=65, column=2)

Button(root, text="List all files in directory", command=list_files).grid(row=85, column=2)

root.mainloop()
