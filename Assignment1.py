import numpy as np
import matplotlib.pyplot as plt

# Define the simulation parameters
service_rate = 0.75
λ = [0.2, 0.4, 0.5, 0.6, 0.65, 0.7, 0.72, 0.74, 0.745]
num_time_slots = int(1e6)
expected_delays = []

# Simulate the queue for each arrival rate and calculate the expected delay
for arrival_rate in λ:
    queue = []
    total_wait_time = 0
    total_packets_served = 0

    # Simulate the queue for a fixed number of time slots
    for i in range(num_time_slots):
        # Generate a new customer arrival with a probability of lambda
        if np.random.random() < arrival_rate:
            # Generate the service time for the new customer using a geometric distribution with mean 1/mu
            queue.append(np.random.geometric(service_rate))

        # If there are customers in the queue, decrement their service time by 1
        if len(queue) > 0:
            total_wait_time += len(queue) - 1
            queue[0] -= 1

            # If the service time for the customer at the front of the queue is over, remove them from the queue
            if queue[0] == 0:
                queue.pop(0)
                total_packets_served += 1

    # Calculate the expected delay and add it to the list of expected delays
    expected_delay = total_wait_time / total_packets_served
    expected_delays.append(expected_delay)

# Plot the expected queueing delay with respect to the arrival rate lambda
plt.plot(λ, expected_delays, color='red')
plt.title("Expected Queueing Delay vs. Arrival Rate")
plt.xlabel("Arrival Rate λ ")
plt.ylabel("Expected Queueing Delay")
plt.show()
