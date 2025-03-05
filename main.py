import numpy as np
import matplotlib.pyplot as plt

def decimal_to_rule(binary_rule):
    return [int(bit) for bit in f"{binary_rule:08b}"]

def generate_next_gen(current_gen, rule):
    next_gen = np.zeros_like(current_gen)
    rule_bin = decimal_to_rule(rule)
    
    for i in range(1, len(current_gen) - 1):
        neighborhood = (current_gen[i - 1] << 2) | (current_gen[i] << 1) | current_gen[i + 1]
        next_gen[i] = rule_bin[7 - neighborhood]
    
    return next_gen

def run_1d_CA(rule, size=100, generations=50):
    grid = np.zeros((generations, size), dtype=int)
    grid[0, size // 2] = 1  # ena ziva v sredini
    
    for gen in range(1, generations):
        grid[gen] = generate_next_gen(grid[gen - 1], rule)
    
    plt.figure(figsize=(10, 10))
    plt.imshow(grid, cmap="binary", interpolation="nearest")
    plt.title(f"1D Cellular Automaton - Rule {rule}")
    plt.show()


rule_number = int(input("Vnesite pravilo (0-255): "))
while rule_number < 0 or rule_number > 255:
    print("Neveljavno pravilo! Vnesite število med 0 in 255.")
    rule_number = int(input("Vnesite pravilo (0-255): "))
    
run_1d_CA(rule_number)