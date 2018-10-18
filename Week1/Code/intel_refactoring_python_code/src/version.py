
import sys
import pandas as pd
import numpy as np
import  scipy
import sklearn
import matplotlib
import seaborn

def main():
    print("Python: {}".format(sys.version))
    print("NumPy: {}".format(np.__version__))   
    print("pandas: {}".format(pd.__version__))   
    print("SciPy: {}".format(scipy.__version__))
    print("scikit-learn: {}".format(sklearn.__version__))
    print("matplotlib: {}".format(matplotlib.__version__))
    print("seaborn: {}".format(seaborn.__version__))
    
if __name__ == '__main__':
    main()