import math

# BEGIN (write your solution here)
def get_square_roots(num_sqr):
    list_sqrt = []
    if num_sqr > 0:
        sqrt = [math.sqrt(num_sqr) * -1,math.sqrt(num_sqr)]
        list_sqrt.extend(sqrt)
        return list_sqrt.extend(sqrt)
    elif num_sqr == 0:
        list_sqrt.append(0)
        return list_sqrt.append(0)
    return list_sqrt
# END


# BEGIN (write your solution here)
def get_range(num_rng):
    list_num_rng = []
    i = 0
    while i < num_rng:
        list_num_rng.append(i)
        i += 1   
    return list_num_rng
#END
get_range(5)
get_range(-5)
get_range(0)
get_square_roots(25)
get_square_roots(0)
get_square_roots(-1)

