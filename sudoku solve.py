board=[
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

# function is to put number(1,9)
 
def solve(b):
    find=find_empty(b)
    if not find:
        return True
    else:
        r,c=find
    for i in range(1,10):
        if isvalid(b,i,(r,c)):
            b[r][c]=i

            if solve(b):
                return True
            else:
                b[r][c]=0
    return False




# function is to check shall i put number is here or not
def isvalid(b,num,pos):
    row=pos[0]
    col=pos[1]
    for i in range(0,9):
        if b[i][col]==num:
            return False
        if b[row][i]==num:
            return False
        if b[3*(row//3)+i//3][3*(col//3)+i%3]==num:
            return False
    return True

# funtion to print board 3*3 matrix
def print_board(b):
    for i in range(len(board)):
        if i%3==0 and i!=0:
            print("-----------------------")
        for j in range(len(b[0])):
            if j%3==0 and j!=0:
                print("|",end="")
            if j==8:
                print(b[i][j])
            else:
                print(str(b[i][j])+" ",end="")

# function which find where empty is available
def find_empty(b):
    for i in range(len(b)):
        for j  in range(len(b[0])):
            if b[i][j]==0:
                return (i,j)

    return None


# calling function (let say run it)

print()
print("Before solve\n")
print_board(board)
solve(board)
print()
print("After solved !\n")
print_board(board)
