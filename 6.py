def single_number(nums):
  seen = set()
  for num in nums:
    if num in seen:
      seen.remove(num)
    else:
      seen.add(num)
  return seen.pop()


if __name__ == "__main__":
  nums = [2, 2, 1]
  print(single_number(nums))
