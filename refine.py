import sys

with open("pincode.txt","r") as f :
    text = f.readlines()

pincodes_list = []

for i in text:
    j = i.strip().split()

    for k in j :
        if k.isdigit() :
            pincodes_list.append(k)

print(pincodes_list)
print(len(pincodes_list))

write = [ i+'\n' for i in pincodes_list]

with open("pincode_list.txt","w") as f :
    f.writelines(write)
