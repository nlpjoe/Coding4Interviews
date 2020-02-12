class CQueue(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, value):
        self.stack1.append(value)
    
    def deleteHead(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop(-1))
        if len(self.stack2) == 0: 
            return -1
        return self.stack2.pop(-1)
