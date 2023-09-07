import random


def approximate_pi(num_points):
    points_inside_circle = 0
    total_points = 0

    while total_points < num_points:
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x ** 2 + y ** 2 < 1:
            points_inside_circle += 1

        total_points += 1

    pi_approximation = 4 * points_inside_circle / total_points
    return pi_approximation


num_points = int(input("Enter the number of random points to generate: "))

approximation = approximate_pi(num_points)
print(f"Approximation of pi using {num_points} random points: {approximation}")
