import time
from notify_run import Notify
#https://notify.run/            #visit this url for more details

url = 'https://notify.run/c/oRzoKsnmcho4Groa'  #This url needs to be open in browser

ind = url.find('/c/')
if ind != -1:
    url = url[:ind] + '/' +  url[ind+3:]
    #the url python uses should not have /c

print(url)

notifyObj = Notify(endpoint = url)
notifyObj.send('Hello world 2')

for i in range(10):
    notifyObj.send(f'Hello world {i}')
    print(i)
    time.sleep(2)
