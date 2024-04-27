import psycopg2

conn = psycopg2.connect(dbname="Cathedra", host="127.0.0.1", user="postgres", password="horosh1337@", port="5432")

cursor = conn.cursor()
 
cursor.execute("INSERT INTO public.books (id, name, description) VALUES(1, 'Мастер и Маргарита', 'Крутая книга')")
 
conn.commit()   # реальное выполнение команд sql1
 
cursor.close()
conn.close()