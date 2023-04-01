

def convert_to_seconds(time):
    return time[0] * 3600 + time[1] * 60 + time[2]

def main(input: str):
    start_time = input.split(" ")[0]
    start_time = [int(x) for x in start_time.split(":")]
    start_second = convert_to_seconds(start_time)

    entries = input.split(" ")[2:]

    submissions = {}
    while entries:
        uid, time, status = entries[:3]

        if status == 'correct':
            submission_time = [int(x) for x in time.split(":")]
            submission_second = convert_to_seconds(submission_time)
            needed_time = submission_second - start_second

            submissions.update({needed_time: [uid, time]})

        entries = entries[3:]

    fastest_time = min(submissions.keys())
    winner = submissions.get(fastest_time)
    print(winner[0], winner[1])

if __name__ == '__main__':
    main("00:59:22 24 656 06:24:33 correct 798 05:37:06 wrong 26 01:01:52 correct 202 17:02:50 wrong 8 04:31:10 wrong 397 04:40:04 correct 134 12:26:33 correct 312 06:52:25 correct 728 03:18:44 correct 895 01:05:06 correct 575 12:37:41 wrong 727 21:36:54 correct 371 11:45:19 correct 314 19:32:39 wrong 785 18:51:27 correct 845 08:35:08 wrong 549 04:25:28 correct 697 21:06:15 correct 385 04:35:47 wrong 618 06:12:13 correct 656 09:16:48 correct 964 16:53:33 wrong 901 05:19:55 correct 227 20:25:07 correct")
    main("02:56:52 78 718 18:44:49 wrong 838 23:13:52 correct 641 13:56:56 correct 803 09:18:23 wrong 524 20:44:47 wrong 996 11:41:31 correct 499 05:05:23 correct 74 11:14:44 wrong 214 06:36:33 wrong 973 04:54:20 wrong 496 09:33:13 correct 96 11:44:22 wrong 257 22:20:48 correct 917 20:14:26 wrong 359 12:20:09 wrong 748 04:42:33 correct 98 08:24:59 correct 559 11:28:49 wrong 464 03:17:01 wrong 754 05:48:01 correct 761 18:48:23 correct 744 09:12:40 wrong 682 06:31:30 correct 518 19:35:26 correct 581 17:33:26 correct 672 04:59:29 wrong 450 12:53:59 correct 284 23:12:49 correct 529 09:38:58 wrong 444 15:21:57 wrong 155 03:32:56 correct 623 06:10:22 wrong 243 14:18:53 wrong 831 16:55:26 wrong 386 05:01:12 correct 916 21:44:29 correct 294 12:45:59 correct 950 06:15:34 wrong 31 05:03:17 correct 57 14:38:36 correct 984 13:52:12 wrong 415 16:34:41 correct 437 09:12:35 wrong 701 14:55:25 correct 217 16:32:16 wrong 253 16:46:49 wrong 552 15:54:13 correct 469 22:49:00 wrong 180 10:29:53 wrong 21 07:03:29 correct 564 17:57:21 wrong 982 03:34:36 correct 320 05:44:33 correct 394 06:16:11 wrong 357 09:19:18 wrong 781 21:46:57 wrong 98 21:21:15 correct 604 07:34:05 wrong 233 13:42:38 correct 284 21:16:48 correct 727 05:12:34 wrong 188 18:35:48 correct 518 04:12:42 correct 79 13:17:07 wrong 304 18:48:49 correct 563 20:21:20 correct 990 15:33:00 correct 24 04:18:34 wrong 732 05:50:18 correct 637 11:25:33 correct 239 09:40:11 correct 908 07:51:12 wrong 684 11:36:46 correct 155 04:04:13 correct 717 10:50:57 correct 312 03:36:05 correct 594 09:03:58 wrong 310 11:17:52 wrong")
    main("17:20:20 36 802 19:35:37 correct 427 19:51:46 correct 650 19:30:09 correct 403 22:20:48 wrong 28 20:57:45 correct 56 19:56:09 wrong 574 21:49:47 wrong 274 20:59:11 correct 350 23:37:55 correct 316 23:34:41 wrong 125 20:23:50 correct 24 18:54:51 wrong 341 20:53:28 correct 765 22:32:00 wrong 79 20:07:37 wrong 458 17:44:29 correct 522 23:32:16 wrong 554 22:32:58 correct 152 17:23:27 correct 482 21:11:33 correct 652 17:23:03 wrong 292 19:53:17 wrong 132 19:53:00 correct 326 19:17:53 wrong 525 20:57:37 wrong 390 23:13:50 wrong 63 22:14:40 wrong 597 19:58:23 wrong 666 22:27:11 wrong 819 20:11:49 wrong 316 23:33:14 wrong 496 17:29:18 correct 16 23:27:52 wrong 40 19:20:50 wrong 114 19:17:16 correct 833 20:56:02 wrong")
    main("10:55:29 81 126 15:21:50 correct 562 15:06:57 wrong 491 16:12:57 correct 638 11:49:50 wrong 474 23:51:18 wrong 385 18:23:39 wrong 730 23:55:27 correct 693 21:29:43 wrong 516 20:06:35 correct 770 22:56:32 wrong 977 21:50:18 wrong 286 11:37:18 wrong 680 18:43:16 correct 147 17:46:33 wrong 788 13:12:57 correct 555 23:26:12 wrong 256 13:08:38 wrong 327 14:32:20 wrong 987 13:33:09 correct 263 11:04:17 wrong 281 11:57:07 wrong 122 16:02:41 wrong 458 19:05:40 wrong 922 11:29:54 wrong 370 22:41:56 correct 687 11:39:07 correct 660 23:34:58 correct 536 15:27:34 correct 104 16:59:43 correct 955 18:21:57 correct 959 17:06:25 wrong 455 12:36:10 wrong 552 12:15:45 wrong 912 14:50:39 wrong 742 13:27:58 correct 270 23:09:37 correct 81 22:20:44 wrong 534 14:08:59 wrong 193 19:12:58 correct 736 13:59:01 correct 763 22:24:54 correct 242 11:20:17 wrong 327 17:57:48 correct 297 21:17:27 wrong 476 21:38:26 correct 968 21:40:23 wrong 842 11:51:56 correct 744 19:31:53 correct 301 22:03:48 correct 944 23:44:47 correct 758 17:41:17 correct 877 15:58:45 correct 183 15:32:42 correct 113 16:02:46 correct 491 22:44:25 wrong 214 22:54:16 wrong 742 18:03:36 correct 303 12:06:25 correct 789 14:26:41 correct 0 21:57:28 wrong 537 21:39:04 correct 36 22:44:33 correct 298 13:16:35 wrong 75 16:05:36 wrong 450 14:33:33 wrong 519 18:39:20 wrong 176 17:48:29 wrong 375 15:25:32 correct 793 20:00:23 correct 146 19:15:01 wrong 466 15:40:00 wrong 234 21:11:31 wrong 533 20:12:38 correct 214 10:57:59 wrong 63 22:58:49 correct 751 19:09:31 wrong 179 17:12:22 correct 969 12:31:00 correct 995 14:46:47 correct 395 17:21:30 correct 991 16:41:21 correct")
    main("01:38:03 62 493 11:28:25 correct 300 09:21:33 wrong 483 15:20:57 wrong 500 17:14:34 correct 44 21:39:53 wrong 346 06:59:38 correct 372 18:30:06 wrong 428 12:37:39 correct 246 13:56:17 correct 419 14:57:52 correct 289 06:03:46 wrong 560 23:01:59 correct 273 04:52:02 correct 308 15:08:09 wrong 793 20:07:26 wrong 609 21:00:48 correct 832 10:28:14 correct 668 23:33:17 wrong 285 07:15:48 correct 765 15:19:34 correct 763 21:28:14 correct 840 02:23:36 wrong 739 11:22:34 wrong 253 10:02:02 correct 979 16:42:07 correct 166 21:40:17 wrong 630 16:27:19 wrong 867 21:15:07 correct 950 09:19:54 correct 198 17:29:27 wrong 645 15:47:56 correct 387 13:35:28 wrong 490 15:50:28 correct 239 02:58:06 correct 844 06:57:11 wrong 147 18:36:27 correct 225 03:39:36 correct 43 08:24:29 wrong 415 15:15:19 wrong 51 13:37:05 correct 411 08:39:58 wrong 996 23:02:41 wrong 899 18:12:34 correct 431 22:30:34 wrong 689 04:08:12 correct 93 10:51:30 correct 455 12:00:08 correct 668 08:39:41 correct 528 14:04:40 correct 905 20:50:39 correct 598 13:20:28 wrong 254 20:10:48 wrong 736 23:07:39 correct 9 22:49:36 wrong 367 10:17:23 correct 413 08:45:13 correct 547 17:27:27 correct 777 02:07:39 correct 485 15:21:14 correct 131 18:25:29 wrong 827 21:23:52 correct 512 07:10:02 wrong")
    main("05:12:14 66 390 15:58:46 correct 727 23:48:39 correct 131 21:40:23 correct 476 21:52:37 correct 356 07:43:38 wrong 487 13:46:19 wrong 338 18:23:07 correct 101 17:59:03 wrong 694 21:22:14 wrong 381 16:46:51 wrong 601 16:44:47 wrong 59 08:28:15 correct 900 12:58:30 correct 812 12:31:49 wrong 454 12:30:26 wrong 779 08:32:33 wrong 914 13:01:05 wrong 122 13:36:51 correct 932 15:15:11 wrong 217 20:03:33 correct 879 16:45:00 correct 707 11:27:10 correct 889 09:27:17 correct 98 08:26:39 wrong 520 13:14:35 wrong 764 10:01:24 correct 820 12:23:05 correct 941 06:07:01 correct 757 17:07:17 correct 682 18:41:44 wrong 504 10:32:44 correct 28 23:15:47 correct 136 21:28:50 correct 240 12:08:53 wrong 264 10:07:14 wrong 633 21:41:49 wrong 486 22:06:22 correct 358 05:22:51 correct 96 12:16:48 correct 220 11:00:02 correct 898 21:06:07 correct 593 22:44:04 wrong 88 13:22:25 correct 638 17:05:20 wrong 574 23:30:22 wrong 929 12:48:19 wrong 309 14:56:16 correct 602 19:05:17 correct 224 07:36:08 correct 32 11:14:05 wrong 994 06:32:40 correct 95 18:21:56 wrong 588 22:51:32 correct 88 18:30:32 wrong 644 10:22:53 correct 672 16:12:32 wrong 250 11:03:28 correct 708 19:17:10 wrong 779 18:12:06 correct 539 09:43:49 correct 28 07:53:25 correct 477 11:01:17 correct 288 22:50:02 wrong 139 08:41:00 correct 758 11:33:01 correct 268 15:40:09 wrong")
    main("13:17:04 33 874 17:57:14 correct 581 15:13:52 wrong 182 13:46:55 correct 754 22:36:55 correct 502 15:53:19 wrong 155 20:16:15 correct 928 15:59:30 wrong 940 15:43:00 correct 969 16:53:21 wrong 916 14:49:06 wrong 969 23:56:27 correct 989 19:31:27 wrong 187 19:16:24 correct 670 19:11:34 correct 331 19:26:44 correct 253 23:29:21 correct 594 21:02:02 correct 342 22:07:00 wrong 301 21:33:05 correct 256 20:21:20 wrong 254 17:16:13 wrong 732 14:09:12 wrong 146 17:26:47 wrong 861 16:04:14 correct 490 14:42:46 correct 785 14:38:53 wrong 359 19:27:29 wrong 482 22:21:23 correct 272 23:18:42 correct 648 14:26:38 wrong 173 20:25:50 correct 777 19:01:43 correct 78 15:05:55 wrong")

