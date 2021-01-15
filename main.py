#todo: Description comment
#imports
try: #Try except to account for Python 2.x and 3.x
    import tkinter as tk #3.x
except:
    import Tkinter as tk #2.x

#Constants
G = 9.81
GEOMETRY = "500x200"
TITLE = "Projectile Motion Simulator"
BACKGROUND = "white"

def visualization(master, xi, yi, vi): #todo: visualization and docstring 
    """"""
    master.destroy() #Closes main window
    print("Visualization WIP")

#Main window asking for initial height, distance, and speed
root = tk.Tk(BACKGROUND) 

#Window settings
root.title(TITLE)
root.geometry(GEOMETRY)
root.configure(bg=BACKGROUND)

#Labels for initial x, y, and v with m and m/s as units
xLabel = tk.Label(root, text="xᵢ = ", bg=BACKGROUND)
yLabel = tk.Label(root, text="yᵢ = ", bg=BACKGROUND)
vLabel = tk.Label(root, text="vᵢ = ", bg=BACKGROUND)
xMLabel = tk.Label(root, text="m", bg=BACKGROUND)
yMLabel = tk.Label(root, text="m", bg=BACKGROUND)
msLabel = tk.Label(root, text="m/s", bg=BACKGROUND)

#Entries for initial x, y, and v
xEntry = tk.Entry(root, width=3, bd=2)
yEntry = tk.Entry(root, width=3, bd=2)
vEntry = tk.Entry(root, width=3, bd=2)

#Submit & Exit button
submitButton = tk.Button(root, text="Submit", bg="#39fc23",
                         command=lambda: visualization(
                                         root,
                                         xEntry.get(),
                                         yEntry.get(),
                                         vEntry.get()))
exitButton = tk.Button(root, text="Exit", bg="red",
                       command=root.destroy)

#Packing/placing components
#todo: for loop
xLabel.pack()
xLabel.place(x=95, y=50)
xEntry.pack()
xEntry.place(x=120, y=50)
xMLabel.pack()
xMLabel.place(x=140, y=50)

yLabel.pack()
yLabel.place(x=220, y=50)
yEntry.pack()
yEntry.place(x=245, y=50)
yMLabel.pack()
yMLabel.place(x=265, y=50)

vLabel.pack()
vLabel.place(x=345, y=50)
vEntry.pack()
vEntry.place(x=370, y=50)
msLabel.pack()
msLabel.place(x=390, y=50)

submitButton.pack()
submitButton.place(x=230, y=120)
exitButton.pack()
exitButton.place(x=240, y=150)

root.mainloop() #Keeps window open until x is pressed
