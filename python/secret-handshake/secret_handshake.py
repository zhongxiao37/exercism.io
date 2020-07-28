COMMANDS = {
    'wink': 1,
    'double blink': 2,
    'close your eyes': 4,
    'jump': 8
}

def commands(number):
    commands = [k for k, v in COMMANDS.items() if v & number]
    return commands[::-1] if number & 16 else commands

def secret_code(actions):
    binary_list = [COMMANDS[act] for act in actions]
    return sum(binary_list) if binary_list[0] <= binary_list[-1] else 16 + sum(binary_list)

