import falcon
from controllers.students_controller import Students

api = falcon.API()
api.add_route('/students',Students())
api.add_route('/teachers',Students())