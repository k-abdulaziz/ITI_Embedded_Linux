
def SET_BIT(NUM, BIT):
    NUM = int(NUM)
    BIT = int(BIT)
    return (NUM | (1<<BIT))

def CLEAR_BIT(NUM, BIT):
    NUM = int(NUM)
    BIT = int(BIT)
    return (NUM & (~(1<<BIT)))

def GET_BIT(NUM, BIT):
    NUM = int(NUM)
    BIT = int(BIT)
    return (NUM & (1<<BIT))