def createboard(size=19):
    board = [[' ' for _ in range(size)] for _ in range(size)]
    return board



def boardsize(selection):
    match selection:
        case 0: return createboard(9)
        case 1: return createboard(13)
    return createboard()


