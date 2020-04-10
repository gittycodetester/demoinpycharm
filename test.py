import mysql.connector
import dns.resolver
mydb = mysql.connector.connect(host="localhost",user="root",passwd="akhil",database="")

mycursor = mydb.cursor()



#mycursor.execute("create table akhi(name varchar(20),college varchar(20))")
#mycursor.execute("insert into akhi values('akhil','vaag'),('arun','bits')")

mycursor.execute("select * from student")
for i in mycursor:
    print(i)