"""
853. Car Fleet
-------------------------------
Difficulty: Medium

There are n cars going to the same destination along a one-lane road.
The destination is target miles away.

You are given two integer arrays: position and speed, both of length n,
where position[i] is the position of the ith car
and speed[i] is the speed of the ith car (in miles per hour).

A car can never pass another car ahead of it,
but it can catch up to it and drive bumper to bumper at the same speed.
The faster car will slow down to match the slower car's speed.
The distance between these two cars is ignored
(i.e., they are assumed to have the same position).

A car fleet is some non-empty set of cars driving at the same position and same
speed. Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point,
 it will still be considered as one car fleet.

Return the number of car fleets that will arrive at the destination.
"""


def car_fleet(target: int, positions: list[int], speeds: list[int]) -> int:
    cars = sorted(zip(positions, speeds), reverse=True)
    time_to_reach_target = [0] * len(positions)
    for i, (position, speed) in enumerate(cars):
        time_to_reach_target[i] = (target - position) / speed

    for i in range(1, len(time_to_reach_target)):
        if time_to_reach_target[i] <= time_to_reach_target[i - 1]:  # Same fleet
            time_to_reach_target[i] = time_to_reach_target[i - 1]

    fleets = 1
    for i in range(1, len(time_to_reach_target)):
        if time_to_reach_target[i] != time_to_reach_target[i - 1]:
            fleets += 1

    return fleets


def test_car_fleet():
    assert car_fleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]) == 3
    assert car_fleet(10, [3], [3]) == 1
    assert car_fleet(100, [0, 2, 4], [4, 2, 1]) == 1


if __name__ == '__main__':
    test_car_fleet()