import numpy as np
import pandas as pd

N = 10000  # Monte Carlo simulations

trade_volume = np.random.lognormal(mean=14, sigma=0.8, size=N)
anomaly_rate = np.random.uniform(0.0003, 0.0012, size=N)
gpu_cost = np.random.normal(0.9e-6, 0.2e-6, size=N)
complexity = np.random.choice([1, 1.2, 1.5], size=N, p=[0.6, 0.3, 0.1])
gpu_tps = np.random.triangular(900, 1200, 1600, size=N)
latency = np.random.gamma(shape=2, scale=8, size=N)

gpu_hours = trade_volume * gpu_cost * complexity
gpu_price = np.random.uniform(1.2, 2.8, size=N)
daily_cost = gpu_hours * gpu_price

df = pd.DataFrame({
    "trade_volume": trade_volume,
    "gpu_hours": gpu_hours,
    "latency": latency,
    "daily_cost": daily_cost
})

df.to_csv("results/summary_stats.csv", index=False)

with open("results/failure_probability.txt", "w") as f:
    f.write(str(np.mean(latency > 60)))
