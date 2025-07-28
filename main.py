import random
from advanced_cpu import advanced_cpu


pos={1:'1', 2:'2', 3:'3',4:'4',5:'5', 6:'6',7:'7',8:'8',9:'9'}
lis_numbr=['1','2','3','4','5','6','7','8','9']


def cpu(pos):
    choice=random.randrange(1,9)
    if (pos[choice]=='X') or (pos[choice]=='O') :
        return cpu(pos)
    return pos.update({choice:'O'})



        
def win_condition(pos):
    values=set(pos.values())
    if (pos[1]=='X' and pos[2]=='X' and pos[3]=='X') or (pos[1]=='X' and pos[4]=='X' and pos[7]=='X')or (pos[2]=='X' and pos[5]=='X' and pos[8]=='X')or (pos[3]=='X' and pos[5]=='X' and pos[7]=='X')or (pos[4]=='X' and pos[5]=='X'and pos[6]=='X') or (pos[7]=='X' and pos[8]=='X' and pos[9]=='X') or (pos[1]=='X' and pos[5]=='X'and pos[9]=='X') or (pos[3]=='X' and pos[6]=='X'and pos[9]=='X') :
        return print('you Win!')
    elif (pos[1]=='O' and pos[2]=='O' and pos[3]=='O') or (pos[1]=='O' and pos[4]=='O' and pos[7]=='O')or (pos[2]=='O' and pos[5]=='O' and pos[8]=='O')or (pos[3]=='O' and pos[5]=='O' and pos[7]=='O')or (pos[4]=='O' and pos[5]=='O'and pos[6]=='O') or (pos[7]=='O' and pos[8]=='O' and pos[9]=='O') or (pos[1]=='O' and pos[5]=='O'and pos[9]=='O')or (pos[3]=='O' and pos[6]=='O'and pos[9]=='O') :
        return print('you Lose!')
    elif values=={'X','O'} or values=={'O','X'}:
        return print('tie!')


    return True    
    
        
        


def draw(pos):
    return print(f' | {pos[1]} | {pos[2]} | {pos[3]} | \n | {pos[4]} | {pos[5]} | {pos[6]} | \n | {pos[7]} | {pos[8]} | {pos[9]} |')

def user_input():
    try:
        ans=input('choose a space: ')
        if (len(ans)>1) or (pos[int(ans)]=='X') or (pos[int(ans)]=='O'):
            print('invalid input!')
            return user_input()
        return int(ans)
    except ValueError:
        print('only numbers!')
        return user_input()


def main():
    draw(pos)
    while win_condition(pos):    
       

        pos.update({user_input():'X'})
        
        advanced_cpu(pos) #hard mode
        #cpu(pos) #easy mode
        draw(pos)
        print(set(pos.values()))


if __name__=='__main__':

    main()