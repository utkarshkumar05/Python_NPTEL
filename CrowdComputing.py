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
plt.plot([1,2,3,4],[1,4,9,16],'g*')

#Using Matplotlib for analysing crowd data
import statistics
import matplotlib.pyplot as plt
Est = [500,1000,200,235,546,896,485,375,453,987,654,321]
y = []
Est.sort()
tv = int(0.1*len(Est))
Est = Est[tv:]
Est = Est[:len(Est)-tv]
for i in range(len(Est)):
    y.append(5)
plt.plot(Est,y,'r--')
plt.plot([statistics.mean(Est)],[5],'ro')
plt.plot([statistics.median(Est)],[5],'bs')
plt.plot([550],[5],'g^')
