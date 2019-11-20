import requests


#--------------------------------------------

url_login = "https://46.101.127.78:9443/rm/j_security_check"
url_rootservices = "https://46.101.127.78:9443/ccm/rootservices"
url_spCatalog = "https://46.101.127.78:9443/qm/oslc_qm/catalog"


response_login = requests.post(
    url_login,
    params={'j_username': 'koneksys', 'j_password': 'koneksys'},
    verify=False
)
#print(response_login.status_code)
#print(response_login.text)
print(response_login.headers)
#print (response_login.text)

#headers = response_login.headers
#JAZZ_AUTH_TOKEN = headers['JAZZ_AUTH_TOKEN']
#print (JAZZ_AUTH_TOKEN)

'''
response_rootServices = requests.get(
    url_rootservices,
    headers={'Accept': 'application/rdf+xml', 
            'OSLC-Core-Version': '2.0', 
            'JAZZ_AUTH_TOKEN': '22a179a635634203b6e804fd437b4d68&yRmZzBnYVWLtQ6xPU0zpF1kxKSrY0JgmIGxJKhcXVg'},
    verify=False
)

#print("RootServices>>>>> ", response_rootServices.text)


response_spCatalog = requests.get(
    url_spCatalog,
    headers={'Accept': 'application/rdf+xml', 
             'Content-Type': 'application/rdf+xml',
            'OSLC-Core-Version': '2.0', 
            'JAZZ_AUTH_TOKEN': '78cd6dec3f924c518e7c8fec766a70f8&diiPmYndH5klcwioHpF89tTvE4WG5Jtz7rcaEhosqTU',
            'JSESSIONID': '0000bB48xgSFXEDrfXwL1E83d1_:877c75dc-dbc3-47ac-b19e-cdd651ef4868',
            'LtpaToken2': 'uRfs+QKKpnt73TmCnPi/AewN7+1605g4nTrRi4Eg0j9FTd5BoUJf2EPdrPkrJvs2YZBN1yFkgnuB8w/D28C/eiKTbjFu/WMZUacuJ3bNvv9arWyDbar/ACMaj5sWSg80mgLPiEzqkgr33TkQYWQYUTzag5X57bR9BMIq0eAJmio+lMYCfg9BKaUifT0q/hkS5drC36c6ughU6Yu3RWKw0dPCeuxx6YV00VJbdunQwLP9T71LEb7iYrCjSFX2eBXONB3OEOaMhp6Vdnb/b/bemJceiyayfHMDS9UWqMJe6g56995jOVjMZhQ16xuH+k7n'},
    verify=False
)

spCatalog_status_code = response_spCatalog.status_code;
print(f"Service Provider Catalog: [ {spCatalog_status_code} ]>>>>> ", response_spCatalog.text)
'''
