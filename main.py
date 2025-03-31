#Implementation of Deep Deterministic Gradient with Tensor Flow"
# Author: Steven Spielberg Pon Kumar (github.com/stevenpjg)
import gym
from gym.spaces import Box, Discrete
import numpy as np
from ddpg import DDPG
from ou_noise import OUNoise
from conf import is_batch_norm, timesteps
import csv
from datetime import datetime
import os


def main():
    experiment= 'MountainCarContinuous-v0' #specify environments here
    env= gym.make(experiment)
    max_steps= env.spec.timestep_limit #steps per episode
    assert isinstance(env.observation_space, Box), "observation space must be continuous"
    assert isinstance(env.action_space, Box), "action space must be continuous"
    #save
    save_path = "D:\\RL_code\\ddpg-aigym-master\\results"
    current_time = datetime.now().strftime("%Y%m%d-%H%M%S")
    file_name = f"{current_time}_{experiment}.csv"
    #Randomly initialize critic,actor,target critic, target actor network  and replay buffer   
    agent = DDPG(env, is_batch_norm)
    exploration_noise = OUNoise(env.action_space.shape[0])
    counter = 0
    reward_per_episode = 0
    total_reward = 0
    num_states = env.observation_space.shape[0]
    num_actions = env.action_space.shape[0]    
    print ("Number of States:", num_states)
    print ("Number of Actions:", num_actions)
    print ("Number of Steps per episode:", max_steps)
    #saving reward:
    reward_st = np.array([0])

    i = 0
    while True:
        i += 1
        observation = env.reset()
        reward_per_episode = 0
        for t in range(max_steps):
            # rendering environmet (optional)
            # env.render()

            x = observation
            action = agent.evaluate_actor(np.reshape(x,[1,num_states]))
            noise = exploration_noise.noise()
            action = action[0] + noise #Select action according to current policy and exploration noise

            observation,reward,done,info=env.step(action)

            #add s_t,s_t+1,action,reward to experience memory
            agent.add_experience(x,observation,action,reward,done)
            #train critic and actor network
            if counter > 128:
                agent.train()
            reward_per_episode += reward
            counter += 1
            # check if episode ends:
            if (done or (t == max_steps - 1)):
                print('EPISODE: ', i, ' Steps: ', t, ' Total Reward: ', reward_per_episode, 'Timestep: ', counter)
                exploration_noise.reset()  # reinitializing random noise for action exploration
                reward_st = np.append(reward_st, reward_per_episode)
                break

            if counter > timesteps:
                break

        average_episode_reward= np.mean(reward_st)

        file_path = os.path.join(save_path, file_name)
        print("Average reward per episode {}".format(average_episode_reward))
        with open(file_path, 'a', newline='\n') as file:
            writer = csv.writer(file)
            # 添加数据行
            writer.writerow([counter, average_episode_reward])

        if counter > timesteps:
            print(counter)
            break

if __name__ == '__main__':
    main()    