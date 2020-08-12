import requests
import json
upload_result_mesg = None
dtype = 1,
DEVICEID = 'yang20200808a'
appkey = 'ce3bc125f87bde6c57f785dce254d6d820d2636f4a8aa0f404a7f76bd55c11c8'
URL_getowner = 'http://ixinbuy.com:7061/getownerdata'
OWNER = 'David'
getowner_result_mesg = None
#query as request
query = {"data_type": dtype, 
"device_id": DEVICEID, 
"owner": OWNER}
response_get = requests.get(URL_getowner, params=query, timeout = 5, headers = {"appkey" : appkey})
get_result = json.loads(response_get.text)
print(get_result['message'])
print(response_get.text)