import requests
import time
import datetime
import sys

if (len(sys.argv) != 3) : 
    print("Не верное количество параметров в строке. Ожидается: логин и пароль")
    print("Например: python3 insagramAutoLike.py xxx@xxx.com yyy")
    quit()
print ('|'+sys.argv[1]+'|')

from InstagramAPI import InstagramAPI

j=-1
like=1
while 1:
        j=j+1
        tag = ['ставрополь','stavropol']
        if j >= len(tag):
                j=0
        r = requests.get('https://www.instagram.com/explore/tags/'+ tag[j] + '/',  timeout=(3.05,5))
        #print (r.text)
        id =  r.text.find('GraphImage')
        ids = []
        text = r.text
        while (text.find('GraphImage') !=-1):
                id =  text.find('GraphImage')
                print (text[id:id + 50], text.find('GraphImage'), text[id:id + 50].split('"')[4])
                ids.append(text[id:id + 50].split('"')[4])
                text = text[id+50 :]

        print ("найдено записей по тегу ",tag[j] ," : ", int(len(ids)))

        api = InstagramAPI(sys.argv[1], sys.argv[2])
        if (api.login()):
            #api.getSelfUserFeed()  # get self user feed
            #print(api.LastJson)  # print last response JSON
            #print("Login succes!")
            for i in range(0, 20): # 20 лайков на один тег
                now = datetime.datetime.now().strftime("%Y-%m-%d %X")
                print (now, "Поставлено лайков от", sys.argv[1], ":", like, '| media id : ', ids[i], '| по тегу :',tag[j])
                try:
                        api.like(ids[i])
                        #api.comment(ids[i],"🔥️")
                        #print (api.getMediaComments(ids[i]))
                        like = like + 1
                except:
                        continue
                time.sleep(60) # время в секундах между лайками
        else:
            print("Can't login!")
        print ("sleep 30")
        time.sleep(30)# время в секундах между тегами
