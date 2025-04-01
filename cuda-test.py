import tensorflow as tf
import os

'''
print("tf version",tf.__version__)
# 创建一个会话并获取其设备列表
sess = tf.compat.v1.Session(config=tf.compat.v1.ConfigProto(log_device_placement=True))

print([x.name for x in sess.list_devices()])'''

# 创建一个配置，用于记录设备分配情况
config = tf.ConfigProto(log_device_placement=True)

# 创建一个会话并传入配置
sess = tf.Session(config=config)

def main(x,y):
 for i in range(100):
  print(x+y+i)


# 确保这段代码只在脚本被直接运行时执行，而不是作为模块导入时执行
if __name__ == "__main__":
 config = tf.ConfigProto()
 config.gpu_options.allow_growth = True
 session = tf.Session(config=config)

 # 调用main函数
 main(3,8)

 # 如果需要，关闭会话
 session.close()