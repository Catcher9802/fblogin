import requests
import sys

# ตรวจสอบเมื่อเกิดความผิดพลาด
try:
	access_token = input("ACCESS_TOKEN : ")
	
	# เมื่อ ACCESS_TOKEN รับข้อมูลเข้ามาใช้ API เพื่อเช็คว่าถูกหรือผิด
	r = requests.get(f"https://graph.facebook.com/v14.0/me?fields=id%2Cname&access_token={access_token}")
	
	# เมื่อ ACCESS_TOKEN ถูก
	if r.ok == True:
		# สร้างตัวแปร User เพื่อรับชื่อเฟสบุ๊คตาม ACCESS_TOKEN
		user = f"{r.json()['name']}" # จะรับชื่อเฟสบุ๊ค
		# สร้างตัวแปร ID เพื่อรับไอดี Username ของชื่อเฟสบุ๊คตาม ACCESS_TOKEN
		ID = f"{r.json()['id']}" # จะรับไอดี Username
		print(f"""
		------
		User : {user}
		ID : {ID}
		""")
	# เมื่อ ACCESS_TOKEN ไม่ถูกต้อง
	else:
		print("ACCESS_TOKEN ไม่ถูกต้อง")
		sys.exit(1)
		
except:
	pass