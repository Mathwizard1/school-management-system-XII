import tkinter as tk
from PIL import Image,ImageTk
import datafile as df
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#global variables
Student_class,Student_sec,Student_name= "empty","empty","empty"
Student_gender,Student_roll="empty","empty"

current_working_days=75
attended_working_days="empty"

Student_marks={"English":0,"Physics":0,"Mathematics":0,"Chemistry":0,"Computer":0}

Student_timetable={"Time":["empty"],"Monday":["empty"],"Tuesday":["empty"],"Wednesday":["empty"],"Thursday":["empty"],"Friday":["empty"],"Saturday":["Holiday"],"Sunday":["Holiday"]}

Class_notifications=["empty"]
Student_notifications=["empty"]

events=[]

def student_data(student_name):
    #Database code working here
    global Student_name,Class_notifications,Student_notifications,Student_marks,attended_working_days
    global Student_class,Student_sec,Student_gender,Student_roll,Student_timetable,events

    student_userdata=df.update_studentdata(student_name)
    Student_name=student_name
    Student_class=12
    Student_sec=student_userdata["sec"]
    Student_gender=student_userdata["gender"]
    Student_roll=student_userdata["rollno"]
    attended_working_days=student_userdata["attend"]

    time_table=df.update_timetable()
    Student_timetable={"Time":["9:00-10:00","10:00-11:00","11:00-11:30","11:30-12:30","12:30-1:30","1:30-2:30"],}
    for i in time_table:
        Student_timetable[i]=time_table[i]
    Student_timetable["Saturday"]=["Holiday"]
    Student_timetable["Sunday"]=["Holiday"]    

    Student_marks=student_userdata["marks"]

    Student_notifications=df.update_student_notifications(Student_roll)
    Class_notifications=df.update_class_notifications(0)

    events=["Computer Project on 21st"]

def refresh_window():
    Student_UI()

