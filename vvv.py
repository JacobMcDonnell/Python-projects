import os
import json
import time
import requests
import praw
from tkinter import *
import tkinter as tk

class pageindex(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

     

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        #container.pack(side="top", fill="both", expand=True)
        container.grid(row=1, rowspan=2, column=1, columnspan=2)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (ytscbyname, ytscbyid, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("ytscbyname")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class ytscbyname(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#323232")
        def Youtube_stats():
            channel = ytuser.get()
            r = requests.get('https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername='+channel+'&key=AIzaSyDdh94NZll6tzTUmO17d5nrh0zMuKcajaw')
            j = r.json()
            subs = j['items'][0]['statistics']['subscriberCount']
            views = j['items'][0]['statistics']['viewCount']
            ytsubs.config(text="{:,}".format(int(subs)))
            ytviews.config(text="{:,}".format(int(views)))
        def Ytreset():
            ytsubs.config(text="")
            ytviews.config(text="")
      

        ytlabel = tk.Label(self, text="Youtube channel Stats by Name", bg="#323232", fg="white", font="none 15 bold")
        ytuser = tk.Entry(self)
        ytgo = tk.Button(self, text="GO", bg="green", command=Youtube_stats)
        ytreset = tk.Button(self, text="Reset", bg="red", command=Ytreset)
        ytsublabel = tk.Label(self, text="Total subs:", bg="#323232", fg="white", font="none 15")
        ytviewslabel = tk.Label(self, text="Total Views:", bg="#323232", fg="white", font="none 15")
        ytsubs = tk.Label(self, text="", bg="#323232", fg="white", font="none 15")
        ytviews = tk.Label(self, text="", bg="#323232", fg="white", font="none 15")

        menu = tk.Menu(self.master)
        self.master.config(menu=menu)
        YoutubeSubCounter = tk.Menu(menu)
        YoutubeSubCounter.add_command(label="Youtube channel Stats by Name", command=lambda: controller.show_frame("ytscbyname"))
        YoutubeSubCounter.add_command(label="Youtube channel Stats by ID", command=lambda: controller.show_frame("ytscbyid"))
        menu.add_cascade(label="Youtube Channel Stats", menu=YoutubeSubCounter)
        
        ytlabel.grid(row=1, column=1, columnspan=2)
        ytuser.grid(row=2, column=1, columnspan=2)
        ytgo.grid(row=3, column=1, sticky="E")
        ytreset.grid(row=3, column=2, sticky="W")
        ytsublabel.grid(row=4, column=1)
        ytsubs.grid(row=4, column=2)
        ytviewslabel.grid(row=5, column=1)
        ytviews.grid(row=5, column=2)


        

        button1 = tk.Button(self, text="Go to Page One",
                            command=lambda: controller.show_frame("ytscbyid"))
        button2 = tk.Button(self, text="Go to Page Two",
                            command=lambda: controller.show_frame("PageTwo"))
        button1.grid(row=6, column=1)
        button2.grid(row=6, column=2)

        
class ytscbyid(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#323232")
        def Youtube_stats():
            ytid = ytuser.get()
            r = requests.get('https://www.googleapis.com/youtube/v3/channels?part=statistics&id='+ytid+'&key=AIzaSyDdh94NZll6tzTUmO17d5nrh0zMuKcajaw')
            j = r.json()
            subs = j['items'][0]['statistics']['subscriberCount']
            views = j['items'][0]['statistics']['viewCount']
            ytsubs.config(text="{:,}".format(int(subs)))
            ytviews.config(text="{:,}".format(int(views)))
        def Ytreset():
            ytsubs.config(text="")
            ytviews.config(text="")
      

        ytlabel = tk.Label(self, text="Youtube channel Stats by channel ID", bg="#323232", fg="white", font="none 15 bold")
        ytuser = tk.Entry(self)
        ytgo = tk.Button(self, text="GO", bg="green", command=Youtube_stats)
        ytreset = tk.Button(self, text="Reset", bg="red", command=Ytreset)
        ytsublabel = tk.Label(self, text="Total subs:", bg="#323232", fg="white", font="none 15")
        ytviewslabel = tk.Label(self, text="Total Views:", bg="#323232", fg="white", font="none 15")
        ytsubs = tk.Label(self, text="", bg="#323232", fg="white", font="none 15")
        ytviews = tk.Label(self, text="", bg="#323232", fg="white", font="none 15")

        ytlabel.grid(row=1, column=1, columnspan=2)
        ytuser.grid(row=2, column=1, columnspan=2)
        ytgo.grid(row=3, column=1, sticky="E")
        ytreset.grid(row=3, column=2, sticky="W")
        ytsublabel.grid(row=4, column=1)
        ytsubs.grid(row=4, column=2)
        ytviewslabel.grid(row=5, column=1)
        ytviews.grid(row=5, column=2)


        

        button1 = tk.Button(self, text="Go to Page One",
                            command=lambda: controller.show_frame("ytscbyname"))
        button2 = tk.Button(self, text="Go to Page Two",
                            command=lambda: controller.show_frame("PageTwo"))
        button1.grid(row=6, column=1)
        button2.grid(row=6, column=2)
class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("ytscbyid"))
        button.pack()


if __name__ == "__main__":
    app = pageindex()
    app.mainloop()
