import requests
import json

tkn = ''
base_url = 'https://grifols-ps1.cloud.modeln.com/ecmws/resources/'
api_token = base_url + 'token'
api_job = base_url + 'job/run'
api_activate = base_url + 'job/bizfunction'

cred = '''<credentials xmlns="urn:imany">
    <username>carsflexp</username>
    <password>Login2RTS!</password>
    <enterpriseCode>SYSTM</enterpriseCode>
</credentials>'''

job_data = {
'name':'APS_MDM_UPD_PRODID',
"params":
[
{
'name':'PARAM_1_NDC11',
'value': '61953000400'
},
{
'name':'PARAM_2_SAP_MATNO',
'value': '123451'
},
{
'name':'PARAM_3_START_DATE',
'value': '20220401'
},
{
'name':'EXECUTION TYPE',
'value': 'DBProcess'
},
{
'name':'DATA SOURCE',
'value': 'RM/MDM/MRB'
},
{
'name':'PROCESS TYPE',
'value': 'APS_MDM_UPD_PRODID'
}
]
}

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

hdr = {"Content-Type": "application/xml"}
response = requests.post(url=api_token,data=cred,headers=hdr)
rslts = response.content.split()
for x in rslts:
    y = x.decode("utf-8").split("=")
    if y[0] == 'value':
        tkn= y[1]
print(tkn)
sc = response.status_code
print(sc)

kookie = {'ECMSSOToken' : tkn.replace('/>',' ')}
hdr = {"Content-Type": "application/json"}

if sc == 200:
    response = requests.post(url=api_job,headers=hdr, data=json.dumps(job_data,indent=4), cookies=kookie )
    sc = response.status_code
    print(response.content)
    print(sc)

if sc == 200:
    response = requests.post(url=api_job,headers=hdr, data=json.dumps(actvt_data), cookies=kookie )
    sc = response.status_code
    print(response.content)
    print(sc)

response.close()

