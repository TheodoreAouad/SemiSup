#%% Add to path
import sys
%cd ..

with open('python_paths.txt', 'r') as f:
    paths = f.read().splitlines()
for path in paths:
    if path not in sys.path:
        sys.path.append(path)

        
print(sys.path)
print(sys.executable)

#%% Reload modules
from importlib import reload

def reload_modules():
    for mudl in []:
        reload(mudl)
        
reload_modules()