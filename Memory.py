# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 10:52:07 2018

@author: Ahmad
"""
import pickle

contacts = {}
contactList = []

def load():
    """ Load saved contacts from file. """
    
    try:
        with open("Memory.data", "rb") as f:
            global contacts
            contacts = pickle.load(f)
    except:#If no file found, so user is newbie.
        print("Hi, Welcome to Memory..")
def save():
    """ Save contacts to file. """
    
    with open("Memory.data", "wb") as f:
        pickle.dump(contacts,f)
    
def checkExist(name):
    """ checkExist(name)
    
    Check if name exists in contactList and return True or False. """
    
    listContacts(False)
    if name in contactList:
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
            \n1. View Contacts
            \n2. Add new contact
            \n3. Edit contact
            \n4. Delete contact
            \n-->"""))
        if order == 1:
            showContacts()
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

        
def listContacts(capital):
    """ listContacts(boolean)
    
    Call whenever a list of contacts keys needed, e.g. in checkExist().
    Initialize contactList[] with keys in contacts{}
    and make key Capitalize or lowecase according to given capital variable. """
    
    global contactList
    if capital:
        contactList = [key.capitalize() for key in contacts.keys()]
    else:
        contactList = [key.lower() for key in contacts.keys()]
    
def showContacts():
    """ Print contacts list. """
    
    listContacts(True)
    if len(contactList) == 0:#If ContactList is empty, run menu() with a message.
        print("There is no contacts. but don't worry, You can add them if you want.")
        menu()
    contactList.sort()
    for contact in contactList:
        print("{0} --> {1}".format(contactList.index(contact),contact))
    try:
        order = int(input("""whay do you want? (Enter Number)
                      \n1. View a contact
                      \n2. Return to Menu
                      \n-->"""))
        if order ==1:
            viewPerson()
        elif order ==2:
            menu()
        else:
            print("Error: Invalid operation")
            menu()
    except:#if order isn't a number, int() raise an error.
        print("This isn't an integer")
        menu()
           
def viewPerson():
    try:
        index = int(input("Enter Contact's index -->"))
        contact = contacts[contactList[index]]#Selected contact to view.
        sep="-"*20
        print(sep)
        print("\nContact Name: {}\n".format(contactList[index]))
        print("Contact Details:")
        print("""\nNumber: {0}
                 \nEmail: {1}
                 \nType: {2}
                """.format(contact[0],contact[1],contact[2]))
        print(sep)
        menu()
        
    except:#if order isn't a number, int() raise an error.
        print("This isn't an integer")
        menu()
    
def addPerson():
    """ Run from menu() to add a person and run setPerson() with given data. """
    
    name = input("Enter contact's name -->").capitalize()
    number = input("Enter contact's number -->")
    email = input("Enter contact's Email -->")
    try:
        Type = int(input("""Enter contact's Type:
            \n1. Family
            \n2. Friend
            \n3. Colleague
            \n-->"""))
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
    
    name = input("Enter Contact's name -->").capitalize()
    if not checkExist(name.lower()):#Check if given name exist in contacts dict.
        print("This Contact doesn't exist")
    else:
        contact = contacts[name]
        newName = ""#used to creat new contact
        try:
            item = int(input("""Enter item's number to edit:
                \n1.Name
                \n2.Number
                \n3.Email
                \n4.Type
                \n-->"""))
            if item == 1:
                newName = input("Enter new name -->").capitalize()
            elif item == 2:
                contact[0] = input("Enter new number -->")
            elif item == 3:
                contact[1] = input("Enter new Email -->")
            elif item == 4:
                try:
                    value = int(input("""Enter new Type's number:
                        \n1. Family
                        \n2. Friend
                        \n3. Colleague
                        \n-->"""))
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
    
    name = input("Enter contact's name -->").capitalize()
    if checkExist(name.lower()):#check if given name exist in contacts dict. 
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