import numpy as np
import scipy.stats as stats
x = np.array([172, 177, 158, 170, 178,175, 164, 160, 169, 165])
y = np.array([ 173, 175, 162, 174, 175, 168, 155, 170, 160])
result = stats.ttest_ind(x,y)
print(result)
