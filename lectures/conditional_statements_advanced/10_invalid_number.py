num = int(input())

# is_range = num >= 100 and num <= 200
# is_zero = num == 0

valid = (num >= 100 and num <= 200) or num == 0

if not valid:
    print("invalid")
