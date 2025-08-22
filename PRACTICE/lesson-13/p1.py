import os
from typing import Dict, Callable

def main() -> None:
    """Main function with type annotations"""
    print("текущее положение на диске", os.getcwd())
    
    x: int = 123
    
    # Raw f-strings
    result1: str = rf'hello {x} world'
    result2: str = fr'hello world'
    
    # Dictionary with lambda
    d: Dict[str, Callable[[int], int]] = {
        "f": lambda x: x ** 2
    }
    
    print(os.stat("p1.py"))

if __name__ == "__main__":
    main()