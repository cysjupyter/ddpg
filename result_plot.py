from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import os
import csv
# 获取当前时间并格式化
current_time = datetime.now().strftime("%Y%m%d-%H%M%S")
# 指定保存路径和文件名
env_name = "InvertedPendulum"  # 假设的环境名称，您可以根据实际情况修改
save_path = "D:\\RL_code\\ddpg-aigym-master\\plots"

file_name = '20250330-200658_MountainCarContinuous-v0.csv'
file_path = os.path.join("D:\\RL_code\\ddpg-aigym-master\\results", file_name)

# 创建文件名
pic_name = "20250330-200658_MountainCarContinuous-v0.png"

x_data = []
y_data = []

with open(file_path , 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)  # 读取标题行（如果有的话）
    # 假设 CSV 文件有两列，第一列是 x 轴数据，第二列是 y 轴数据
    for row in csvreader:
        x_data.append(float(row[0]))  # 将第一列数据转换为浮点数并添加到 x_data 列表
        y_data.append(float(row[1]))  # 将第二列数据转换为浮点数并添加到 y_data 列表

# 使用 Matplotlib 绘制图表
plt.figure(figsize=(10, 5))  # 设置图表大小
plt.plot(x_data, y_data, label='Data from CSV')  # 绘制线条
plt.xlabel('Timesteps')  # 设置 x 轴标签
plt.ylabel('Averager Episode Return')  # 设置 y 轴标签
plt.title('InvertedPendulum-v1')  # 设置图表标题
plt.savefig(os.path.join(save_path, pic_name))
plt.legend()  # 显示图例
plt.grid(True)  # 显示网格
plt.show()  # 显示图表