import os

class ConfigDict(dict):

    def __init__(self,filename):
        self._filename=filename
        if not os.path.isfile(self._filename):
       	    try:
		open(self._filename,'w').close()
	    except IOError:
		raise IOError('arg to ConfigDict must be a valid pathname')

	with open(self._filename) as fh:
            for line in fh:
                line = line.rstrip()
                key,val = line.split("=",1)
                dict.__setitem__(self,key,val)

    def __setitem__(self,key,val):
        dict.__setitem__(self,key,val)
        with open(self._filename,'w') as fh:
            for key,val in self.items():
                fh.write("{}={}\n".format(key,val))
                
    def __getitem__(self,key):
        try:
            return dict.__getitem__(self,key)
        except KeyError:
            raise ConfigKeyError(self,key)
            
class ConfigKeyError(Exception):
    def __init__(self,*args):
        self.message = "Key '{}' not found. Available keys: {}".format(args[1],tuple(args[0].keys()))

    def __str__(self):
	return self.message
