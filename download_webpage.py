"""
Program to download webpage
In this program I will download a json file from website
"""

import requests

url = r'https://partnerweb.vmware.com/service/vsan/all.json'
response = requests.get(url)

# Raise an exception in case response is not 200
# Alternatively, it can be checked using response == requests.codes.ok
response.raise_for_status()

# Save the content in file
# file is opened in binary mode to preserve unicode text
with open('all.json', 'wb') as fh:
    fh.write(response.text)

# Alternatively data can be saved in file in small chunks
# fh = open('all.json', 'wb')
# for chunk in response.iter_content(chunk_size=100000):
#     fh.write(chunk)

