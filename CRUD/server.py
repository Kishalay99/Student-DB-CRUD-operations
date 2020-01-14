import falcon
#from falcon_cors import CORS    
#cors = CORS(allow_origins_list=['http://127.0.0.1'],allow_all_headers=True, allow_all_methods=True)   
from falcon.http_status import HTTPStatus
from controllers.students_controller import Students
from controllers.student_controller import Student


class HandleCORS(object):
    def process_request(self, req, resp):
        resp.set_header('Access-Control-Allow-Origin', '*')
        resp.set_header('Access-Control-Allow-Methods', '*')
        resp.set_header('Access-Control-Allow-Headers', '*')
        resp.set_header('Access-Control-Max-Age', 1728000)  # 20 days
        if req.method == 'OPTIONS':
            raise HTTPStatus(falcon.HTTP_200, body='\n')


api = falcon.API(middleware=[ HandleCORS() ])

api.add_route('/students',Students())
api.add_route('/teachers',Students())
api.add_route('/students/{sid:int}',Student())
