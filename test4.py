import sys
from assignment4 import ConfigDict

cd = ConfigDict('revanalysis.config')

if len(sys.argv) == 3:
    key = sys.argv[1]
    value = sys.argv[2]
    print('writing data: {}, {}'.format(key,value))
    cd[key]=value

elif len(sys.argv) == 2:
    print('reading a value')
    key = sys.argv[1]
    print('the value for {} is {}'.format(sys.argv[1],cd[key]))

else:
    print('keys/values:')
    for key in cd.keys():
        print('    {} = {}'.format(key,cd[key]))


