from InstagramAPI import InstagramAPI
import requests
import time
import datetime

j=-1
like=0
while 1:
	j=j+1
	tag = ['stv','фото', 'russia']
	if j >= len(tag):
		j=0
	r = requests.get('https://www.instagram.com/explore/tags/'+ tag[j] + '/',  timeout=(3.05, 27) )     
	#print (r.text)
	id =  r.text.find('GraphImage')
	ids = []
	text = r.text
	while (text.find('GraphImage') !=-1):	
		id =  text.find('GraphImage')
		print (text[id:id + 50], text.find('GraphImage'), text[id:id + 50].split('"')[4])
		ids.append(text[id:id + 50].split('"')[4])
		text = text[id+50 :]
		

	api = InstagramAPI("login", "pass")
	if (api.login()):
	    #api.getSelfUserFeed()  # get self user feed
	    #print(api.LastJson)  # print last response JSON    
	    print("Login succes!")
	    for i in range(0,len(ids)):
	    	now = datetime.datetime.now().strftime("%Y-%m-%d %X")
	    	print (now, "like is:",like, ids[i], 'tag ',tag[j])
	    	try:
	    		api.like(ids[i])
	    		like = like + 1	    		
	    	except:
	    		continue
	    	time.sleep(50)
	else:
	    print("Can't login!")
	print ("sleep 30")
	time.sleep(300)
