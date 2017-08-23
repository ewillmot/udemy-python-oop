

class MaxSizeList(object):
    
    def __init__(self,maxsize):
        self.mylist = list([])
        self.maxsize=maxsize
        
    def get_list(self):
        return self.mylist
        
    def push(self,val):
        self.mylist.append(val)
        
        while len(self.mylist)>self.maxsize:
            self.mylist.pop(0)
    
