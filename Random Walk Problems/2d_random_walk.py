import random as rng
import matplotlib.pyplot as plt

triallst = []
sample = 100

for s in range(sample):
    successes = 0
    trials = 1000
    
    for t in range(trials):
        x = 0
        y = 0
        
        for step in range(1000):
            if rng.choice([0, 1]):
                x += rng.choice([-1, 1])
            else:
                y += rng.choice([-1, 1])
            if not x and not y:
                successes += 1
                break
    
    success_rate = (successes * 100) / trials
    triallst.append(success_rate)
    print(f"Sample {s+1}: {success_rate:.2f}%")

plt.figure(figsize=(10, 6))
binwidth = 0.05
plt.hist(triallst, bins=range(int(min(triallst)), int(max(triallst)) + 1, 1),
         edgecolor="yellow", color="brown")
plt.title('Distribution of Success Rates')
plt.xlabel('Success Rate (%)')
plt.ylabel('Frequency')
plt.grid(True, alpha=0.3)
plt.show()