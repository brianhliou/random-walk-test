from collections import defaultdict
import random
import matplotlib.pyplot as plt
import numpy as np

def update_heatmap(heatmap, x, y):
    """Update the heatmap with the new position."""
    heatmap[(x, y)] += 1

def random_walk(n, heatmap):
    """Perform a single random walk within a specified boundary."""
    x, y = 0, 0
    steps = 0
    exit_direction = None

    while abs(x) <= n and abs(y) <= n:
        update_heatmap(heatmap, x, y)
        direction = random.choice(['up', 'down', 'left', 'right'])
        if direction == 'up':
            y += 1
        elif direction == 'down':
            y -= 1
        elif direction == 'left':
            x -= 1
        elif direction == 'right':
            x += 1
        steps += 1

    exit_direction = 'right' if x > n else 'left' if x < -n else 'up' if y > n else 'down'
    return steps, exit_direction

def simulate_random_walks(num_walks, max_boundary):
    """Simulate multiple random walks and return the statistics."""
    heatmap = defaultdict(int)
    steps = []
    exit_directions = []
    for _ in range(num_walks):
        s, d = random_walk(max_boundary, heatmap)
        steps.append(s)
        exit_directions.append(d)
    return steps, exit_directions, heatmap

def plot_heatmap(heatmap, grid_size):
    """Plot the heatmap of the random walks."""
    heatmap_grid = np.zeros((2 * grid_size + 1, 2 * grid_size + 1))
    for (x, y), count in heatmap.items():
        heatmap_grid[grid_size - y, x + grid_size] = count

    plt.figure(figsize=(8, 8))
    plt.imshow(heatmap_grid, cmap='hot', interpolation='nearest')
    plt.colorbar(label='Visit Count')
    plt.title('Random Walk Heatmap')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.xticks(np.arange(2 * grid_size + 1), np.arange(-grid_size, grid_size + 1))
    plt.yticks(np.arange(2 * grid_size + 1), np.arange(-grid_size, grid_size + 1))
    plt.grid(True, which='both', color='black', linestyle='-', linewidth=0.5)
    plt.gca().invert_yaxis()
    plt.show()

if __name__ == '__main__':
    num_walks = 1000
    max_boundary = 3
    steps, exit_directions, heatmap = simulate_random_walks(num_walks, max_boundary)
    print(f'Average number of steps: {sum(steps)/len(steps):.2f}')
    for direction in ['right', 'left', 'up', 'down']:
        print(f'Number of walks that exit to the {direction}: {exit_directions.count(direction)}')

    grid_size = max(max(abs(x), abs(y)) for x, y in heatmap.keys()) + 1
    plot_heatmap(heatmap, grid_size)
