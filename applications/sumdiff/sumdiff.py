"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

# q = set(range(1, 10))
q = set(range(1, 200))
# q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here
def combo_solutions(nums):
    nums = list(nums)
    plus = {}
    minus = {}
    for i in range(len(nums)):
        for j in range(len(nums)):
            plus_result = f(nums[i]) + f(nums[j])
            plus_index = (nums[i], nums[j])
            plus[plus_index] = plus_result

            minus_index = f(nums[i]) - f(nums[j])
            minus_result = (nums[i], nums[j])
            if minus_index not in minus:
                minus.setdefault(minus_index, [minus_result])
            else:
                minus[minus_index].append(minus_result)

    for (key, value) in plus.items():
        if value in minus:
            for i in minus[value]:
                print(f"f({key[0]}) + f({key[1]}) = f({i[0]}) - f({i[1]})    {f(key[0])} + {f(key[1])} = {f(i[0])} - {f(i[1])}")
   
    
import time
start_time = time.time()
combo_solutions(q)
end_time = time.time()
print(f"Solution took: {end_time - start_time}")


