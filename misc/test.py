import json

actvt_data = {
'params':
[
{
'name':'EXECUTION TYPE',
'value':'DBProcess'
},
{
'name':'DATA SOURCE',
'value':'RM/MDM/MRB'
},
{
'name':'PROCESS TYPE',
'value':'APS_PRODACTALL'
},
{
'name':'PARAM_1_NUMBER_OF_REQUEST',
'value':'1'
},
{
'name':'PARAM_2_PRODUCT_LEVEL',
'value':'2'
},
{
'name':'PARAM_3_TRACE_FLAG',
'value': 'N'
}
]
}

jb=json.dumps(actvt_data)
print(jb)