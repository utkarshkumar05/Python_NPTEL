#Using stats
from scipy import stats
Experiments = [500,1000,200,235,546,896,485,375,453,987,654,321]
Experiments.sort()
m = stats.trim_mean(Experiments,0.1)
print(m)

#Without using stats (Using mean forom statistics)
from statistics import mean
Experiments = [500,1000,200,235,546,896,485,375,453,987,654,321]
Experiments.sort()
tv = int(0.1*len(Experiments))
Experiments = Experiments[tv:]
Experiments = Experiments[:len(Experiments)-tv]
print(mean(Experiments))

#Matplotlib
import matplotlib.pyplot as plt
plt.plot([1,2,3,4],[1,4,9,16],'b*')