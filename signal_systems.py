import numpy as np
import matplotlib.pyplot as plt
import os

# Create folder for graphs
os.makedirs("graphs", exist_ok=True)

# Time axis
t = np.linspace(-5, 5, 1000)

# -----------------------------
# 1. Unit Step Signal
# -----------------------------
unit_step = np.where(t >= 0, 1, 0)

plt.figure()
plt.plot(t, unit_step)
plt.title("Unit Step Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid()
plt.savefig("graphs/unit_step.png")
plt.show()

# -----------------------------
# 2. Unit Impulse Signal
# -----------------------------
unit_impulse = np.where(np.abs(t) < 0.01, 1, 0)

plt.figure()
plt.plot(t, unit_impulse)
plt.title("Unit Impulse Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid()
plt.savefig("graphs/unit_impulse.png")
plt.show()

# -----------------------------
# 3. Ramp Signal
# -----------------------------
ramp = np.where(t >= 0, t, 0)

plt.figure()
plt.plot(t, ramp)
plt.title("Ramp Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid()
plt.savefig("graphs/ramp.png")
plt.show()

# -----------------------------
# 4. Sine Wave
# -----------------------------
sine_wave = np.sin(2 * np.pi * t)

plt.figure()
plt.plot(t, sine_wave)
plt.title("Sine Wave")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid()
plt.savefig("graphs/sine_wave.png")
plt.show()

# -----------------------------
# 5. Exponential Signal
# -----------------------------
exponential = np.exp(-0.5 * t)

plt.figure()
plt.plot(t, exponential)
plt.title("Exponential Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid()
plt.savefig("graphs/exponential.png")
plt.show()

print("All signal graphs have been saved successfully!")