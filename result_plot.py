from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import os
lines = np.loadtxt("episode_reward.txt", comments="#", delimiter="\n", unpack=False)


# 指定保存路径和文件名
env_name = "InvertedPendulum"  # 假设的环境名称，您可以根据实际情况修改
save_path = "D:\\RL_code\\ddpg-aigym-master\\plots"

# 获取当前时间并格式化
current_time = datetime.now().strftime("%Y%m%d-%H%M%S")

# 创建文件名
file_name = f"{current_time}_{env_name}.png"

plt.plot(lines)

# 保存图表到指定的路径
plt.savefig(os.path.join(save_path, file_name))
plt.show()

