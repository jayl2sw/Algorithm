def solution(records):
    users = {}
    result = []
    answer =[]
    for record in records:
        action, *user = record.split()
        if action == 'Enter':
            users[user[0]] = user[1]
            result.append((action, user[0]))
        elif action == 'Leave':
            result.append((action, user[0]))
        else:
            users[user[0]] = user[1]

    for r in result:
        action, user_id = r[0], r[1]
        if action == 'Enter':
            answer.append(f"{users[user_id]}님이 들어왔습니다.")
        elif action == 'Leave':
            answer.append(f"{users[user_id]}님이 나갔습니다.")

    return answer

records = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(records))