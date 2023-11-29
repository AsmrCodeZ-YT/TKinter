import customtkinter
from tkinter.filedialog import askdirectory
from tkinter import messagebox
from pytube import YouTube


customtkinter.set_appearance_mode("dark") 
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.title("YouTube Downloader")
root.geometry("425x80")
# root.geometry()


def widgets():
    link_input = customtkinter.CTkEntry(root,width=250,height=40,
                          textvariable=video_link, font=("ubuntu", 20),text_color="white",corner_radius=5)
    link_input.grid(row=0, column=1)
    
    
    link_input = customtkinter.CTkEntry(root,width=250,height=40,
                          textvariable=download_dir, font=("ubuntu", 20),text_color="white",corner_radius=5)
    link_input.grid(row=1, column=1, sticky="w")

    # bottom for Youtube
    download_btm = customtkinter.CTkButton(root,text="Download",
                            command=download)
    download_btm.grid(row=0 ,column=2,padx=15)
    
    #bootom for dir
    place_btm = customtkinter.CTkButton(root, text="Save",
                        command=browse)
    place_btm.grid(row=1 ,column=2,padx=15)


################## function for input
def browse():
    directtory = askdirectory(initialdir="Your Directory", title="save")
    download_dir.set(directtory)

def download():
    link = video_link.get()
    save_dir = download_dir.get()
    # print(link,save_dir)
    yt = YouTube(link)
    yt.streams.filter(res="720p").download(save_dir)
    messagebox.showinfo(title="Success", message="Your Video Download Successfully")
    
# #################

download_dir = customtkinter.StringVar()
video_link   = customtkinter.StringVar()
sel          = customtkinter.StringVar() # string variable 


widgets()
root.mainloop()