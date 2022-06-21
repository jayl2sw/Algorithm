import numpy as np

np.random.seed(0)

# def solution(array,shift):
#     if shift == "rotated":
#         answer = np.rot90(array, 1)
#     elif shift == "flipped":
#         answer = np.flip(array,0)
#     elif shift == "rolled":
#         answer = np.roll(array, 1)
#     else:
#         answer = [array[i][:] for i in range(len(array))]
#         for i in range(len(array)):
#             for j in range(len(array[0])):
#                 answer[i][j] += round(np.random.normal(0, 0.05),2)
#
#
#     return answer




def solution(array, shift):
    np.random.seed(0)

    noise = np.random.normal(0, 0.05, array.shape)
    answer = {"rotated" : np.rot90(array, 1),
              "flipped": np.flip(array, 0),
              "rolled" : [np.roll(row, shift) for row in array],
              "noised" : array + noise}

    return answer

array = [[1, 1, 1, 0],
         [1, 0, 1, 0],
         [1, 1, 1, 0],
         [0, 0, 1, 0]]

array = np.array(array)
print(solution(array, 3).get('rotated'))
print(solution(array, 3).get('flipped'))
print(solution(array, 3).get('rolled'))
print(solution(array, 3).get('noised'))


