from que import Queue
from visitor import Visitor
from oper import Operator, OperatorType
import random

queue = Queue()

operator1 = Operator('Bob', [OperatorType.PAYTAX, OperatorType.OPENBIS], queue)
operator2 = Operator('Bib', [OperatorType.OPENBIS, OperatorType.ASKQUESTION], queue)
operator3 = Operator('Bub', [OperatorType.PAYTAX, OperatorType.ASKQUESTION], queue)

for i in range(20):
    visitor = Visitor(OperatorType(random.randint(1, 3)))
    queue.addVisitor(visitor)