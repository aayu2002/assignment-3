def next_permutation(nums):
  i = len(nums) - 1
  while i > 0 and nums[i - 1] >= nums[i]:
    i -= 1
  if i == 0:
    nums.reverse()
  else:
    j = len(nums) - 1
    while nums[j] <= nums[i - 1]:
      j -= 1
    nums[i - 1], nums[j] = nums[j], nums[i - 1]
    nums[i:] = nums[i:][::-1]
  return nums


if __name__ == "__main__":
  nums = [1, 2, 3]
  print(next_permutation(nums))
