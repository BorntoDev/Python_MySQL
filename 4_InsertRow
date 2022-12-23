import mysql.connector

#ทำการเชื่อมต่อกับฐานข้อมูลง่าย ๆ แค่ใส่ Host / User / Password ให้ถูกต้อง
connection = mysql.connector.connect(
  host="localhost",
  user="กรอก Username ตรงนี้",
  password="กรอกรหัสผ่านตรงนี้"
)

db_cursor = connection.cursor()

#สร้าง String ไว้รอใส่คำสั่งได้เลย
sql_command = "INSERT INTO employees (name, address) VALUES (%s, %s)"

#Value ที่ต้องการใส่ใน Command ทำไว้ในรูปแบบ Tuple ไว้ทำการ map กับคำสั่งด้านบนในตรง VALUES
val = ("Jazz", "Papiyong Kook Kook")

#สั่งให้คำสั่งทำงานได้เลย
db_cursor.execute(sql_command, val)

connection.commit()

#แสดงว่ามีกี่แถวที่ทำงานสำเร็จ
print(db_cursor.rowcount, "Succeed !")
