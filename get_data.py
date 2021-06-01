import os
import json

with open("data.json","r") as f :
    data = json.load(f)

for i in data['sessions'] :
    if i['available_capacity_dose2'] > 0 :
        print('\n')
        print('CENTER')
        print('--------------------------------------------------------------------------------')
        print(i)


