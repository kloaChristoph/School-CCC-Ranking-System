

def convert_to_seconds(time):
    return time[0] * 3600 + time[1] * 60 + time[2]


def main(input):
    start_time = input.split(" ")[0]
    start_time = [int(x) for x in start_time.split(":")]

    end_time = input.split(" ")[1]
    end_time = [int(x) for x in end_time.split(":")]

    start_second = convert_to_seconds(start_time)
    end_second = convert_to_seconds(end_time)

    print(end_second - start_second)


if __name__ == '__main__':
    main("18:30:39 20:55:42")
    main("02:44:58 19:08:55")
    main("22:26:11 22:47:04")
    main("14:42:35 16:12:11")
    main("05:49:56 20:29:11")
    main("09:17:24 16:34:51")
