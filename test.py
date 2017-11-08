import traffic
import curses
import time

stdscr = curses.initscr()
curses.noecho()
curses.curs_set(0)
curses.start_color()
for i in range(1, 7):
  curses.init_pair(i, 7 - i, curses.COLOR_BLACK)
t = traffic.Traffic(n = 1000, density = .5, prob = .3)
for i in range(1000):
  stdscr.clear()
  t.iterate()
  stdscr.addstr(str(t), curses.color_pair(i % 6 + 1))
  stdscr.refresh()
  time.sleep(.3)
