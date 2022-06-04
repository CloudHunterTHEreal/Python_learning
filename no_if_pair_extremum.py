"""Get maximum without using  if-else, loops and standard max() / min() functions
Example of using class features"""

from typing import Iterable
from dataclasses import dataclass

def my_abs(arg):
    """Getting absolute value the arg. (Don't beat me, please, just I'm training.)"""
    return (arg ** 2) ** 0.5


@dataclass
class PairExtremum:
    """Stores pair of numbers. Returns max() and min() of this numbers."""
    pair: Iterable

    def __init__(self, pair: Iterable):
        self.pair = pair
        self._difference = self.pair[0] - self.pair[1]


    def _result(self) -> float:
        """Main idea of the solution. Processing and returning."""
        return self.pair[int(bool((self._difference) - my_abs(self._difference)))]

    
    def max(self) -> float:
        """Preparation of finding the maximum number"""
        return self._result()

    
    def min(self) -> float:
        """Preparation of finding the minimum number"""
        self._difference = self.pair[1] - self.pair[0]
        return self._result()


numbers = [float(input(f"Enter the {number_name} number of the pair: "))
           for number_name in ('first',
                               'second')]

data = PairExtremum(numbers)
print(f"\nAnalyzed pair of numbers: {data.pair}\n"
      f"Maximum number in a pair: {data.max()}\n"
      f"Minimum number in a pair: {data.min()}")
