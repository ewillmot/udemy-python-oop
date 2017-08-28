
import abc
from datetime import datetime

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
    

class WriteFile(object):
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def write(self):
        return
    
    def __init__(self,filename):
        self.filename = filename
    
    def write_line(self,text):
        fh = open(self.filename,'a')
        fh.write(text+ '\n')
        fh.close()
        
class DelimFile(WriteFile):
    def __init__(self,filename,delim):
        super(DelimFile,self).__init__(filename)
        self.delim = delim
        
    def write(self,this_list):
        line = self.delim.join(this_list)
        self.write_line(line)
        
class LogFile(WriteFile):
    def write(self,this_line):
        dt = datetime.now()
        date_str = dt.strftime('%Y-%m-%d %H:%M')
        self.write_line('{0}   {1}'.format(date_str,this_line))
        