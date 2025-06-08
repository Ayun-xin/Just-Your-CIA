# Just-Your-CIA--只属于你的中情局
## 一 下载库
安装PyQt5（包含QtWidgets、QtCore、QtGui等模块）

pip install PyQt5

安装智谱AI官方SDK

pip install zhipuai

安装OpenAI官方库

pip install openai

## 二 将三个py文件打包为exe程序
 用这个命令打包三个文件
  pyinstaller --onefile --windowed 目标文件名.py
  
![image](https://github.com/user-attachments/assets/e6cb3051-8987-419e-9cf5-85b9a765e0ef)

将这三个用红框标记的文件打包

将run.exe 移动回根目录中

![image](https://github.com/user-attachments/assets/e023eafe-d5ee-452c-832d-a41c8b172c7d)


## 三 将两个空的txt文件的放入dist的文件夹

名称分别是 newsput.txt output.txt

![image](https://github.com/user-attachments/assets/69efcec4-4273-4e08-a2b0-a2bd40cb0155)

## 四 修改代码中的文件路径

run.py 中需要修改为自己文件路径的地方

![image](https://github.com/user-attachments/assets/ea37dc87-f0ba-4d5a-b448-32322db49ce5)

AI.py 中需要修改文件路径的地方

![image](https://github.com/user-attachments/assets/37c0d0d3-23b6-40c9-946b-09db3fd706aa)

新闻热点AI个性化聚焦.py 中需要修改文件路径的地方

![image](https://github.com/user-attachments/assets/1593ebcd-a170-4660-8bc5-c1d39966e902)

## 五 如果需要其开机自启动

将三个exe程序快捷方式拖放到开机自启动文件夹中

如果不需要双击 run.exe 运行即可 随后打开 界面.exe 与 新闻界面.exe 查看结果