#student user interface function
def Student_UI():

    #Student window
    Student_window=tk.Tk()
    Student_window.title("Student Dashboard")

    #getting the width and height of screen
    scr_width= Student_window.winfo_screenwidth()
    scr_height= Student_window.winfo_screenheight()
    Student_window.geometry("%dx%d" % (scr_width,scr_height))

    #maximum and minimum size of screen window
    Student_window.maxsize(int(scr_width),int(scr_height))
    Student_window.minsize(int(scr_width/2),int(scr_height/2))

    #Partial frame for canvas and scrollbar
    Student_frame=tk.Frame(Student_window,width=scr_width/2,height=scr_height/2)
    Student_frame.pack(fill="both",expand="true")

    #option menu
    menu_frame=tk.Frame(Student_frame)
    menu_frame.pack(side="top",fill="x")

    m=tk.Menu(menu_frame)
    Student_window.config(menu=m)

    def close_window():
        Student_window.destroy()

    submenu=tk.Menu(m)
    m.add_cascade(label='Options',menu=submenu)
    submenu.add_command(label='Refresh',command=lambda:[close_window(),refresh_window()])
    submenu.add_command(label='Exit', command=close_window)
    submenu.add_separator()

    #main canvas
    Student_canvas=tk.Canvas(Student_frame,bg='#C2E5D3',width=scr_width/3,height=scr_height/3,scrollregion=(0,0,scr_width,scr_height))

    #vertical scrollbar
    vbar=tk.Scrollbar(Student_frame,orient="vertical")
    vbar.pack(side="right",fill="y")
    vbar.config(command=Student_canvas.yview)

    Student_canvas.config(width=scr_width/3,height=scr_height/3)
    Student_canvas.config(yscrollcommand=vbar.set)
    Student_canvas.pack(side="left",expand=True,fill="both")

    #student images
    my_image1= Image.open(".\\file\\boy_bg.png")
    Myimage1_w,Myimage1_h=my_image1.size
    boyi_ratio=Myimage1_w/Myimage1_h

    boy_image= my_image1.resize((int(boyi_ratio*scr_height*2/10),int(scr_height*2/10)), Image.LANCZOS)
    boy_bg= ImageTk.PhotoImage(boy_image)

    my_image2= Image.open(".\\file\\girl_bg.png")
    Myimage2_w,Myimage2_h=my_image2.size
    girli_ratio=Myimage2_w/Myimage2_h
    
    girl_image= my_image2.resize((int(girli_ratio*scr_height*2/10),int(scr_height*2/10)), Image.LANCZOS)
    girl_bg= ImageTk.PhotoImage(girl_image)

    #background image
    my_image3=Image.open(".\\file\\type1_bg.png")
    Myimage3_w,Myimage3_h=my_image3.size
    sui_ratio=Myimage3_w/Myimage3_h

    sui_image=my_image3.resize((int(sui_ratio*scr_height*14/15),int(scr_height*14/15)), Image.LANCZOS)
    sui_bg= ImageTk.PhotoImage(sui_image)   

    Student_canvas.create_image(int(scr_width/2),int(scr_height/2),image=sui_bg,anchor="center")

    #nameholder display
    my_image4=Image.open(".\\file\\nameholder_bg.png")
    Myimage4_w,Myimage4_h=my_image4.size
    holder_ratio=Myimage4_w/Myimage4_h*1.25

    holder_image=my_image4.resize((int(holder_ratio*scr_height*1/2.25),int(scr_height*1/2.25)), Image.LANCZOS)
    holder_bg= ImageTk.PhotoImage(holder_image)   

    Student_canvas.create_image(int(scr_width/2),int(scr_height/3.5),image=holder_bg,anchor="center")

    #Basic info display    
    Student_canvas.create_text(int(scr_width/2),int(scr_height/4),font=("Helvetica",int(scr_width/50)),text="Welcome "+Student_name+",")    
    Student_canvas.create_text(int(scr_width/1.95),int(scr_height/3),font=("Helvetica",int(scr_width/60)),text="Class: "+str(Student_class)+" Section: "+Student_sec+" Roll no: "+str(Student_roll)) 

    if(Student_gender=="Male"):
        Student_canvas.create_image(int(scr_width/3.15),int(scr_height/3.25),image=boy_bg,anchor="center")        
    elif(Student_gender=="Female"):
        Student_canvas.create_image(int(scr_width/3.15),int(scr_height/3.25),image=girl_bg,anchor="center")
    else:
        Student_canvas.create_text(int(scr_width/3.15),int(scr_height/3.25),font=("Helvetica",int(scr_width/75)),text="no data",anchor="center")

    def data_window():
        userdata_window=tk.Toplevel(Student_window)
        userdata_window.title("User data")
        userdata_window.geometry("%dx%d" % (scr_width*4/5,scr_height/3))
        
        #maximum and minimum size of screen window
        userdata_window.maxsize(int(scr_width*4/5),int(scr_height/3))
        userdata_window.minsize(int(scr_width/2),int(scr_height/3))

        #other label
        l=tk.Label(userdata_window,text="Data",font=("Helvetica",int(scr_width/90)))
        l.pack()

        #scrollbar
        s=tk.Scrollbar(userdata_window)
        s.pack(side="right",fill="y")

        #text
        t=tk.Text(userdata_window,wrap="word",yscrollcommand=s.set,font=("Helvetica",int(scr_width/85)),bg="#FFFDD0")
        t.pack(side="left",fill="both",expand="true")

        #display
        d={"name":Student_name,"class":Student_class,"section":Student_sec,"roll no":Student_roll,"gender":Student_gender}

        #display loop
        for i in d:
            t.insert('end',i+": "+str(d[i])+"\n")

        s.config(command=t.yview)
        t.config(state='disabled')

        #buttons
        b=tk.Button(userdata_window,text="EXIT",font=int(scr_width/50),command=lambda:[userdata_window.destroy()])
        b.pack(side="bottom")
        userdata_window.mainloop()

    Student_user_btn=tk.Button(Student_frame,font=("Helvetica",int(scr_width/85),"underline"),text='User data',bd='3',command=lambda:[data_window()])
    Student_canvas.create_window(int(scr_width*2/3),int(scr_height/2.45),window=Student_user_btn,anchor="center")
    
    #widget image
    timetable_image= tk.PhotoImage(file='.\\file\\timetable_bg.png')
    attendence_image= tk.PhotoImage(file='.\\file\\attendence_bg.png')
    grades_image= tk.PhotoImage(file='.\\file\\grades_bg.png')
    events_image= tk.PhotoImage(file='.\\file\\events_bg.png')

    timetable_bg= timetable_image.subsample(4,4)
    attendence_bg= attendence_image.subsample(4,4)
    grades_bg= grades_image.subsample(4,4)
    events_bg= events_image.subsample(3,3)

    #widget functions
    def show_mytimetable():
        userdata_window=tk.Toplevel(Student_window)
        userdata_window.title("Schedule")
        userdata_window.geometry("%dx%d" % (scr_width*3/4,scr_height/2))
        
        #maximum and minimum size of screen window
        userdata_window.resizable(0,0)

        #other label
        l=tk.Label(userdata_window,text="Time table",font=("Helvetica",int(scr_width/90)))
        l.pack()
        s=tk.Scrollbar(userdata_window)
        s.pack(side="right",fill="y")
        t=tk.Text(userdata_window,wrap="word",yscrollcommand=s.set,font=("Helvetica",int(scr_width/85)),bg="#FFFDD0")
        t.pack(side="left",fill="both",expand="true")

        #display
        for i in (Student_timetable):
            t.insert("end",i+": ")
            for j in ((Student_timetable[i])):
                t.insert('end',j+" | ")
            t.insert('end',"\n")
        t.config(state='disabled')

        s.config(command=t.yview)
        b=tk.Button(userdata_window,text="EXIT",font=int(scr_width/50),command=lambda:[userdata_window.destroy()])
        b.pack(side="bottom")
        userdata_window.mainloop()
    
    def show_myevents():
        userdata_window=tk.Toplevel(Student_window)
        userdata_window.title("Events")
        userdata_window.geometry("%dx%d" % (scr_width*3/4,scr_height/3))
        
        #maximum and minimum size of screen window
        userdata_window.resizable(0,0)

        #other label
        l=tk.Label(userdata_window,text="School Events",font=("Helvetica",int(scr_width/90)))
        l.pack()
        s=tk.Scrollbar(userdata_window)
        s.pack(side="right",fill="y")
        t=tk.Text(userdata_window,wrap="word",yscrollcommand=s.set,font=("Helvetica",int(scr_width/85)),bg="#FFFDD0")
        t.pack(side="left",fill="both",expand="true")

        #display
        t.insert('end',"Events:"+"\n")
        for i in events:
            t.insert('end',str(i)+"\n")
        t.config(state='disabled')

        s.config(command=t.yview)
        b=tk.Button(userdata_window,text="EXIT",font=int(scr_width/50),command=lambda:[userdata_window.destroy()])
        b.pack(side="bottom")
        userdata_window.mainloop()

    def show_myattendence():
        #database and pandas needed
        userdata_window=tk.Toplevel(Student_window)
        userdata_window.title("Attendence Card")
        userdata_window.geometry("%dx%d" % (scr_width*7/10,scr_height*9/10))
        
        #maximum and minimum size of screen window
        userdata_window.resizable(0,0)

        #other label
        l=tk.Label(userdata_window,text="Attendence",font=("Helvetica",int(scr_width/90)))
        l.pack(side='top')

        #marks data
        data1={"Columns":["attended","total days"],"attended":[attended_working_days,current_working_days]}
        dataf1=DataFrame(data1,columns=["Columns","attended"])

        #plot graph
        graph=plt.figure(figsize=(6,8),dpi=100)
        ax1=graph.add_subplot(111)
        bargraph=FigureCanvasTkAgg(graph,userdata_window)
        bargraph.get_tk_widget().pack(side="left",fill='y')
        df1=dataf1[['Columns','attended']].groupby('Columns').sum()
        df1.plot(kind="bar",legend=True,ax=ax1)
        ax1.set_title("Attendence")

        #marks digits display
        l1=tk.Text(userdata_window,height=int(scr_height/3),width=int(scr_width/10),font=("Helvetica",int(scr_width/85)))
        l1.pack(side='right',fill='y')
        l1.insert('end','Name: '+str(Student_name)+"\n")
        l1.insert('end','Total working days: '+str(current_working_days)+"\n")
        l1.insert('end','Total days attended: '+str(attended_working_days)+"\n")
        l1.config(state='disabled')
        userdata_window.mainloop()

    def show_mygrades():
        #database and pandas needed
        userdata_window=tk.Toplevel(Student_window)
        userdata_window.title("Marks Report")
        userdata_window.geometry("%dx%d" % (scr_width*7/10,scr_height*9/10))
        
        #maximum and minimum size of screen window
        userdata_window.resizable(0,0)

        #other label
        l=tk.Label(userdata_window,text="Grades",font=("Helvetica",int(scr_width/90)))
        l.pack(side='top')

        #marks data
        mysubject=list(Student_marks.keys())
        mymarks=list(Student_marks.values())
        data1={"Subjects":mysubject,"Marks":mymarks}
        dataf1=DataFrame(data1,columns=["Subjects","Marks"])

        #plot graph
        graph=plt.figure(figsize=(6,8),dpi=100)
        ax1=graph.add_subplot(111)
        bargraph=FigureCanvasTkAgg(graph,userdata_window)
        bargraph.get_tk_widget().pack(side="left",fill='y')
        df1=dataf1[['Subjects','Marks']].groupby('Subjects').sum()
        df1.plot(kind="bar",legend=True,ax=ax1)
        ax1.set_title("Marks Report")

        #marks digits display
        l1=tk.Text(userdata_window,height=int(scr_height/3),width=int(scr_width/10),font=("Helvetica",int(scr_width/85)))
        l1.pack(side='right',fill='y')
        l1.insert('end','Name: '+str(Student_name)+"\n\nMarks obtained:\n")
        for i in Student_marks:
            l1.insert('end',str(i)+": "+str(Student_marks[i])+"\n")
        l1.config(state='disabled')
        userdata_window.mainloop()

    #option widgets
    sui_timetable_btn=tk.Button(Student_frame,font=("Helvetica",int(scr_width/60),"underline"),text='Time table',image=timetable_bg,compound="left",bd='5',command=lambda:[show_mytimetable()])
    sui_Attendence_btn=tk.Button(Student_frame,font=("Helvetica",int(scr_width/60),"underline"),text='Attendence',image=attendence_bg,compound="left",bd='5',command=lambda:[show_myattendence()])
    sui_grades_btn=tk.Button(Student_frame,font=("Helvetica",int(scr_width/60),"underline"),text='Grade and score',image=grades_bg,compound="right",bd='5',command=lambda:[show_mygrades()])
    sui_events_btn=tk.Button(Student_frame,font=("Helvetica",int(scr_width/60),"underline"),text='Events',image=events_bg,compound="right",bd='5',command=lambda:[show_myevents()])

    Student_canvas.create_window(int(scr_width*4/11),int(scr_height*7/11),window=sui_timetable_btn,anchor="center")
    Student_canvas.create_window(int(scr_width*4/11),int(scr_height*9/11),window=sui_Attendence_btn,anchor="center")
    Student_canvas.create_window(int(scr_width*7/11),int(scr_height*7/11),window=sui_grades_btn,anchor="center")
    Student_canvas.create_window(int(scr_width*7/11),int(scr_height*9/11),window=sui_events_btn,anchor="center")

    #notifications panel
    my_notificationframe=tk.Frame(Student_canvas)
    Student_canvas.create_window(int(scr_width/8),int(scr_height/2),height=int(scr_height*5/6),width=int(scr_width/5.5),window=my_notificationframe,anchor="center")

    #notifcation box
    mylabel=tk.Label(my_notificationframe,font=("Helvetica",int(scr_width/75),"underline italic"),text="Notifications")
    mytextbox=tk.Text(my_notificationframe,wrap="word",height=int(scr_height*5/6),width=int(scr_width/6),font=("Helvetica",int(scr_width/85)),bg="#D1FFEA")
    
    mylabel.pack()
    mytextbox.pack(expand="true",fill="both")

    #display notifications
    mytextbox.insert('end',"Class notifications"+"\n")
    for i in range(0,len(Class_notifications)):
        mytextbox.insert('end',"*"+Class_notifications[i])
        mytextbox.insert('end',"\n")
    mytextbox.insert('end','\nStudent notifications'+'\n')
    for i in range(0,len(Student_notifications)):
        mytextbox.insert("end","-"+Student_notifications[i])
        mytextbox.insert('end',"\n")
    mytextbox.config(state='disabled')

    Student_window.mainloop()

#Stand alone testing
#student_data("Anshurup Gupta")
#Student_UI()