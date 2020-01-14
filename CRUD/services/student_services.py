import mysql.connector
import json
from datetime import datetime

mydb = mysql.connector.connect(host='localhost', user='kishalay', passwd='master$123', database='students')
cur = mydb.cursor()

att = ['id','name','dob','gender','branch','last_updated']

class student_services:
	def read(self, sid):
		print('services function called')
		query = 'select * from student where id=%s'
		cur.execute(query,(sid, ))
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

	def update(self, data, sid):
		sid = data['id']
		name = data['name']
		dob = data['dob']
		gender = data['gender']
		branch = data['branch']

		update_query = 'update student set name=%s, dob=%s, gender=%s, branch=%s where id=%s'
		values = (name,dob,gender,branch,sid)
		cur.execute(update_query, values)
		if cur.rowcount!=0:
			mydb.commit()
			return True
		else:
			return False
	
	def delete(self, sid):
		del_query = 'delete from student where id = %s'
		values = (sid, )
		cur.execute(del_query,values)
		mydb.commit()
		falcon.HTTPSeeOther('/students', headers=None)