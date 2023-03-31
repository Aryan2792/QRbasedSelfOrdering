from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from tkinter import filedialog
import cv2
import webbrowser

class main:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('200x200')
        self.mainMenu = Menu(self.root)
        self.root.config(menu=self.mainMenu)

        self.mainMenu.add_command(label='Select File', command=self.selecImage)

        self.root.mainloop()

    def selecImage(self):
        path = filedialog.askopenfilename()
        img = cv2.imread(path)

        decoder = cv2.QRCodeDetector()
        link = decoder.detectAndDecode(img)[0]
        print(link)
        option = msg.askokcancel('','Open Link in Browser')
        # print(option)
        if option:
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(r'C:\Program Files\Google\Chrome\Application\chrome.exe'))
            webbrowser.get('chrome').open_new_tab(link)
            # webbrowser.get(r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe').open_new_tab(link)


main()
