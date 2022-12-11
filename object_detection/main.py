# data class demo
from dataclasses import dataclass
from dataclasses import field

@dataclass
class Investor:

    name : str = field(init=False,default= 'noel')
    age : int
    cash : float = field(repr=False)


i1 = Investor(age=33,cash=22903)
print(i1)