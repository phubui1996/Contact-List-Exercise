class ContactList:
    contact_list = []
    people = {
        'name': '',
        'number': ''
    }
    def __init__(self, name, phone_number):
        self._name = name
        self._phone_number = phone_number
        ContactList.people['name'] = self._name
        ContactList.people['number'] = self._phone_number
        ContactList.contact_list.append(ContactList.people)

    def __str__(self):
        return f'Name: {self._name}, number: {self._phone_number}'

    @property
    def get_name(self):
        return self._name
    @get_name.setter
    def set_name(self, new_name):
        self._name = new_name

    @property
    def get_phone_number(self):
        return self._phone_number
    @get_phone_number.setter
    def set_phone_number(self, new_phone_number):
        self._phone_number = new_phone_number

    # @staticmethod
    # def add_contact():
    #     input_name = input("Please enter your name: ")
    #     input_phone = input('Please enter your phone number: ')
    #     ContactList.people['name'] = input_name
    #     ContactList.people['number'] = input_phone
        #ContactList.contact_list.append(ContactList.people)

    @classmethod 
    def add_contact(cls):
        input_name = input("Please enter your name: ")
        input_phone = input('Please enter your phone number: ')
        cls(input_name, input_phone)
        print(ContactList.contact_list)

    @staticmethod
    def remove_contact():
        person = input("Please enter the name of the contact that you would like to remove: ")
        for i in range(len(people)):
            if(people[i][0] == person):
                people[i].remove()

    @staticmethod
    def find_shared_contacts(list_1, list_2):
        new_list = []
        for i in list_1:
            #print(i)
            for j in list_2:
                #print(j)
                if i._phone_number == j._phone_number:
                    #print(i._name)
                    new_list.append(i._name)
        return new_list



ContactList.add_contact()
ContactList.add_contact()

# person1 = ContactList.add_contact()
# person2 = ContactList.add_contact()
# print(ContactList.contact_list)
# print(ContactList.contact_list)


# friends = [ContactList('Alice','867-5309' ), ContactList('Bob', '555-5555')]
# work_buddies = [ContactList('Alice','867-5309' ), ContactList('Carlos', '555-5556')]

# print(ContactList.find_shared_contacts(friends,work_buddies))


# friends = [{'name':'Alice','number':'867-5309'},{'name':'Bob', 'number':'555-5555'}]
# work_buddies = [{'name':'Alice','number':'867-5309'},{'name':'Carlos', 'number':'555-5555'}]
# friend = ContactList('My Friends', friends)
# family = ContactList('Work Buddies', work_buddies)

# print(friend)
# print(work_buddies)


# ContactList.add_contact()
# print(ContactList.people)

#person1.find_shared_contacts(person2)



        