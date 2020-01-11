import mysql.connector
import json
from datetime import datetime

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

	def insert(self, data):
		# print(type(data))
		data = json.loads(data)
		name = data['name']
		dob = data['dob']#datetime.strptime(data['dob'], '%y/%m/%d')
		gender = data['gender']
		branch = data['branch']
		print(dob)
		query = "insert into student (name, dob, gender, branch) values (%s,%s,%s,%s)"
		values = (name,dob,gender,branch)
		cur.execute(query,values)

		if(cur.rowcount==1):
			mydb.commit()
			return True
		else:
			return False

	def update(self, data):
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
		fetch_query = 'select id from student'
		cur.execute(fetch_query)
		res = cur.fetchall()
		print(res)
		all_ids = []
		for tupl in res:
			all_ids.append(str(tupl[0]))
		print(all_ids)
		if sid in all_ids:
			del_query = 'delete from student where id = %s'
			values = (sid, )
			cur.execute(del_query,values)
			mydb.commit()
			return True
		else:
			return False