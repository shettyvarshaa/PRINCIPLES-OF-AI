import itertools
import sys

def calculate_total_distance(route, distances):
    """
    Calculate the total distance for a given route based on the distances matrix.
    
    Parameters:
    - route: List representing the order of cities to visit.
    - distances: 2D matrix representing the distances between cities.
    
    Returns:
    - Total distance for the given route.
    """
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distances[route[i]][route[i + 1]]
    total_distance += distances[route[-1]][route[0]]
    return total_distance

def traveling_salesman_bruteforce(distances):
    """
    Solve the traveling salesman problem using a brute-force approach.
    
    Parameters:
    - distances: 2D matrix representing the distances between cities.
    
    Returns:
    - Tuple containing the best route and the minimum distance.
    """
    num_cities = len(distances)
    all_routes = list(itertools.permutations(range(num_cities)))

    min_distance = sys.maxsize
    best_route = None

    for route in all_routes:
        distance = calculate_total_distance(route, distances)
        if distance < min_distance:
            min_distance = distance
            best_route = route

    return best_route, min_distance

# Example distances matrix
distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Find and print the best route and minimum distance
best_route, min_distance = traveling_salesman_bruteforce(distances)
print(f"Best Route: {best_route}")
print(f"Minimum Distance: {min_distance}")
