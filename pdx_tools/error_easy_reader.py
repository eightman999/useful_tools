import re

def EERer( PATH, mode):
    if not PATH.endswith("error.log"):
        if mode == 0:
            raise ValueError("Invalid file name")
        elif mode == -1 and not PATH.endswith(".log"):
            raise ValueError("Invalid file type")
        elif mode == 1:
            pass
        else:
            raise ValueError("Invalid mode")

    with open(PATH, 'r') as file:
        content = file.read()

    # Remove [no_game_date] and [HH:MM:SS] patterns
    content = re.sub(r'\[no_game_date\]', '', content)
    content = re.sub(r'\[\d{2}:\d{2}:\d{2}\]', '', content)
    content = re.sub(r'\[\d{4}.\d{2}.\d{2}.\d{2}\]', '', content)
    with open(PATH, 'w') as file:
        file.write(content)


