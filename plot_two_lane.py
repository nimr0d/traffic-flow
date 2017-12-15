import numpy as np
import matplotlib.pyplot as plt

import two_lane_traffic as traffic

densitys = np.array(range(100), dtype = float) / 100
flows = []
for density in densitys:
    print(density)
    s = 0
    t = traffic.Traffic(n = 100, density = density, prob = .1)
    for i in range(1000):
        t.iterate()
        s += t.flow
    avg_flow = s / float(2 * t.n * 1000)
    flows.append(avg_flow)
    print(avg_flow)
plt.figure(1)
plt.plot(densitys,flows,'y')
plt.xlabel('density')
plt.ylabel('flow')
plt.title('two lane density vs flow graph')
plt.savefig('graph/two_lane_fund.png')