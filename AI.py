# -*- coding: utf-8 -*-
import os
os.system(r"python D:\情报站完美成果测试站\GLM-4工具.py")
with open('abilities_tool.txt', 'r', encoding='utf-8') as file:
    # 按行读取文件内容，readlines()会自动将每行作为一个元素存储在列表中
    data_list = file.readlines()
with open('max_ability.txt', 'r', encoding='utf-8') as file:
    max_ability = file.read()
with open('API_key.txt', 'r', encoding='utf-8') as file:
    # 按行读取文件内容，readlines()会自动将每行作为一个元素存储在列表中
    data_list_API = file.readlines()
API_key_list = [s.replace('\n', '') for s in data_list_API]
API_key=str(API_key_list[0])

if isinstance(API_key, str):
    print("是字符串")
else:
    print("不是字符串")
all_news = [s.replace('\n', '') for s in data_list]
all_continue=''
for t in all_news:
    with open('{}.txt'.format(t), 'r', encoding='utf-8') as file:
        content = file.read()
    all_continue+=content

print('AI,干完了')
print(all_news)
# print(API_key)
import os
from openai import OpenAI

client = OpenAI(
    # 若没有配置环境变量，请用阿里云百炼API Key将下行替换为：api_key="sk-xxx",
    api_key=API_key,  # 如何获取API Key：https://help.aliyun.com/zh/model-studio/developer-reference/get-api-key
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

completion = client.chat.completions.create(
    model="deepseek-r1",  # 此处以 deepseek-r1 为例，可按需更换模型名称。
    messages=[
        {'role': 'user', 'content':"这些是最新的关于我喜欢的工具的消息"+all_continue+ "请你根据它再依据我的"+max_ability+"这些能力为我分析出对我有用的工具,然后再生成一句鼓励我的话"}
    ]
)

# 通过reasoning_content字段打印思考过程
print("思考过程：")
print(completion.choices[0].message.reasoning_content)

# 通过content字段打印最终答案
print("最终答案：")
print(completion.choices[0].message.content)
with open('./dist/output.txt', 'w', encoding='utf-8') as f:
    f.write(completion.choices[0].message.content)