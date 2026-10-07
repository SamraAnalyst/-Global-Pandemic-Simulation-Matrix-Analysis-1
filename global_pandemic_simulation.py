import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("--- Step 1: Initialising Global Population /matrix Core ---")

total_population = 100000
beta = 0.4
gamma = 0.1
days_timeline = 90

S = np.zeros(days_timeline)
I = np.zeros(days_timeline)
R = np.zeros(days_timeline)

I[0] = 100
S[0] = total_population - I[0]
R[0] = 0

print("Running iterative differential mathematical calculus loops...")

for t in range(1, days_timeline):
     new_infections = (beta * S[t-1] * I[t-1]) / total_population
     new_recoveries = gamma * I[t-1]
    
     S[t] = S[t-1] - new_infections
     I[t] = I[t-1] + new_infections - new_recoveries
     R[t] = R[t-1] + new_recoveries


simulation_dictionary = {
    "Day": np.arange(1, days_timeline + 1),
    "Susceptible_Pool": np.round(S),
    "Active_Infections": np.round(I),
    "Recovered_Population": np.round(R)

}
df = pd.DataFrame(simulation_dictionary)

print("/n--- Simulation Complete: Intial Trend Matrix Logs ---")
print(df.head(10))

print("\n--- Step 3: Generating Advanced Visual Epidemic Peaks ---")
plt.figure(figsize=(10, 5))

plt.plot(df["Day"], df["Susceptible_Pool"], color="#4A4644", label="Susceptible (Healthy)", linewidth=2)
plt.plot(df["Day"], df["Active_Infections"], color="#8B8589", label="Active Infections (Peak)", linewidth=2.5)
plt.plot(df["Day"], df["Recovered_Population"], color="#D2B48C", label="Recovered (Immune)", linewidth=2)

plt.title("Global Pandemic Infection Spread & Mathematical Matrix Analysis", fontsize=11, fontweight="bold")
plt.xlabel("Timeline Duration (Days)", fontsize=10)
plt.ylabel("Active Population Scale Count", fontsize=10)
plt.grid(axis='both', linestyle='--', alpha=0.5)
plt.legend(loc="upper right")
plt.tight_layout()
print("Force rendering layout charts...")
plt.show(block=True)

