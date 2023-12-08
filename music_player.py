from tkinter import*
import tkinter as tk
from tkinter import ttk, filedialog
from pygame import mixer
import os


root = Tk()
root.title("Music Player")
root.geometry('920x470+290+85')
root.resizable(False,False)
root.configure(bg="#ffdde1")

mixer.init()

def open_folder():
    #Ask user to select directory path
    dir_path = filedialog.askdirectory()
    if dir_path:
        # change the current working directory to new path
        os.chdir(dir_path)
        songs = os.listdir(dir_path)
#       print(songs)
        for song in songs:
            if song.endswith(".mp3"):
                play_list.insert(END,song)
        

def play_song():
    music_name = play_list.get(ACTIVE)
    mixer.music.load(play_list.get(ACTIVE))
    mixer.music.play()
    music.config(text=music_name[0:-4])



#image icon
image_icon = PhotoImage(file="music_player/music icon.png")
root.iconphoto(False,image_icon)

#top photo image
top_photo = PhotoImage(file="music_player/Untitled design.png")
Label(root,image=top_photo,bg="#ffdde1").pack()

#logo
Logo = PhotoImage(file="music_player/downloadg.png")
img_logo = Logo.subsample(2)
Label(root,image=img_logo,bg="#ffdde1").place(x=80,y=50)

#button_play
play_button = PhotoImage(file="music_player/play button.png")
img_play = play_button.subsample(9)
Button(root,image=img_play,bg="#ffdde1",bd=0,command = play_song).place(x=120,y=220)

#button_stop
stop_button = PhotoImage(file="music_player/stop button.png")
img_stop = stop_button.subsample(11)
Button(root,image=img_stop,bg="#ffdde1",bd=0,command=mixer.music.stop).place(x=40,y=325)

#button_resume
play_resume = PhotoImage(file="music_player/resume button.png")
img_resume = play_resume.subsample(11)
Button(root,image=img_resume,bg="#ffdde1",bd=0,command=mixer.music.unpause).place(x=110,y=325)

#button_pause
play_pause = PhotoImage(file="music_player/pause button.png")
img_pause = play_pause.subsample(11)
Button(root,image=img_pause,bg="#ffdde1",bd=0,command=mixer.music.pause).place(x=180,y=325)

#label
music = Label(root,text="",font=("arial",15),fg="white",bg="#0f1a2b")
music.place(x=150,y=340,anchor="center")


#Music_track(menu)
music_track = PhotoImage(file="music_player/menu.png")
Label(root,image=music_track,bg="#ffdde1").pack(padx=10,pady=50,side=RIGHT)

#frame
music_frame = Frame(root,bd=2,relief=RIDGE)
music_frame.place(x=300,y=140,width=560,height=250)

#button_on frame
Button(root,text="Open Folder",width=15,height=2,font=("arial",10,"bold"),fg="white",bg="#21b3de",command=open_folder).place(x=320,y=150)

scroll = Scrollbar(music_frame)
play_list = Listbox(music_frame,width=100,font=("arial",10),bg="#333333",fg="grey", selectbackground="lightblue",cursor="hand2",bd=0,yscrollcommand=scroll.set)
scroll.config(command=play_list.yview)
scroll.pack(side=RIGHT,fill=Y)
play_list.pack(side=LEFT,fill=BOTH)




root.mainloop()