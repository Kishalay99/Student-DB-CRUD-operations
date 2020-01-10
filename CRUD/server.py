import falcon
from falcon_cors import CORS    
cors = CORS(allow_origins_list=['http://127.0.0.1'],allow_all_headers=True, allow_all_methods=True)   

from controllers.students_controller import Students

api = falcon.API(middleware=[cors.middleware])
api.add_route('/students',Students())
api.add_route('/teachers',Students())