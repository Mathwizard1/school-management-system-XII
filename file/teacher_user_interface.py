import tkinter as tk
from PIL import Image,ImageTk
import datafile as df
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#global variables
Teacher_name= "empty"
Teacher_roll="empty"
Teacher_subject="empty"
Teacher_gender,Teacher_salary="empty",0

current_working_days=75
attended_working_days="empty"

Teacher_timetable={"Time":["empty"],"Monday":["empty"],"Tuesday":["empty"],"Wednesday":["empty"],"Thursday":["empty"],"Friday":["empty"],"Saturday":["Holiday"],"Sunday":["Holiday"]}

Class_notifications=["empty"]

events=[]

def teacher_data(teacher_name):
    #Database code working here
    global Teacher_name,Class_notifications,Teacher_salary,attended_working_days
    global Teacher_roll,Teacher_timetable,events,Teacher_subject,Teacher_gender

    teacher_userdata=df.update_teacherdata(teacher_name)
    Teacher_name=teacher_name
    Teacher_roll=teacher_userdata["rollno"]
    Teacher_subject=teacher_userdata["subject"]
    Teacher_gender=teacher_userdata["gender"]
    Teacher_salary=teacher_userdata["salary"]
    attended_working_days=teacher_userdata["attend"]

    time_table=df.update_timetable()
    Teacher_timetable={"Time":["9:00-10:00","10:00-11:00","11:00-11:30","11:30-12:30","12:30-1:30","1:30-2:30"],}
    for i in time_table:
        Teacher_timetable[i]=time_table[i]
    Teacher_timetable["Saturday"]=["Holiday"]
    Teacher_timetable["Sunday"]=["Holiday"]   

    Class_notifications=df.update_class_notifications(0)
    events=["Computer Project on 21st"]

def refresh_window():
    Teacher_UI()

