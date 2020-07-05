import pandas as pd
data = {'DATE' : ['May 20 23:07:45 2020', 'May 21 23:07:45 2020', 'May 22 23:07:45 2020', 'May 23 23:07:45 2020', 'May 24 23:07:45 2020' ,
'May 25 23:07:45 2020', 'May 26 23:07:45 2020', 'May 27 23:07:45 2020', 'May 28 23:07:45 2020', 'May 29 23:07:45 2020' ],
'DATATYPE': [2,2,2,2,2,2,2,2,2,2],
'API' : ['http://108.48.52.183:7061', 'http://108.48.52.183:7061', 'http://108.48.52.183:7061', 'http://108.48.52.183:7061', 'http://108.48.52.183:7061',
'http://108.48.52.183:7061', 'http://108.48.52.183:7061', 'http://108.48.52.183:7061', 'http://108.48.52.183:7061', 'http://108.48.52.183:7061'],
'REGISTER':['success', 'test_yang is already registered', 'test_yang is already registered', 'test_yang is already registered', 'test_yang is already registered',
'test_yang is already registered', 'test_yang is already registered', 'test_yang is already registered', 'test_yang is already registered', 'test_yang is already registered'] , 
'UPLOAD':[' test_yang is not registered yet', 'COVID19 data uploaded successfully', 'COVID19 data uploaded successfully', 'COVID19 data uploaded successfully', 'COVID19 data uploaded successfully', 'COVID19 data uploaded successfully', 'COVID19 data uploaded successfully', 'COVID19 data uploaded successfully', 'COVID19 data uploaded successfully', 'COVID19 data uploaded successfully'],
'GETDATA':['no data has been shared yet', 'no data has been shared yet', 'no data has been shared yet', 'no data has been shared yet', 'You are not authorized to view the data', 'You are not authorized to view the data', 'no data has been shared yet', 'no data has been shared yet', 'no data has been shared yet', 'fail to retrieve data' ]}

df = pd.DataFrame(data)
df.to_csv(r'/Users/yangyuan/Documents/ttdata/dash/dash_sample.csv', index = False)
