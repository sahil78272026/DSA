import requests

origin= "33.815496,75.031491"
destination="20.352611,85.799043"
url = f'https://router.hereapi.com/v8/routes?apikey=8Ytn-wBh0soC3fWo5_7gbuJtklv9HxhGZEQ0Yxf001c&origin={origin}&destination={destination}&return=polyline,summary,actions,instructions,tolls&spans=notices&transportMode=truck&vehicle[grossWeight]=12000&vehicle[height]=400&departureTime=2021-11-01T10:00:00'

list1 = ['direction','severity','exit']
data = requests.get(url)
data_dict = dict(data.json())
action_data = data_dict['routes'][0]['sections'][0]['actions']
departure = data_dict['routes'][0]['sections'][0]['departure']
summary = data_dict['routes'][0]['sections'][0]['summary']
polyline = data_dict['routes'][0]['sections'][0]['polyline']
spans = data_dict['routes'][0]['sections'][0]['spans']
language = data_dict['routes'][0]['sections'][0]['language']
transport = data_dict['routes'][0]['sections'][0]['transport']
tolls = data_dict['routes'][0]['sections'][0]['tolls']
tollSystems = data_dict['routes'][0]['sections'][0]['tollSystems']


keys = data_dict['routes'][0]['sections'][0].keys()
# for i in action_data:
#     for j in list1:
#         if j not in i.keys():
#             i[j]=None

# for i in action_data:
#     print(i)

print(keys) # dict_keys(['id', 'type', 'actions', 'departure', 'arrival', 'summary', 'polyline', 'spans', 'language', 'transport', 'tolls', 'tollSystems'])
print(action_data)
print(tollSystems)
