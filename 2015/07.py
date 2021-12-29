# Advent of code 2015 7 dic
# --- Day 7: Some Assembly Required ---

# This year, Santa brought little Bobby Tables a set of wires and bitwise logic gates! Unfortunately, little Bobby is a little under the recommended age range, and he needs help assembling the circuit.

# Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535). A signal is provided to each wire by a gate, another wire, or some specific value. Each wire can only get a signal from one source, but can provide its signal to multiple destinations. A gate provides no signal until all of its inputs have a signal.

# The included instructions booklet describes how to connect the parts together: x AND y -> z means to connect wires x and y to an AND gate, and then connect its output to wire z.

# For example:

#     123 -> x means that the signal 123 is provided to wire x.
#     x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
#     p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
#     NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.

# Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). If, for some reason, you'd like to emulate the circuit instead, almost all programming languages (for example, C, JavaScript, or Python) provide operators for these gates.

# For example, here is a simple circuit:

# 123 -> x
# 456 -> y
# x AND y -> d
# x OR y -> e
# x LSHIFT 2 -> f
# y RSHIFT 2 -> g
# NOT x -> h
# NOT y -> i

# After it is run, these are the signals on the wires:

# d: 72
# e: 507
# f: 492
# g: 114
# h: 65412
# i: 65079
# x: 123
# y: 456

# In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire a?
# Your puzzle answer was 956.

# --- Part Two ---

# Now, take the signal you got on wire a, override wire b to that signal, and reset the other wires (including wire a). What new signal is ultimately provided to wire a?

# Your puzzle answer was 40149.

class Circuito:
    def __init__(self):
        self.varTable = {}
        self.collegamenti = {}

    def inserisciCollegamento(self,op,z,x,y):
        if op == '->' and x.isnumeric(): # se l'operazione è una semplice assegnazione lo inserisco subito tra i valori
            self.varTable.update( { z: int(x) })    # equivalent to self.varTable[z] = int(x)
        else:
            self.collegamenti.update({ z: { 'op': op, 'x': x, 'y': y } })

    def inserisciComando(self,comando): 
        # estraggo dall'intero comando l'operazione, gli operandi e la destinazione
        elementi = comando.split(' ')
        if len(elementi) == 4:
            op = elementi[0]
            x = elementi[1]
            y = None
            z = elementi[3]
        elif len(elementi) == 3:
            op = elementi[1]
            x = elementi[0]
            y = None
            z = elementi[2]
        else:
            op = elementi[1]
            x = elementi[0]
            y = elementi[2]
            z = elementi[4]
        self.inserisciCollegamento(op,z,x,y)
    
    def risolviCircuito(self, nodo): # trovo il valore del nodo inserito per parametro
        if self.collegamenti[nodo] is None: # se non trovo il nodo richiesto -> il nodo non è collegato a nulla -> il suo valore è 0
            return 0
        operazione = self.collegamenti[nodo]
        # recupero il valore del primo operando, se non ce l'ho ancora lo calcolo ricorsivamente
        if operazione['x'].isnumeric():
            xVal = int(operazione['x'])
        elif self.varTable.get(operazione['x']) is None:
            xVal = self.risolviCircuito(operazione['x'])
        else:
            xVal = self.varTable[operazione['x']]
        # recupero il valore del secondo operando, se necessario
        if operazione['y'] is not None:
            if operazione['y'].isnumeric():
                yVal = int(operazione['y'])
            elif self.varTable.get(operazione['y']) is None:
                yVal = self.risolviCircuito(operazione['y'])
            else:
                yVal = self.varTable[operazione['y']]
        # eseguo l'operazione richiesta
        match operazione['op']:
            case 'RSHIFT':
                zVal = xVal >> yVal
            case 'LSHIFT':
                zVal = xVal << yVal
            case 'AND':
                zVal = xVal & yVal
            case 'OR':
                zVal = xVal | yVal
            case 'NOT':
                zVal = ~ xVal   # ~ x -> complemento di x. si può anche ottenere con -x-1
            case '->':
                zVal = xVal
        self.varTable.update({ nodo: zVal })
        return zVal



circuito = Circuito()
with open("input/07.txt", 'r') as file:
    for line in file:
        circuito.inserisciComando(line.rstrip('\n')) #compongo il circuito. AAA rimuovo il \n da fine stringa
        # circuito.inserisciComando('956 -> b') # parte 2. assegno il valore calcolato precedentemente di a in b e risolvo nuovamente il circuito
print(f'Il valore del nodo a è: {circuito.risolviCircuito("a")}')
