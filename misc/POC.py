import requests
import json
import re


tkn = ''
base_url = 'https://grifols-ps1.cloud.modeln.com'
##base_url ='https://grifols-qa1.cloud.modeln.com'
api_token = base_url + '/ecmws/resources/token'
api_job = base_url + '/ecmws/resources/job/run'
api_activate = base_url + '/ecmws/resources/job/bizfunction'

#replace '*' with UID and PWD
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
'value': '68516521604'
},
{
'name':'PARAM_2_SAP_MATNO',
'value': '23497844'
},
{
'name':'PARAM_3_START_DATE',
'value': '20220601'
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
'name':'APS_PRODACTALL',
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

#Get SSO Token
response = requests.post(url=api_token,data=cred,headers=hdr)
rslts = response.content.split()
#print(rslts)
for x in rslts:
    y = x.decode("utf-8").split("=")
    if y[0] == 'value':
        tkn= re.findall(r'"([^"]*)"', x.decode("utf-8"))

##print(tkn[0])
sc = response.status_code
print("Response Status Code:" + str(sc))

kookie = {'ECMSSOToken' : tkn[0]}
hdr = {"Content-Type": "application/json"}

#Insert Prod ID 
if sc == 200:
    response = requests.post(url=api_job,headers=hdr, data=json.dumps(job_data,indent=4), cookies=kookie )
    sc = response.status_code
    ##print(response.content)
    print("Response Status Code:" + str(sc))

#Activate Product
##if sc == 200:
##if True:
 ##   response = requests.post(url=api_job,headers=hdr, data=json.dumps(actvt_data,indent=4), cookies=kookie )
 ##   sc = response.status_code
##    print(response.content)
 ##   print("Response Status Code:" + str(sc))

response.close()

