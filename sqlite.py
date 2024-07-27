import sqlite3

#Connect to SQlite
connection=sqlite3.connect("COMPANY.db")

# Create a cursor object to insert record,create table

cursor=connection.cursor()

## create the table
table_info="""
Create table COMPANY(FIRST_NAME VARCHAR(25),LAST_NAME VARCHAR(25),DEPT VARCHAR(25),
SALARY VARCHAR(25),AGE INT);

"""
cursor.execute(table_info)

## Insert Some more records

cursor.execute('''Insert Into COMPANY values('Jaya', 'Chandran','Data Science','$1000',35)''')
cursor.execute('''Insert Into COMPANY values('Karthy','R','DEVOPS','$900',33)''')
cursor.execute('''Insert Into COMPANY values('Anbu', 'Alagan','AEM','$800',33)''')
cursor.execute('''Insert Into COMPANY values('Sivam','Sivam','DEVOPS','$1000',30)''')
cursor.execute('''Insert Into COMPANY values('Mani','Ratam','Data Science','$500',20)''')
cursor.execute('''Insert Into COMPANY values('Kasi','Nathan','Security','$400',23)''')
cursor.execute('''Insert Into COMPANY values('Ravi','Kumar','.Net','$150',25)''')

## Disspaly All the records

print("The inserted records are")
data=cursor.execute('''Select * from COMPANY''')
for row in data:
    print(row)

## Commit your changes int he databse
connection.commit()
connection.close()
