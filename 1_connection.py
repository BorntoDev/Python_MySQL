import mysql.connector

#ทำการเชื่อมต่อกับฐานข้อมูลง่าย ๆ แค่ใส่ Host / User / Password ให้ถูกต้อง
connection = mysql.connector.connect(
  host="localhost",
  user="กรอก Username ตรงนี้",
  password="กรอกรหัสผ่านตรงนี้"
)

print(connection)
