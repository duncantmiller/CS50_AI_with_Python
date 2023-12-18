from logic import *

# If it is not raining, then Harry visited Hagrid
# Harry either visited Hagrid or Dumbledore
# Harry did not visit both
# Harry visited Dumbledore

harry = Symbol("harry")
hagrid = Symbol("hagrid") # Harry visited Hagrid
dumbledore = Symbol("dumbledore") # Harry visited Dumbledore

knowledge = And(
    Implication(Not(rain), hagrid),
    Or(hagrid, dumbledore),
    Not(And(hagrid, dumbledore)),
    dumbledore
)

print(knowledge.formula())
