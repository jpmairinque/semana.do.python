print("Find the mean (average) of a list of numbers in an array. ")

def find_average(nums):
    return float(sum(nums)) / len(nums) if len(nums) !=0 else 0

#sum() functions = sums all of the items in an array // scnd parameter = sum's start point