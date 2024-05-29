import sys
"""find the nth fibonacci number"""
class Fibonacci:
    def fibonacci(num):
        if num < 2:
            return num 
        return Fibonacci.fibonacci(num - 1) + Fibonacci.fibonacci(num - 2)

if "__name__" == "__main__":
    if len(sys.argv) == 1:
        num = sys.argv[1]
    print(Fibonacci.fibonacci(num))




            
