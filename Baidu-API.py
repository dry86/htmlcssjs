from aip import AipNlp
import json
#Baidu-NLP-API-KEY
APP_ID = '24093252'
API_KEY = 'VDeeMjwKexaYWpUTFQRV4CVa'
SECRET_KEY = '6viE1h8aKrVqxnLUaUcfGFjvRC0yqCjz'
client = AipNlp(APP_ID, API_KEY, SECRET_KEY)


result = client.simnet('你好呀','嗨')

print(json.dumps(result,ensure_ascii=False,sort_keys=True, indent=4, separators=(',', ': ')))

