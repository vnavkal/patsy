from patsy.user_util import demo_data
from patsy import dmatrix
import numpy as np
data = demo_data('a')
mat = dmatrix('1 + a', data)
