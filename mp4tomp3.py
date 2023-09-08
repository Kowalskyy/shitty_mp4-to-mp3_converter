from moviepy.editor import VideoFileClip
import tkinter as tk
from tkinter import filedialog
import os

root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename(filetypes=[("video", "*.mp4")])
folder_path = filedialog.askdirectory(title="lmfao")
def converttomp3(file_path, folder_path):
    video=VideoFileClip(file_path)
    audio=video.audio
    audio.write_audiofile(folder_path)
    audio.close()
    video.close()
audio = os.path.splitext(os.path.basename(file_path))[0]
converttomp3(file_path, f'{folder_path}\\{audio}.mp3')