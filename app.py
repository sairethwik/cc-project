import mysql.connector
mydb = mysql.connector.connect(
    host="cc-project.cdrsgaxcidkg.us-east-1.rds.amazonaws.com",
    user="admin",
    password="admin123",
    port="3306",
    database="project"
)

c = mydb.cursor()
#c.execute("CREATE DATABASE project")