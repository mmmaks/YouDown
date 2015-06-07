from Tkinter import *
from PIL import Image, ImageTk
import pafy

#Function to download the entered Format of Video
def downloadfun():
    print vec.get()
    st = vec.get()
    global v
    video = v.streams[st]
    print "Size in KB : ",video.get_filesize()/1024
    video.download(filepath="downloads/"+video.title + "." + video.extension)

#window configure
root = Tk()
root.wm_title("Youtube Download Manager(YDM)")
root.configure(background='black')
root.geometry("600x400")

global v
global pos
pos=40
vec = IntVar()
vec.set(0)

#function which will show all info about video after you clicked Download
def poo():
    #print("URL : %s\n" %(e.get()))
    url = e.get()
    global v
    v = pafy.new(url)
    b = v.streams
    global pos
    global s
    global man
    x=0
    print "video Title : ",v.title
    print "video.duration : ",v.duration
    print "video length : ",v.length
    for i in b:
        #Label(root, text=str(i)).grid(row=pos, column=0)
        size_KB = i.get_filesize()/(1024)
        size_MB = size_KB/1024
        mand = str(i)+"  \t\t  Size In KB "+str(size_KB)+"  \t\t  Size in MB "+str(size_MB)
        #print mand
        Radiobutton(root, 
                text=mand,
                padx = 200,
                variable=vec,
                command=downloadfun,
                value=x).pack(anchor=W)
        x=x+1
        pos=pos+1
        size_v = i.get_filesize()/1024
        #print(str(i),size_v," KB")
        #print i.get_filesize()/1024



Label(root, text="Enter URL").grid(row=pos)
e = Entry(root)

e.grid(row=pos, column=5)
pos = pos+2

Button(root, text='Download', command = poo).grid(row=pos-2, column=9, sticky=W, pady=4)

mainloop()
