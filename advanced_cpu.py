import random
def advanced_cpu(pos):
    values=set(pos.values())
    if values=={'X','O'} or values=={'O','X'}:
        return None
    elif (pos[2]=='X' and pos[3]=='X' and pos[1]=='1'):
        return pos.update({1:'O'})
    elif (pos[1]=='X' and pos[3]=='X' and pos[2]=='2'):
        return pos.update({2:'O'})
    elif (pos[2]=='X' and pos[1]=='X' and pos[3]=='3'):
        return pos.update({3:'O'})
    elif (pos[6]=='X' and pos[5]=='X' and pos[4]=='4'):
        return pos.update({4:'O'})
    elif (pos[4]=='X' and pos[6]=='X' and pos[5]=='5'):
        return pos.update({5:'O'})
    elif (pos[4]=='X' and pos[5]=='X' and pos[6]=='6'):
        return pos.update({6:'O'})
    elif (pos[8]=='X' and pos[9]=='X' and pos[7]=='7'):
        return pos.update({7:'O'})
    elif (pos[7]=='X' and pos[9]=='X' and pos[8]=='8'):
        return pos.update({8:'O'})
    elif (pos[7]=='X' and pos[8]=='X' and pos[9]=='9'):
        return pos.update({9:'O'})
    elif (pos[4]=='X' and pos[7]=='X' and pos[1]=='1'):
        return pos.update({1:'O'})
    elif (pos[1]=='X' and pos[7]=='X' and pos[4]=='4'):
        return pos.update({4:'O'})
    elif (pos[4]=='X' and pos[1]=='X' and pos[7]=='7'):
        return pos.update({7:'O'})
    elif (pos[8]=='X' and pos[5]=='X' and pos[2]=='2'):
        return pos.update({2:'O'})
    elif (pos[2]=='X' and pos[8]=='X' and pos[5]=='5'):
        return pos.update({5:'O'})
    elif (pos[2]=='X' and pos[5]=='X' and pos[8]=='8'):
        return pos.update({8:'O'})
    elif (pos[6]=='X' and pos[9]=='X' and pos[3]=='3'):
        return pos.update({3:'O'})
    elif (pos[3]=='X' and pos[9]=='X' and pos[6]=='6'):
        return pos.update({6:'O'})
    elif (pos[3]=='X' and pos[6]=='X' and pos[9]=='9'):
        return pos.update({9:'O'})
    elif (pos[5]=='X' and pos[9]=='X' and pos[1]=='1'):
        return pos.update({1:'O'})
    elif (pos[1]=='X' and pos[9]=='X' and pos[5]=='5'):
        return pos.update({5:'O'})
    elif (pos[1]=='X' and pos[5]=='X' and pos[9]=='9'):
        return pos.update({9:'O'})
    elif (pos[5]=='X' and pos[7]=='X' and pos[3]=='3'):
        return pos.update({3:'O'})
    elif (pos[3]=='X' and pos[7]=='X' and pos[5]=='5'):
        return pos.update({5:'O'})
    elif (pos[3]=='X' and pos[5]=='X' and pos[7]=='7'):
        return pos.update({7:'O'})
    else:
        choice=random.randrange(1,9)
        if(pos[choice]=='X') or (pos[choice]=='O'):
            return advanced_cpu(pos)
        return pos.update({choice:'O'})
