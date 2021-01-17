try:
    import tkinter.messagebox as mb
except:
    import Tkinter.messagebox as mb
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np

#Constants
G = 9.81

def main(master, xEntry, yEntry, vEntry): 
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

        mb.showerror("Value Error", "One or more of your inputted values are not numbers.")
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
    
    axTheta = plt.axes([0.12, 0.1, 0.78, 0.03])
    axTime = plt.axes([0.12, 0.05, 0.78, 0.03])

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
        
        try:
            
            if (newYPoint[0] > 0):

                tPoint.set_ydata(newYPoint)
                tPoint.set_xdata(newXPoint)
            
            else:

                tPoint.set_ydata(0)
            
                if time == 0: #For 0, 0

                    tPoint.set_xdata(0)

                else: #For x, 0

                    tPoint.set_xdata(newXRange)

        except IndexError:

            tPoint.set_xdata(0)
            tPoint.set_ydata(0)

        fig.canvas.draw_idle()


    sTheta.on_changed(update)
    sTime.on_changed(update)
    plt.show()
