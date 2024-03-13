# bounce.py
#
# Exercise 1.5
# height = 100
# for i in range(10):
#     height = 3 * height/5
#     print(height)


def calculate_bounce_height(initial_height: float, bounce_factor: float,
                            num_bounces: int) -> list:
    """
    Calculate the height of the ball after each bounce.

    Args:
        initial_height (float): The initial height of the ball in meters.
        bounce_factor (float): The factor by which the ball's height reduces after each bounce.
        num_bounces (int): The number of bounces to calculate.

    Returns:
        list: A list containing the height of the ball after each bounce.
    """
    heights = []
    for _ in range(num_bounces):
        initial_height = bounce_factor * initial_height
        heights.append(initial_height)
    return heights


def main():
    initial_height = 100.0
    bounce_factor = 0.6
    num_bounces = 10

    print(calculate_bounce_height(initial_height, bounce_factor, num_bounces))


if __name__ == "__main__":
    main()
