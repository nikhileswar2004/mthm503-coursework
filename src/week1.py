
def try_points(tries):
    """
    Calculate the number of points scored from tries.
    Each try is worth 5 points.
    """
    return tries * 5


def conversion_points(conversions):
    """
    Calculate the number of points scored from conversions.
    Each successful conversion is worth 2 points.
    """
    return conversions * 2


def penalty_points(penalties):
    """
    Calculate the number of points scored from penalties.
    Each penalty goal is worth 3 points.
    """
    return penalties * 3


def drop_goal_points(drop_goals):
    """
    Calculate the number of points scored from drop goals.
    Each drop goal is worth 3 points.
    """
    return drop_goals * 3


def total_score(tries, conversions, penalties, drop_goals):
    """
    Calculate the total score for a rugby team.
    """
    return (
        try_points(tries)
        + conversion_points(conversions)
        + penalty_points(penalties)
        + drop_goal_points(drop_goals)
    )


def is_valid_conversion_count(tries, conversions):
    """
    Determine whether a conversion count is valid.
    """
    return conversions <= tries


def result_message(team_name, score):
    """
    Create a message describing a team's score.
    """
    return f"{team_name} scored {score} points."
