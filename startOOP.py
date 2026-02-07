from utils import publicmodules as pm #used my own "lib"

class People:
    def __init__(self):
        self.name = ''
        self.age = 0
        self.weight = 0
        
    def set_name(self):
        while True:
            name = input('please enter your name here: ').title().strip()
            if name.replace(' ' , '').isalpha():
                self.name = name
                break
            else:
                print('enter a valid name')
            
    def set_age(self):
        while True:
            try:
                age = int(input(f'enter {self.name} age here: '))
                while age > 110 or age < 0:
                    age = int(input(f'enter a valid age (0 - 110): '))
                else:
                    self.age = age
                break
            except ValueError:
                print('please enter a valid value')
                
    def set_weight(self):
        while True:
            try:
                weight = float(input(f'please enter {self.name} weight here: '))
                while weight < 1 or weight > 400:
                    weight = float(input(f'please enter a valid weight here (1 - 400): '))
                else:
                    self.weight = float(f'{weight:.3f}')
                break
            except ValueError:
                print('enter a valid value')
            

    def organize_person(self): #organize data
        """ Full creation process: name + age + weight + return dict """
        self.set_name()
        self.set_age()
        self.set_weight()

        return {
            'name': self.name,
            'age': self.age,
            'weight': self.weight
}
    
#start program
people_list = []

while True:

    person = People()
    person_dict = person.organize_person()
    people_list.append(person_dict)
    
    rep = pm.get_repeat() #repeat program or no
    if rep == 'yes':
        continue
    else:
        print(people_list)
        print(f'\nFINISHED PROGRAM')
        break