## Purpose: provide a generic service for testing API calls
## Author : Simon Li
## Date   : May 5, 2020
##
## RS     - 108.48.52.183:7061
## ZN     - 112.17.170.154:7061
## ttdata - ixinbuy.com:7061
##
## Usage:  
## import TTDataService
## ttdata = TTDataService("108.48.52.183")
    
import requests
import json

class TTDataService:
    def __init__(self, host = "ixinby.com", port = 7061):
        '''
            TTDataService: host(str), port(int)
        '''
        self.__url = "http://%s:%d" % (host, port)
        
    @staticmethod
    def getUrl(base, route):
        '''
           make a url string
           In : base(str), route(str)
           Out: url(str) 
        '''
        url = base
        if route[0] != '/':
           url += '/' + route
        else:
            url += route
        return url
    
    @staticmethod
    def JSONParseIfPossible(text):
        '''
           JSON parse the string to dict if possible
           In : text(str)
           Out: a dict or original string
        '''
        try: 
            result = json.loads(text) 
        except:
            result = text
        return result

    @property
    def url(self):
        return self.__url

    @property
    def json(self):
        '''
           expose json 
        '''
        return json

    @property
    def requests(self):
        '''
           expose requests 
        '''
        return requests

    @url.setter
    def url(self, url):
        self.__url = url
    
    def get(self, route):
        '''
           GET request
           In :  route(str), e.g. /getshareddata?data_type=2&device_id=ttdata
           Out: tuple(int, dict/str)
        '''
        url = TTDataService.getUrl(self.__url, route)
        response = requests.get(url)
        return (response.status_code, TTDataService.JSONParseIfPossible(response.text))

    def post(self, route, payload):
        '''
           POST request
           In : route(str), payload(dict or json string)
           Out: tuple(int, dict/str)
        '''
        url = TTDataService.getUrl(self.__url, route)
        if isinstance(payload, dict):
            response = requests.post(url, json = payload)
        else:
            try:
                response = requests.post(url, json = json.loads(payload))
            except:
                response = requests.post(url, data = payload)    

        return (response.status_code, TTDataService.JSONParseIfPossible(response.text))

if __name__ == '__main__':
    ttdata = TTDataService("108.48.52.183")
    # Register
    print("== /register ==")
    payload = '{"device_id": "ttdata-1"}'
    response = ttdata.post("/register", payload)
    print(response)

    # Upload data
    print("\n== /uploaddata ==")
    payload = {
                "data_type": 2, 
                "device_id": "ttdata-1", 
                "device_data": {
                                    "date": "2020-05-06", 
                                    "province": "ON",
                                    "country": "Canada", 
                                    "city": "Toronto",
                                    "last_update": "2020-05-03T10:43:02",
                                    "confirmed":370,
                                    "deaths": 84,
                                    "recovered": 14,
                                    "latitude":43.6532,
                                    "longitude": 79.3832,
                                    "key": "date|province|city|country"	
                }   
    }
    response = ttdata.post("/uploaddata", payload)
    #print(json.dumps(payload))
    print(response)

    # Get shared data
    print("\n== /getshareddata ==")
    response = ttdata.get("/getshareddata?data_type={0}&device_id={1}".format(2, "ttdata-1"))
    print(response)