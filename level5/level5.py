

def convert_to_seconds(time):
    return time[0] * 3600 + time[1] * 60 + time[2]

def main(input: str):
    start_time = input.split(" ")[0]
    start_time = [int(x) for x in start_time.split(":")]
    start_second = convert_to_seconds(start_time)


    X = input.split(" ")[1]
    entries = input.split(" ")[3:]


    task_stats: dict[int,dict] = {}
    users: dict = {}
    users_with_wrong_answers = []

    while entries:
        uid, time, status, task_id = entries[:4]

        if not task_id in task_stats:
            task_stats.update({ task_id:{} })

        if status == 'correct':

            submission_time = [int(x) for x in time.split(":")]
            submission_second = convert_to_seconds(submission_time)
            needed_time = submission_second - start_second

            task_stats[task_id].update({needed_time: [uid, time, task_id]})

        elif status == 'wrong':
            users_with_wrong_answers.append(uid)

        entries = entries[4:]
    
    for task_id in task_stats:
        task_stats[task_id] = dict(sorted(task_stats[task_id].items()))

    for task_winners in task_stats.values():
        x = int(X)
        for winner in task_winners.values():
            if not winner[0] in users:
                users.update({winner[0]: 0})
            users[winner[0]] += x 
            x -= 1

    points_dict: dict[int, list] = {}
    for user in users_with_wrong_answers:
        if user in users:
            users.pop(user)
    users_with_wrong_answers.sort()

    for user in users.items():
        points = user[1]
        if not points in points_dict:
            points_dict.update({points: []})
        points_dict[points].append(user)

    for point in points_dict:
        points_dict[point] = sorted(points_dict[point])

    points_dict = dict(sorted(points_dict.items(), reverse=True))

    solution = ""
    for point in points_dict.values():
        for user in point:
            solution += f"{user[1]} {user[0]} "
        
    for user in users_with_wrong_answers:
        solution += f"0 {user} "

    print(solution)
    print("\n")


if __name__ == '__main__':
    main("07:41:57 420 103 103 12:19:54 wrong 10 184 15:46:58 wrong 7 131 10:45:10 correct 1 129 23:20:45 wrong 7 114 10:41:16 correct 6 171 08:30:35 wrong 6 128 20:58:29 correct 9 115 21:36:56 wrong 0 186 13:17:05 correct 7 149 11:06:18 correct 7 136 08:51:55 wrong 8 191 18:50:06 correct 3 170 15:31:24 correct 10 115 12:26:12 wrong 3 166 20:42:29 wrong 9 119 13:51:25 wrong 6 187 23:40:21 wrong 1 159 12:19:54 correct 5 117 23:58:49 wrong 5 174 23:13:04 correct 8 182 21:37:02 wrong 4 185 17:03:13 correct 0 145 16:09:20 correct 7 130 10:42:45 correct 9 142 15:39:57 wrong 4 169 16:27:04 wrong 2 130 09:49:25 wrong 1 140 19:47:07 correct 3 184 16:50:59 wrong 3 140 23:10:20 correct 4 155 10:29:29 wrong 1 157 08:10:16 correct 10 126 13:17:07 correct 8 177 21:19:25 wrong 10 187 20:03:14 wrong 7 134 21:02:37 wrong 10 114 22:05:23 correct 3 200 07:47:54 wrong 4 193 22:43:58 correct 5 119 18:37:56 wrong 6 191 22:37:56 wrong 2 172 08:55:05 correct 5 172 12:52:01 correct 0 110 14:18:32 wrong 5 101 08:43:12 correct 6 118 09:33:05 correct 9 126 09:34:03 wrong 7 128 21:41:22 correct 3 192 13:55:13 wrong 2 135 11:09:21 correct 6 122 20:32:05 correct 0 163 22:34:13 correct 10 115 14:24:49 correct 3 108 14:34:52 correct 0 185 09:31:04 wrong 9 198 17:01:32 correct 3 178 13:19:22 correct 7 112 13:46:23 correct 7 177 14:06:42 correct 5 193 14:51:47 correct 1 144 18:13:46 wrong 9 105 13:45:43 correct 1 146 11:10:58 wrong 10 196 21:22:01 correct 4 115 16:25:18 correct 2 173 14:21:24 correct 10 143 12:10:00 correct 4 175 10:01:42 wrong 2 153 08:44:26 wrong 3 161 11:48:28 correct 2 161 09:30:58 wrong 7 198 22:11:26 wrong 1 144 21:08:20 correct 9 112 09:46:10 wrong 9 134 16:45:38 correct 3 135 08:59:29 correct 1 130 21:42:25 correct 0 176 13:14:37 wrong 1 114 15:22:30 correct 9 154 17:05:28 wrong 10 160 21:31:16 correct 0 193 07:42:09 correct 2 110 12:51:36 correct 2 105 21:49:49 wrong 2 172 12:01:23 correct 10 149 20:26:12 wrong 6 108 08:41:34 wrong 4 189 22:35:22 correct 9 156 13:45:38 correct 5 141 13:53:11 correct 7 103 17:48:52 correct 9 139 21:44:14 wrong 4 164 15:21:57 wrong 0 107 22:08:23 correct 1 140 14:47:45 wrong 4 147 10:47:27 correct 1 138 12:47:05 wrong 4 155 07:49:14 wrong 4 129 16:55:03 correct 2 152 12:01:40 correct 6 156 12:27:20 wrong 7 145 18:41:12 wrong 0 196 11:47:03 wrong 4")
