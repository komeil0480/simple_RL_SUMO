import traci

class SimulateVehicle:
    def __init__(self, depart, route_id):
        routes=["route1","route2","route3","route4","route5"]
        self.depart = depart
        self.route_id = routes[route_id]

    def run(self):
        # Set the path to the SUMO configuration file
        config_file = "TEST_SUMO_CONFIG.sumocfg"
        vehicle_id = "1000"

        # Connect to the SUMO simulation
        traci.start(["sumo", "-c", config_file])

        # Add a vehicle to the simulation
        traci.vehicle.add(vehicle_id, self.route_id, typeID="CAR", depart=str(self.depart))

        # Simulation loop
        counter = 0
        while traci.simulation.getMinExpectedNumber() > 0:
            counter += 1
            traci.simulationStep()
            if vehicle_id in traci.vehicle.getIDList():
                finish_time = traci.simulation.getTime()

        # Close the simulation
        traci.close()
        travel_time = int(finish_time) - self.depart
        return travel_time

# Example usage:
if __name__ == "__main__":
    depart_time = 30
    route = 1
    
    simulation = SimulateVehicle(depart_time, route)
    travel_time = simulation.run()
    
    print(f"Travel time of the vehicle: {travel_time} seconds")
