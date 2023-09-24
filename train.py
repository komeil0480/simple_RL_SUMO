import numpy as np
from SUMO_run import SimulateVehicle
import csv


def epsilon_greedy(q_table,state_space,action_space,epsilon):
    if np.random.rand() < epsilon:
        state = np.random.choice(state_space)
        action = np.random.choice(action_space)

        while(q_table[state][action]!= -1000):
            state = np.random.choice(state_space)
            action = np.random.choice(action_space)

    else:
        done=False
        while not done:
            state = np.random.choice(state_space)
            # select 20 nearest neighbors
            if state < 10:
                compareList=q_table[:21]
                compareList=np.delete(compareList,state,axis=0)
            elif 10<= state <=89:
                compareList=q_table[state-10:state+10]
                compareList=np.delete(compareList,11,axis=0)
            else:
                compareList=q_table[79:99]
                compareList=np.delete(compareList,state-80,axis=0)
            # masked_array = np.ma.masked_equal(compareList, -1000)
            # masked_array.fill_value = 0
            # compareList = masked_array.filled()
            #compareList[compareList == -1000] = 0
            #print("compareList",compareList)
            actionRewards = np.sum(compareList, axis=0)
            print("actionReward:",actionRewards)
            actionList = np.argsort(-actionRewards)
            print("actionlist: ",actionList)
            action=0
            for action in actionList:
                #print("actionnnn: ",action)
                if q_table[state][action]==-1000:
                    done=True
                    break


    return state, action
# Define state and action spaces
state_space = range(100)
action_space = range(0, 5)

# Initialize Q-table
q_table = np.full((len(state_space), len(action_space)),-1000)

# Hyperparameters
# learning_rate = 0.1
# discount_factor = 0.9
epsilon = 0.8
epsilon_decay = 0.995  # Decay factor for exploration rate
epsilon_min = 0.01  # Minimum exploration rate
num_episodes = 50
print(q_table)
# Q-learning algorithm
for episode in range(num_episodes):
    state,action=epsilon_greedy(q_table,state_space,action_space,epsilon)
    
    # Simulate taking the action and observe the reward
    # You need to define your own reward function based on the chosen action and state (time)
    simulation = SimulateVehicle(state, action)
    travel_time = simulation.run()
    reward = -travel_time

    # Q-value update
    q_table[state][action] = reward

    # change the value of epsilon
    epsilon = max(epsilon * epsilon_decay, epsilon_min)

# Now you can use the q_table to make predictions for the best route given a specific time.
print(q_table)
with open("q_table.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(q_table)