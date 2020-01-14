from services.student_services import student_services
import json

class Student:
	def on_get(self, req, resp, sid):#read
		print('get request arrived')
		print(sid)
		instance=student_services()
		#resp.status = falcon.HTTP_200
		resp.body = instance.read(sid)
		
	def on_delete(self, req, resp, sid):#delete
		#sid = json.loads(req.stream.read())['id']
		print(sid)
		instance = student_services()
		bool_val = instance.delete(sid)
		if bool_val:
			print('delete executed successfully')
			resp.body = 'Student deleted successfully'
		else:
			print('failed to delete student')
			resp.body = 'Student with id '+str(sid)+' doesn\'t exist'
	
	def on_put(self, req, resp, sid):#update
		data = json.loads(req.stream.read())
		print(data)
		instance = student_services()
		bool_val = instance.update(data, sid)
		if bool_val:
			resp.body = 'Student updated successfully'
			print('updated successfully')
		else:
			resp.body = 'Failed to update student'
			print('Failed to update student details')