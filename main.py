##################################################################
# Projectile Motion --- Program that visualizes trajectory of a  #
# projectile with a given initial distance, height, and velocity.#
# @author Preston Garcia                                         #
##################################################################

#imports
try: #Try except to account for Python 2.x and 3.x
    import tkinter as tk #3.x
except:
    import Tkinter as tk #2.x
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np

#Constants
G = 9.81
GEOMETRY = "500x200"
TITLE = "Projectile Motion Simulator"
BACKGROUND = "white"

def visualization(master, xEntry, yEntry, vEntry): #todo: separate into another file
    """Visualizes the trajectory of a projectile given
       initial x position, initial y position, and
       initial velocity. User can manipulate angle and
       point in time using sliders.
       @master - The root tkinter window
       @xEntry - String of user input for initial x
       @yEntry - String of user input for initial y
       @vEntry - String of user input for initial v"""

    try:

        #Converts strings from entries to ints
        xi = float(xEntry)
        yi = float(yEntry)
        vi = float(vEntry)
        master.destroy() #Closes main window
        
    except ValueError: #Ensures user inputted ints/floats

        print("One or more of your inputs are not numbers.") #todo: Create a popup for this
        return
    
    #t = (v0 * sin(theta) + sqrt((v0*sin(theta))^2 + 2g * y0) / g
    #max time will be when theta = 45 degrees or pi/4 radians
    maxT = (vi * np.sin(np.pi/2) + np.sqrt(np.square(vi*np.sin(np.pi/2)) + 2 * G * yi)) / G

    #max x value will be at the end of the trajectory when theta = 45 degrees or pi/4 radians
    maxX = vi ** 2 * np.sin(2 * np.pi/4) / G

    #max y value will be in the middle of the trajectory when theta = 90 degrees or pi/2 radians
    maxY = yi + vi ** 2 * np.sin(np.pi/2) ** 2 / (2 * G)

    t = np.arange(0.0, maxT, 0.001)
    
    #x = xi + vi * cos(theta)t
    x = xi + vi * np.cos(np.pi/4) * t 

    #y = yi + vi * sin(theta)t - gt^2/2
    y = yi + vi * np.sin(np.pi/4) * t - G * t ** 2 / 2 

    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.25)
    delta = 0.01
    trajectory, = plt.plot(x, y)
    tPoint, = plt.plot(0, 0, 'ro')
    plt.title("y vs. x")
    plt.xlabel("x(m)")
    plt.ylabel("y(m)")
    plt.xlim([0, maxX])
    plt.ylim([0, maxY])
    
    axTheta = plt.axes([0.12, 0.1, 0.76, 0.03])
    axTime = plt.axes([0.12, 0.05, 0.76, 0.03])

    sTheta = Slider(axTheta, "Theta", 0, 90.0, valinit=45, valstep=delta)
    sTime = Slider(axTime, "Time", 0, maxT, valinit=0, valstep=delta)


    def update(val):
        """Updates the data on the visualization graph based on
        where the slider is.
        @val - Data for the sliders changed"""
        
        #Angle and time slider values
        angle = sTheta.val 
        time = sTime.val
        
        #Update x and y
        newX = xi + vi * np.cos(angle * np.pi/180) * t 
        newY = yi + vi * np.sin(angle * np.pi/180) * t - G * t ** 2 / 2
        newXRange = vi ** 2 * np.sin(2 * angle * np.pi/180) / G
        newXPoint = newX[np.where(t == time)]
        newYPoint = newY[np.where(t == time)]
        trajectory.set_xdata(newX)
        trajectory.set_ydata(newY)
        
        
        if (newYPoint[0] > 0):

            tPoint.set_ydata(newYPoint)
            tPoint.set_xdata(newXPoint)
            
        else:

            tPoint.set_ydata(0)
            
            if time == 0: #For 0, 0

                tPoint.set_xdata(0)

            else: #For x, 0

                tPoint.set_xdata(newXRange)

        fig.canvas.draw_idle()


    sTheta.on_changed(update)
    sTime.on_changed(update)
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
