#1. How many total combinations are possible? Show the math along with the code

def total_combinations():
    combinations = 0    
    num_faces = 6    
    combinations = num_faces * num_faces    
    return combinations
print("Total combinations:", total_combinations())

#2. Calculate and display the distribution of all possible combinations that can beobtained when rolling both Die A and Die B together. Show the math along with the code!
def calculate_distribution():
    
    distribution_matrix = [[0] * 6 for _ in range(6)]
    for i in range(1, 7):
        for j in range(1, 7):
            distribution_matrix[i-1][j-1] = i + j
    
    return distribution_matrix

def display_distribution(matrix):
    for row in matrix:
        print(" ".join(str(cell) for cell in row))


distribution = calculate_distribution()


print("Distribution Matrix (6x6):")
display_distribution(distribution)

#3.Calculate the Probability of all Possible Sums occurring among the number of combinations from (2).

def calculate_probability(distribution_matrix):
    total_combinations = sum(sum(row) for row in distribution_matrix)
    probabilities = {}
    for i in range(2, 13):
        combinations_for_sum = sum(row.count(i) for row in distribution_matrix)
        probabilities[i] = combinations_for_sum / total_combinations
    return probabilities


probabilities = calculate_probability(distribution)
print("Probability of each sum:")
for sum_value, probability in probabilities.items():
    print(f"P(Sum = {sum_value}) = {probability:.2f}")


