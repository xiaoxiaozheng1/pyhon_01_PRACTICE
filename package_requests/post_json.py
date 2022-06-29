# post请求json类型
"""
需求：
需求：
1. 请求微商城项目的登录接口，请求数据（ {"username":"admin123","password":"admin123"}）
2. 登录接口URL：http://121.196.13.152:8080/admin/auth/login
"""
# 1. 导包
import requests

# 2. 请求post方法
login_url = "http://121.196.13.152:8080/admin/auth/login"
login_data = {"username": "admin123", "password": "admin123"}
headers = {"Content-Type": "application/json"}
response = requests.post(login_url, json=login_data, headers=headers)
text_result = response.text
print("text_result:", text_result)
# print(text_result.get('data').get('adminInfo'))  结果是个字符串故不能调用字典的方法
json_result = response.json()
print("json_result:", json_result)
print(json_result.get('data').get('adminInfo'))  # 结果是个字典形式
