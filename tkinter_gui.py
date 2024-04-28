from tkinter import *
import webbrowser

# Function to open the home page in the browser
def open_home():
    webbrowser.open('http://127.0.0.1:5000')

# Function to open the about page in the browser
def open_about():
    webbrowser.open('http://127.0.0.1:5000/about')

# Create the Tkinter window
root = Tk()
root.title("Flask App GUI")

# Create a button to open the home page
home_button = Button(root, text="Home", command=open_home)
home_button.pack()

# Create a button to open the about page
about_button = Button(root, text="About", command=open_about)
about_button.pack()

# Start the Tkinter event loop
root.mainloop()





