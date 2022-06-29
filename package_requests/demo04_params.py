# 查询参数：url地址中的最后一部分
"""
需求：
1. 访问TPshop搜索商品的接口，通过查询字符串的方式传递搜索的关键字 iPhone ，并查看响 应数
据
2. 请求路径格式为： http://localhost/Home/Goods/search.html?q=iPhone
"""
import requests

# # 实现方式1:传递完整的url
# url = "http://localhost/Home/Goods/search.html?q=iPhone"
# response = requests.get(url)
# print(response.text)

# 实现方式2:查询参数部分以字典形式传递
# url1 = "http://localhost/Home/Goods/search.html"
# params = {"q": "iphone"}
# response = requests.get(url1, params = params)
# print(response.text)

# 实现方式3:
url2 = "http://localhost/Home/Goods/search.html"
params = 'q = iphone'
response = requests.get(url2, params=params)
print(response.text)
