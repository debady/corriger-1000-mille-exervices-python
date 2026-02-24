import itertools

def print_combinations():
    for i in range(1, 100):
        if i<0:
            print('0',i)
        else:
            print(f"{i:02d}", end=" ")
    print()

print_combinations()