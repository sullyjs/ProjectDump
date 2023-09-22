import tkinter as tk
from tkinter import filedialog, Text
import os #access os system

root = tk.Tk()
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f: #readit
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps  if x.strip()]

def addApp():
    for widget in frame.winfo_children():
        widget.destroy()
        
    filename= filedialog.askopenfile(initialdir="/", title="Select File", filetypes=(("executables", ".exe"), ("all files", "*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()
        
def runApps():
    for app in apps:
        os.startfile(app)
    

canvas = tk.Canvas(root, height=700, width=700, bg="#81DAF5")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#81DAF5", command=addApp) #fg is color of text
openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="white", bg="#81DAF5", command=runApps) #fg is color of text
runApps.pack()


for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

with open('save.txt', 'w',) as f: #write it
    for app in apps:
        f.write(app+',')