from test import setup_data, calc_time, calc_delta

from tree import gen_bin_tree, gen_bin_tree_req

if __name__ == '__main__':
  print("Loop")
  print("height time")

  data = setup_data(100, 10)
  timetable = calc_time(gen_bin_tree, data)
  delta = calc_delta(timetable)

  for i, d in enumerate(data):
    start = timetable[i][0]
    end = timetable[i][1]
    time = end - start
    print(d[0], time)

  timetable = calc_time(gen_bin_tree_req, data)
  delta = calc_delta(timetable)
  print("Recursive")
  print("height time")
  for i, d in enumerate(data):
    start = timetable[i][0]
    end = timetable[i][1]
    time = end - start
    print(d[0], time)
