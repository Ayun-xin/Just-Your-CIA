
# -*- coding: utf-8 -*-
# 打开文件（假设文件名为data.txt）
with open('abilities.txt', 'r', encoding='utf-8') as file:
    # 按行读取文件内容，readlines()会自动将每行作为一个元素存储在列表中
    data_list = file.readlines()
new_list = [s.replace('\n', '') for s in data_list]
with open('API_key.txt', 'r', encoding='utf-8') as file:
    # 按行读取文件内容，readlines()会自动将每行作为一个元素存储在列表中
    data_list_API = file.readlines()
API_key_list = [s.replace('\n', '') for s in data_list_API]
API_key=str(API_key_list[0])
# 打印结果列表
all_continue=''
for s in new_list:
    all_continue+=s

print('listdemo干完了')
import os
from openai import OpenAI

client = OpenAI(
    # 若没有配置环境变量，请用阿里云百炼API Key将下行替换为：api_key="sk-xxx",
    api_key=os.getenv(API_key),  # 如何获取API Key：https://help.aliyun.com/zh/model-studio/developer-reference/get-api-key
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

completion = client.chat.completions.create(
    model="deepseek-r1",  # 此处以 deepseek-r1 为例，可按需更换模型名称。
    messages=[
        {'role': 'user', 'content':"我的能力有"+all_continue+ "请你为这几个能力做一个专业的介绍"}
    ]
)

# 通过reasoning_content字段打印思考过程
print("思考过程：")
print(completion.choices[0].message.reasoning_content)

# 通过content字段打印最终答案
print("最终答案：")
print(completion.choices[0].message.content)
with open('max_ability.txt', 'w', encoding='utf-8') as f:
    f.write(completion.choices[0].message.content)