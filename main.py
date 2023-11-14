from analyzer_json import group_name_extraction
from pprint import pprint

groups_to_cadaster = group_name_extraction()
pprint(type(groups_to_cadaster))