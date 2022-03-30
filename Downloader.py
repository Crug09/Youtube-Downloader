import pytube as pt, os
from curses import BUTTON1_CLICKED, window
from tkinter import *
from tkinter import ttk, Text
from pytube import YouTube
from pytube import Playlist
from PIL import Image, ImageTk
from pytube import YouTube


blk = "#1b1b1b"

def Stupid():
    global Sng
    Sng = "Playlist"

Stupid()

def single():
    global Sng
    Sng = YouTube(link.get(1.0, END))



#About the App
app = Tk()
app.title("Downloader")
app.configure(background=blk)
photo = PhotoImage(file = "Icon.png")
app.iconphoto(False, photo)



#Window Size
width = 1280
height = 500
app.geometry(f'{width}x{height}+{100}+{100}')
app.resizable(False, False)




Youtube = Label(app,
    text = "Youtube Downloader", 
    font=("Helvetica", 40),
    relief="sunken",
    bg = blk, fg="white", bd = 0)
Youtube.pack(fill="x")




Text1 = Label(app,
    text = "Enter your\nlink here",
    font = ("helvetica", 18),
    bg = blk,fg="white", bd = 0)
Text1.pack(side=LEFT, anchor=NW, padx=20, pady=8,)




link = Text(width=73, height=1)
link.pack(side=LEFT, anchor=NW, padx=10, pady=20,)




#Download Button
canvas = Canvas(app, bg = blk, width=256, height=256, highlightthickness=0, borderwidth=0)
canvas.place(x = 850, y = 45)

binactive = Image.open("button2.png")
bactive = Image.open("button1.png")

app.binactive = ImageTk.PhotoImage(binactive)
app.bactive = ImageTk.PhotoImage(bactive)

def enter(event):
    button.config(image=app.bactive)

def leave(enter):
    button.config(image=app.binactive)

def Download(self):
    try:
        single()
        Down.config(text='It is a Single Video')
    except:
        try:
            Play = Playlist(link.get(1.0, END))
            print(Play)
            Down.update()
            Down.config(text='It is a Playlist')
            
        except:
            Play = "Single"
            Down.config(text="Your'e link doesn't work")

    

    if Sng != "Playlist":
        Audio = Sng.streams.filter(only_audio=True).first()
        Down.config(text='Downloading: ' + Sng._title)
        Down.update()
        file = Audio.download(output_path=Path.get(1.0, END))
        Down.config(text="Downloading Done")


        #Mp3 stuff
        base, ext = os.path.splitext(file)
        Nfile = base + '.mp3'
        os.rename(file, Nfile)
    
    elif Play != "Single":
        for video in Play.videos:
            Audio = video.streams.filter(only_audio=True).first()
            Down.config(text='Downloading: ' + video.title)
            Down.update()
            file = Audio.download(output_path=Path.get(1.0, END))

            #Mp3 stuff
            base, ext = os.path.splitext(file)
            Nfile = base + '.mp3'
            os.rename(file, Nfile)
        Down.config(text="Downloading Done")

button = Button(app, image=app.binactive, bg = blk, highlightthickness=0, borderwidth=0, activebackground=blk)

canvas.create_window(128, 128, window = button, )

button.bind("<Enter>", enter)
button.bind("<Leave>", leave)
button.bind("<Button-1>", Download)




Text2 = Label(app,
    text = "Directory for\n your music\n(It will make a fold)",
    font=("helvetica", 18),
    bg= blk, fg="white", bd = 0).place(x=20, y= 150)
# Text2.pack(anchor=SW, fill='both')




Path = Text(width=67, height=1)
Path.place(x = 180, y = 180)




Down = Label(app, text='',
    font=('helvetica', 18),
    bg = blk, fg = 'white')
Down.place(x=250, y = 400)




#delete button #1
canvas2 = Canvas(app, width = 16, height = 16)
canvas2.place(x = 770, y= 75)

def Clear1():
    link.delete(1.0, END)

But = ImageTk.PhotoImage(Image.open("Delete.png"))

button2 = Button(app, image=But, command=Clear1)

canvas2.create_window(16, 16, window=button2)


#delete button #2
canvas3 = Canvas(app, width = 16, height = 16)
canvas3.place(x = 740, y= 180)

def Clear2():
    Path.delete(1.0, END)

button3 = Button(app, image=But, command=Clear2)

canvas3.create_window(16, 16, window=button3)



app.mainloop()