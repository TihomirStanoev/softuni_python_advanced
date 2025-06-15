def draw_cards(*args,**kwargs):
    result = []
    cards = kwargs

    for card, spell in args:
        if card not in cards.keys():
            cards[card] = spell

    monsters = sorted({k:v for k,v in cards.items() if v == 'monster'}.items(), key=lambda k: k[0], reverse=True)
    spells = sorted({k:v for k,v in cards.items() if v == 'spell'}.items(), key=lambda k: k[0])

    if monsters:
        result.append('Monster cards:')
        for monster, _ in monsters:
            result.append(f'  ***{monster}')

    if spells:
        result.append('Spell cards:')
        for spell, _ in spells:
            result.append(f'  $$${spell}')

    return '\n'.join(result)


print(draw_cards(("brave attack", "spell"), ("freeze", "spell"), lightning_bolt="spell", fireball="spell",))