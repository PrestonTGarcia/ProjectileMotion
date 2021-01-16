#todo: Description comment
#imports
try: #Try except to account for Python 2.x and 3.x
    import tkinter as tk #3.x
except:
    import Tkinter as tk #2.x
import matplotlib.pyplot as plt
import numpy as np

#Constants
G = 9.81
GEOMETRY = "500x200"
TITLE = "Projectile Motion Simulator"
BACKGROUND = "white"

def visualization(master, xEntry, yEntry, vEntry): #todo: visualization 
    """Visualizes the trajectory of a projectile given
       initial x position, initial y position, and
       initial velocity. User can manipulate angle and
       point in time using sliders."""

    try:

        #Converts strings from entries to ints
        xi = float(xEntry)
        yi = float(yEntry)
        vi = float(vEntry)
        master.destroy() #Closes main window
        
    except ValueError: #Ensures user inputted ints/floats

        print("One or more of your inputs are not numbers.")
        return

    plt.title("y vs. x")
    plt.xlabel("x(m)")
    plt.ylabel("y(m)")
    maxT = (vi * np.sin(np.pi/4) + np.sqrt(np.square(vi*np.sin(np.pi/4)) + 2 * G * yi)) / G
    maxX = xi + vi * np.cos(np.pi/4) * maxT
    maxY = yi + vi * np.sin(np.pi/2) * maxT/2 - G * maxT/2 ** 2 / 2
    tPoints = np.arange(0.0, maxT, 0.001)
    xPoints = [xi + vi * np.cos(np.pi/4) * t for t in tPoints]
    plt.xlim([0,maxX])
    yPoints = [yi + vi * np.sin(np.pi/4) * t - G * t ** 2 / 2 for t in tPoints]
    plt.ylim([0, maxY])
    plt.plot(xPoints, yPoints)
    plt.show()

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

componentsArray = [[xLabel, xEntry, xMLabel],
                   [yLabel, yEntry, yMLabel],
                   [vLabel, vEntry, msLabel]]
iteratingX = 95 #Starts at 95 since xLabel is at x=95

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
for i in componentsArray:
    
    i[0].pack()
    i[0].place(x=iteratingX, y=50)
    iteratingX += 25
    i[1].pack()
    i[1].place(x=iteratingX, y=50)
    iteratingX += 20
    i[2].pack()
    i[2].place(x=iteratingX, y=50)
    iteratingX += 80
    
submitButton.pack()
submitButton.place(x=230, y=120)
exitButton.pack()
exitButton.place(x=240, y=150)

root.mainloop() #Keeps window open until x is pressed
