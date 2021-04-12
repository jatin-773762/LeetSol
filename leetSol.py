#author: Jatin Garg

import requests as req
import os

try:
    os.mkdir('codes')
except OSError as err:
    print("Directory already exists")

# cookie of signed in leetcode
cookie = '_ga=GA1.2.296230509.1600921110; __stripe_mid=db11e80d-95e2-4b7b-996d-6cc480eedea38cba7d; __cfduid=d48746dee61f41807b3b8230ae0085b261617598809; _gid=GA1.2.1266198675.1618162464; __cf_bm=1494b82f7f80bc6b65b4bb7aeb77a7619202fe96-1618246720-1800-Add256U9fjMAnk2UMJaJlSINJi1keD4QzLW4n/FixW+tubMMfASixQPCw18ZIZn0UVfjbx7i8Ph6RqbkESozdXw=; csrftoken=eOz1ytWt26fwFce719i2uaqXb6j9112fsJHF2HvIh5EQJMWiZpiz5yxqvRTwDAXm; messages="5274e1055824a5f86b282413f73b4059a2a0541b$[[\"__json_message\"\0540\05425\054\"Password successfully changed.\"]\054[\"__json_message\"\0540\05425\054\"Successfully signed in as user8710O.\"]\054[\"__json_message\"\0540\05425\054\"You have signed out.\"]\054[\"__json_message\"\0540\05425\054\"Successfully signed in as user8710O.\"]]"; LEETCODE_SESSION=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiMzA4NTIzNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImFsbGF1dGguYWNjb3VudC5hdXRoX2JhY2tlbmRzLkF1dGhlbnRpY2F0aW9uQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6ImI2NTBkNmRjNDQ4MzQxOTg5OWYyNTk1MzUxYzAzNGRlNGVhY2ExY2MiLCJpZCI6MzA4NTIzNiwiZW1haWwiOiJqYXRpbi5tYW51Z2FyZ0BnbWFpbC5jb20iLCJ1c2VybmFtZSI6InVzZXI4NzEwTyIsInVzZXJfc2x1ZyI6InVzZXI4NzEwTyIsImF2YXRhciI6Imh0dHBzOi8vYXNzZXRzLmxlZXRjb2RlLmNvbS91c2Vycy91c2VyODcxME8vYXZhdGFyXzE2MTUxNDYwNDgucG5nIiwicmVmcmVzaGVkX2F0IjoxNjE4MjQ2ODQ1LCJpcCI6IjI0MDk6NDA0MzoyOGU6ZmZmNDo1OGMyOmY3MWM6OGQzNTpiM2ZjIiwiaWRlbnRpdHkiOiI4M2Y3NWZlOGQ1YzJmNDBjMjQzNzYwYzA0ZjYwY2M0ZSIsInNlc3Npb25faWQiOjc5OTcyMzYsIl9zZXNzaW9uX2V4cGlyeSI6MTIwOTYwMH0.yhhsS55BM2kb02Nge7TLFPIoKNtyhzDVuH4NPUwG9vU; __atuvc=0%7C11%2C0%7C12%2C0%7C13%2C0%7C14%2C2%7C15; __atuvs=60747d7557227636000; c_a_u=dXNlcjg3MTBP:1lVzye:calOWDetX9BJuJcTQWNm72GPgpA; _gat=1'

offset = 0
last_key=""
count=0
err_count=0

while True:
    url = 'https://leetcode.com/api/submissions/?offset='+str(offset)+'&limit=20&lastkey='+last_key
    response = req.get(url = url,cookies = {'cookie':cookie}).json()
    try:
        # submission list
        list = response['submissions_dump']
        for x in list:
            if(x['status_display']=='Accepted'):
                filename = x['title_slug']
                lang = x['lang']
                # creating file named after title
                f = open("codes/"+filename+"."+lang,"w")
                content = "/**\n* Title: "+x['title']+"\n*\n* Ques link: https://leetcode.com/problems/"+filename+"/\n*\n**/\n\n"+x['code']
                # writing content to file
                f.write(content.replace('\\n', '\n').replace('\\t', '\t'))
                f.close()
                count+=1
                print(str(count)+") "+filename+"."+lang +" Created\n")
        offset = offset+20
        last_key = response['last_key']
        if response['has_next']!=True:
            break
    except:
        err_count+=1
        print("An error occurred")
        if err_count>2:
            break
    
print("Task Completed")