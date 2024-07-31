def parse_input(user_input):
    """
    Parse user input into command and arguments.

    Args:
    - user_input (str): Input string containing command and optional arguments.

    Returns:
    - tuple: A tuple containing the command (str) and arguments (list).
    """
    
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args