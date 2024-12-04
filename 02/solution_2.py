#! /usr/bin/python


def all_sorted(report):
    return report == sorted(report) or report == list(reversed(sorted(report)))


def gradual_change(report):
    prev = report[0]
    for i in report[1:]:
        if not (1 <= abs(i - prev) <= 3):
            return False
        prev = i

    return True


def report_safe(report):
    return all_sorted(report) and gradual_change(report)


safe = 0

with open("input", "r") as fp:
    for line in fp:

        data = [int(i) for i in line.rstrip().split()]

        if report_safe(data):
            safe += 1
        else:
            for i in range(len(data)):
                if report_safe(data[:i] + data[i + 1 :]):
                    safe += 1
                    break


print(safe)
