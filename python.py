

# class Cat(Resource):
#     def get(self):
#         return {'data':'get'}
#
#     def post(self):
#         return {'data': 'post'}
#
#     def put(self):
#         return {'data': 'put'}
#
#     def delete(self):
#         return {'data': 'delete'}
from pip._vendor.distlib.resources import Resource


class Home(Resource):
    def get(self):
        # return render_template('test.html')
        pass

class Market(Resource):
    def get(self):
        # return render_template('market/market.html')
        pass


class Cart(Resource):
    def get(self):
        # return render_template('art/cart.html')
        pass


class Mine(Resource):
    def get(self):
        # return render_template('mine/mine.html')
        pass



print("sss")