#Teacher user interface function
def Teacher_UI():

    #Student window
    Teacher_window=tk.Tk()
    Teacher_window.title("Teacher Dashboard")

    #getting the width and height of screen
    scr_width= Teacher_window.winfo_screenwidth()
    scr_height= Teacher_window.winfo_screenheight()
    Teacher_window.geometry("%dx%d" % (scr_width,scr_height))

    #maximum and minimum size of screen window
    Teacher_window.maxsize(int(scr_width),int(scr_height))
    Teacher_window.minsize(int(scr_width/2),int(scr_height/2))

    #Partial frame for canvas and scrollbar
    Teacher_frame=tk.Frame(Teacher_window,width=scr_width/2,height=scr_height/2)
    Teacher_frame.pack(fill="both",expand="true")

    #option menu
    menu_frame=tk.Frame(Teacher_frame)
    menu_frame.pack(side="top",fill="x")

    m=tk.Menu(menu_frame)
    Teacher_window.config(menu=m)

    def close_window():
        Teacher_window.destroy()

    submenu=tk.Menu(m)
    m.add_cascade(label='Options',menu=submenu)
    submenu.add_command(label='Refresh',command=lambda:[close_window(),refresh_window()])
    submenu.add_command(label='Exit', command=close_window)
    submenu.add_separator()

    #main canvas
    Teacher_canvas=tk.Canvas(Teacher_frame,bg='#C2E5D3',width=scr_width/3,height=scr_height/3,scrollregion=(0,0,scr_width,scr_height))

    #vertical scrollbar
    vbar=tk.Scrollbar(Teacher_frame,orient="vertical")
    vbar.pack(side="right",fill="y")
    vbar.config(command=Teacher_canvas.yview)

    Teacher_canvas.config(width=scr_width/3,height=scr_height/3)
    Teacher_canvas.config(yscrollcommand=vbar.set)
    Teacher_canvas.pack(side="left",expand=True,fill="both")

    #Subject images
    math_image= Image.open(".\\file\\math_bg.png")
    math_image_w,math_image_h=math_image.size
    mathi_ratio=math_image_w/math_image_h

    math_img= math_image.resize((int(mathi_ratio*scr_height*2/10),int(scr_height*2/10)), Image.LANCZOS)
    math_bg= ImageTk.PhotoImage(math_img)

    comp_image= Image.open(".\\file\\comp_bg.png")
    comp_image_w,comp_image_h=comp_image.size
    compi_ratio=comp_image_w/comp_image_h

    comp_img= comp_image.resize((int(compi_ratio*scr_height*2/10),int(scr_height*2/10)), Image.LANCZOS)
    comp_bg= ImageTk.PhotoImage(comp_img)

    eng_image= Image.open(".\\file\\eng_bg.png")
    eng_image_w,eng_image_h=eng_image.size
    engi_ratio=eng_image_w/eng_image_h

    eng_img= eng_image.resize((int(engi_ratio*scr_height*2/10),int(scr_height*2/10)), Image.LANCZOS)
    eng_bg= ImageTk.PhotoImage(eng_img)

    chem_image= Image.open(".\\file\\chem_bg.png")
    chem_image_w,chem_image_h=chem_image.size
    chemi_ratio=chem_image_w/chem_image_h

    chem_img= chem_image.resize((int(chemi_ratio*scr_height*2/10),int(scr_height*2/10)), Image.LANCZOS)
    chem_bg= ImageTk.PhotoImage(chem_img)

    phy_image= Image.open(".\\file\\phy_bg.png")
    phy_image_w,phy_image_h=phy_image.size
    phyi_ratio=phy_image_w/phy_image_h

    phy_img= phy_image.resize((int(phyi_ratio*scr_height*2/10),int(scr_height*2/10)), Image.LANCZOS)
    phy_bg= ImageTk.PhotoImage(phy_img)

    #background image
    my_image3=Image.open(".\\file\\type1_bg.png")
    Myimage3_w,Myimage3_h=my_image3.size
    tui_ratio=Myimage3_w/Myimage3_h

    tui_image=my_image3.resize((int(tui_ratio*scr_height*14/15),int(scr_height*14/15)), Image.LANCZOS)
    tui_bg= ImageTk.PhotoImage(tui_image)   

    Teacher_canvas.create_image(int(scr_width/2),int(scr_height/2),image=tui_bg,anchor="center")

    #nameholder display
    my_image4=Image.open(".\\file\\nameholder_bg.png")
    Myimage4_w,Myimage4_h=my_image4.size
    holder_ratio=Myimage4_w/Myimage4_h*1.25

    holder_image=my_image4.resize((int(holder_ratio*scr_height*1/2.25),int(scr_height*1/2.25)), Image.LANCZOS)
    holder_bg= ImageTk.PhotoImage(holder_image)   

    Teacher_canvas.create_image(int(scr_width/2),int(scr_height/3.5),image=holder_bg,anchor="center")

    #Basic info display    
    Teacher_canvas.create_text(int(scr_width/2),int(scr_height/4),font=("Helvetica",int(scr_width/50)),text="Welcome "+Teacher_name+",")    
    Teacher_canvas.create_text(int(scr_width/1.95),int(scr_height/3),font=("Helvetica",int(scr_width/60)),text=" Subject:"+Teacher_subject+"  Roll no:"+str(Teacher_roll)) 
    imager=phy_bg
    if(Teacher_subject=="Mathematics"):
        imager=math_bg
    elif(Teacher_subject=="Computer"):
        imager=comp_bg
    elif(Teacher_subject=="English"):
        imager=eng_bg
    elif(Teacher_subject=="Chemistry"):
        imager=chem_bg
    elif(Teacher_subject=="Physics"):
        imager=phy_bg
    Teacher_canvas.create_image(int(scr_width/3.5),int(scr_height/3.25),image=imager,anchor="center")

    def data_window():
        userdata_window=tk.Toplevel(Teacher_window)
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
        d={"name":Teacher_name,"subject":Teacher_subject,"roll no":Teacher_roll,"gender":Teacher_gender,"Salary":Teacher_salary}

        #display loop
        for i in d:
            t.insert('end',i+": "+str(d[i])+"\n")

        s.config(command=t.yview)
        t.config(state='disabled')

        #buttons
        b=tk.Button(userdata_window,text="EXIT",font=int(scr_width/50),command=lambda:[userdata_window.destroy()])
        b.pack(side="bottom")
        userdata_window.mainloop()

    Teacher_user_btn=tk.Button(Teacher_frame,font=("Helvetica",int(scr_width/85),"underline"),text='Teacher data',bd='3',command=lambda:[data_window()])
    Teacher_canvas.create_window(int(scr_width*2/3),int(scr_height/2.45),window=Teacher_user_btn,anchor="center")

    #widget image
    timetable_image= tk.PhotoImage(file='timetable_bg.png')
    attendence_image= tk.PhotoImage(file='attendence_bg.png')
    events_image= tk.PhotoImage(file='events_bg.png')

    timetable_bg= timetable_image.subsample(4,4)
    attendence_bg= attendence_image.subsample(4,4)
    events_bg= events_image.subsample(3,3)

    #widget functions
    def show_mytimetable():
        userdata_window=tk.Toplevel(Teacher_window)
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
        for i in (Teacher_timetable):
            t.insert("end",i+": ")
            for j in ((Teacher_timetable[i])):
                t.insert('end',j+" | ")
            t.insert('end',"\n")
        t.config(state='disabled')

        s.config(command=t.yview)
        b=tk.Button(userdata_window,text="EXIT",font=int(scr_width/50),command=lambda:[userdata_window.destroy()])
        b.pack(side="bottom")
        userdata_window.mainloop()

    def show_myattendence():
        #database and pandas needed
        userdata_window=tk.Toplevel(Teacher_window)
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
        l1.insert('end','Name: '+str(Teacher_name)+"\n")
        l1.insert('end','Total working days: '+str(current_working_days)+"\n")
        l1.insert('end','Total days attended: '+str(attended_working_days)+"\n")
        l1.config(state='disabled')
        userdata_window.mainloop()

    def quick_update(m):
        global Class_notifications
        df.update_class_notifications(1,m)
        Class_notifications=df.update_class_notifications(0)

    def show_myevents():
        userdata_window=tk.Toplevel(Teacher_window)
        userdata_window.title("Class notifications")
        userdata_window.geometry("%dx%d" % (scr_width*3/4,scr_height*4/5))
        
        #maximum and minimum size of screen window
        userdata_window.resizable(0,0)

        #other label
        frame1=tk.Frame(userdata_window)
        frame1.grid(row=0,column=0)
        l=tk.Label(frame1,text="Class notifications",font=("Helvetica",int(scr_width/90)))
        l.grid(row=0,column=0)

        mymessage=tk.StringVar("")
        frame2=tk.Frame(userdata_window)
        frame2.grid(row=4,column=0)
        b=tk.Button(frame2,text="Add",font=int(scr_width/50),command=lambda:[quick_update(mymessage.get()),userdata_window.destroy(),show_myevents()])
        b.pack()

        frame3=tk.Frame(userdata_window)
        t=tk.Text(frame3,wrap="word",font=("Helvetica",int(scr_width/100)),bg="#FFFDD0")
        t.grid(row=0,column=0,sticky="N")
        for i in Class_notifications:
            t.insert("end",i+"\n") 
        t.config(state='disabled')
        frame3.grid(row=2,column=0)

        frame4=tk.Frame(userdata_window)
        frame4.grid(row=3,column=0)
 
        mymessage_label=tk.Label(frame4,font=("Arial",int(scr_width/70)),text='message')
        mymessage_entry=tk.Entry(frame4,width=int(scr_width/60),font=("default",int(scr_width/75)),textvariable=mymessage)
        mymessage_label.grid(row=0,column=0)
        mymessage_entry.grid(row=0,column=1)
        userdata_window.mainloop()

    #option widgets
    tui_timetable_btn=tk.Button(Teacher_frame,font=("Helvetica",int(scr_width/60),"underline"),text='Time table',image=timetable_bg,compound="left",bd='5',command=lambda:[show_mytimetable()])
    tui_Attendence_btn=tk.Button(Teacher_frame,font=("Helvetica",int(scr_width/60),"underline"),text='Working days',image=attendence_bg,compound="right",bd='5',command=lambda:[show_myattendence()])
    tui_events_btn=tk.Button(Teacher_frame,font=("Helvetica",int(scr_width/60),"underline"),text='Class notifications',image=events_bg,compound="right",bd='5',command=lambda:[show_myevents()])

    Teacher_canvas.create_window(int(scr_width*4/11),int(scr_height*7/11),window=tui_timetable_btn,anchor="center")
    Teacher_canvas.create_window(int(scr_width*7/11),int(scr_height*7/11),window=tui_Attendence_btn,anchor="center")
    Teacher_canvas.create_window(int(scr_width*4/11),int(scr_height*9/11),window=tui_events_btn,anchor="center")

    Teacher_window.mainloop()

#Stand alone testing
#teacher_data("Kopal ma'am")
#Teacher_UI()