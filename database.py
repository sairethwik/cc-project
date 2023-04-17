import mysql.connector

mydb = mysql.connector.connect(
    host="cc-project.cdrsgaxcidkg.us-east-1.rds.amazonaws.com",
    user="admin",
    password="admin123",
    port="3306",
    database="project"
)
c = mydb.cursor()





def add_data(Student_ID, Subject, Dates, Teach_ID,class_ID):

    c.execute('INSERT INTO class(Student_ID, Subject, Dates, Teach_ID,class_ID) VALUES (%s,%s,%s,%s,%s)',(Student_ID, Subject, Dates, Teach_ID,class_ID))

    mydb.commit()

def add_attendance( Class_ID,Dates, Student_ID):

    c.execute('INSERT INTO attendance(Class_ID,Dates, Student_ID) VALUES (%s,%s,%s)',(Class_ID,Dates, Student_ID))

    mydb.commit()

def add_student(Student_ID,F_name,L_name,email_ID,Phone_no,password):

    c.execute('INSERT INTO student(Student_ID,F_name,L_name,email_ID,Phone_no,password) VALUES (%s,%s,%s,%s,%s,%s)',(Student_ID,F_name,L_name,email_ID,Phone_no,password))

    mydb.commit()
def remove_student(Student_ID,):
    c.execute('DELETE FROM student WHERE Student_ID ="{}"'.format(Student_ID))
    mydb.commit()

def view_all_data(Student_ID,Subject,Dates,Teach_ID,class_ID):

    c.execute('SELECT * FROM class')

    data = c.fetchall()

    return data

def view_only_class_names():

    c.execute('SELECT class_ID FROM class')

    data = c.fetchall()

    return data

def view_attendan(Class_ID,Dates,Student_ID):
    c.execute('SELECT * FROM attendance')
    data = c.fetchall()
    return data


def get_Train(Name):

    c.execute('SELECT * FROM class WHERE Dates ="{}"'.format(Name))

    data = c.fetchall()

    return data



def update_details(new_Student_ID,new_F_name,new_L_name,new_email_ID,new_phone_no,new_password,Student_ID):

    c.execute("UPDATE student SET Student_ID=%s,F_name=%s,L_name=%s,email_ID=%s,Phone_no=%s,password = %s WHERE Student_ID=%s", (new_Student_ID,new_F_name,new_L_name,new_email_ID,new_phone_no,new_password,Student_ID))


    mydb.commit()

    data = c.fetchall()

    return data