import numpy as np
import matplotlib.pyplot as plt
from math import *

# Constants
length = 2
angles = np.linspace(0, 90, 91)  # angles in degrees

# Create the figure and set fixed axes
plt.figure()
plt.grid(False)
plt.xlim(-2.5, 2.5)
plt.ylim(-2.5, 2.5)
plt.axis('equal')

# Plot the segment for each angle
for angle in angles:
    plt.clf()  # Clear the current figure
    plt.grid(True)
    plt.xlim(-2.5, 2.5)
    plt.ylim(-2.5, 2.5)
    
    
    # Convert angle to radians
    angle_rad = angle * pi / 180
    
    # Calculate endpoint coordinates
    x = length * cos(angle_rad)
    y = length * sin(angle_rad)
    
    # Plot the segment
    plt.plot([0, x], [0, y], 'b-', linewidth=2)
    
    plt.title(f'Angle: {angle:.0f}°')
    plt.pause(0.05)

plt.show()