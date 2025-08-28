# Loop Exercises

# 1. Print numbers 1 to 10
def print_numbers():
    for i in range(1, 11):
        print(i)

# 2. Multiplication table
def multiplication_table(n):
    i = 1
    while i <= 10:
        print(f"{n} x {i} = {n*i}")
        i += 1

# 3. Pyramid
def pyramid(n):
    for i in range(1, n+1):
        print("*" * i)

# 4. Prime numbers up to n
def primes_up_to(n):
    primes = []
    for num in range(2, n+1):
        if all(num % i != 0 for i in range(2, int(num**0.5)+1)):
            primes.append(num)
    return primes

# 5. Factorial (recursion)
def factorial(n):
    if n == 0: return 1
    return n * factorial(n-1)

# 6. Function with args/kwargs
def sum_args(*args, **kwargs):
    return sum(args) + sum(kwargs.values())

# 7. Skip 5 using continue
def skip_five():
    for i in range(1, 11):
        if i == 5:
            continue
        print(i)

# 8. Stop at 7 using break
def stop_at_seven():
    for i in range(1, 11):
        if i == 7:
            break
        print(i)

# 9. Tower of Hanoi
def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    hanoi(n-1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    hanoi(n-1, auxiliary, target, source)

# 10. Tic-tac-toe simulation (simple board)
def tic_tac_toe():
    board = [" "]*9
    def print_board():
        for i in range(0,9,3):
            print("|".join(board[i:i+3]))
    turn = "X"
    for _ in range(9):
        print_board()
        pos = int(input(f"Player {turn}, enter position (0-8): "))
        if board[pos] == " ":
            board[pos] = turn
            turn = "O" if turn == "X" else "X"
    print_board()
