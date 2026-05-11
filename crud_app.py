import sqlite3

conn = sqlite3.connect("nowaBaza.db")

cursor = conn.cursor()

cursor.execute("""create table if not exists members(
id integer primary key autoincrement,
imie text(20),
email text(30))""")

while True:        
   operation = """
   1. Dodaj użytkownika
   2. Wyświetl wszystkich
   3. Usuń użytkownika
   4. Wyjdź"""
   print(operation)
   choose = input("Wybierz operacje: ")
   match choose:
        case "1":
           name = input("Podaj imie: ")
           email = input("Podaj email: ")
           cursor.execute("insert into members(imie, email) values(?, ?)", (name, email))
           conn.commit()
        case "2":
           cursor.execute("select* from members ")
           for records in cursor.fetchall():
               print(records)
        case "3":
           delId = input("Podaj id użytkownika do usunięcia: ")
           if int(delId) <= 0:
               print("Błędna wartość")
           else:
                cursor.execute("delete from members where id = ?", (delId,))
                conn.commit()
        case "4":
           break
            
                
conn.commit()
conn.close()