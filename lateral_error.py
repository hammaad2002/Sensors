import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

def perpendicular_given_four_points(x1, x2, y1, y2, length=10):
    # Original line
    x_original = [x1, x2]
    y_original = [y1, y2]

    # Calculate slope of original line
    slope_original = (y_original[1] - y_original[0]) / (x_original[1] - x_original[0])

    # Calculate midpoint of original line
    midpoint_x = (x_original[0] + x_original[1]) / 2
    midpoint_y = (y_original[0] + y_original[1]) / 2

    # Calculate perpendicular slope
    slope_perpendicular = -1 / slope_original if slope_original != 0 else float('inf')
    # print(slope_perpendicular)

    # Arbitrary target length
    target = 10

    # Generate points for perpendicular line
    if slope_perpendicular != float('inf'):
        x_perp = np.array([midpoint_x - target, midpoint_x + target])
        y_perp = slope_perpendicular * (x_perp - midpoint_x) + midpoint_y
    else:
        x_perp = np.array([midpoint_x, midpoint_x])
        y_perp = np.array([midpoint_y - target, midpoint_y + target])

    def normalize_line(x1, y1, x2, y2, new_length=1):
        # Calculate vector
        dx = x2 - x1
        dy = y2 - y1
        
        # Calculate length
        length = np.sqrt(dx**2 + dy**2)
        
        # Normalize
        dx_normalized = dx / length
        dy_normalized = dy / length

        # Midpoint
        mid_x = (x1 + x2) / 2
        mid_y = (y1 + y2) / 2
        
        # Calculate new endpoint
        new_x = [mid_x - dx_normalized * (new_length/2), mid_x + dx_normalized * (new_length/2)]
        new_y = [mid_y - dy_normalized * (new_length/2), mid_y + dy_normalized * (new_length/2)]
        
        return new_x, new_y 

    desired_length = length
    x_perp, y_perp = normalize_line(x_perp[0], y_perp[0], x_perp[1], y_perp[1], new_length=desired_length)

    return x_perp, y_perp

tempOne = [[367.069, -330.61], [369.329, -330.61], [371.137, -330.61], [372.719, -330.61], [374.979, -330.61], [376.788, -330.61], [379.048, -330.599], [380.63, -330.576], [382.438, -330.546], [384.687, -330.385], [386.254, -330.158], [388.008, -329.747], [390.112, -328.933], [391.482, -328.157], [392.899, -327.045], [394.341, -325.325], [395.117, -323.948], [395.765, -322.274], [396.147, -320.051], [396.253, -318.475], [396.305, -316.667]]
tempTwo = [[367.242, -330.396], [369.162, -330.299], [371.081, -330.238], [373, -330.228], [374.919, -330.266], [376.838, -330.341], [378.757, -330.43], [380.677, -330.514], [382.596, -330.575], [384.514, -330.598], [386.426, -330.441], [388.314, -330.098], [390.096, -329.396], [391.733, -328.397], [393.21, -327.175], [394.445, -325.709], [395.437, -324.069], [396.011, -322.244], [396.265, -320.342], [396.35, -318.426], [396.35, -316.506]]

# Extract x and y coordinates from the data
tempOne_x = [point[0] for point in tempOne]
tempOne_y = [point[1] for point in tempOne]

tempTwo_x = [tempTwo[i][0] for i in range(len(tempTwo))]
tempTwo_y = [tempTwo[i][1] for i in range(len(tempTwo))]

# Create the cubic spline interpolation
cs = CubicSpline(tempOne_x, tempOne_y)

# Generate points for a smooth curve
x_smooth = np.linspace(min(tempOne_x), max(tempOne_x), 500)
y_smooth = cs(x_smooth)

# Plot the results
plt.figure(figsize=(12, 6))
plt.plot(tempOne_x, tempOne_y, 'ro', label='Original points line 1')
plt.plot(tempTwo_x, tempTwo_y, 'ro', label='Original points line 2')
plt.plot(tempTwo_x, tempTwo_y, label='Original points line 2')
plt.plot(x_smooth, y_smooth, 'b-', label='Cubic Spline Interpolation')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Cubic Spline Interpolation of Data Points')
plt.legend()
plt.grid(True)
# plt.show()

# Function to get y value for any x
def get_y_for_x(x):
    return cs(x)

for x in tempOne_x:

    step_h = 0.01
    x1, x2 = x - step_h, x + step_h
    y1, y2 = get_y_for_x(x1), get_y_for_x(x2)

    # print(x1, ',', x2, ',', y1, ',', y2)
    xperp, yperp = perpendicular_given_four_points(x1, x2, y1, y2, length=2)
    plt.plot(xperp, yperp, color='g')

plt.show()


def find_point_on_line(line_one_x, line_one_y, line_two_x, line_two_y):

    m1 = (line_one_y[1] - line_one_y[0]) / (line_one_x[1] - line_one_x[0])
    c1  = line_one_y[0] - (m1 * line_one_x[0])
    m2 = (line_two_y[1] - line_two_y[0]) / (line_two_x[1] - line_two_x[0])
    c2 = line_two_y[0] - (m2 * line_two_x[0])

    # Check if the lines are parallel
    if m1 == m2:
        return None
    else:
        point_x = (c2 - c1) / (m1 - m2)
        point_y = m1 * point_x + c1

        # Check if the point is on the line
        if point_x < line_one_x[0] or point_x > line_one_x[1] and point_y < line_one_y[0] or point_y > line_one_y[1]:
            return None
        else:
            return point_x, point_y
        
''' 
Testing purposes
'''

line_one_x = [1.5, 2]
line_one_y = [3, 4.5]
line_two_x = [1, 4]
line_two_y = [5, 6]
out = find_point_on_line(line_one_x, line_one_y, line_two_x, line_two_y)
print(out)

line_one_x = [1.5, 2]
line_one_y = [3, 9]
line_two_x = [1, 4]
line_two_y = [5, 6]
out = find_point_on_line(line_one_x, line_one_y, line_two_x, line_two_y)
print(out)