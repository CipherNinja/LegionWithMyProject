from tkinter import *
from tkinter import messagebox
from PIL import Image , ImageTk
import pyttsx3
engine = pyttsx3.init()


def PdfConverter():
#PROVIDING A NAME FOR FILE BY USER INPUT
    file_name = file_name_entry.get()
    file_extension = '.pdf'
    Real_file_name = str(file_name)+file_extension

    if len(Real_file_name) > 19:
        engine.say('try again ! Validation error given PDF name is too long ')
        engine.runAndWait()
        messagebox.showerror('Validation Error !','PDF name is too Long')

    else:

    #------------MAIN WORKING IS DOWN
        pressed = input_window.get()

        if pressed == "This software is developed by__ PRIYESH PANDEY                                                   ":
            input_window.delete(0,END)
            input_window.insert(0,'USER DETAIL IS NOT AN IDEAL INPUT')
            engine.say('USER DETAIL IS NOT AN IDEAL INPUT ')
            engine.runAndWait()
        elif pressed == "USER DETAIL IS NOT AN IDEAL INPUT" or pressed == "Entre the path of DocX or (JPEG,JPG,PNG) file                                                   ":
            input_window.delete(0,END)
            input_window.insert(0,'Oops wrong input method Try again !')
            engine.say('Oops wrong input method Try again !')
            engine.runAndWait()
        elif pressed == 'Oops wrong input method Try again !':
            input_window.delete(0, END)
            input_window.insert(0, 'Oops Wrong input method Try again !')
            engine.say('Clear All and Try Again !')
            engine.runAndWait()
        else:
            img1 = Image.open(pressed)
            im1 = img1.convert('RGB')
            im1.save(Real_file_name)
            input_window.delete(0,END)
            input_window.insert(0,'Your PDF is ready here --> Priyesh Pandey\PycharmProjects\pythonProject\Software_Manager\Software_Testing')

            engine.say('Your PDF is created. Follow the path as given !')
            engine.runAndWait()

            messagebox.askokcancel('PDF Ready','PDF saved at Priyesh Pandey\PycharmProjects\pythonProject\Software_Manager\Software_Testing')
    pass

    #for testing a photo is given --> C:\Users\Priyesh Pandey\Pictures\Screenshots\Screenshot (4).png <without " " signs >



def ClearScreen():
    input_window.delete(0,END)
    file_name_entry.delete(0,END)
    pass

def Info():
    info = "Entre the path of DocX or (JPEG,JPG,PNG) file                                                   "
    info2 = "Entre a Name of PDF and press Validate key                                                   "
    input_window.insert(0,info)
    file_name_entry.insert(0, info2)
    engine.say('This Software is Developed by Priyesh Pandey')
    engine.runAndWait()
    pass



screen = Tk()
screen.maxsize(400,420)
screen.minsize(400,200)
screen.config(bg='yellow')
screen.title('IMG TO PDF CONVERTER APP')



frame4 = Frame(screen,borderwidth=4,bg='#A442DC',pady=20,padx=10)
text = Label(frame4,text='TYPE NAME OF YOUR PDF FILE AND VALIDATE',font='lucida 12 italic',bg='#EB96EB').grid(columnspan='2')

file_name_entry = Entry(frame4,width=50, bg='#6441A4', borderwidth=5, fg='white')
file_name_entry.grid()

button5 = Button(frame4,bg='red',text='Validate_Name',padx='25',pady='5',font='lucida 12 bold',command=PdfConverter).grid(rowspan='4',columnspan='5')

frame4.pack()






noframe = frame3 = Frame(screen,borderwidth=4,bg='yellow',padx=40).pack()
noframe = frame3 = Frame(screen,borderwidth=4,bg='yellow',padx=40).pack()
noframe = frame3 = Frame(screen,borderwidth=4,bg='yellow',padx=40).pack()
noframe = frame3 = Frame(screen,borderwidth=4,bg='yellow',padx=40).pack()
noframe = frame3 = Frame(screen,borderwidth=4,bg='yellow',padx=40).pack()
noframe = frame3 = Frame(screen,borderwidth=4,bg='yellow',padx=40).pack()




frame1 = Frame(screen,bg='#A442DC',pady=20,padx=40)
Label1 = Label(frame1,text='IMAGE --> PDF CONVERTER',bg='#EB96EB',font='lucida 13 bold')
Label1.grid(columnspan=2)
Label2 = Label(frame1,text=' ',bg='#A442DC')
Label2.grid(columnspan=2)
Label_path = Label(frame1,text='ENTRE THE PATH OF THE FILE HERE | ',bg='#EB96EB',font='lucida 13 bold')
Label_path.grid(columnspan=2)
Label2 = Label(frame1,text=' ',bg='#A442DC')
Label2.grid(columnspan=2)
input_window = Entry(frame1,width=50, bg='#6441A4', borderwidth=5, fg='white')
input_window.grid()
Label2 = Label(frame1,text=' ',bg='#A442DC')
Label2.grid(columnspan=2)
frame1.pack()



noframe = frame3 = Frame(screen,borderwidth=4,bg='yellow',padx=40).pack()
noframe = frame3 = Frame(screen,borderwidth=4,bg='yellow',padx=40).pack()
noframe = frame3 = Frame(screen,borderwidth=4,bg='yellow',padx=40).pack()
noframe = frame3 = Frame(screen,borderwidth=4,bg='yellow',padx=40).pack()





frame3 = Frame(screen,borderwidth=4,bg='#A442DC',pady=4,padx=40)
dash = Label(frame3,text=' ',bg='#A442DC').grid(columnspan=2)
button1 = Button(frame3,bg='red',text='Submit',padx='25',pady='5',font='lucida 12 bold',command=PdfConverter).grid(row='1',column='1')

button2 = Button(frame3,bg='green',text='Clear',padx='25',pady='5',font='lucida 12 bold',command=ClearScreen).grid(row='1',column='2',padx='6')

button3 = Button(frame3,bg='cyan',text='info',padx='25',pady='5',font='lucida 12 bold',command=Info).grid(row='1',column='3',padx='3')

dash = Label(frame3,text=' ',bg='#A442DC').grid(columnspan=2)

frame3.pack()


screen.mainloop()