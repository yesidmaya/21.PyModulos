# -*- coding: utf-8 -*-
# v = 4.7

from lamp import Lamp # del modulo lamp importate la class Lamp... -
                      # en esta linea podemos colocar todas las clases que queramos llamar 
                      # separadas por coma asi: from lamp import Lamp, Foco

def run():
    lamp = Lamp(isTurned_on = False)

    while True:
        command = str(input('''
            Que deseas hacer?

            [p]render la lampara
            [a]pagar la lampara
            [s]alir
        '''))

        if command == 'p':
            lamp.turn_on()
        elif command == 'a':
            lamp.turn_off()
        else:
            break

if __name__ == "__main__": # si el modulo que se esta ejecutando se llama main ejecute la funcion run()
    run()