import os
import time
from playwright.sync_api import Playwright, sync_playwright, expect

# 定义文件名
last_run_file = "last_run.txt"

# 获取当前时间
current_time = time.time()
current_date = time.strftime("%Y-%m-%d", time.localtime(current_time))
if os.path.exists("abilities.txt"):
    pass
else:
    os.system(r"python D:\情报站完美成果测试站\能力.py")
    os.system(r"python D:\情报站完美成果测试站\listdemo.py")

if os.path.exists("API_key.txt"):
    pass
else:
    os.system(r"python D:\情报站完美成果测试站\API_key.py")
# 检查文件是否存在
if os.path.exists(last_run_file):
    # 读取文件中的时间
    with open(last_run_file, "r") as f:
        last_run_time = float(f.readline())
        last_run_date = time.strftime("%Y-%m-%d", time.localtime(last_run_time))
else:
    # 创建文件并记录当前时间
    with open(last_run_file, "w") as f:
        f.write(str(current_time))
    last_run_time = current_time
    last_run_date = current_date

# 检查是否需要执行exe程序和py代码文件
if current_time - last_run_time >=86400:  # 86400秒 = 24小时
    os.system(r"python D:\情报站完美成果测试站\新闻热点AI个性化聚焦.py")
    # with sync_playwright() as playwright:
    #     run(playwright)

    # 执行py代码文件
    # with sync_playwright() as playwright:
    #     run(playwright)

# 检查是否需要执行另一个文件
if current_date > last_run_date:
    # 计算日期差
    date_diff = (current_time - last_run_time) // 86400
    if date_diff >= 7:
        # time.sleep(20)
        os.system(r"python D:\情报站完美成果测试站\AI.py")

        # with sync_playwright() as playwright:
        #     run1(playwright)
        # 执行另一个文件


# 更新文件中的时间
with open(last_run_file, "w") as f:
    f.write(str(current_time))
