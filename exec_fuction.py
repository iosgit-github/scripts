from pyzabbix import ZabbixAPI
from bs4 import BeautifulSoup 
from pprint import pprint
import json


zapi = ZabbixAPI("http://10.91.1.82/")
zapi.login(api_token='05a9f38f701aa9bdce82280b222c9308fbbd26cbc14d6670f4efe53fa48381e7')
print("Connected to Zabbix API Version %s" % zapi.api_version())

with open('zbx_export_hosts.xml', 'r', encoding="utf8") as f: 
    data = f.read() 
    Bs_data = BeautifulSoup(data, "xml") 
    
