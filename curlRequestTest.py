#For Python3

import os.path
import requests
import json
import getpass

print('***Automatic ticket creator with curl command for Zendesk API***')
print('Note: Place a json payload file at the same directory of this program with file name "payload.json"')

name = input('Zendesk username (email address): ')
psd = getpass.getpass(prompt='Password?: ')
subdomain = input('Subdomain: ')
repeatTime = input('How many times do you want to run?: ')

#Check the user authentication with GET request
authtest = requests.get(url='https://{0}.zendesk.com/api/v2/tickets.json'.format(subdomain), auth=(name,psd))
authresult = authtest.status_code
print(f'HTTP status code: {authresult}')

#Run another GET API request with curl multiple times

    #payld = '[{  "ticket": { "subject":  "My printer is on fire!", "comment":  { "body": "The smoke is very colorful." },"priority": "urgent" }}]'
    #payld = '[{  "ticket": { "subject":  "My printer is on fire!", "comment":  { "body": "The smoke is very colorful." }}}]'
    #jsondata = json.loads(payld)

p = "curl https://{0}.zendesk.com/api/v2/tickets.json -d @payload.json -H \"Content-Type: application/json\"  -X POST -u {1}:{2}".format(subdomain,name,psd)
p4display = "curl https://{0}.zendesk.com/api/v2/tickets.json -d @payload.json -H \"Content-Type: application/json\"  -X POST -u {1}:xxxx".format(subdomain,name)
print(p4display)

if authresult == 200:
    if int(repeatTime) < 10:
        for i in range(int(repeatTime)):
            req = os.system(p)
            print(req)
            print (f'{i+1} times done!')
    else:
        print('That is too much!')
else:
     print(f'Error by HTTP response code= {authresult}')
