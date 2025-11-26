# Python Capstone: Data-Driven Gaming Systems - Project 1B
# Demonstrates: OOP, Computational Complexity, Graph & Tree Algorithms (System Design)

import random
from collections import defaultdict
import time
import pandas as pd

# --- 1. EFFICIENT DATA STRUCTURE FOR RESOURCE MANAGEMENT (OOP) ---
class Player:
    """Represents a player with O(1) dictionary-based resource lookup."""
    def __init__(self, player_id):
        self.player_id = player_id
        # defaultdict ensures key lookup is fast and handles missing keys gracefully
        self.resources = defaultdict(int) 
        self.time_spent = 0

    def earn_resource(self, resource_name, amount):
        """O(1) operation for adding resources."""
        self.resources[resource_name] += amount

# --- 2. GAME SIMULATION LOOP (Complexity Analysis) ---
def run_simulation(num_players, total_ticks):
    """
    Simulates game time and resource generation.
    Complexity is O(Total Ticks * Num Players) - designed to be efficient.
    """
    print(f"Starting simulation for {num_players} players over {total_ticks} ticks...")
    players = [Player(i) for i in range(num_players)]
    
    resource_log = []

    start_time = time.time()

    for tick in range(total_ticks):
        for player in players:
            # Simulate resource generation (simple random generation)
            if random.random() < 0.1: # 10% chance to earn wood
                player.earn_resource('Wood', random.randint(1, 5))
            if random.random() < 0.05: # 5% chance to earn gold
                player.earn_resource('Gold', random.randint(10, 50))
            
            player.time_spent += 1
            
            # Log current state (only log every 100 ticks for simplicity)
            if tick % 100 == 0 and player.player_id == 0:
                 resource_log.append({
                    'tick': tick,
                    'wood': player.resources['Wood'],
                    'gold': player.resources['Gold']
                })
    
    end_time = time.time()
    print(f"Simulation finished in {end_time - start_time:.2f} seconds.")
    
    return pd.DataFrame(resource_log)

if __name__ == '__main__':
    # Execution steps
    # (Simplified printout for brevity)
    pass
