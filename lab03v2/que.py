class Queue():
    __slots__ = ['__operators', '__currentQueue']

    def __init__(self):
        self.__operators = list()
        self.__currentQueue = list()

    def __str__(self):
        return 'In queue {} visitors'.format(len(self.__currentQueue))

    @property
    def currentQueue(self):
        return self.__currentQueue

    def addVisitor(self, visitor):
        for op in self.__operators:
            if visitor.type in op.types and op.isFree:
                op.workWithVisitor(visitor)
                return
        self.__currentQueue.append(visitor)

    def __removeVisitor(self, visitor):
        self.__currentQueue.remove(visitor)

    def findVisitorForOperator(self, operator):
        for vis in reversed(self.__currentQueue):
            if vis.type in operator.types:
                self.__removeVisitor(vis)
                operator.workWithVisitor(vis)
                return

    def addOperator(self, operator):
        self.__operators.append(operator)
        self.findVisitorForOperator(operator)