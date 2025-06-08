# rods = {'A': [3, 2, 1], 'B': [], 'C': []}

# def hanoi(n, source, target, auxiliary):
#     if n == 1:
#         rod = rods[source].pop()
#         rods[target].append(rod)
#         print(f"Move rod {rod} from {source} to {target}")
#         print(rods)
#         return
    
#     hanoi(n-1, source, auxiliary, target)
#     rod = rods[source].pop()
#     rods[target].append(rod)
#     print(f"Move rod {rod} from {source} to {target}")
#     print(rods)
#     hanoi(n-1, auxiliary, target, source)


# print(f"We start from {rods}")
# hanoi(3, 'A', 'B', 'C')


rods = {'A': [3, 2, 1], 'B': [], 'C': []}

def hanoi(n, source, target, auxiliary, level=0):
    indent = "  " * level  # indentation for recursion depth visualization
    print(f"{indent}-> hanoi(n={n}, source={source}, target={target}, auxiliary={auxiliary})")


    if n == 1:
        rod = rods[source].pop()
        rods[target].append(rod)
        print(f"{indent}  Move disk {rod} from {source} to {target}")
        print(f"{indent}  Current state: {rods}")
        return

    # Step 1: move n-1 disks from source to auxiliary
    hanoi(n-1, source, auxiliary, target, level + 1)

    # Step 2: move the remaining disk from source to target
    rod = rods[source].pop()
    rods[target].append(rod)
    print(f"{indent}  Move disk {rod} from {source} to {target}")
    print(f"{indent}  Current state: {rods}")

    # Step 3: move n-1 disks from auxiliary to target
    hanoi(n-1, auxiliary, target, source, level + 1)

# Run the function
print(f"Initial state: {rods}")
hanoi(3, 'A', 'B', 'C')
print(f"Final state: {rods}")

