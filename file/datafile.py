import mysql.connector as sqltor

mydatabase=sqltor.connect(host="localhost",user="user",password="mypass",database="class12")
mycursor=mydatabase.cursor()


def update_username_password():
    name=[]
    password=[]
    userId=[]
    mycursor.execute("select Name,Password from studentrecord")
    data=mycursor.fetchall()
    for i in data:
        name.append(i[0])
        password.append(i[1])
        userId.append("Student")
    mycursor.execute("select Name,Password from teacher")
    data=mycursor.fetchall()
    for i in data:
        name.append(i[0])
        password.append(i[1])
        userId.append("Teacher")
    mycursor.execute("select Name,Password from admins")
    data=mycursor.fetchall()
    for i in data:
        name.append(i[0])
        password.append(i[1])
        userId.append("Admin")
    dataname=tuple(name)
    datapassword=tuple(password)
    datauserId=tuple(userId)
    return (dataname,datapassword,datauserId)    

def update_studentdata(name):
    st_data={}
    mycursor.execute("select Name,Rollno,section,gender,English,Physics,Mathematics,Chemistry,Computer,attendence from studentrecord")
    data=mycursor.fetchall()
    for i in data:
        if(i[0]==name):
            st_data["rollno"]=i[1]
            st_data["sec"]=i[2]
            if(i[3]=="M" or i[3]=="m"):
                st_data["gender"]="Male"
            else:
                st_data["gender"]="Female"
            st_data["attend"]=i[9]
            st_data["marks"]={"English":i[4],"Physics":i[5],"Math":i[6],"Chemistry":i[7],"Computer":i[8]}
    return st_data

def update_teacherdata(name):
    t_data={}
    mycursor.execute("select Name,Rollno,Subject,gender,Salary,Working_days from teacher")            
    data=mycursor.fetchall()
    for i in data:
        if(i[0]==name):
            t_data["rollno"]=i[1]
            t_data["subject"]=i[2]
            if(i[3]=="M" or i[3]=="m"):
                t_data["gender"]="Male"
            else:
                t_data["gender"]="Female"
            t_data["salary"]=i[4]
            t_data["attend"]=i[5]
    return t_data

def update_timetable():
    ttable_data={"Monday":[],"Tuesday":[],"Wednesday":[],"Thursday":[],"Friday":[]}
    mycursor.execute("select Monday,Tuesday,Wednesday,Thursday,Friday from 12d_timetable")            
    data=mycursor.fetchall()
    for i in data:
        ttable_data["Monday"].append(i[0])
        ttable_data["Tuesday"].append(i[1])
        ttable_data["Wednesday"].append(i[2])
        ttable_data["Thursday"].append(i[3])
        ttable_data["Friday"].append(i[4])
    return ttable_data

def update_student_notifications(rollno):
    snotif=[]
    mycursor.execute("select StudentRollno,message from student_notification")
    data=mycursor.fetchall()
    for i in data:
        if(i[0]==rollno):
            snotif.append(i[1])
    return snotif

def update_class_notifications(mystate,mymessage=""):
    if(mystate==0):
        cnotif=[]
        mycursor.execute("select message from 12d_notification")
        data=mycursor.fetchall()
        for i in data:
            cnotif.append(i[0])
        return cnotif
    elif(mystate==1 and mymessage!=""):
        mycursor.execute("select message from 12d_notification")
        data=mycursor.fetchall()
        n=len(data)
        mycursor.execute("insert into 12d_notification values(%s,%s)",(str(n+1),mymessage))
        mydatabase.commit()

#stand alone testing
#update_username_password()
#update_studentdata()