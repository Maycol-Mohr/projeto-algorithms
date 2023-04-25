period = [('2', 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]


def study_schedule(permanence_period, target_time):
    if target_time is None or target_time == '':
        return None

    quantity = 0

    for start, end in permanence_period:
        if type(start) != int or type(end) != int:
            return None

        if start <= target_time and end >= target_time:
            quantity = quantity + 1

    return quantity


print(study_schedule(period, 2))
