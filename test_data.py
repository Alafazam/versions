from requests import put

put('http://192.168.59.103/update', data={'systems':'dev', 'components': 'components 1', 'version': 'version 2.', 'source': 'alaf','user':'q','pass':'a'}).json()

