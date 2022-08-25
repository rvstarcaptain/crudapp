import pymysql
​
mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="Mohit1667@",
    database="school"
)
# create cursor:
cur = mydb.cursor()
​
# create table:
# t = """
#     create table if not exists students(
#         roll_no int(10) not null auto_increment,
#         student_name varchar(100) not null,
#         email_id varchar(100) not null,
#         course varchar(500) not null,
#         hod_name varchar(50) not null,
#         year int(10) not null,
#         city varchar(50) not null,
#         state varchar(50) not null,
#         primary key(roll_no)
#     )
#     """
# cur.execute(t)
​
# insert sample data in table:
# query = """
#         insert into students(student_name,email_id,course,hod_name,year,city,state)
#         values(%s,%s,%s,%s,%s,%s,%s)
#         """
# value = (
#     "Mohit Verma",
#     "mohverma1998@gmail.com",
#     "MCA",
#     "Poonam gupta",
#     1,
#     "Faridabad",
#     "Haryana"
# )        
# cur.execute(query,value)
# mydb.commit()
# print("Data inserted successfully")