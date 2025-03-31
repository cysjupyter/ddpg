#episodes=100000 #最大迭代次数
timesteps=400000 #总共的时间步
is_batch_norm = False #batch normalization switch
average_batch=1000 #取平均值的步数

REPLAY_MEMORY_SIZE = 10000
BATCH_SIZE = 128
GAMMA=0.99
is_grad_inverter = False

critic_tau = 0.05
critic_learning_rate= 0.003#0.001
critic_batch_size = 64

actor_tau = 0.05
actor_learning_rate = 0.0001
actor_batch_size = 64
#noise
mu = 0
theta = 0.15
sigma = 0.2