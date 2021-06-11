import os
import json
import sys

with open("data.json","r") as f :
    data = json.load(f)

check_for = sys.argv[1]

for i in data['sessions'] :
    if i[check_for] > 0 :
        json_obj = json.dumps(i,indent=4)
        with open("available.json","a") as f :
            f.write(json_obj)

        print('\n')
        print('CENTER')
        print('--------------------------------------------------------------------------------')
        print(i)

