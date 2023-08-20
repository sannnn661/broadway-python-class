#Given a list a = [(4, 12, 5), (6, 1), (11, 12), (6, 7, 8)],
# sort the list based on the last item of each tuple inside the list.


data=[(4,12,5),(6,1),(11,12),(6,7,8)]


def get_result(ans):
    return ans[-1]

data.sort(key=get_result)
print(data)  # [(6, 1), (4, 12, 5), (6, 7, 8), (11, 12)]



