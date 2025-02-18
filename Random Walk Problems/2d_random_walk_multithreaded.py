import random as rng
import matplotlib.pyplot as plt
from concurrent.futures import ProcessPoolExecutor

def simulate_batch(params):
    steps, trials = params
    successes = 0
    
    for _ in range(trials):
        x = 0
        y = 0
        
        for _ in range(steps):
            if rng.choice([0, 1]):
                x += rng.choice([-1, 1])
            else:
                y += rng.choice([-1, 1])
            if not x and not y:
                successes += 1
                break
    
    return (successes * 100) / trials

def run_simulation():
    while True:
        try:
            steps = int(input("Enter the number of steps per trial: "))
            if steps <= 0:
                print("Please enter a positive number")
                continue
            break
        except ValueError:
            print("Please enter a valid integer")
    
    sample = 100
    trials = 1000
    
    params = [(steps, trials)] * sample

    with ProcessPoolExecutor() as executor:
        triallst = list(executor.map(simulate_batch, params))
        
        for i, success_rate in enumerate(triallst):
            print(f"Sample {i+1}: {success_rate:.2f}%")
    
    plt.figure(figsize=(10, 6))
    plt.hist(triallst, 
             bins=range(int(min(triallst)), int(max(triallst)) + 1, 1),
             edgecolor="yellow", 
             color="brown")
    plt.title(f'Distribution of Success Rates ({steps} steps per trial sample)')
    plt.xlabel('Success Rate (%)')
    plt.ylabel('Frequency')
    plt.grid(True, alpha=0.3)
    plt.show()

if __name__ == '__main__':
    run_simulation()