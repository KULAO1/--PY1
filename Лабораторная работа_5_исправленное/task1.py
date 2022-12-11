from pprint import pprint

pprint([{'bin': bin(count_), 'dec': count_, 'hex': hex(count_), 'oct': oct(count_)} for count_ in range(16)])
