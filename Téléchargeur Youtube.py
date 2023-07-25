from pytube import YouTube
from pytube import *
from customtkinter import *
from tkinter import messagebox


def mp3():
    try:
        url = ent.get()
        
        YouTube(url).streams.get_audio_only().download(r".\Desktop\Audio")
        messagebox.showinfo(title="Fichier audio téléchargée", message="Votre fichier audio a été bien téléchargée")
    except:
        messagebox.showerror(title="Le fichier audio n'est pas téléchargée", message="Votre fichier audio n'a pas été téléchargée")

def mp4():
    try:
        url = ent.get()
        YouTube(url).streams.get_highest_resolution().download(r".\Desktop\Video")
        messagebox.showinfo(title="Vidéo téléchargée", message="Votre vidéo a été bien téléchargée")
    except:
        messagebox.showerror(title="La vidéo n'est pas téléchargée", message="Votre vidéo n'a pas été téléchargée")

root = CTk()
set_appearance_mode('system')
root.geometry("566x384")
root.resizable(False,False)
root.title("Téléchargeur Youtube")
root.iconbitmap("yt.ico")


fnt = CTkFont(family="Agency FB",size=48,weight="bold")
ttl = CTkLabel(root,text="Téléchargeur Youtube",font=fnt)
ttl.grid(row=0,column=2,pady=10)

fnt2 =  CTkFont(family="Agency FB",size=24)
ent_lbl = CTkLabel(root,text="Entrez le lien: ",font=fnt2 )
ent_lbl.grid(row=1,column=1,pady=10)

ent = CTkEntry(root, placeholder_text=("Entrez l'URL"))
ent.grid(row=1,column=2,pady=10,sticky="ew")

mp4_btn = CTkButton(root,fg_color='Red',text="MP4",text_color='Black',hover_color="White",command= mp4)
mp4_btn.grid(row=2,column=1,pady=10,padx=10,ipady=10,ipadx=15)

mp3_btn = CTkButton(root,fg_color='Red',text="MP3",text_color='Black',command=mp3,hover_color="White")
mp3_btn.grid(row=3,column=1,pady=10,padx=10,ipady=10,ipadx=15)



root.mainloop()
