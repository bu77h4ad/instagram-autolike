import requests
import time
import datetime
import sys

if (len(sys.argv) < 5 ) : 
    print("\nНе верное количество параметров в строке. \nОжидается: логин, пароль, время лайка в секундах, hashtag. \nНапример: python3 insagramAutoLike.py xxx@xxx.com pass 60 russia")  
    quit()
print ('|'+sys.argv[1]+'|')

from InstagramAPI import InstagramAPI

like=1
while True:
        tag = str(sys.argv[4])        
        r = requests.get('https://www.instagram.com/explore/tags/'+ tag + '/',  timeout=(3.05,5))
        #print (r.text)
        id =  r.text.find('GraphImage')
        ids = []
        text = r.text
        while (text.find('GraphImage') !=-1):
                id =  text.find('GraphImage')
                print (text[id:id + 50], text.find('GraphImage'), text[id:id + 50].split('"')[4])
                ids.append(text[id:id + 50].split('"')[4])
                text = text[id+50 :]

        print ("найдено записей по тегу ",tag ," : ", int(len(ids)))

        api = InstagramAPI(sys.argv[1], sys.argv[2])
        if (api.login()):
            #api.getSelfUserFeed()  # get self user feed
            #print(api.LastJson)  # print last response JSON
            #print("Login succes!")
            for i in range(0, 20): # 20 лайков на один тег
                now = datetime.datetime.now().strftime("%Y-%m-%d %X")
                print (now, "Поставлено лайков от", sys.argv[1], ":", like, '| media id : ', ids[i], '| по тегу :',tag)
                try:
                        api.like(ids[i])
                        #api.comment(ids[i],"🔥️")
                        #print (api.getMediaComments(ids[i]))
                        like = like + 1
                except:
                        continue
                time.sleep(int(sys.argv[3])) # время в секундах между лайками
        else:
            print("Can't login!")
        
        

