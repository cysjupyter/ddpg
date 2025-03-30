import gym
from gym import envs
env_list = envs.registry.all()
env_ids = [env_item.id for env_item in env_list]

print(env_ids)