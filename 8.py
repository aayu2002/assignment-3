def can_attend_all_meetings(intervals):

  intervals.sort()
  for i in range(1, len(intervals)):
    if intervals[i][0] < intervals[i - 1][1]:
      return False
  return True


if __name__ == "__main__":
  intervals = [[0, 30], [5, 10], [15, 20]]
  print(can_attend_all_meetings(intervals))
