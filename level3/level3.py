

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

    sorted_winners = dict(sorted(submissions.items()))

    solution = f"{len(sorted_winners)} "
    for winner in sorted_winners.values():
        solution += f"{winner[0]} {winner[1]} "

    print(solution)
    print("\n\n\n")

if __name__ == '__main__':
    main("14:02:08 54 350 20:41:47 wrong 947 15:56:27 wrong 533 21:25:17 wrong 206 22:26:40 wrong 116 21:24:31 wrong 669 19:21:12 wrong 195 14:13:30 wrong 771 18:33:10 wrong 380 17:54:08 wrong 988 17:37:39 correct 37 14:56:38 wrong 412 21:07:34 wrong 137 20:00:44 wrong 877 16:14:26 wrong 470 18:07:21 wrong 974 19:23:26 correct 422 18:45:05 wrong 352 14:45:13 wrong 880 22:17:25 wrong 678 23:19:59 wrong 45 18:28:26 wrong 878 23:22:56 correct 751 14:31:00 correct 530 18:34:09 correct 334 14:22:33 wrong 359 15:25:55 wrong 141 19:27:22 correct 130 23:17:06 wrong 109 18:19:39 wrong 810 22:50:35 wrong 791 19:04:29 wrong 956 22:50:53 correct 547 16:30:36 wrong 818 15:16:45 wrong 330 21:06:21 correct 808 23:58:05 correct 904 22:38:12 correct 409 21:13:47 wrong 697 16:55:21 correct 921 16:49:28 wrong 203 23:01:49 correct 602 21:15:05 wrong 986 22:56:11 correct 850 23:04:01 wrong 38 16:59:10 wrong 882 19:17:47 wrong 970 14:22:24 wrong 15 20:43:48 wrong 298 21:08:07 correct 401 19:39:22 correct 786 17:42:27 correct 405 14:37:20 correct 429 16:57:57 correct 954 15:49:03 wrong")
    main("18:22:47 68 303 18:58:58 correct 479 20:40:05 correct 25 21:38:40 wrong 321 22:24:49 wrong 941 18:41:41 wrong 923 22:39:05 correct 537 19:57:44 wrong 827 22:37:07 correct 591 21:53:35 correct 968 18:40:04 correct 726 22:00:13 wrong 477 23:55:55 correct 473 20:31:25 wrong 106 19:24:29 correct 184 20:51:40 correct 520 23:49:51 correct 640 21:57:05 wrong 500 22:55:36 correct 109 19:19:02 wrong 826 21:28:45 wrong 775 18:36:44 correct 723 20:35:33 correct 820 20:00:25 wrong 505 20:39:38 correct 486 22:35:26 wrong 782 19:55:36 wrong 916 23:24:45 wrong 831 19:55:12 wrong 203 23:55:17 wrong 729 21:25:36 wrong 937 22:38:54 correct 191 18:39:00 wrong 991 22:56:53 wrong 428 20:39:48 correct 238 19:10:37 correct 596 23:35:45 wrong 416 18:50:27 wrong 86 19:28:54 wrong 806 21:11:10 wrong 718 23:31:39 correct 755 19:19:46 wrong 238 20:28:03 wrong 568 22:59:00 correct 140 19:36:12 wrong 884 21:24:33 wrong 998 23:10:58 correct 94 23:43:20 wrong 87 22:03:19 correct 530 23:19:58 wrong 839 21:51:22 wrong 221 23:35:36 correct 477 23:25:34 correct 834 21:01:26 wrong 467 22:26:50 wrong 31 23:37:10 wrong 847 20:48:33 wrong 683 21:29:31 wrong 554 22:05:22 wrong 809 23:46:34 correct 785 19:44:30 wrong 954 23:21:47 correct 195 18:27:25 wrong 275 20:58:10 wrong 116 22:54:59 correct 468 23:02:12 wrong 168 22:21:35 wrong 474 22:40:32 correct 983 22:32:14 wrong")
    main("23:18:26 69 248 23:31:49 wrong 202 23:48:40 correct 455 23:29:02 wrong 926 23:48:36 correct 409 23:22:21 wrong 78 23:54:54 wrong 759 23:57:47 wrong 329 23:48:44 wrong 801 23:35:42 correct 650 23:59:15 correct 699 23:34:47 wrong 17 23:42:33 correct 47 23:47:56 wrong 915 23:59:51 correct 949 23:29:53 correct 346 23:52:42 wrong 993 23:32:13 wrong 362 23:40:35 wrong 570 23:27:25 wrong 182 23:35:41 correct 503 23:48:26 wrong 356 23:59:09 correct 140 23:19:08 correct 916 23:41:16 correct 989 23:28:41 wrong 43 23:22:28 wrong 415 23:21:57 wrong 483 23:44:22 correct 99 23:43:29 wrong 760 23:59:10 correct 463 23:54:07 correct 453 23:50:25 correct 64 23:37:25 wrong 264 23:18:55 wrong 592 23:42:21 correct 637 23:23:12 correct 772 23:37:08 correct 767 23:35:12 wrong 162 23:40:34 correct 97 23:44:15 correct 838 23:37:18 correct 546 23:40:47 correct 279 23:49:56 wrong 89 23:51:08 correct 74 23:28:31 correct 141 23:48:09 wrong 286 23:47:00 wrong 418 23:39:20 wrong 947 23:30:13 correct 465 23:30:02 wrong 938 23:41:21 correct 606 23:48:20 wrong 891 23:48:27 correct 785 23:40:33 correct 968 23:59:23 wrong 436 23:27:51 correct 208 23:35:29 wrong 279 23:18:30 wrong 817 23:47:26 wrong 642 23:42:56 correct 489 23:28:26 wrong 564 23:41:53 correct 418 23:49:32 correct 413 23:47:04 wrong 455 23:26:08 correct 140 23:58:38 wrong 485 23:31:36 wrong 929 23:51:31 correct 922 23:27:58 wrong")
    main("03:45:07 26 80 08:45:22 wrong 368 20:23:25 correct 215 15:45:22 wrong 688 04:23:40 correct 358 23:38:17 wrong 594 13:43:04 wrong 623 09:53:34 correct 924 19:53:39 correct 538 10:28:18 correct 924 06:42:55 wrong 218 19:27:53 wrong 433 09:31:43 correct 819 07:16:49 correct 795 11:15:12 wrong 403 22:17:49 correct 301 19:18:50 wrong 168 12:28:22 wrong 913 18:14:56 correct 882 14:18:07 correct 427 22:20:18 wrong 137 03:52:13 correct 740 14:15:25 wrong 598 13:09:13 wrong 310 23:33:52 wrong 527 21:32:22 wrong 774 16:37:12 correct")
    main("22:32:09 20 982 23:21:29 correct 991 22:33:03 correct 725 22:46:01 correct 236 23:47:41 wrong 162 23:11:59 correct 255 22:47:30 correct 615 22:42:00 wrong 356 22:32:57 correct 952 23:22:12 wrong 540 23:59:40 wrong 283 23:33:05 correct 711 23:47:15 wrong 331 22:56:01 correct 640 23:19:36 wrong 639 23:15:42 correct 353 22:39:40 wrong 491 23:33:14 wrong 887 23:36:07 correct 536 23:12:44 correct 855 23:02:34 wrong")
    main("06:14:02 85 201 18:36:54 wrong 316 16:47:32 wrong 623 19:32:24 correct 706 15:56:47 wrong 86 06:33:59 wrong 737 09:51:19 wrong 690 18:17:22 wrong 16 10:13:32 correct 373 17:48:28 wrong 508 23:55:21 wrong 482 11:36:14 wrong 386 14:05:07 correct 359 17:18:52 wrong 829 06:28:15 correct 10 07:12:15 wrong 586 19:19:42 correct 616 15:00:43 wrong 895 21:46:03 wrong 208 15:49:04 wrong 701 19:37:52 correct 860 07:49:45 wrong 70 19:11:31 correct 411 20:38:21 wrong 639 13:08:18 wrong 553 12:59:45 correct 735 14:28:56 wrong 632 14:17:48 correct 595 13:54:50 correct 408 15:12:34 correct 641 09:30:48 correct 807 18:17:21 correct 661 20:59:40 wrong 791 13:19:35 wrong 612 10:34:09 wrong 425 09:35:11 wrong 343 20:21:02 wrong 754 13:12:48 correct 705 20:58:55 correct 25 23:58:13 wrong 377 07:24:37 correct 953 09:06:53 wrong 545 18:48:56 wrong 220 06:50:11 wrong 921 13:50:01 correct 152 13:06:41 correct 455 10:23:53 wrong 948 14:15:59 wrong 619 19:48:00 wrong 706 17:00:28 wrong 744 09:19:35 wrong 384 20:32:47 correct 276 20:45:30 correct 848 15:42:09 wrong 636 10:19:36 correct 319 06:16:19 correct 851 12:28:38 wrong 302 12:31:47 correct 864 13:58:31 correct 511 09:25:12 correct 706 06:46:37 wrong 596 07:21:19 correct 362 12:14:31 wrong 264 11:43:40 wrong 127 06:25:17 correct 849 15:20:31 wrong 343 15:48:45 correct 960 10:14:03 correct 970 16:27:38 correct 85 14:18:46 wrong 705 12:31:31 wrong 129 07:39:29 correct 68 11:50:21 wrong 124 12:10:42 wrong 437 22:29:31 wrong 313 07:30:36 wrong 125 06:55:13 wrong 267 22:26:38 wrong 770 11:08:09 correct 409 09:13:29 correct 538 11:26:40 wrong 142 22:40:42 correct 192 15:29:07 wrong 152 16:56:09 wrong 419 12:03:48 wrong 436 18:00:20 correct")
    main("21:00:10 33 486 23:41:19 correct 564 22:56:24 wrong 639 22:01:27 wrong 565 22:22:29 wrong 818 22:44:44 wrong 43 23:48:07 wrong 889 22:09:02 wrong 490 22:20:37 wrong 131 22:54:54 wrong 941 21:15:43 correct 659 23:12:12 correct 605 23:15:46 wrong 146 23:03:41 correct 993 21:53:33 correct 499 21:59:11 correct 517 22:26:38 correct 394 22:39:10 correct 452 22:31:46 wrong 675 22:53:08 wrong 966 21:42:19 wrong 917 23:40:23 wrong 171 21:42:34 correct 511 22:04:03 wrong 222 21:38:28 correct 656 23:24:45 correct 371 23:02:02 correct 181 23:52:02 wrong 809 23:43:14 wrong 267 21:20:48 wrong 412 23:37:21 wrong 693 22:15:09 correct 487 22:01:17 correct 480 23:07:07 correct")

