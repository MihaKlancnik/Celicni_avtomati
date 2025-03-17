import numpy as np
import matplotlib.pyplot as plt
import pygame
import sys

def decimal_to_rule(binary_rule):
    return [int(bit) for bit in f"{binary_rule:08b}"]

def generate_next_gen(current_gen, rule):
    next_gen = np.zeros_like(current_gen)
    rule_bin = decimal_to_rule(rule)
    
    for i in range(1, len(current_gen) - 1):
        neighborhood = (current_gen[i - 1] << 2) | (current_gen[i] << 1) | current_gen[i + 1]
        next_gen[i] = rule_bin[7 - neighborhood]
    
    return next_gen

def run_1d_cellular_automaton(rule, size=100, generations=50):
    grid = np.zeros((generations, size), dtype=int)
    grid[0, size // 2] = 1  # Začetni pogoj: ena živa celica v sredini
    
    for gen in range(1, generations):
        grid[gen] = generate_next_gen(grid[gen - 1], rule)
    
    plt.figure(figsize=(10, 10))
    plt.imshow(grid, cmap="binary", interpolation="nearest")
    plt.title(f"1D Cellular Automaton - Rule {rule}")
    plt.show()

def run_2d_game_of_life(grid_size=50, cell_size=10, generations=100):
    pygame.init()
    screen = pygame.display.set_mode((grid_size * cell_size, grid_size * cell_size))
    clock = pygame.time.Clock()
    
    grid = np.random.choice([0, 1], (grid_size, grid_size), p=[0.5, 0.5])
    
    for _ in range(generations):
        new_grid = np.copy(grid)
        
        for i in range(grid_size):
            for j in range(grid_size):
                neighbors = np.sum(grid[max(i - 1, 0):min(i + 2, grid_size), max(j - 1, 0):min(j + 2, grid_size)]) - grid[i, j]
                
                if grid[i, j] == 1 and (neighbors < 2 or neighbors > 3):
                    new_grid[i, j] = 0
                elif grid[i, j] == 0 and neighbors == 3:
                    new_grid[i, j] = 1
        
        grid = new_grid
        
        screen.fill((0, 0, 0))
        for i in range(grid_size):
            for j in range(grid_size):
                color = (255, 255, 255) if grid[i, j] == 1 else (0, 0, 0)
                pygame.draw.rect(screen, color, (j * cell_size, i * cell_size, cell_size, cell_size))
        
        pygame.display.flip()
        clock.tick(5)
    
    pygame.quit()


rule_number = int(input("Vnesite pravilo za 1D avtomat (0-255): "))
while rule_number < 0 or rule_number > 255:
    print("Neveljavno pravilo! Vnesite število med 0 in 255.")
    rule_number = int(input("Vnesite pravilo (0-255): "))

run_1d_cellular_automaton(rule_number)


input("Pritisnite Enter za začetek 2D celičnega avtomata")
run_2d_game_of_life()
