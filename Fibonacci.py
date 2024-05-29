import sys
"""find the nth fibonacci number"""
class Fibonacci:
    @staticmethod
    def fibonacci(num):
        if num < 2:
            return num 
        return Fibonacci.fibonacci(num - 1) + Fibonacci.fibonacci(num - 2)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scriptname integer")
        sys.exit(1)
    try:
        num = int(sys.argv[1])
    except ValueError:
        print("The argument must be an integer.")
        sys.exit(1)
    print(Fibonacci.fibonacci(num))




            
