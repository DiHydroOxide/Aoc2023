from heapq import heappush, heappop

file_name = 'puzzle-input.txt'
# file_name = 'sample.txt'
seen = set()
pq = [(0, 0, 0, 0, 0, 0)]  # (Heat Loss, row, col, direction row, direction col, distance)  is state

with open(file_name, 'r') as f:
    grid = [list(map(int, line.strip())) for line in f]

# heaps are binary trees with the smallest element as the parent (root)
# This works because the first element in a state (tuple) is an int
# Which is known how to compare and is what we want the smallest value of first

# Using Dijkstra algorithm (Look at lowest heat loss first of all paths)
while pq:  # While we have a state in the queue
    hl, r, c, dr, dc, n = heappop(pq)  # Get the smallest state (smallest heat loss, if equal smallest row, ...)

    # Check if we are in the bottom right corner
    # We check this first since we are always checking the state with the lowest heat loss first
    if r == len(grid) - 1 and c == len(grid[0]) - 1 and n >= 4:
        print(f"Minimum heat loss is {hl}")
        break

    # If we moved to a state in the same direction and distance
    if (r, c, dr, dc, n) in seen:
        continue  # Move to next item in pq

    seen.add((r, c, dr, dc, n))  # Don't add heat loss to prevent looping to same spot with increasing heat loss

    # Check forward first
    if n < 10 and (dr, dc) != (0, 0):  # If we can move in the same direction and we are moving
        nr = r + dr  # Get next row and col positions
        nc = c + dc

        # If we are in bounds add next position to queue with adding heat and distance
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
            heappush(pq, (hl + grid[nr][nc], nr, nc, dr, dc, n + 1))

    if n >= 4 or (dr, dc) == (0, 0):  # If we have moved the minimum distance or are not moving (start)
        # Check left and right directions
        for (ndr, ndc) in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # For each possible direction
            # If we aren't moving in the same direction and not backwards
            if (ndr, ndc) != (dr, dc) and (ndr, ndc) != (-dr, -dc):
                nr = r + ndr  # Next row, col position
                nc = c + ndc

                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):  # Check bounds
                    heappush(pq, (hl + grid[nr][nc], nr, nc, ndr, ndc, 1))
