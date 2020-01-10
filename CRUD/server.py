import falcon

api = falcon.API()
api.add_route('/students',Student())
api.add_route('/teachers',