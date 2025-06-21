def sort_games(*args,**kwargs):
    console_games = {}
    pc_games = {}
    result = []

    for platform, game in args:
        if game in kwargs.values():
            for rel_id, name in kwargs.items():
                if game == name:
                    if platform == 'console':
                        console_games[rel_id] = game
                    elif platform == 'pc':
                        pc_games[rel_id] = game



    if console_games:
        sorted_console_games = sorted(console_games.items(), key=lambda rg: rg[0])
        result.append('Console Games:')
        for date, game in sorted_console_games:
            result.append(f'>>>{date[:-4]}: {game}')

    if pc_games:
        sorted_pc_games = sorted(pc_games.items(), key=lambda rg: rg[0], reverse=True)
        result.append('PC Games:')
        for date, game in sorted_pc_games:
            result.append(f'<<<{date[:-4]}: {game}')


    return '\n'.join(result)




print(sort_games(
    ("pc", "Iron Comet"),
    ("pc", "Neon Skyline"),
    ("pc", "Sky Frontier"),
    April_12_2025_002="Neon Skyline",
    April_12_2025_005="Iron Comet",
    February_14_2025_009="Sky Frontier",
))