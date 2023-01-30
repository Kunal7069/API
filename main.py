from flask import *
import json
import pandas as pd
# BASE_URL = 'http://jaink7069.pythonanywhere.com/'
app = Flask(__name__)

data = pd.read_csv('Book1.csv')
lent = len(data)
data_set= []
for i in range(lent):
    data_set.append([str(int(data['year'][i])), data['name'][i], data['field'][i], data['branch'][i]])

@app.route('/data/',methods=['GET'])
def home_page():
    data2 = pd.read_csv('Book1.csv')
    lent2 = len(data2)
    data_set2 = []
    for i in range(lent2):
        data_set2.append([str(int(data['year'][i])), data['name'][i], data['field'][i], data['branch'][i]])

    json_dump = json.dumps(data_set2)
    return json_dump
@app.route('/add/',methods=['GET'])
def add_page():
    user_query1 = str(request.args.get('year'))
    user_query2 = str(request.args.get('name'))
    user_query3 = str(request.args.get('field'))
    user_query4 = str(request.args.get('branch'))
    data1 = pd.read_csv('Book1.csv')
    lent1 = len(data)
    data1.loc[lent1, 'year'] = user_query1
    data1.loc[lent1, 'name'] = user_query2
    data1.loc[lent1, 'field'] = user_query3
    data1.loc[lent1, 'branch'] = user_query4
    data1.to_csv('Book1.csv', index=False)
    data2 = pd.read_csv('Book1.csv')
    print(data2)

@app.route('/',methods=['GET'])
def mix_page():
    # user_query1, user_query2, user_query3, user_query4 = "default"
    user_query1 = str(request.args.get('year'))
    user_query2 = str(request.args.get('name'))
    user_query3 = str(request.args.get('field'))
    user_query4 = str(request.args.get('branch'))
    mix_set1 = []
    mix_set2 = []
    mix_set3 = []
    mix_set4 = []
    if user_query1 != "default":
        for x, i in enumerate(data_set):
            if data_set[x][0] == user_query1:
                mix_set1.append(data_set[x])
    if user_query2 != "default":
        for x, i in enumerate(data_set):
            if data_set[x][1] == user_query2:
                mix_set2.append(data_set[x])
    if user_query3 != "default":
        for x, i in enumerate(data_set):
            if data_set[x][2] == user_query3:
                mix_set3.append(data_set[x])
    if user_query4 != "default":
        for x, i in enumerate(data_set):
            if data_set[x][3] == user_query4:
                mix_set4.append(data_set[x])
    # lst3 = [value for value in lst1 if value in lst2] intersection
    # final_list = lst1 + lst2 union
    result_set = []
    if user_query1 != "default":
        result_set = mix_set1
    elif user_query2 != "default":
        result_set = mix_set2
    elif user_query3 != "default":
        result_set = mix_set3
    elif user_query4 != "default":
        result_set = mix_set4
    else:
        result_set = data_set
    if user_query1 != "default":
        result_set = [value for value in result_set if value in mix_set1]
    if user_query2 != "default":
        result_set = [value for value in result_set if value in mix_set2]
    if user_query3 != "default":
        result_set = [value for value in result_set if value in mix_set3]
    if user_query4 != "default":
        result_set = [value for value in result_set if value in mix_set4]
    json_dump = json.dumps(result_set)
    return json_dump
if __name__=='__main__':
    app.run(debug=False,host='0.0.0.0')
