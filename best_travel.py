#~/usr/bin/env python

import itertools as it

def choose_best_sum(distances, towns, max_distance):

    """
    Args:
        distances (List[int]): List of distances of towns
        towns (int): Number of towns to visit
        max_distance (int): Max distance to travel
    
    Returns:
        List[int]: Distances that have the higheset distance <= max_distance
                   for the given amount of towns
    """

    if towns < 0:
        raise ValueError("towns must be a positive integer")

    if max_distance < 0:
        raise ValueError("max_distance must be a positive integer")

    if type(distances) is not list:
        raise ValueError("distance must be a list")

    best_sum = 0
    best_combo = None
    combinations = list(it.combinations(distances, towns))
    for combo in combinations:
        temp_sum = sum(combo)
        if temp_sum > best_sum and temp_sum <= max_distance:
            best_sum = temp_sum
            best_combo = combo

    return best_combo

if __name__ == '__main__':
    print(choose_best_sum([50, 55, 57, 58, 60], 3, 174))
