from setup import knights, items


def board_state():

    board = [[' ',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' ',' ']]

    for item in items:
        if item.holder is None:
            board[item.position[0]][item.position[1]] = item.code

    for knight in knights:
        if knight.status == 'ALIVE':
            board[knight.position[0]][knight.position[1]] = knight.code

    for line in board:
        print('|'.join(line))


def game_state():

    game_state = {}

    for knight in knights:
        if knight.item is None:
            game_state[knight.name] = [knight.position,
                                    knight.status,
                                    None,
                                    knight.attack,
                                    knight.defence]
        else:
            game_state[knight.name] = [knight.position,
                                    knight.status,
                                    knight.item.name,
                                    knight.attack + knight.item.attack,
                                    knight.defence + knight.item.defence]

    for item in items:
        holder = item.holder
        if holder is None:
            item.holder = 'No'
        else:
            item.holder = 'Yes'
        game_state[item.name] = [item.position,
                                item.holder]

    print('{')
    for key, value in game_state.items():
        print(f'"{key}":', value)
    print('}')
