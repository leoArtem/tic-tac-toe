
#n= [1+(0*3)(1,1),2+(0*3)(2,1),3+(0*3)(3,1),1+(1*3)(1,2),2+(1*3)(2,2)...1+(2*3)
#board[n]=x




def game_process():
    board = [0,0,0,
             0,0,0,
             0,0,0]
    game = True
    while game == True:

        def pl_turn():



            print(board)

            row = int(input("ведите ряд --- "))
            if row < 1 or row > 3:
                print("вы за пределами поля")
                return pl_turn()


            col = int(input("введите колонну --- "))
            if col < 1 or col > 3:
                print("вы за пределами поля")
                return pl_turn()


            place = ((col - 1) + ((row - 1) * 3))


            inp = int(input("введите 1 или -1 --- "))
            if inp != 1 and inp != -1:
                print("введите нужное значение")
                return pl_turn()
            elif board[place] != 0:
                print("место занято")
                return pl_turn()

            board[place]=inp
        # if board == any[[][][][]]:
            #game = False
        pl_turn()




game_process()