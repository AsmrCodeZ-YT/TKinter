import tkinter as tk
from tkinter.filedialog import askdirectory
from tkinter import messagebox
from pytube import YouTube

#### pytube ????

window = tk.Tk()
window.title("YouTube Downloader")
window.configure(bg='Black')


def widgets():
    link_input = tk.Entry(window,background="yellow", width=20,
                          textvariable=video_link, font=("ubuntu", 20) )
    link_input.grid(row=0, column=1)

    link_input = tk.Entry(window, background="yellow", width=20,
                          textvariable=download_dir, font=("ubuntu", 20))
    link_input.grid(row=1, column=1, sticky="w")

    #bottom for Youtube
    download_btm = tk.Button(window, text="Download", width=10,
                             height=3, bg="blue", fg="White", command=download)
    download_btm.grid(row=0 ,column=2,padx=15)
    
    #bootom for dir
    place_btm = tk.Button(window, text="Open", width=10,
                          height=3, bg="red", fg="White", command=browse)
    place_btm.grid(row=1 ,column=2,padx=15)


################## function for input
def browse():
    directtory = askdirectory(initialdir="Your Directory", title="save")
    download_dir.set(directtory)

def download():
    link = video_link.get()
    save_dir = download_dir.get()
    yt = YouTube(link)
    yt.streams.filter(res="720p").download(save_dir)
    messagebox.showinfo(title="Success", message="Your Video Download Successfully")
#################

download_dir = tk.StringVar()
video_link = tk.StringVar()
sel=tk.StringVar() # string variable 

widgets()
window.mainloop()