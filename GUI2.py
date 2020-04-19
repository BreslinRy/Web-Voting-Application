#   Rylie Breslin
#   SE420 Assignment 4
from tkinter import *
from Count_V2 import count

#   Taken from user Unutbu on Stack Overflow
#   Resizes the GUI to full screen
#   Press escape to toggle the size between default and full screen
class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master = master
        pad = 3
        self._geom = '200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth() - pad, master.winfo_screenheight() - pad))
        master.bind('<Escape>', self.toggle_geom)

    def toggle_geom(self, event):
        geom = self.master.winfo_geometry()
        print(geom, self._geom)
        self.master.geometry(self._geom)
        self._geom = geom

# def submit():
    # Interface with a database here

class GUIApplication():
    mgui = Tk()     # Setting tkinter equal to a callable name
    mgui.title('Vote')      # Setting the title for the GUI
    voteSheriff = IntVar()     # Will allow us to tell if this option was checked
    voteMayor = IntVar()  # Will allow us to tell if this option was checked
    voteGovernor = IntVar() # Will allow us to know who was voted for

    # Creates a label that tells the user what category is being voted for (tkinter name, tezt displayed, location on screen)
    Label(mgui, text="Sheriff", font=("Ariel", 36), padx=(mgui.winfo_screenwidth()/2)-25).grid(row=0, sticky=W)

    # Creating a checkbox(tkinter name, candidate option, save state of box location, location on screen)
    Radiobutton(mgui, text='John Johnson', font=("Ariel", 18), variable=voteSheriff, value = 1, padx=mgui.winfo_screenwidth()/2 - 50).grid(row=1, sticky=W)
    # Creating a checkbox(tkinter name, candidate option, save state of box location, location on screen)
    Radiobutton(mgui, text='Sam Samson', font=("Ariel", 18), variable=voteSheriff, value=2, padx=mgui.winfo_screenwidth()/2 - 50).grid(row=2, sticky=W)

    # Creates a label that tells the user what category is being voted for (tkinter name, tezt displayed, location on screen)
    Label(mgui, text="Mayor", font=("Ariel", 36), padx=(mgui.winfo_screenwidth() / 2) - 25).grid(row=4, sticky=W)

    # Creating a checkbox(tkinter name, candidate option, save state of box location, location on screen)
    Radiobutton(mgui, text='Tom Tompson', font=("Ariel", 18), variable=voteMayor, value=1, padx=mgui.winfo_screenwidth() / 2 - 50).grid(row=5,
                                                                                                           sticky=W)
    # Creating a checkbox(tkinter name, candidate option, save state of box location, location on screen)
    Radiobutton(mgui, text='Jack Jackson', font=("Ariel", 18), variable=voteMayor, value=2, padx=mgui.winfo_screenwidth() / 2 - 50).grid(row=6,
                                                                                                         sticky=W)

    # Creates a label that tells the user what category is being voted for (tkinter name, tezt displayed, location on screen)
    Label(mgui, text="Governor", font=("Ariel", 36), padx=(mgui.winfo_screenwidth() / 2) - 50).grid(row=7, sticky=W)

    # Creating a checkbox(tkinter name, candidate option, save state of box location, location on screen)
    Radiobutton(mgui, text='Jim Jimmyson', font=("Ariel", 18), variable=voteGovernor, value=1, padx=mgui.winfo_screenwidth() / 2 - 50).grid(row=8,
                                                                                                               sticky=W)
    # Creating a checkbox(tkinter name, candidate option, save state of box location, location on screen)
    Radiobutton(mgui, text='John Smith', font=("Ariel", 18), variable=voteGovernor, value=2, padx=mgui.winfo_screenwidth() / 2 - 50).grid(row=9,
                                                                                                                sticky=W)

    # Creating a button(tkinter instance, Button text, what function the button calls, location on screen)
    button = Button(mgui, text='Submit', font=("Ariel", 24), command=mgui.quit, padx=mgui.winfo_screenwidth()/2 - 20).grid(row=11, sticky=W, pady=4)

    app = FullScreenApp(mgui)       # Calls function to make the gui full screen (tkinter instance)
    mgui.mainloop()     # Creates the GUI

    count(voteSheriff.get())   # Counts the votes for each candidate (value returned from the radiobutton)
    count(voteMayor.get())  # Counts the votes for each candidate (value returned from the radiobutton)
    count(voteGovernor.get())  # Counts the votes for each candidate (value returned from the radiobutton)

# Launches and instance of the gui created above
gui = GUIApplication()

