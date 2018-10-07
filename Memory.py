# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 10:52:07 2018

@author: Ahmad
"""
import pickle

contacts = {}


def load():
    """ Load saved contacts from file. """
    
    with open("Memory.data", "rb") as f:
        global contacts
        contacts = pickle.load(f)
def save():
    """ Save contacts to file. """
    
    with open("Memory.data", "wb") as f:
        pickle.dump(contacts,f)
    
def checkExist(name):
    """ Check if a contact exists. """
    
    if name in contacts.keys():
        return True
    else:
        return False
    
def setType(Type):
    """ Give a number and return corresponding contact type. """
    
    if Type == 1:
        Type = 'Family'
    elif Type == 2:
        Type = 'Friend'
    elif Type == 3:
        Type = 'Colleague'
    else : print("Error: Invalid Type")
    return Type
    
def setPerson(name,number,email,Type):
    """ Give contact's data and creat the contact according to its type. """
    
    if Type == 'Family':
        p = FamilyPerson(name,number,email)
        p.add()
    elif Type == 'Friend':
        p = FriendPerson(name,number,email)
        p.add()
    elif Type == 'Colleague':
        p = ColleaguePerson(name,number,email)
        p.add()

def menu():
    """" Run when program starts and run functions according to order value. """
    
    try:
        order = int(input("""Please select an operation (Enter number):
            1. View Contacts
            2. Add new contact
            3. Edit contact
            4. Delete contact
            -->"""))
        if order == 1:
            listContacts()
        elif order == 2:
            addPerson()
        elif order == 3:
            editPerson()
        elif order == 4:
            delPerson()
        else:
            print("Error: Invalid Operation")
    except:#if order isn't a number, int() raise an error.
        print("This isn't an integer")
        menu()

        
def listContacts():
    """ Print contacts. """
    
    for i in contacts:
        print("{0} | {1}".format(i, contacts[i]))
    menu()
    
def addPerson():
    """ Run from menu() to add a person and run setPerson() with given data. """
    
    name = input("Enter contact's name -->")
    number = input("Enter contact's number -->")
    email = input("Enter contact's Email -->")
    try:
        Type = int(input("""Enter contact's Type:
            1. Family
            2. Friend
            3. Colleague
                     -->"""))
    except:#if order isn't a number, int() raise an error.
        print("This isn't an integer")
        menu()

    setPerson(name,number,email,setType(Type))
    menu()
    
def editPerson():
    """" Run from menu() to edit existing person.
    
    If the contact exsit, this function delete it and creat new contact
    using setPerson().
    """
    
    name = input("Enter Contact's name -->")
    if not checkExist(name):#Check if given name exist in contacts dict.
        print("This Contact doesn't exist")
    else:
        contact = contacts[name]
        newName = ""#used to creat new contact
        try:
            item = int(input("""Enter item's number to edit:
                1.Name
                2.Number
                3.Email
                4.Type
                -->
                """))
            if item == 1:
                newName = input("Enter new name -->")
            elif item == 2:
                contact[0] = input("Enter new number -->")
            elif item == 3:
                contact[1] = input("Enter new Email -->")
            elif item == 4:
                try:
                    value = int(input("""Enter new Type's number:
                        1. Family
                        2. Friend
                        3. Colleague
                        -->
                        """))
                    contact[2] = setType(value)
                except:#if order isn't a number, int() raise an error.
                    print("This isn't an integer")
                    menu()
            else:
                print("Error: Invalid Item")
            
            del contacts[name]#delete existing contcat
            if newName == "":
                newName = name#set old name as new name if name not changed.
            setPerson(newName,*contact)#star before a list as argument return its items.
            print("{0} edited successfully.".format(name))
        except:#if order isn't a number, int() raise an error.
            print("This isn't an integer")
            menu()

    menu()
    
def delPerson():
    """ Run from menu() to delete existing contact. """
    
    name = input("Enter contact's name -->")
    if checkExist(name):#check if given name exist in contacts dict. 
        confirm = input("Are you sure to delete {0}? (Y,N)".format(name))
        if confirm.upper() == "Y":
            del contacts[name]
            save()
            print("{0} deleted successfully".format(name))
        elif confirm.upper() == "N":
            print("You canceled the operation")
        else:
            print("Error: Invalid answer")
    else:
        print("This Contact doesn't exist")
    menu()
    
class Person:
    """ General person class used by inherited classes. """
    
    def __init__(self, name, number,email):
        self.name = name
        self.number = number
        self.email = email
    def add(self):
        contacts[self.name] = [self.number, self.email,self.type]
        save()
        
class FamilyPerson(Person):
    """ Family person class, set type to 'Family'. """
    def __init__(self, name, number, email):
        Person.__init__(self,name,number,email)
        self.type = 'Family'


class FriendPerson(Person):
    """ Friend person class, set type to 'Friend'. """
    def __init__(self, name, number, email):
        Person.__init__(self,name,number,email)
        self.type = 'Friend'

class ColleaguePerson(Person):
    """ Colleague person class, set type to 'Colleague'. """
    def __init__(self,name,number,email):
        Person.__init__(self,name,number,email)
        self.type = 'Colleague'


        

load()
menu()