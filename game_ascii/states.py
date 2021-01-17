from setup import knights, items

def game_state():
    game_state = {}
    for knight in knights:
        for item in items:
            if knight.item == item:
                weapon = item
        game_state[knight.name] = [knight.position,
                                knight.status,
                                weapon.name,
                                knight.attack + weapon.attack,
                                knight.defence + weapon.defence]
    for item in items:
        holder = item.holder
        if holder is None:
            item.holder = 'No'
        else:
            item.holder = 'Yes'
            item.position = holder.position

        game_state[item.name] = [item.position,
                                item.holder]
    print('{')
    for key, value in game_state.items():
        print(f'"{key}":', value)
    print('}')

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
