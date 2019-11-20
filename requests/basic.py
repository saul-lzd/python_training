#Import requests library
import requests
import json
from requests.exceptions import HTTPError



# Status Codes
#--------------------------

# execute simple GET request
requests.get('https://api.github.com')

# the return value of get() is an instance of Response
# https://www.w3schools.com/python/ref_requests_response.asp
response = requests.get('https://api.github.com')

# status code
status = response.status_code
print(status)

# Example 1
# validate response status

if response.status_code ==  200:
    print('OK')
elif response.status_code == 404:
    print('NOT FOUND')

# Response instance is a conditional expresion,
# it will evaluate to TRUE  if the status code 
# was between 200 and 400, and FALSE otherwise.

#Example 2
if response:
    print ('OK')
else:
    print('ERROR')


# raise_for_status() is raised when 
# the requests was unsuccesful
print('------------------------------------------------------------')
print('Status code')
print('------------------------------------------------------------')
for url in ['https://api.github.com', 'https://httpstat.us/404', 'https://httpstat.us/401', 'http://www.dummieshtm.com/nofileexisting.html']:
    try:
        response = requests.get(url)
        #status = response.status_code
        response.raise_for_status() # if response is successful, no Exception is raised
    except HTTPError as http_err:
        print(f'Http error ocurred {http_err}')
    except Exception as err:
       print(f'Exception ocurred {err}')
    else:
        print(f'A successful response from server was received: {status}')



print('------------------------------------------------------------')
print('Content')
print('------------------------------------------------------------')

response = requests.get('https://api.github.com')

# .content returns raw bytes of the response payload
response.content
# .text returns a string using a character encoding such as UTF-8.
response.text
# set explicit encoding
response.encoding = 'utf-8'
response.text

# deserialize body
# json.loads() and .json() returns a dictionary
# so you can access values in the response content by key

j1 = json.loads(response.text)
print('1> current_user_authorizations_html_url: ', j1['current_user_authorizations_html_url'])

j2 = response.json()
print('2> current_user_authorizations_html_url: ', j2['current_user_authorizations_html_url'])


print('------------------------------------------------------------')
print('Headers')
print('------------------------------------------------------------')

# get headers
headers = response.headers
print(f'Headers:  {headers}')

# .headers returns a dictionary-like object
contentType = headers['Content-Type']
print(f'Content Type:  {contentType}')

server = headers['server']
print(f'server:  {server}')


print('------------------------------------------------------------')
print('Query String parameters')
print('------------------------------------------------------------')

server = 'https://api.github.com/search/repositories'

# execute get with parameters 
# https://api.github.com/search/repositories?q=requests+language:pyhton
response = requests.get(
    server, 
    params={'q': 'requests+language:pyhton'}
)
# get response as dictionary
json_response = response.json()
# get first element of the items property
repository = json_response['items'][0]

#print(repository)
# print each property of the object to inspect
print(f'Repository name: {repository["name"]}')
print(f'Repository description: {repository["description"]}')
print(f'Repository owner: {repository["owner"]["login"]}')


print('------------------------------------------------------------')
print('Request Headers')
print('------------------------------------------------------------')

response = requests.get(
    server, 
    params={'q': 'requests+language:pyhton'},
    headers={'Accept': 'application/vnd.github.v3.text-match+json'}
)

json_response = response.json()
repository = json_response['items'][0]
print(f'Text matches: {repository["text_matches"]}')


print('------------------------------------------------------------')
print('POST request')
print('------------------------------------------------------------')

'''
requests.post(url, data={key: value}, json={key: value}, args)

data -> 'application/x-www-form-urlencoded'
json -> 'application/json'
args -> https://www.w3schools.com/python/ref_requests_post.asp
'''

element = {'name' : 'saul', 'last_name': 'lopez'}

response = requests.post(
    'https://httpbin.org/post',
    json=element
)

json_response = response.json();
print(f'Response: {json_response}')

headers = json_response['headers']
#print(f'Response: {json_response["headers"]}')
print(f'Headers: {headers}')


print('------------------------------------------------------------')
print('Inspecting request')
print('------------------------------------------------------------')
# When you make a request, 
# the requests library prepares the request 
# before actually sending it to the destination server. 
# Request preparation includes things like 
# validating headers and serializing JSON content. 
dummy_server = 'https://httpbin.org/post'
params = {'name' : 'saul', 'last_name': 'lopez'}

response = requests.post(
    dummy_server,
    data=params
)

response2 = requests.post(
    dummy_server,
    json=params
)


'''
print ('data: ', response.request.url)
print ('json: ', response2.request.url)
print (response.request.body)
print (response2.request.body)
print (response.request.headers)
print (response2.request.headers)
'''

