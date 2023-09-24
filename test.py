import csv
import numpy as np



q_table = []
with open("q_table.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        q_table.append([int(cell) for cell in row])


# Define the state (time) for validation
validation_time = 75 #(0-99)

# Define the radius for considering neighboring states
neighbor_radius = 20  # Adjust this value based on your problem
print(q_table[validation_time])
#print(q_table[validation_time-neighbor_radius:validation_time+neighbor_radius])

# Validation loop
state = validation_time

# Get the Q-values for the current state
q_values = q_table[state]

# Initialize a weighted sum of Q-values
weighted_q_sum = np.zeros_like(q_values, dtype=float)

# Calculate weights based on proximity to the current state
for i in range(len(q_values)):
    if(q_values[i] != -1000):
        weighted_q_sum[i] = q_values[i]
    else:
        for distance in range(1, neighbor_radius + 1):
            # Consider neighboring states within the radius
            if state - distance >= 0:
                if(q_table[state - distance][i] != -1000):
                    weighted_q_sum[i] += q_table[state - distance][i] / distance
            if state + distance >= 99:
                if state + distance < len(q_table):
                    if(q_table[state + distance][i] != -1000):
                        weighted_q_sum[i] += q_table[state + distance][i] / distance

# Choose the action with the highest weighted sum of Q-values
weighted_q_sum[weighted_q_sum == 0] = -1000
print("weighted_q_sum: ",weighted_q_sum)
action = np.argmax(weighted_q_sum)
print("action: ",action)

print("it is better to chose route number ",action+1, " and you will arive about ", -weighted_q_sum[action], "secounds.")