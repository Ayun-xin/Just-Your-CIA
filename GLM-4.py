# -*- coding: utf-8 -*-
with open('abilities.txt', 'r', encoding='utf-8') as file:
    # 按行读取文件内容，readlines()会自动将每行作为一个元素存储在列表中
    data_list = file.readlines()
all_news = [s.replace('\n', '') for s in data_list]
with open('API_key.txt', 'r', encoding='utf-8') as file:
    # 按行读取文件内容，readlines()会自动将每行作为一个元素存储在列表中
    data_list = file.readlines()
API_key_list = [s.replace('\n', '') for s in data_list]
API_key=str(API_key_list[1])
if isinstance(API_key, str):
    print("是字符串")
else:
    print("不是字符串")
print('GLM-4干完了')
print(all_news)
# print(API_key)
for t in all_news:
    from zhipuai import ZhipuAI

    client = ZhipuAI(api_key=API_key)  # 填写您自己的APIKey

    response = client.web_search.web_search(
        search_engine="search-pro",
        search_query="关于"+t+"的实时新闻"
    )

    content = ''
    if not response.search_result:
        print("response.search_result is empty")
    else:
        # 确保 i 在 response.search_result 的范围内
        for i in range(len(response.search_result)):
            content += response.search_result[i].content + '\n'
    with open('{}.txt'.format(t), 'w', encoding='utf-8') as f:
        f.write(content)

