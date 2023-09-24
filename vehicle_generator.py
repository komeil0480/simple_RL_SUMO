import random

# Define vehicle types and their probabilities
vehicle_types = ["CAR", "BUS"]
vehicle_probabilities = [0.75, 0.25]

# Define route IDs
route_ids = ["route1", "route2", "route3", "route4", "route5"]

# Read the existing SUMO route file
with open("TEST_SUMO_CONFIG.rou.xml", "r") as f:
    lines = f.readlines()

# Find the position where new vehicles should be added (after the last </routes> tag)
insert_position = len(lines) - 1

vehicles = []
# Generate 500 vehicles and insert them into the existing content
for vehicle_id in range(100):
    # Randomly select vehicle type based on probabilities
    vehicle_type = random.choices(vehicle_types, vehicle_probabilities)[0]

    # Randomly select a route
    route_id = random.choice(route_ids)

    # Randomly select a departure time between 0 and 100
    depart_time = random.uniform(0, 100)

    # Generate a random color (excluding red)
    color = "{:.2f},{:.2f},{:.2f}".format(random.random(), random.random(), random.random())

    # Create the vehicle definition
    new_vehicle = f'    <vehicle id="{vehicle_id}" type="{vehicle_type}" depart="{depart_time:.2f}" route="{route_id}" color="{color}"/>\n'
    vehicles.append((depart_time, new_vehicle))
    
    #print (vehicles)
    # Insert the new vehicle definition at the specified position
    # lines.insert(insert_position, new_vehicle)
    # insert_position = len(lines) -1
vehicles.sort(key=lambda x: x[0])

for _,vehicle in vehicles:
    lines.insert(insert_position, vehicle)
    insert_position = len(lines) -1

# Write the updated content back to the file
with open("TEST_SUMO_CONFIG.rou.xml", "w") as f:
     f.writelines(lines)