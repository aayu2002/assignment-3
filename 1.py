def closest_sum_of_three(nums, target):
  closest_sum = float("inf")
  for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
      for k in range(j + 1, len(nums)):
        sum = nums[i] + nums[j] + nums[k]
        if abs(target - sum) < abs(target - closest_sum):
          closest_sum = sum
  return closest_sum


if __name__ == "__main__":
  nums = [-1, 2, 1, -4]
  target = 1
  print(closest_sum_of_three(nums, target))
