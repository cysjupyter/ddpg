import scipy.stats as stats
import numpy as np
import os
import csv
import matplotlib.pyplot as plt

# 设置文件夹路径
folder_path = 'D:\RL_code\ddpg-aigym-master\mountaincar-plot'  # 请将此路径替换为你的CSV文件所在的文件夹路径

# 初始化一个列表来存储所有文件的numpy数组
all_arrays = []
time_array = np.arange(1000,401000,1000)

# 遍历文件夹中的所有文件
for filename in os.listdir(folder_path):
    # 检查文件是否为CSV文件
    if filename.endswith('.csv'):
        # 构建完整的文件路径
        filepath = os.path.join(folder_path, filename)
        # 初始化一个列表来存储当前文件的数据
        data = []
        # 打开并读取CSV文件
        with open(filepath, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            # 逐行读取数据
            for row in csvreader:
                # 只获取每行的第二列数据并尝试转换为浮点数
                try:
                    data.append(float(row[1]))
                except ValueError:
                    print(f"Error converting data in file {filename}: {row[1]}")
        all_arrays.append(np.array(data))

def calculate_mean_and_std(array):
    # 计算所有数组的平均值和标准差
    mean = np.mean(array)
    std = np.std(array)
    return mean, std
def calculate_confidence_interval(mean, sigma, n, p):
    # 计算双侧检验的alpha值
    alpha = 1 - p

    # 计算z值（临界值）
    z = stats.norm.ppf(1 - alpha / 2)

    # 计算置信区间
    margin_of_error = z * (sigma / np.sqrt(n))
    lower_bound = mean - margin_of_error
    upper_bound = mean + margin_of_error

    return lower_bound, upper_bound

number = len(all_arrays)
trust_interval = 0.80
upper_array = []
lower_array = []
mean_array = []
for t in range(len(time_array)):
    t_time_data = []
    for j in range(number):
        t_time_data.append(all_arrays[j][t])
    mean, std = calculate_mean_and_std(t_time_data)
    lower, upper = calculate_confidence_interval(mean, std, number, trust_interval)
    upper_array.append(upper)
    lower_array.append(lower)
    mean_array.append(mean)

# 使用 Matplotlib 绘制图表
plt.figure(figsize=(10, 5))  # 设置图表大小
#plt.plot(time_array, upper_array, label='upper')
#plt.plot(time_array, lower_array, label='lower')
plt.plot(time_array, mean_array, label='mean', color='#2a882a')# 绘制线条
plt.fill_between(time_array, lower_array, upper_array, color='#cce6cc')
plt.xlabel('Timesteps')  # 设置 x 轴标签
plt.ylabel('Averager Episode Return')  # 设置 y 轴标签
plt.title('InvertedPendulum-v1')  # 设置图表标题
#plt.savefig(os.path.join(save_path, pic_name))
plt.legend()  # 显示图例
plt.grid(True)  # 显示网格
plt.show()  # 显示图表