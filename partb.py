def calculate_probability(distribution_matrix):
    total_combinations = sum(sum(row) for row in distribution_matrix)
    probabilities = {}
    for i in range(2, 13):
        combinations_for_sum = sum(row.count(i) for row in distribution_matrix)
        probabilities[i] = combinations_for_sum / total_combinations
    return probabilities

def undoom_dice(die_a, die_b,total_combinations):
    original_distribution = calculate_probability(distribution)
    
    
    target_distribution = original_distribution.copy()  
    num_combinations_needed = {sum_value: int(probability * total_combinations) for sum_value, probability in original_distribution.items()}
    
    
    new_die_a = []
    for num_spots in die_a:
        if num_spots <= 4:
            new_die_a.append(num_spots)
        else:
            
            for face in range(1, 7):
                if num_combinations_needed[face + 1] > 0:
                    new_die_a.append(face + 1)
                    num_combinations_needed[face + 1] -= 1
                    break

    
    new_die_b = die_b.copy()    
    return new_die_a, new_die_b


Die_A = [1, 2, 3, 4, 5, 6]
Die_B = [1, 2, 3, 4, 5, 6]

def calculate_distribution():
    distribution_matrix = [[0] * 6 for _ in range(6)]
    for i in range(1, 7):
        for j in range(1, 7):
            distribution_matrix[i-1][j-1] = i + j
    return distribution_matrix

distribution = calculate_distribution()
total_combinations = 36

New_Die_A, New_Die_B = undoom_dice(Die_A, Die_B,total_combinations)
print("New Die A:", New_Die_A)
print("New Die B:", New_Die_B)