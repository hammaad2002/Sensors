import numpy as np
import matplotlib.pyplot as plt

freq = 1

tempTime = np.linspace(0, 10, 100)
tempSignal = np.sin(2 * np.pi * freq * tempTime)

# tempTime = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]) # First try interpolation part in this simple example then try to
#                                                  # transfer it to the example with sine wave
# tempSignal = np.array([0, 1, 2, 1, 0, -1, -2, -1, 0])

plt.subplot(311)
plt.plot(tempTime, tempSignal, marker='o')
# plt.show()

diff = []
sign = []
for i in range(len(tempSignal)-1):
    if tempSignal[i+1] > tempSignal[i]:
        sign.append(1)
    else:
        sign.append(-1)
    diff.append(abs(tempSignal[i+1] - tempSignal[i]))

# Mapped the signal to a cumulative sum
cumsum = np.cumsum(diff)
plt.subplot(312)
plt.plot(diff)
plt.subplot(313)
plt.plot(cumsum)
# plt.show()

# Recalculating the original signal from the cumulative signal back
plt.figure()
recal_diff = []
for i in range(len(cumsum)):
    if i == 0:
        recal_diff.append(cumsum[i])
    else:
        recal_diff.append(cumsum[i] - cumsum[i - 1])

plt.subplot(311)
plt.plot(cumsum)
plt.subplot(312)
plt.plot(recal_diff)
plt.subplot(313)

recal_tempSignal = []
recal_diff = [0] + recal_diff # just appending it because the first iteration is gonna be useless
for i, elem in enumerate(recal_diff):
    if i == 0:
        recal_tempSignal.append(tempSignal[0])
    else:   
        if sign[i-1] == 1:
            recal_tempSignal.append(recal_tempSignal[-1] + elem)
        else:
            recal_tempSignal.append(recal_tempSignal[-1] + (-1.0 * elem))

plt.plot(tempTime, recal_tempSignal, marker='o')
plt.show()