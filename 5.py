def plus_one(digits):
  n = len(digits)
  carry = 1
  for i in range(n - 1, -1, -1):
    if digits[i] + carry == 10:
      digits[i] = 0
      carry = 1
    else:
      digits[i] += carry
      carry = 0
  if carry == 1:
    digits.append(1)
  return digits


if __name__ == "__main__":
  digits = [1, 2, 3]
  print(plus_one(digits))
