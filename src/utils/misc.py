import re


def validate_gamename_and_tagline(input_string):
    """
    Validate the input string for the game name and tagline rules.

    Rules:
    - Game names: 3-16 Unicode characters, no `#`.
    - Separator: `-` between game name and tagline.
    - Tagline: 3-5 alphanumeric characters (supports Unicode letters).

    :param input_string: str, input string to validate
    :return: bool, True if valid, False otherwise
    """
    pattern = r"^(?P<game_name>[^#]{3,16})#(?P<tagline>[\w]{3,5})$"
    match = re.match(pattern, input_string)
    return bool(match)
