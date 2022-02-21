from tkinter import *
from tkinter import filedialog
def encryption():
    file1 = filedialog.askopenfile(mode='r', filetype=[('jpg file', '*.jpg'), ('png file', '*.png')])
    if file1 is not None:

        file_name = file1.name

    key = entry1.get(0.1, END)
    print(file_name, key)
    fi = open(file_name, 'rb')
    image=fi.read()
    fi.close()
    image=bytearray(image)
    for index,value in enumerate(image):
        image[index]=value^int(key)
        fi1=open(file_name,'wb')
        fi1.write(image)
        fi1.close()

root = Tk()
root.geometry("480x480")
root.title("ED")

root.minsize(50, 50)
root.maxsize(600, 600)
heading = Label(text='Encryption and Decryption')
heading.pack()
b1 = Button(root, text="encrypt", command=encryption)
b1.place(x=100, y=100)
entry1 = Text(root, height=2, width=20)
entry1.place(x=50, y=20)
root.mainloop()