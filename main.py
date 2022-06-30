import psycopg2


print("PostgresSQL connecting...")
connection = psycopg2.connect(host="localhost",database="Entertainment_Booking_System",user="postgres",password="admin")
cursor = connection.cursor()
print("PostgresSQL connected")


# display the PostgreSQL database server version
cursor.execute('SELECT version()')
db_version = cursor.fetchone()
print(db_version)


# # Query 1
# ch="Insert into main_db.manager values(5,'ABC Kumar','abckumar23@gmail.com',3209529823)"
# print(ch)
# cursor.execute(ch)
# connection.commit()


# # Query 2
ch="select * from main_db.manager order by m_id"
print(ch)
cursor.execute(ch)
rows=cursor.fetchall()
for r in rows:
    print(r[0],r[1],r[2],r[3])


# # Query 3
city=input('Enter the name of the city where you want to find all the events: ')
ch="select * from main_db.event_details where location='"+city+"'"
cursor.execute(ch)
rows=cursor.fetchall()
for r in rows:
    print("event_id = ",r[0], " type_id= ",r[1] , "event_name= ",r[2] ,"price= ",r[3] ,"event_date= ",r[4] ,"location= ",r[5] ,"event_time= ",r[6],"duration= ",r[7] ,"total_tickets= ",r[8] ,"tickets_left= ",r[9] ,"rating= ",r[10])
    

# Query 4
while(1):
    print('--------------------------------------')
    print('Welcome to the Menu...')
    print('1: Managers')
    print('2: Customers')
    print('3: event_type')
    print('4: event_details')
    print('5: events_booked')
    print('6: exit')
    print('-------------------------------------')
    choice = int(input('Enter your choice:'))
    print('-------------------------------------')
    if choice == 1:
        print('Manager details')
        ch="select * from main_db.manager order by m_id"
        cursor.execute(ch)
        rows=cursor.fetchall()
        for r in rows:
            for c in r:
                print(c,end='  ')
            print()
    elif choice == 2:
        print('customers details')
        ch="select * from main_db.customer"
        cursor.execute(ch)
        rows=cursor.fetchall()
        for r in rows:
            for c in r:
                print(c,end='  ')
            print()
    elif choice == 3:
        print('event_types details')
        ch="select * from main_db.event_type"
        cursor.execute(ch)
        rows=cursor.fetchall()
        for r in rows:
            for c in r:
                print(c,end='  ')
            print()
    elif choice == 4:
        print('event_details details')
        ch="select * from main_db.event_details"
        cursor.execute(ch)
        rows=cursor.fetchall()
        for r in rows:
            for c in r:
                print(c,end='  ')
            print()
    elif choice == 5:
        print('event_booked details')
        ch="select * from main_db.event_booked"
        cursor.execute(ch)
        rows=cursor.fetchall()
        for r in rows:
            for c in r:
                print(c,end='  ')
            print()
    else:
        print('Thank you for visiting...')
        print()
        break
