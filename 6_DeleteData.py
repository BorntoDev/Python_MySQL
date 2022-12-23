import mysql.connector

#ทำการเชื่อมต่อกับฐานข้อมูลง่าย ๆ แค่ใส่ Host / User / Password ให้ถูกต้อง
connection = mysql.connector.connect(
  host="localhost",
  user="กรอก Username ตรงนี้",
  password="กรอกรหัสผ่านตรงนี้",
  database="OurDB"
)

db_cursor = connection.cursor()

#สร้าง String สำหรับใส่คำสั่งลบพนักงานออกตาม Address ที่ระบุไว้
sql_command = "DELETE FROM employees WHERE address = 'Papiyong Kook Kook'"

#สั่งให้คำสั่งทำงานได้เลย
db_cursor.execute(sql_command)

connection.commit()

#แสดงว่ามีกี่แถวที่ทำงานสำเร็จ
print(db_cursor.rowcount, "Deleted !")
