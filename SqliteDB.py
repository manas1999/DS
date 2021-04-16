import sqlite3
try :
      conn = sqlite3.connect('first.db')
      print("open database success")
except Exception as e:
      print('error')
result = conn.execute("create table User(UserID int not null unique,Email varchar(30) not null,Password varchar(30) not null,IsAdmin boolean,primary key(UserID));")
conn.execute("create table Train(TrainID int not null unique,Name varchar(30),Date varchar(30),LFrom varchar(30),LTo varchar(30),arrival_time varchar(30),Dep_time varchar(30),primary key(TrainID));")
conn.execute("create table Ticket(TicketID int not null unique,Availability boolean,TDate date,TrainID int not null,Population int,foreign key(TrainID) references Train(TrainID),primary key(TicketID));")
print(result)

#insert data for user
conn.execute("insert into User values ( 12,'mad@gmail.com','MadMan',0);")
#insert data for trains
conn.execute("insert into Train values ( 12704,'FALAKNUMA EXP','16-04-2021','Hyderabad','Kharagpur','3:55AM','3:35PM');")
conn.execute("insert into Train values ( 18646,'EAST COST EXP','16-04-2021','Hyderabad','Kharagpur','10:20AM','1:43PM');")
conn.execute("insert into Train values ( 14645,'SHALIMAR EXP','16-04-2021','Delhi','Jammu','09:06AM','10:55PM');")
conn.execute("insert into Train values ( 12437,'RAJDHANI EXP','16-04-2021','Kolkata','Delhi','10:00AM','1:35PM');")
conn.execute("insert into Train values ( 12009,'SHATABDI EXP','16-04-2021','Mumbai','Ahmedabad','06:25AM','1:10PM');")

#insert data for tickets 
Result= conn.execute("select TrainID from Train")
for Id in Result:
      for i in range(20):
            conn.execute("insert into Ticket values ("  + str(Id)[1:6]+str(i)+ "," +  str((random.getrandbits(1)))  +  "," + str(str((16+(i%6)))+"-04-2021")+"," + str(Id)[1:6] + ",300" + ");" )



conn.close()      
