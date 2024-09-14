# python-imports

Files to be imported into Python scripts or Jupyter Notebooks.

Yes, `import *` is bad practice.

Quick Start:
```python
import os, sys
PATH_TO_LIB = os.path.expanduser('~/dirs/my-robot-toolbox/python-imports')
if PATH_TO_LIB not in sys.path:
    sys.path.insert(1, PATH_TO_LIB)
from myimports import *
```

Quick Reload in Jupyer:
```python
import myhelpers
import importlib
importlib.reload(myhelpers)
from myhelpers import *
```

Run Pytest:
```bash
pytest
```
