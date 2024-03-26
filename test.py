import numpy as np
from scipy.integrate import quad

# Define the integrand function
def integrand(x):
    return x * np.sqrt(1 + (-4.5 * np.pi * np.cos(x * np.pi / 8) * np.sin(x * np.pi / 8))**2)

# Integrate the function from 0 to 2*pi
result, error = quad(integrand, 0, 2*np.pi)

print("Result of the integration:", result)
print("Estimated error:", error)