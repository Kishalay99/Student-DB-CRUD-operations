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
			resp.body = 'Student deleted successfully'
		else:
			resp.body = 'Student with id '+sid+' doesn\'t exist'
	def on_put(self, req, resp):#upsdate
		pass