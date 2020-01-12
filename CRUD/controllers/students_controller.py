from services.students_services import students_services
import json

class Students:
	def on_get(self, req, resp):#read
		print('get request arrived')
		instance=students_services()
		#resp.status = falcon.HTTP_200
		resp.body = instance.read()
	
	def on_post(self, req, resp):#create
		print('post request arrived')
		data = req.stream.read()
		instance = students_services()
		bool_val = instance.insert(data)
		if(bool_val):
			#resp.status = falcon.HTTP_201
			resp.body = 'Student added successfully'
		else:
			#resp.status = falcon.HTTP_400
			resp.body = 'Failed to insert student'
		
	def on_delete(self, req, resp):#delete
		sid = json.loads(req.stream.read())['id']
		print(sid)
		instance = students_services()
		bool_val = instance.delete(sid)
		if bool_val:
			print('delete executed successfully')
			resp.body = 'Student deleted successfully'
		else:
			print('failed to delete student')
			resp.body = 'Student with id '+str(sid)+' doesn\'t exist'
	
	def on_put(self, req, resp):#update
		data = json.loads(req.stream.read())
		print(data)
		instance = students_services()
		bool_val = instance.update(data)
		if bool_val:
			resp.body = 'Student updated successfully'
			print('updated successfully')
		else:
			resp.body = 'Failed to update student'
			print('Failed to update student details')