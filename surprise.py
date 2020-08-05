import cmd
import sys, os, time
from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen


os.system('clear')

print("Surprize Togepi! lets have a small quize together and a small prize at the end!(only if you complete it)\n")
print("Instructions:\n")
print("Simple, answer the questions, in between if you want to exit, just type q and enter!\n")

questions_answers = {
    "1986"   :"In which year mam finished her graduation?",
    "9"      :"How many flower pots are there in your house?",
    "3.14159":"Write the value of Pi till 5 places from decimal.",
    "man's search for meaning":"What is the name of the book that Anupam Karn is bought recently",
    "ANSH": "Decipher this word 'CPUJ', (hint: It is ciphered using one of simplest ciphering techniques you have studied, number 2 plays a role in it)",
    "guido van rossum": "Who is the inventer of Python language?",
    "mahima": "What is the Sharad bhaiya's wife",
    "11.2":"What is the escape velocity of earth in km/s?",
    "bethal":"What is the name of the class where you went to learn keyboard?",
    "6":"What is the atomic number of Carbon?"
}

class HelloWorld(cmd.Cmd):

    intro = 'Enter start to start the quiz!\n'
    prompt = '(go_togepi):'
    
    def demo(self, screen):
        effects = [
            Cycle(
                screen,
                FigletText("ISHA PALI", font='big'),
                int(screen.height / 2 - 8)),
            Cycle(
                screen,
                FigletText("ROCKS!", font='big'),
                int(screen.height / 2 + 3)),
            Stars(screen, 200)
        ]
        screen.play([Scene(effects, 500)])

    def do_start(self, line):

        question_counter = 0
        for answer, question in questions_answers.items():

            question_counter = question_counter + 1
            print(question)
            counter = 3
            while counter != 0:
            
                response = input()
                if response == answer:
                    print("Welldone! \n")
                    counter = 3
                    break
                else:
                    counter = counter - 1
                    if counter != 0:
                        print("You have {0} chances left".format(counter))
            
            if counter == 0:
                print("Pagli ladhki! try again from starting (enter start to restart)")
                return      

        if question_counter == 10:

            os.system('clear')
            print("Woohoo you completed the quiz good job! It doesn't matter you fail or pass the most important thing is you tried! and that's what matters the most. So try and keep trying harder everytime!")
            time.sleep(6)
            os.system('clear')
            print("So")
            time.sleep(2)
            os.system('clear')
            print("Here is the surprise")
            time.sleep(3)
            os.system('clear')

            Screen.wrapper(self.demo)
            
            
    def do_q(self, line):
        return True

if __name__ == '__main__':
    HelloWorld().cmdloop()