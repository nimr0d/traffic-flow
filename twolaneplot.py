import numpy as np
import matplotlib.pyplot as plt

import twolane

densitys=np.array(range(100),dtype=float)/100
list_of_flow=[]
for density in densitys:
    print(density)
    flows=[]
    a=twolane.traffic(density=density)
    for i in range(1000):
        a.iteration()
        flows.append(a.flow())

    list_of_flow.append(np.mean(flows))
    print(np.mean(flows))

plt.figure(1)
plt.plot(densitys,list_of_flow,'r')
plt.xlabel('densitys')
plt.ylabel('flow')
plt.title('two lane density vs flow graph')
plt.savefig('graph/twolanefigure.png')
