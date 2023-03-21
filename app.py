import random
from urllib.request import urlopen
from flask import Flask, request
from flask_restful import Resource, Api
import json
import datetime

# 創建Flask app物件
app = Flask(__name__)
api = Api(app)


@app.route("/")
def hello():
    return "<h1>Hello , This a Restful Api Server by Flask...</h1>"


# 創建一個陣列(創一個名為apple物品當測試)，存放品項
items = [
    {
        "name": "apple",
        "price": 32.3
    }
]


class Item(Resource):

    # 單一品項查詢
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item else 404

    # 建制新品項
    def post(self, name):
        # 如果該品項已經存在 items 內，就找出並回傳給客戶端該品項已經存在
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message': f'An item with name {name} already exists ..'}, 403
        # 如果該品項不存在，則解析客戶端傳來的body，並將其品項寫入 items
        data = request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201


class squat(Resource):
    # 建制新squat record
    def post(self):
        if request.is_json: # 判斷是不是 JSON
           file1 = open("MyFile1.txt", "a")
           data = request.get_json()
   
           data.update({"empid": "12345"})  # 增加元素
           data.update({"skey": random.randrange(100)})  # 增加元素  
           data.update({"createdate": str(datetime.datetime.now())})  # 增加元素  
           print(type(data))  #'dict'
           print(data)
           
           #json.dumps() , 將python物件轉成json字串，返回type為str , 從python物件轉換為json字串
           #json.loads() , 將json字串，返回python物件，返回type為dict, 從json字串轉換為python物件
           #data.setdefault('c','ddd') #新增字典的key和value值使用.setdefault()
           #print(data)
           
           json_data = json.dumps(data) 
           
           print(json_data)
           print(type(json_data)) 
           
           with open('data.json','r+') as file11: 
                file_data = json.load(file11)
                file_data["emp_details"].append(data) 
                file11.seek(0)
                json.dump(file_data, file11, indent = 4)
           
           file1.write(str(json_data)+'\n')
           file1.close()
           dict_json = json.dumps(request.get_json()) # 從資料中獲取值
        else:
           result = 'Not JSON Data'
        #return json.dumps(dict_json)
        return  json_data 
        
    # function to add to JSON
    def write_json(new_data, filename='data.json'):
        with open(filename,'r+') as file:
            # First we load existing data into a dict.
            file_data = json.load(file)
            # Join new_data with file_data inside emp_details
            file_data["emp_details"].append(new_data)
            # Sets file's current position at offset.
            file.seek(0)
            # convert back to json.
            json.dump(file_data, file, indent = 4)

class ItemsList(Resource):
    # 取得所有品項
    def get(self):
        return {'items': items}


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemsList, '/items')
api.add_resource(squat, '/squat')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # app.run(port=5000, debug=True)
