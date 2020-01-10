import mysql.connector
import json

mydb = mysql.connector.connect(host='localhost', user='kishalay', passwd='master$123', database='students')
cur = mydb.cursor()

att = ['id','name','dob','gender','branch','last_updated']

class students_services:
	def read(self):
		print('services function called')
		query = 'select * from student'
		cur.execute(query)
		data=[]
		
		for row in cur:
			entry={}
			for i,attribute in enumerate(att):
				if attribute=='last_updated':
					entry[attribute]=row[i].strftime("%d/%m/%Y, %H:%M:%S")
					continue
				if attribute=='dob':
					entry[attribute]=row[i].strftime("%d/%m/%Y")
					continue
				entry[attribute] = row[i]
			
			data.append(entry)
		print('data fetched')
		return json.dumps(data)