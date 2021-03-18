from tkinter import *
import generateGraph
import ctypes
from win32api import GetSystemMetrics
import tkinter as tk
import webbrowser
from tkinter import messagebox 
# from threading import Thread

class RoundedButton(tk.Canvas):
    def __init__(self, parent, bg, width, height, text, command=None, color = "red", textColor = "black", padding = 0, cornerradius = None):
        height = width if height == None else height
        cornerradius = min(width, height) / 2 if cornerradius == None else cornerradius
        fontsize = getFontSize(width, text)

        tk.Canvas.__init__(self, parent, borderwidth=0, 
            relief="flat", highlightthickness=0, bg=bg)
        self.command = command

        if cornerradius > 0.5*width:
            print("Error: cornerradius is greater than width.")
            return None

        if cornerradius > 0.5*height:
            print("Error: cornerradius is greater than height.")
            return None

        rad = 2*cornerradius
        def shape():
            self.create_polygon((padding,height-cornerradius-padding,padding,cornerradius+padding,padding+cornerradius,padding,width-padding-cornerradius,padding,width-padding,cornerradius+padding,width-padding,height-cornerradius-padding,width-padding-cornerradius,height-padding,padding+cornerradius,height-padding), fill=color, outline=color)
            self.create_arc((padding,padding+rad,padding+rad,padding), start=90, extent=90, fill=color, outline=color)
            self.create_arc((width-padding-rad,padding,width-padding,padding+rad), start=0, extent=90, fill=color, outline=color)
            self.create_arc((width-padding,height-rad-padding,width-padding-rad,height-padding), start=270, extent=90, fill=color, outline=color)
            self.create_arc((padding,height-padding-rad,padding+rad,height-padding), start=180, extent=90, fill=color, outline=color)

        id = shape()
        (x0,y0,x1,y1)  = self.bbox("all")
        width = (x1-x0)
        height = (y1-y0)

        self.create_text(width/2, height/2, text=text, font = ("", fontsize), fill = textColor)

        self.configure(width=width, height=height)
        self.bind("<ButtonPress-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)

    def _on_press(self, event):
        # print(event)
        self.configure(relief="sunken")

    def _on_release(self, event):
        # print(event)
        self.configure(relief="raised")
        if self.command is not None:
            self.command()

def createHeading(headingText, master, multiplier = 1):
    # headingText = "Run Time Visualizer"
    heading = Label(master, text = headingText, font = ("", int(getFontSize(WIDTH, headingText) * multiplier)), fg = "black", bg = "#008057")
    heading.place(x = 0, y = 0, width = WIDTH, height = 15*hu)

def createSubtitle(master, subtitleText, multiplier, yPosition, _height):
    subtitle = Label(master, text = subtitleText, font = ("", getFontSize(WIDTH, subtitleText) * multiplier), fg = "white", bg = BACKGROUND)
    subtitle.place(x = 0, y = yPosition, width = WIDTH, height = _height)

def createButton(xPosition, text, func, buttonMaster = None, buttonWidth = None, yPosition = None, buttonHeight = None):
    if buttonMaster is None:buttonMaster = root
    if buttonWidth is None:buttonWidth = 40*wu
    if buttonHeight is None:buttonHeight = 20*hu
    if yPosition is None:yPosition = 75*hu

    buttonForeGround = "#802D00"
    aboutButton = RoundedButton(buttonMaster, BACKGROUND, buttonWidth, buttonHeight, text,  func, buttonForeGround)
    aboutButton.place(x = xPosition, y = yPosition)

def exitFunction(master):
    master.quit()
    master.place_forget()
    

def createBackButton(master, width, _x = 0, _y = 0):
    Button(master, text = "Go Back", font = (" ", getFontSize(width, 7 * " ")), justify = "center", bg = "red", command = lambda : exitFunction(master)).place(x = _x, y = _y)


def aboutProgram():
    win = Frame(root, bg = BACKGROUND)

    createHeading("About The Program", win, 0.8)
    createBackButton(win, 17.5*wu, 0, 15*hu)

    subtitleText = """This Run Time Visualizer is made with python, it visualizes
different run times of algorithms with different sizes of inputs, it can
be used for estimating the Big O Notation of Algorithms. the user's python
file should have a function named "main"(this function will be the algorithm
whose time would be measured), the python file would also need to have a 
dictionary named "inputTimes", the dictionary would need to have numbers 
as the keys and any data-structure (list/tuples/integers/string etc.) as 
a value, The data-structure in the dictionary values should be the 
input for the function and the keys corresponding to each data-structure
in the dictionary should be representing how large the data-structure is.
"""

    createSubtitle(win, subtitleText, 17, 25*hu, 55*hu)

    createButton(wu*20, "view on github", lambda : webbrowser.open("https://github.com/Ved-programmer/Run-Time-Visualizer"), win, wu*60, 80*hu, 15*hu)


    win.place(x = 0, y = 0, width = WIDTH, height = HEIGHT)

    win.mainloop()

def createGraph(event = None):
    # messagebox.showinfo("graph generation", "The graph will be generated in a new window in some time, please click on ok to view the graph, the window might lag but after you close the graph it will come back to normal.")

    generateGraph.generateGraphFromFile(userFile.get())


def setDimensions(root):
    ctypes.windll.shcore.SetProcessDpiAwareness(2)
    global WIDTH, HEIGHT, wu, hu

    WIDTH, HEIGHT = GetSystemMetrics(0)*5//7, GetSystemMetrics(1)*5//7
    wu = WIDTH/100
    hu = HEIGHT/100
    root.geometry(f"{WIDTH}x{HEIGHT}")

def setWindowSettings(root):
    global BACKGROUND

    root.title("Run Time Visualizer")
    algoExpertLogo = PhotoImage(file = 'algoExpertLogo.png')
    root.iconphoto(False, algoExpertLogo)
    BACKGROUND = "#020080"
    root.config(bg = BACKGROUND)

def createEntry(root):
    global userFile

    userFileWidth = int(WIDTH*9/10)
    userFile = Entry(root,  font = ("", getFontSize(userFileWidth, " "*25)), background = "#03a7ff")
    userFile.insert(0, "Enter Your File Name Here")
    userFile.place(x = (WIDTH - userFileWidth)//2, y = 50*hu, width = userFileWidth, height = 20*hu)

def main(root):

    setDimensions(root)
    setWindowSettings(root)

    createHeading("Run Time Visualizer", root)

    subtitleText = """Please click the 'About Program' button to understand how this program works.
Don't include the '.py' or '.pyw' extension when entering your file name. 
The file should be in the same folder in which this program's files are kept.
Once you have entered the file name, press the 'Create Graph' button."""

    createSubtitle(root, subtitleText, 6, 20*hu, 25*hu)

    createEntry(root)

    createButton(5*wu, "About Program", aboutProgram)
    createButton(55*wu, "Create Graph", createGraph)

    root.bind("<Return>", createGraph)

    root.mainloop()


def getFontSize(buttonWidth, text):
    return int(buttonWidth // len(text))


if __name__ == '__main__':
    root = Tk()
    main(root)
    


