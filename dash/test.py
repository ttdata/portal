def send_upload_request(n_clicks,  URL, dtype, DEVICEID,  keyfield, payload):
    URL_upload = URL + '/uploaddata'
    upload_result_mesg = None
    if n_clicks:
        payload = {"data_type": dtype, 
                    "device_id": DEVICEID, 
                    "key": "datetime", 
                    "required_field": "datetime",
                    "device_data": payload   
                }
        print(payload)
        #Passing payload as dict
        # response_upload = requests.post(URL_upload, 
        #     json = payload, 
        #     timeout = 5, 
        #     headers = {"appkey" : appkey})
        # upload_result = json.loads(response_upload.text)
        # upload_result_mesg = upload_result['message']
    return upload_result_mesg

load_data = [
		{
			"datetime": "2020-03-23T01:01:01",
			"issuer": "lab1",
			"owner": "John simth",
			"Height":180,
			"weight":150,
			"med_data": {
				"temperature": 36.5,
				"heart_rate": 76,
				"glucose": 101,
				"blood_pressure": {
					"high": 130,
					"low": 70
				}
			}
		},
		{
			"datetime": "2020-03-24T01:01:01",
			"issuer": "lab1",
			"owner": "David",
			"Height":181,
			"weight":150,
			"med_data": {
				"temperature": 36.5,
				"heart_rate": 76,
				"glucose": 101,
				"blood_pressure": {
					"high": 130,
					"low": 70
				}
			}
		}
	]
send_upload_request(1, "xinbuy", 1, "yuantest", "date", load_data)