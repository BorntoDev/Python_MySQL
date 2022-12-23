import mysql.connector

#ทำการเชื่อมต่อกับฐานข้อมูลง่าย ๆ แค่ใส่ Host / User / Password ให้ถูกต้อง
connection = mysql.connector.connect(
  host="localhost",
  user="กรอก Username ตรงนี้",
  password="กรอกรหัสผ่านตรงนี้",
  database="OurDB"
)

db_cursor = connection.cursor()

#เราสามารถรันคำสั่ง SQL ในการสร้าง Database  ได้เลย
db_cursor.execute("CREATE DATABASE OurDB")

#สร้าง Table ลงไป ก็ใช้ Execute ได้เช่นกัน
db_cursor.execute("CREATE TABLE employees (name VARCHAR(255), address VARCHAR(255))")
