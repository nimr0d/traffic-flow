import two_lane_traffic as traffic
import time

t = traffic.Traffic(n = 100, density = .3, prob = .1)
for i in range(200):
  print(str(t))
  t.iterate()
  print(t.num_cars, t.flow)
  time.sleep(1)
