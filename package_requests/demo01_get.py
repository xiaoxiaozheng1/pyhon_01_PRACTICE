# 请求百度的地址；http://www.baidu.com

# 1.导包
import requests

# 2.使用get方法去请求
response = requests.get("http://www.baidu.com")
print(response.text)
