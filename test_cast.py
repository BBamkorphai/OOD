def format_coordinates(coordinates):
    queue = []
    for coord in coordinates:
        queue.append(tuple(coord))
    return "Queue: " + str(queue)

# Example usage:

coords2 = [[5, 6], [4, 5]]

  # Output: Queue: [(1, 6)]
print(format_coordinates(coords2))  # Output: Queue: [(8, 3), (7, 4), (6, 5), (5, 4)]