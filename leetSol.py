#author: Jatin Garg

import requests as req
import os

try:
    os.mkdir('codes')
except OSError as err:
    print("Directory already exists")

# cookie of signed in leetcode
cookie = 'paste your leetcode cookie here'

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
