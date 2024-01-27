def study_schedule(permanence_period, target_time):
    if not isinstance(target_time, int):
        return None

    count = 0

    for i in permanence_period:
        if not isinstance(i[0], int) or not isinstance(i[1], int):
            return None

        if i[0] <= target_time <= i[1]:
            count += 1

    return count
