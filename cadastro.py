# Importação de Bibliotecas e Dependencias
from pyzabbix import ZabbixAPI
from pyzabbix import *
import json
from pprint import pprint
import pandas as pd
from collections import Counter

# ---------------------------Conexão API Zabbix--------------------------------------
zapi = ZabbixAPI("http://172.23.38.192/zabbix/")
zapi.login(api_token='ae5ca16c30490a9ef33b3f461f01e1e4119fe6b21dcfeb0e20df79b56e354277')
print("Conexão realizada com sucesso, versão de API %s" % zapi.api_version())

sla_get = zapi.sla.get(output='extend')
pprint(sla_get)

# -------------------------Tratando a Base de dados --------------------------------
#Service Pai
data_frame_services_pai = pd.read_excel("Modelo Padrão Excell.xlsx", sheet_name="Service Pai")
services_pai = pd.DataFrame(data_frame_services_pai)
json_coluns_service_pai = services_pai.to_json(orient='columns')
json_service_pai = json_coluns_service_pai
json_string_service_pai =json_service_pai
lista_service_pai  = json_object = json.loads(json_string_service_pai)
final_list_service_pai = list(lista_service_pai.items())
tuple_service_pai_name = final_list_service_pai[0] 
lista_service_pai_final = mylist = list(tuple_service_pai_name)
data_service_register =  lista_service_pai_final[1]['0']
zapi.service.create(
    name= data_service_register,
    algorithm = 1,
    sortorder = 1,
)
pprint("Serviço Pai criado com sucesso")
serviceid = zapi.service.get(filter= {'name': data_service_register})
service_id_colect = serviceid[0]['serviceid']

#Criação dos Services filhos
data_frame_services_filho = pd.read_excel("Modelo Padrão Excell.xlsx", sheet_name="Service Filho")
services_filho = pd.DataFrame(data_frame_services_filho)
json_coluns_services_filho = services_filho.to_json(orient='columns')
json_service_filho = json_coluns_services_filho
json_string_services_filho =json_service_filho
lista_services_filho  = json_object = json.loads(json_string_services_filho)
final_list_service_filho = list(lista_services_filho.items())
tuple_service_filho_name = final_list_service_filho
service_name_to_register_final = tuple_service_filho_name[0][1]
service_tag_to_register_final = tuple_service_filho_name
name_tag_value_service_problem=service_tag_to_register_final[3][1]

for i in range(0,len(service_name_to_register_final)):
    servi_name= service_name_to_register_final[f'{i}']
    tag_service_problems_value = name_tag_value_service_problem[f'{i}']
    name_tag = 'sla'
    zapi.service.create(
        name = servi_name,
        algorithm = 1,
        sortorder = 1,
        tags= [{'tag':"sla", "value": "1cta"}],
        parents=[{'serviceid':service_id_colect}],
        problem_tags = [{
            'tag': f'{name_tag}', 'value': tag_service_problems_value, 'operator':'0', }]
                )
    
# SLA Create   
data_frame_sla = pd.read_excel("Modelo Padrão Excell.xlsx", sheet_name="SLA")
sla = pd.DataFrame(data_frame_sla)
json_coluns_sla = sla.to_json(orient='columns')
json_sla = json_coluns_sla
json_string_sla =json_sla
lista_sla  = json_object = json.loads(json_string_sla)
final_list_sla = list(lista_sla.items())
tuple_sla = final_list_sla
list_externa_sla_create = []

for i in range (0,len(tuple_sla)):
    sla_sla = tuple_sla[i]
    name = sla_sla[1]
    for l in range (0, len(name)):
        var_definitiva = name[f'{l}']
        var_definitiva = [var_definitiva]
        list_externa_sla_create.append(var_definitiva)


Name = list_externa_sla_create[0][0]
slo = list_externa_sla_create[1][0]
period = list_externa_sla_create[2][0]
Time_zone = list_externa_sla_create[3][0]
Schedule = 1
service_tag_name = list_externa_sla_create[4][0]
service_tag_value = list_externa_sla_create[5][0]

zapi.sla.create(
    name = Name,
    slo = slo,
    period = 0,
    timezone = Time_zone,
    effective_date = 1690243200,
    service_tags = [{
        "tag": service_tag_name,
        "operator": "0",
        "value": service_tag_value,
    }],
)
        