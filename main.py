from flask import Flask, request
from flask_restx import Api, Resource, fields, reqparse


# field name
REGION = 'region'
PRICE = 'price'
DATE = 'date'

# TEST
data = dict()
data['seoul'] = 1701
data['busan'] = 1608
data['daegu'] = 1573
data['jeju'] = 1632


app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument(REGION, type=str, default=None, help='If there is no value, all data is returned')


@api.route('/read')
class ReadData(Resource):
    @api.expect(parser)
    def get(self):
        args = parser.parse_args()
        region = args.get(REGION)
        if region is None:
            return data

        return {region: data.get(region)}


resource_fields = api.model('Data', {
        REGION: fields.String,
        PRICE: fields.Float
    })


@api.route('/create')
class CreateData(Resource):
    @api.expect(resource_fields)
    def post(self):
        region = request.json[REGION]
        price = request.json[PRICE]

        if region in data:
            return f'[KeyError] Already exists {region} key', 404

        data[region] = price
        return data


@api.route('/update')
class UpdateData(Resource):
    @api.expect(resource_fields)
    def post(self):
        region = request.json[REGION]
        price = request.json[PRICE]

        if region not in data:
            return f"[KeyError] Invalid key: {region}", 404

        data[region] = price
        return f'Successfully updated {region}:{price}'


@api.route('/delete/<string:region>')
class DeleteData(Resource):
    def put(self, region):
        if region not in data:
            return f"[KeyError] Invalid key: {region}", 404

        price = data.pop(region)
        return f'Successfully deleted {region}:{price}'


if __name__ == '__main__':
    app.run()
