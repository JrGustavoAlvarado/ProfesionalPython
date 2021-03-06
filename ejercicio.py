from typing import Generic, TypeVar

T = TypeVar('T')

def make_divisor_by(n: int) -> Generic[T]:
    def numerator(x: int) -> float: 
        assert n != 0, 'Todo divido en Cero'
        return x/n
    return numerator
    

def main():
    divided_by_2 = make_divisor_by(2)
    print(divided_by_2(10))
     
     
if __name__ == '__main__':
    main()        