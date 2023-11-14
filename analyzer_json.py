import json
from pprint import pprint

class zbx_json_analizer:
    def group_name_extraction():
        with open('zbx_export_hosts.json', 'r') as f:
            group_name_to_creation = []
            dados = json.loads(f)
            data_analize_results=dados['zabbix_export']['host_groups']
            for i in range(0, len(data_analize_results)):
                group_name = data_analize_results[i]['name']
                group_name_to_creation.append(group_name)
            return group_name_to_creation
        
    def host_extraction_data():
        with open('zbx_export_hosts.json', 'r') as f:
            group_name_to_creation = []
            dados = json.load(f)
            data_analize_results=dados['zabbix_export']
            pprint(data_analize_results)

    host_extraction_data()  
           