import math  # This gives us access to advanced math tools like 'e'

# 1. Setup our starting conditions
ambient_temp = 20.0    # Room temperature in Celsius
initial_temp = 85.0    # Starting cup temperature in Celsius
cooling_rate = 0.05    # The constant 'k' (how fast heat escapes)
time_passed = 10       # Time in minutes

# 2. The formula: T(t) = T_ambient + (T_initial - T_ambient) * e^(-kt)
temperature = ambient_temp + (initial_temp - ambient_temp) * math.exp(-cooling_rate * time_passed)

# 3. Print the result
print("Temperature after 10 minutes is:", temperature)

