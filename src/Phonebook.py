import json
class Phonebook : 
    def __init__(self) : 
        newContact = {
            "name": "",
            "mobile": ""
        }
        jsonFile = open("./json/contacts.json")
        contacts = json.load(jsonFile)
        print("\nSaved Contacts")
        for contact in contacts : 
            print("==================")
            print(contact['name'])
            print(contact['mobile'])
        print("\nCreate Contact")
        newContact['name'] = input("Enter name :- ")
        if newContact['name'] == "exit()" : quit()

        newContact['mobile'] = input("Enter mobile :- ")
        if newContact['mobile'] == "exit()" : quit()
        
        contacts.append(newContact)
        file = open("./json/contacts.json","w")
        string = json.dumps(contacts)
        file.write(string)
        file.close()
        print("Contact Saved !")

