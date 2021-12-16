#Advent of code 2015 6 dic
# --- Day 6: Probably a Fire Hazard ---

# Because your neighbors keep defeating you in the holiday house decorating contest year after year, you've decided to deploy one million lights in a 1000x1000 grid.

# Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to display the ideal lighting configuration.

# Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

# To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order.

# For example:

#     turn on 0,0 through 999,999 would turn on (or leave on) every light.
#     toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
#     turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.

# After following the instructions, how many lights are lit?

# Your puzzle answer was 400410.

# --- Part Two ---

# You just finish implementing your winning light pattern when you realize you mistranslated Santa's message from Ancient Nordic Elvish.

# The light grid you bought actually has individual brightness controls; each light can have a brightness of zero or more. The lights all start at zero.

# The phrase turn on actually means that you should increase the brightness of those lights by 1.

# The phrase turn off actually means that you should decrease the brightness of those lights by 1, to a minimum of zero.

# The phrase toggle actually means that you should increase the brightness of those lights by 2.

# What is the total brightness of all lights combined after following Santa's instructions?

# For example:

#     turn on 0,0 through 0,0 would increase the total brightness by 1.
#     toggle 0,0 through 999,999 would increase the total brightness by 2000000.

# Your puzzle answer was 15343601.

class Griglia:
    def __init__(self):
        self.grid = [[0 for col in range(0,1000)] for row in range(1000)]
        self.unos = 0
    def __repr__(self):  #quando provo a stampare l'oggetto come stringa viene chiamata questa funzione posso anche usare il costruttore __str__()
        return f'Il numero di luci accese è: {self.unos}'
    def toggle(self,x1,y1,x2,y2):
        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                # self.grid[x][y] = 1 if self.grid[x][y] == 0 else 0
                if self.grid[x][y] == 0:
                    self.grid[x][y] = 1
                    self.unos += 1
                else:
                    self.grid[x][y] = 0
                    self.unos -= 1
        return self.unos
    def turnOn(self,x1,y1,x2,y2):
        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                if self.grid[x][y] == 0:
                    self.grid[x][y] = 1
                    self.unos += 1
        return self.unos
    def turnOff(self,x1,y1,x2,y2):
        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                if self.grid[x][y] == 1:
                    self.grid[x][y] = 0
                    self.unos -= 1
        return self.unos
    def getUnos(self):
        return self.unos

class Griglia2:
    def __init__(self):
        self.grid = [[0 for col in range(0,1000)] for row in range(1000)]
        self.totalBrightness = 0
    def __str__(self):
        return f'La luminosità totale è: {self.totalBrightness}'
    def toggle(self,x1,y1,x2,y2):
        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                self.grid[x][y] += 2
                self.totalBrightness += 2
    def turnOn(self,x1,y1,x2,y2):
        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                    self.grid[x][y] += 1
                    self.totalBrightness += 1
    def turnOff(self,x1,y1,x2,y2):
        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                if self.grid[x][y] > 0:
                    self.grid[x][y] -= 1
                    self.totalBrightness -= 1
    def getBrightness(self):
        return self.totalBrightness

def extractCoordinates(line):
    splittedLine = line.split(' ')
    indexOfFirstCoordinates = 2 if len(splittedLine) == 5 else 1
    coordinates1 = [ int(x) for x in splittedLine[indexOfFirstCoordinates].split(',') ]
    coordinates2 = [ int(x) for x in splittedLine[indexOfFirstCoordinates+2].split(',') ]
    return coordinates1[0],coordinates1[1],coordinates2[0],coordinates2[1]

griglia = Griglia() # per la prima parte
# griglia = Griglia2() ### per la seconda parte
with open("input/06.txt", 'r') as file:
    for line in file:
        coordinates = extractCoordinates(line)
        if line[0:2] == 'tu':   # dai primi due caratteri capisco se si tratta di toggle o turn on/off
            if line[6:7] == 'n': # dal 7 carattere capisco se si tratta di turn on or turn off
                griglia.turnOn( *coordinates )  # uso l'operatore * per l'unpacking. equivale a (coordinates[0], coordinates[1], coordinates[2], coordinates[3])
            else:
                griglia.turnOff( *coordinates )
        else:
            griglia.toggle( *coordinates )
print(griglia)  # stampo 