##################################################################
# main --- Program that opens up the main window asking the user #
# to give an initial x distance, y height, and v speed for the   #
# projectile. This window is opened using tkinter. Once all these#
# variables are inputted correctly, the visualiztion window opens#
# up and visualizes the trajectory with the variables.           #
# @author Preston Garcia                                         #
##################################################################

#imports
try: #Try except to account for Python 2.x and 3.x
    import tkinter as tk #3.x
except ImportError:
    import Tkinter as tk #2.x
import visualization

#Constants
GEOMETRY = "500x200"
TITLE = "Projectile Motion Simulator"
BACKGROUND = "white"

def main():
    """main method of the visualization, opens a matplotlib
    window and controls behavior of the visualization along with
    the sliders"""

    #Main window asking for initial height, distance, and speed
    root = tk.Tk(BACKGROUND) 

    rootIcon = tk.PhotoImage(file="C:\\Users\\prest\\Desktop\\Coding\\Python\\ProjectileMotion\\Images\\Trajectory.png")

    #Window settings
    root.title(TITLE)
    root.geometry(GEOMETRY)
    root.configure(bg=BACKGROUND)
    root.iconphoto(False, rootIcon)

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
                             command=lambda: visualization.main(
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

if __name__ == "__main__":
    main()
