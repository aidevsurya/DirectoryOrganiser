#!/usr/bin/python3

from tkinter import filedialog, messagebox
from shutil import move
from os import path
import os, sys

path = filedialog.askdirectory()

folder_ex = {
    'Programming Files': set(['ipynb','cpp','asm','c','h','hpp','css','vb','go','r', 'py', 'java', 'cs', 'js', 'vsix', 'jar', 'cc', 'ccc', 'html', 'xml', 'kt','bat','sh','ps']),
    'Compressed': set(['zip', 'rar', 'arj', 'gz', 'sit', 'sitx', 'sea', 'ace', 'bz2', '7z']),
    'Applications': set(['exe', 'msi', 'deb', 'rpm']),
    'Pictures':  set(['jpeg', 'jpg', 'png', 'gif', 'tiff', 'raw', 'webp', 'jfif', 'ico', 'psd', 'svg', 'ai']),
    'Videos':  set(['mp4', 'webm', 'mkv', 'MPG', 'MP2', 'MPEG', 'MPE', 'MPV', 'OGG', 'M4P', 'M4V', 'WMV', 'MOV', 'QT', 'FLV', 'SWF', 'AVCHD', 'avi', 'mpg', 'mpe', 'mpeg', 'asf', 'wmv', 'mov', 'qt', 'rm']),
    'Documents': set(['txt', 'pdf', 'doc', 'xlsx', 'pdf', 'ppt', 'pps', 'docx', 'pptx']),
    'Music':  set(['mp3', 'wav', 'wma', 'mpa', 'ram', 'ra', 'aac', 'aif', 'm4a', 'tsa']),
    'Torrents': set(['torrent']),
    'Other': set([])
}


def create_folders():
    '''Creates the required folders to organize files ('Pictures', 'Videos'..).
    '''
    for root in folder_ex:
        try:
            os.mkdir(os.path.join(path,root))
            print(f'{root:20} Created ✔')
        except OSError:
            print(f'{root:20} Already Exists')


def get_folder(ext):
    '''Returns the Folder that corresponds to the given extension.

    Args:
        ext (String): The extension of the file.

    Returns:
        String: The name of the Folder that holds the ext.
    '''
    for f, ex in folder_ex.items():
        if ext in ex:
            return f
    return 'Other'


def start():
    '''Organize files on the current directory, each to the corresponding folder.
    '''
    for filename in os.listdir(path):
        # Check it's not filemover.py, a hidden file or a directory
        if filename != __file__ and filename[0] != '.' and '.' in filename:
            ext = os.path.basename(filename).split('.')[-1]
            folder = os.path.join(path,get_folder(ext))
            if not os.path.isfile(os.path.join(folder, filename)):
                move(os.path.join(path,filename), os.path.join(path,folder))


if __name__ == '__main__':
    if path == "":
       messagebox.showerror("Empty Path","You haven't Selected any Directory")
       sys.exit()
    create_folders()
    start()
    messagebox.showinfo("Completed","Files Organized Successfully.")