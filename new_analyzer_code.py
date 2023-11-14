import json
from pprint import pprint


group_name_to_creation = []
with open('zbx_export_hosts.json', 'r') as f:
    dados = json.load(f)
    data_analize_results=dados['zabbix_export']['host_groups']
    
    for i in range(0, len(data_analize_results)):
        group_name = data_analize_results[i]['name']
        group_name_to_creation.append(group_name)

pprint(group_name_to_creation)

