import tkinter as tk
from PIL import Image,ImageTk
import student_user_interface as sui
import teacher_user_interface as tui
import datafile as df

#database coding work here
dataname,datapassword,datauserId=df.update_username_password()
#print(dataname,datapassword,datauserId)

#global variable
entered_data=[]

store_username="empty"
store_password="empty"
store_val="empty"

#valid check functions
def valid_credentials(user_login):
    #print("checking the wrapped data",user_login)
    My_username,My_userpassword,My_userId=user_login

    if(My_username in dataname):
        n=dataname.index(My_username)
        if(My_username==dataname[n] and My_userpassword==datapassword[n] and My_userId==datauserId[n]):
            l = list(user_login)
            l=l.copy()

            global entered_data 
            entered_data=tuple(l)
            return True
    else:
        return False

#First login frame
my_login_window=tk.Tk()
my_login_window.title("Login Window")


#getting the width and height of screen
scr_width= my_login_window.winfo_screenwidth()
scr_height= my_login_window.winfo_screenheight()
my_login_window.geometry("%dx%d" % (scr_width,scr_height))

#maximum and minimum size of screen window
my_login_window.maxsize(scr_width,scr_height)
my_login_window.minsize(int(scr_width/2),int(scr_height/2))

#background login image
my_image1= Image.open(".\\file\\login_bg.png")
Myimage_w,Myimage_h=my_image1.size
bg_ratio=Myimage_w/Myimage_h

bg_image= my_image1.resize((int(3*bg_ratio*scr_height/4),int(3*scr_height/4)), Image.LANCZOS)
scr_bg= ImageTk.PhotoImage(bg_image)

#image canvas
login_bg=tk.Canvas(my_login_window,bg="#88cffa",width=int(3/4*scr_width))
login_bg.pack(fill="both",expand=True)
login_bg.create_image(int(scr_width/2),int(scr_height/2.05),image=scr_bg,anchor="center")

#text
login_bg.create_text(int(scr_width/2),int(scr_height/4),font=("Helvetica",int(scr_width/40)),text="Login Page")
login_bg.create_text(int(scr_width/2),int(scr_height/6),font=("Helvetica",int(scr_width/35),"underline"),text="Bangalore International Academy")

#login credentials
username_val=tk.StringVar(value="")
password_val=tk.StringVar(value="")

username_label=tk.Label(my_login_window,font=("Arial",int(scr_width/64)),text='Name')
password_label=tk.Label(my_login_window,font=("Arial",int(scr_width/64)),text='Password')

username=tk.Entry(my_login_window,width=int(scr_width/55),font=("default",int(scr_width/65)),textvariable=username_val)
password=tk.Entry(my_login_window,width=int(scr_width/55),font=("default",int(scr_width/65)),textvariable=password_val)

display_username_label=login_bg.create_window(int(scr_width/5),int(scr_height*2/5),window=username_label,anchor="center")
display_username=login_bg.create_window(int(scr_width*4/10),int(scr_height*2/5),window=username,anchor="center")
display_password_label=login_bg.create_window(int(scr_width/5),int(scr_height*1/2),window=password_label,anchor="center")
display_password=login_bg.create_window(int(scr_width*4/10),int(scr_height*1/2),window=password,anchor="center")

#single option buttons
btn_val=tk.StringVar(value="Student")

student_box=tk.Radiobutton(my_login_window,font=("default",int(scr_width/65)),text='Student',value='Student',variable=btn_val)
Teacher_box=tk.Radiobutton(my_login_window,font=("default",int(scr_width/65)),text='Teacher',value='Teacher',variable=btn_val)
Admin_box=tk.Radiobutton(my_login_window,font=("default",int(scr_width/65)),text='Admin',value='Admin',variable=btn_val)

display_student_box=login_bg.create_window(int(scr_width*3/10),int(scr_height*4/7),window=student_box,anchor="center")
display_Teacher_box=login_bg.create_window(int(scr_width*4/10),int(scr_height*4/7),window=Teacher_box,anchor="center")
display_Admin_box=login_bg.create_window(int(scr_width*5/10),int(scr_height*4/7),window=Admin_box,anchor="center")

#enter button
def submit():
    global store_username,store_password,store_val
    store_username=username_val.get()
    store_password=password_val.get()
    store_val=btn_val.get()
    t=(store_username,store_password,store_val)

    if(valid_credentials(t)==True):
        my_login_window.destroy()
    else:
        my_Text=login_bg.create_text(int(scr_width/2),int(scr_height/3),text="Incorrect userdata",font=("default",int(scr_width/67),"underline"),fill="red")
        my_login_window.after(3000,login_bg.delete, my_Text)

login_btn=tk.Button(my_login_window,font=("Helvetica",int(scr_width/65),"underline"),text='LOGIN',bd='5',command=lambda: [submit()])
display_login_btn=login_bg.create_window(int(scr_width*1/2),int(scr_height*5/7),window=login_btn,anchor="center")

my_login_window.mainloop()

#print("final value",entered_data)

if(entered_data!=[]):
    if(entered_data[2]=="Student"):
        sui.student_data(entered_data[0])
        sui.Student_UI()
    elif(entered_data[2]=="Teacher"):
        tui.teacher_data(entered_data[0])
        tui.Teacher_UI()
    elif(entered_data[2]=="Admin"):
        pass
else:
    print("ERROR")
