

def convert_to_seconds(time):
    return time[0] * 3600 + time[1] * 60 + time[2]

def main(input: str):
    start_time = input.split(" ")[0]
    start_time = [int(x) for x in start_time.split(":")]
    start_second = convert_to_seconds(start_time)

    wanted_task_id = input.split(" ")[1]
    entries = input.split(" ")[3:]


    submissions = {}
    while entries:
        uid, time, status, task_id = entries[:4]

        if status == 'correct' and task_id == wanted_task_id:
            submission_time = [int(x) for x in time.split(":")]
            submission_second = convert_to_seconds(submission_time)
            needed_time = submission_second - start_second

            submissions.update({needed_time: [uid, time]})

        entries = entries[4:]

    sorted_winners = dict(sorted(submissions.items()))

    solution = f"{len(sorted_winners)} "
    for winner in sorted_winners.values():
        solution += f"{winner[0]} {winner[1]} "

    print(solution)
    print("\n")

if __name__ == '__main__':
    main("15:12:41 9 94 186 22:34:27 wrong 9 144 18:10:32 correct 10 145 22:30:01 wrong 5 145 21:02:44 wrong 0 100 15:15:51 wrong 8 130 22:41:37 correct 4 182 16:16:56 correct 5 182 20:41:47 correct 6 106 23:08:39 correct 2 166 21:24:23 wrong 4 189 19:01:25 wrong 7 104 18:40:49 wrong 3 200 22:42:58 correct 10 170 17:46:49 correct 6 110 16:11:02 wrong 4 109 18:45:41 wrong 8 115 23:50:53 wrong 7 198 16:33:39 wrong 4 153 19:10:55 correct 6 160 21:18:11 wrong 5 122 16:40:32 correct 5 194 23:10:57 correct 2 175 22:06:34 correct 0 111 15:34:43 correct 5 131 17:57:54 correct 1 198 20:57:51 correct 4 182 18:39:30 correct 1 148 20:03:50 correct 9 151 23:06:38 correct 7 140 21:55:26 wrong 2 197 17:22:10 correct 5 111 15:20:05 correct 9 143 18:02:44 correct 8 145 15:22:55 correct 3 149 18:39:32 correct 10 152 16:36:02 wrong 3 170 16:32:24 correct 4 108 18:18:01 correct 6 193 20:03:42 wrong 10 132 16:07:37 wrong 9 187 16:45:42 wrong 6 129 23:34:49 wrong 5 105 16:35:36 wrong 6 118 16:28:29 wrong 1 184 20:44:32 wrong 2 127 23:19:33 wrong 1 139 16:09:58 wrong 6 129 15:50:25 wrong 4 136 17:21:00 correct 2 127 16:46:31 correct 9 160 17:44:01 wrong 7 141 17:07:00 correct 1 153 22:50:39 wrong 1 133 19:32:22 correct 8 123 20:10:00 wrong 3 105 22:04:07 wrong 3 125 17:29:45 wrong 9 177 23:28:35 correct 1 118 22:35:15 wrong 2 160 15:45:17 correct 6 138 16:06:32 wrong 8 180 20:05:12 correct 0 145 15:18:58 wrong 8 199 19:31:33 correct 10 181 16:09:45 correct 8 199 16:25:06 wrong 10 146 16:14:03 wrong 8 109 15:21:33 wrong 0 143 18:09:05 correct 2 188 16:28:43 correct 7 136 20:05:55 correct 0 166 23:50:30 wrong 7 126 19:21:23 correct 2 176 21:03:43 correct 4 188 19:58:15 correct 1 133 19:51:53 wrong 10 108 23:29:21 correct 7 173 16:48:43 correct 8 104 23:41:31 wrong 7 118 18:05:10 correct 0 102 20:27:51 correct 3 119 16:07:44 wrong 7 182 16:09:41 correct 10 105 15:47:48 wrong 1 195 23:12:00 correct 0 178 16:42:15 wrong 5 107 22:45:15 wrong 7 109 20:13:16 correct 0 140 19:03:07 wrong 0 157 20:05:21 wrong 4 129 22:19:33 wrong 5 119 19:56:05 wrong 0 144 20:38:43 wrong 6 187 15:43:56 wrong 5")
    main("21:20:33 9 46 142 21:49:42 correct 4 141 22:37:17 wrong 6 163 22:14:52 wrong 4 133 23:00:33 wrong 7 152 23:24:01 correct 1 193 21:39:31 wrong 9 166 23:09:31 correct 8 160 23:53:04 wrong 9 180 21:39:19 wrong 0 101 23:38:54 wrong 3 200 22:47:14 wrong 0 143 21:44:05 wrong 6 165 22:23:10 correct 2 159 22:12:44 wrong 4 108 21:54:05 correct 0 142 23:27:30 wrong 5 122 22:45:43 correct 3 133 21:43:18 wrong 8 121 21:30:11 correct 9 120 22:38:23 wrong 0 188 22:36:35 wrong 6 119 21:40:24 correct 4 130 21:56:34 wrong 0 123 22:52:20 wrong 8 151 22:21:07 wrong 8 159 21:26:31 wrong 8 110 21:27:56 correct 2 169 23:29:21 correct 7 150 22:30:46 wrong 2 179 21:22:47 correct 9 122 23:48:08 wrong 6 128 23:03:50 correct 4 161 21:28:37 wrong 5 133 22:39:32 wrong 7 162 23:58:12 correct 2 154 22:01:19 correct 10 116 23:04:07 correct 8 107 21:23:30 correct 0 177 21:47:23 correct 10 147 21:43:30 correct 2 154 22:41:44 wrong 1 110 22:13:07 wrong 4 157 23:15:42 wrong 7 158 22:51:28 wrong 8 163 21:29:41 correct 3 141 22:56:36 correct 3")
    main("18:33:16 4 57 172 23:11:12 correct 4 173 18:59:53 wrong 10 107 18:42:13 wrong 10 128 23:41:10 correct 4 159 23:19:26 wrong 3 159 20:26:57 wrong 3 181 23:50:04 correct 8 104 22:07:11 wrong 9 145 19:44:53 wrong 6 173 21:49:51 wrong 5 132 22:52:31 correct 9 131 20:32:32 wrong 9 175 21:15:57 wrong 6 183 23:01:00 correct 0 155 21:39:46 correct 1 141 21:46:28 wrong 10 105 21:09:11 wrong 3 185 18:50:44 wrong 9 198 23:54:27 wrong 5 116 22:13:11 wrong 0 146 23:18:50 correct 9 158 23:47:18 correct 7 118 18:47:21 correct 0 193 23:33:53 wrong 2 163 22:04:24 wrong 2 153 18:52:57 wrong 7 125 22:12:54 correct 9 130 20:56:30 correct 8 142 22:41:22 correct 1 117 19:57:35 correct 8 143 22:42:19 wrong 1 109 23:57:47 wrong 6 177 23:51:39 wrong 8 114 22:35:39 correct 7 111 23:58:05 correct 3 156 18:49:47 wrong 9 136 20:55:14 wrong 1 157 19:47:07 wrong 0 142 21:59:25 correct 4 151 21:08:59 correct 8 199 23:03:20 wrong 3 200 19:55:41 correct 4 109 18:51:11 wrong 5 128 23:09:14 wrong 9 153 22:42:06 wrong 0 146 19:59:53 wrong 3 134 22:40:55 wrong 0 141 19:13:19 correct 9 167 19:54:00 wrong 6 121 18:33:55 wrong 7 113 21:48:06 wrong 5 175 23:13:58 wrong 9 124 22:58:54 correct 8 162 23:26:33 wrong 3 124 23:42:42 correct 2 175 23:18:04 wrong 5 105 19:33:17 wrong 2")
    main("08:27:50 7 18 131 17:03:32 correct 4 100 10:09:32 correct 7 110 22:50:03 wrong 0 161 15:41:52 wrong 6 169 09:37:02 wrong 5 118 20:37:58 wrong 10 117 17:22:39 wrong 7 190 14:47:10 correct 2 133 11:01:38 wrong 3 134 22:22:59 correct 6 101 09:51:21 wrong 5 158 14:20:20 correct 4 105 08:29:55 wrong 7 154 13:57:22 wrong 1 111 15:17:40 wrong 5 100 19:26:13 wrong 1 184 12:20:33 correct 5 158 17:49:44 correct 0")
    main("07:58:22 2 75 177 19:13:29 correct 1 134 11:12:19 wrong 4 118 16:59:39 wrong 7 195 21:35:33 wrong 8 171 16:21:38 wrong 9 138 22:59:27 wrong 2 179 17:05:32 correct 4 178 08:04:57 wrong 7 117 13:59:47 correct 10 131 16:36:53 wrong 6 141 08:55:07 wrong 4 106 19:55:48 wrong 1 102 19:24:29 wrong 5 175 21:45:18 correct 8 181 08:05:25 wrong 4 177 15:26:42 wrong 1 178 21:08:21 wrong 4 116 09:03:44 wrong 3 134 15:17:55 correct 3 166 08:24:15 correct 10 131 13:38:25 wrong 8 162 15:54:18 wrong 6 146 21:48:03 correct 0 115 11:54:14 wrong 8 129 13:57:54 correct 3 141 17:57:58 correct 10 166 17:07:35 correct 6 165 12:42:21 correct 4 113 14:34:29 wrong 9 125 10:35:45 correct 2 154 16:06:52 correct 10 193 08:35:42 wrong 3 162 23:13:34 wrong 6 138 16:03:15 wrong 1 110 12:18:08 correct 3 146 21:18:04 wrong 8 183 19:07:10 correct 2 145 08:20:09 correct 3 125 22:41:08 wrong 8 186 19:49:10 correct 4 119 13:05:09 correct 2 181 08:15:25 wrong 9 164 17:04:01 correct 0 118 08:57:11 wrong 2 132 17:30:09 wrong 2 200 10:54:55 correct 7 198 12:11:26 correct 5 194 22:40:32 wrong 9 157 12:17:00 correct 7 148 09:49:17 correct 5 198 22:37:22 wrong 10 137 21:32:13 correct 8 144 21:51:37 correct 5 138 18:30:20 wrong 2 181 13:26:24 correct 4 179 21:47:31 wrong 7 182 11:49:31 wrong 0 128 12:17:52 wrong 8 194 18:13:04 correct 0 152 18:39:01 wrong 1 102 18:54:43 wrong 1 152 17:13:30 correct 8 157 13:14:37 wrong 1 154 23:23:15 correct 7 188 18:18:26 wrong 9 156 16:02:19 correct 3 162 08:58:54 correct 5 171 09:27:42 correct 5 107 16:02:49 correct 7 133 18:45:58 correct 3 118 08:49:42 wrong 2 184 08:30:44 wrong 8 139 17:52:40 wrong 2 130 17:32:04 wrong 9 173 10:20:53 wrong 1")
    main("19:14:40 4 20 113 22:55:32 wrong 3 182 22:07:39 wrong 4 189 23:19:22 correct 2 167 22:26:40 correct 5 141 22:52:52 wrong 0 128 21:18:45 correct 5 124 23:51:07 correct 2 154 22:43:43 wrong 2 182 21:28:15 wrong 7 152 23:19:49 wrong 4 187 22:17:32 correct 3 123 22:05:35 correct 1 129 23:37:50 wrong 5 101 22:29:09 correct 10 118 22:01:39 wrong 4 195 23:37:21 wrong 10 104 23:07:45 correct 10 141 23:39:10 correct 5 142 21:20:00 correct 2 161 21:48:17 wrong 1")
    