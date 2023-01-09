\textbf
print("************** School Management **************")

#creating database
import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root",passwd="1234")
mycursor=mydb.cursor()
mycursor.execute("create database if not exists pyschool")
#mycursor.execute("------------------")
mycursor.execute("use pyschool")
#creating required tables
mycursor.execute("create table if not exists pystudent(name varchar(50)not null,class varchar(25)not null,roll_no varchar(25),gender char(1))")
#mycursor.execute("create table if not exists pystudent(name varchar(50)not null,roll_no varchar(25)not null,gender char(1)not null)")
mycursor.execute("create table if not exists pystaff(name varchar(50)not null,gender char(1),subject varchar(25)not null,salary varchar(25))")
mydb.commit()
while(True):

    print("1 = Enter data for new student")
    print("2 = Enter data for new staff data")
    print("3 = Search student data")
    print("4 = Search staff data")
    print("5 = Remove student record")
    print("6 = Remove staff record")
    print("7 = Exit")
    ch=int(input("Enter your choice : "))

#procedure for entering a new student record
    if(ch==1):
        print("all the information prompted are mandatory to be filled")
        name=input("enter name(limit 35 characters) : ")
        classs=str(input("enter class : "))
        #classs=input("enter class: ")
        roll_no=str(input("enter roll number: "))
        gender=str(input("enter gender(M/F): "))
        mycursor.execute("insert into pystudent values('"+name+"','"+classs+"','"+roll_no+"','"+gender+"')")
        #mycursor.execute("insert into pystudent values('"++"')")
        mydb.commit()
        print("Student record has been saved successfully!!")
        
#procedure for entering a new staff record
    elif(ch==2):
        sname=str(input("enter staff member name: "))
        gender=str(input("enter gender(M/F): "))
        dep=str(input("enter department or subject: "))
        sal=int(input("enter salary: "))
        mycursor.execute("insert into pystaff values('"+sname+"','"+gender+"','"+dep+"','"+str(sal)+"')")
        mydb.commit()
        print("staff record has been saved successfully!!")
        
             
             
#procedure for displaying staff record
    elif(ch==3):
        
        roll_no=str(input("Enter student roll no.: "))
        mycursor.execute("select* from pystudent where roll_no='"+roll_no+"'")
        #mycursor.execute("select* from pystudent where roll_no='"+variable name+"'")
        for i in mycursor:
            name,classs,roll_no,gender=i
            #name,class,rno,gender=[(name),(classs),(roll_no),(gender)]
            #print(f"name:-{name}")
            print(f'name:-{name}')
            print(f'class:-{classs}')
            print(f'roll number:-{roll_no}')
            print(f'gender:-{gender}')
             
             
#procedure for display staff record
    elif(ch==4):       
        
        name=str(input("Enter name: "))
        mycursor.execute("select* from pystaff where name='"+name+"'")
        for i in mycursor: #[(name),(gender),(dep),(sal),()]
            name,gender,dep,sal=i
            print(f"Name:- {name}")
            print(f"Gender:- {gender}")
            print(f"Departmant:- {dep}")
            print(f"sal:- {sal}")

#procedure for deleting student record
    elif(ch==5):
        r_no=str(input("Enter roll number"))
        mycursor.execute("delete from pystudent where roll_no='"+r_no+"'")
        mydb.commit()
        print("student record is successfully deleted")

#procedure for deleting staff record
    elif(ch==6):
        name=str(input("Enter name"))
        mycursor.execute("delete from pystaff where name='"+name+"'")
        mydb.commit()
        print("staff record is successfully deleted")
    else:
        break



         
    
