from datetime import *


def file_reader(filename="txt.txt"):
    s = open(filename, encoding='utf-8').read().strip().splitlines()
    return s


def get_time(str_time):
    hour, min = map(int, str_time.split(':'))
    return timedelta(hours=hour, minutes=min)


def get_delta_time(t1, t2):
    delta = timedelta(hours=4, minutes=00)
    duration = t2 - t1
    return duration if duration > delta else None


def main():
    data = file_reader()
    for user in data:
        fio, t1, t2 = user.split(', ')
        t1 = get_time(t1)
        t2 = get_time(t2)

        if get_delta_time(t1, t2):
            print_to_file(fio, get_delta_time(t1, t2))


main()
