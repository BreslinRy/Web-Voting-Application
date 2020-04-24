#   Rylie Breslin
#   SE420 Assignment 4
from tkinter import *
from Count_V2 import count

mgui = Tk()     # Setting tkinter equal to a callable name
mgui.title('Vote')      # Setting the title for the GUI
voteSheriff = IntVar()     # Will allow us to tell if this option was checked
voteMayor = IntVar()  # Will allow us to tell if this option was checked

# Pound defines don;t exist in python so replace any magic numbers with these
screensize = 200    #
padAmount = 0       #
#--------------------


#   Taken from user Unutbu on Stack Overflow
#   Changes size of the GUI to full screen
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


def category(position, candidate1, candidate2, variable, row):
    # Creates a label that tells the user what category is being voted for (tkinter name, tezt displayed,...
    # location on screen)
    Label(mgui, text='%s' % position, font=("Ariel", 36), padx=(mgui.winfo_screenwidth() / 2) - 25).grid(row=row,
                                                                                                         sticky=W)
    # Creating a checkbox(tkinter name, candidate option, save state of box location, location on screen)
    Radiobutton(mgui, text='%s' % candidate1, variable=variable, value=1,
                padx=mgui.winfo_screenwidth() / 2).grid(row=row + 1, sticky=W)
    # Creating a checkbox(tkinter name, candidate option, save state of box location, location on screen)
    Radiobutton(mgui, text='%s' % candidate2, variable=variable, value=2,
                padx=mgui.winfo_screenwidth() / 2).grid(row=row + 2, sticky=W)


def submit():
    count(voteSheriff.get())   # Counts the votes for each candidate (value returned from the radiobutton)
    count(voteMayor.get())  # Counts the votes for each candidate (value returned from the radiobutton)


class GUIApplication:
    # Adds a position to vote for and the candidates
    category('Sheriff', 'John Johnson', 'Sam Samson', voteSheriff, 0)

    # Adds a position to vote for and the candidates (position, candidate 1, candidate 2, variable that the tally is
    # saved under, row of where it the option is placed in the GUI
    category('Mayor', 'John Doe', 'Jane Doe', voteMayor, 3)

    # Creating a button(tkinter instance, Button text, button font and size, button color, ...
    # what function the button calls, location on screen)
    button = Button(mgui, text='Submit', font=("Ariel", 20), bg='gray', command=mgui.quit,
                    padx=mgui.winfo_screenwidth()/2).grid(row=7, sticky=W, pady=4)

    app = FullScreenApp(mgui)       # Calls function to make the gui full screen (tkinter instance)
    mgui.mainloop()     # Creates the GUI

    submit()


# Launches and instance of the gui created above
gui = GUIApplication()

