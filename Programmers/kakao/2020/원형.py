from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)  # 원형좌표를 1자로 늘렸습니다.

    answer = len(dist) + 1

    for start in range(length):  # length개의 좌표중 몇번째 부터 시작할 지
        for workers in list(permutations(dist, len(dist))):  # permutation 통해 일꾼 순서 결정
            idx = 0
            position = weak[start] + workers[idx]  # 시작점부터 idx 번째 worker가 커버할 수 있는 범위까지 이동
            for index in range(start, start + length): # 출발부터 length개 까지 중에
                if position < weak[index]:  # position이 weak 보다 작으면 아직 다 수리하지 않았음을 의미
                    idx += 1                # idx += 1하고
                    if idx + 1 > len(dist):   # 만약 인원수보다 idx + 1이 크면 불가능하므로
                        break   #멈춤
                    position = weak[index] + workers[idx] # 수리되지 않은 index부터  idx번째 worker가 커버할 수 있는 범위까지 이동
            answer = min(answer, idx+1)  # 답이랑 인원수 중 작은것으로 갱신
    if answer > len(dist):
        return -1

    return answer
solution(12, [1, 5, 6, 10], [1, 2, 3, 4])