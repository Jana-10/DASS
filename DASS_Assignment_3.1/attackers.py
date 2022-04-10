from constants import COL,ROW

class attackers:
    def __init__(self,name,game,y_coord, x_coord,symbol, hitpoint, speed):
        self.name = name
        self.game = game
        self.hitpoint = hitpoint
        self.speed = speed
        self.symbol = symbol
        self.health = 100
        self.x = y_coord
        self.y = x_coord


class king(attackers):
    def __init__(self,game,y_coord,x_coord,name="KING",symbol='K',hitpoint= 50,speed= 1 ):
        super().__init__(name,game,y_coord, x_coord, symbol, hitpoint, speed)
        self.Strength = 500
        self.prev_move = ""
        self.game.board[self.y][self.x] = self.symbol


    def left_move(self):
        self.prev_move = 'L'
        if(self.x > 0):
            if(self.game.board[self.y][self.x-1]==' '):
                self.game.board[self.y][self.x] = ' '
                self.game.board[self.y][self.x-1] = self.symbol
                self.x -= 1
    
    def right_move(self):
        self.prev_move = 'R'
        if(self.x < COL - 2):
            if(self.game.board[self.y][self.x+1]==' '):
                self.game.board[self.y][self.x] = ' '
                self.game.board[self.y][self.x+1] = self.symbol
                self.x += 1

    def up_move(self):
        self.prev_move = 'U'
        if(self.y > 0):
            if(self.game.board[self.y-1][self.x]==' '):
                self.game.board[self.y][self.x] = ' '
                self.game.board[self.y-1][self.x] = self.symbol
                self.y -= 1

    def down_move(self):
        self.prev_move = 'D'
        if(self.y < ROW - 1):
            if(self.game.board[self.y+1][self.x]==' '):
                self.game.board[self.y][self.x] = ' '
                self.game.board[self.y+1][self.x] = self.symbol
                self.y += 1

    def attack(self):
        if(self.prev_move == 'L'):
            if(self.x-1>0):
                self.game.map[self.y][self.x-1].attack(self.hitpoint)
        elif(self.prev_move == 'R'):
            if(self.x+1<COL-1):
                self.game.map[self.y][self.x+1].attack(self.hitpoint)
        elif(self.prev_move == 'U'):
            if(self.y-1>0):
                self.game.map[self.y-1][self.x].attack(self.hitpoint)
        elif(self.prev_move == 'D'):
            if(self.y+1<ROW-1):
                self.game.map[self.y+1][self.x].attack(self.hitpoint)

class barbarian(attackers):
    def __init__(self,game,y_coord,x_coord,name="BARBARIAN",symbol='B',hitpoint= 50,speed= 1 ):
        super().__init__(name,game,y_coord, x_coord, symbol, hitpoint, speed)
        self.Strength = 100
        self.game.board[self.y][self.x] = self.symbol
        
    def find_target(self):


        for building in self.game.layout.existing_building:
            if(building.name == "")
                