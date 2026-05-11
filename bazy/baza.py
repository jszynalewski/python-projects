import sqlite3

conn = sqlite3.connect("baza.db")

cursor = conn.cursor()

cursor.execute("""create table if not exists użytkownicy(
id integer primary key autoincrement,
imie text(20),
email text(30))""") ##tworzy tablice 

name = input("Podaj swoje imię: ")

email = input("Podaj swój email: ") 

cursor.execute("""update użytkownicy set "email" = "nowy@examle.com" where id = 1 """) #update email
cursor.execute("""delete from użytkownicy where id = 2""") #usuwa uż o id = 2
cursor.execute("""insert into użytkownicy(imie, email) values(?, ?)""", (name, email)) #dodaje uż przez input


cursor.execute("""select * from użytkownicy """)

for record in cursor.fetchall():
    print(record)




conn.commit()
conn.close()





