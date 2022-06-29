# response:
"""
包括的属性和方法：
response.text ：获取响应的文本形式
response.url：获取响应的url
response.encode:获取编码/修改编码
response.headers:获取响应体
response.json：获取json类型的数据
"""
"""
案例
1. 访问百度首页的接口 http://www.baidu.com ，获取以下响应数据
2. 获取响应状态码
3. 获取请求URL
4. 获取响应字符编码
5. 获取响应头数据
6. 获取文本形式的响应内容
"""
# 1.倒包
import requests

# 2.请求百度
response = requests.get("http://www.baidu.com")
response.encoding = 'utf-8'
print("响应状态码", response.status_code)
print("请求URL", response.url)
print("获取编码", response.encoding)
print("获取响应头数据", response.headers)
print("获取消息", response.reason)
print("获取文本形式", response.text)
