from services.students_services import students_services

class Students:
	def on_get(self, req, resp):#read
		print('request arrived')
		x=students_services()
		resp.body = x.read()
	def on_post(self, req, resp):#create
		pass
	def on_delete(self, req, resp):#delete
		pass
	def on_put(self, req, resp):#upsdate
		pass