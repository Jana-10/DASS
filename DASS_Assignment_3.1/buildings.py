from colorama import Fore, Back, Style
import colorama

class cell:
    def __init__(self,game,name,y_coord,x_coord):
        self.game = game
        self.name = name
        self.x_start = y_coord
        self.y_start = x_coord

class building(cell):
    
    
    def __init__(self,game,name,health,strength,color,x_start,y_start,height,width):
        super().__init__(game,name,x_start,y_start)
        self.health = health
        self.strength = strength
        self.color = color
        self.height = height
        self.width = width
        self.x2 = self.x_start + width 
        self.y2 = self.y_start + height 
    
    def show(self):
        
        for y_coord in range(self.x_start,self.x2):
            for x_coord in range(self.y_start,self.y2):
                self.game.board[x_coord][y_coord] =self.color
                self.game.map[x_coord][y_coord] = self
    
    def attack(self,hitpoint):
        self.health -= hitpoint
        if(self.health <= 0):
            self.destroy_building()
    
    def destroy_building(self):

        for y_coord in range(self.x_start,self.x2):
            for x_coord in range(self.y_start,self.y2):
                self.game.board[x_coord][y_coord] = ' '
                self.game.map[x_coord][y_coord] = empty(self.game,y_coord,x_coord)
                

class town_Hall(building):

    def __init__(self,game,x_start,y_start,name="Town Hall",health=100,strength = 250,color=colorama.Back.YELLOW + ' ' + colorama.Style.RESET_ALL,height=3,width=4):
        super().__init__(game,name,health,strength,color,x_start,y_start,height,width)

    
            
    
        
class hut(building):

    def __init__(self,game,x_start,y_start,name="Hut",health=100,strength = 150,color=colorama.Back.BLUE + ' ' + colorama.Style.RESET_ALL,height=2,width=2):
        super().__init__(game,name,health,strength,color,x_start,y_start,height,width)


class cannon(building):

    def __init__(self,game,x_start,y_start,target=1,damage=1,name="Cannon",health=100,strength = 100,color = colorama.Back.BLACK + ' ' + colorama.Style.RESET_ALL,height=2,width=2):
        super().__init__(game,name,health,strength,color,x_start,y_start,height,width)
        self.damage =  damage
        self.target = target
        self.active = True

    def destroy_building(self):
        self.active = False
        super().destroy_building()

class wall(building):
    def __init__(self,game,x_start,y_start,name="Wall",health=100,strength = 50,color=colorama.Back.RED + ' ' + colorama.Style.RESET_ALL,height=1,width=1):
        super().__init__(game,name,health,strength,color,x_start,y_start,height,width)

class empty(cell):
    def __init__(self,game,x_start,y_start,name="Empty"):
        super().__init__(game,name,x_start,y_start)
    