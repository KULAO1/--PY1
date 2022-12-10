from pprint import pprint

count_ = 15

pprint([{'bin': bin(_), 'dec': _, 'hex': hex(_), 'oct': oct(_)} for _ in range(count_+1)])
