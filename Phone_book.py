class Contact:
    number_of_contact=0
    number_directory = []

    def __init__(self,name,phone):
        self.name=name
        self.phone=phone

        Contact.number_directory.append(self)
        Contact.number_of_contact=Contact.number_of_contact +1
        print("Number Added Successfully ")

    def display(self):
        print("-------------------------")
        print("Name :",self.name)
        print("Phone :",self.phone)

    @classmethod
    def display_all(cls):
        c=1
        if Contact.number_of_contact>0:
            print("----------------------\n")
            print("Number of contacts =",Contact.number_of_contact)
            print()
            for i in Contact.number_directory:
                print(c,']',sep='')
                print("Name :",i.name)
                print("phone :",i.phone)
                print()
                c=c+1
                
            print("----------------------")

        else:
            print("----------------------")
            print("contacts not added yet!!!")
            print("----------------------")

    @classmethod 
    def search(self,name):
        flag=False

        for i in Contact.number_directory:
            if i.name.lower()==name.lower():
                print("----------------------")
                print("Phone :",i.phone)
                print("----------------------")
                flag=True

        if not(flag):
            print("----------------------")
            print("The Number is not found!!!!!!!!")
            print("----------------------")


    @classmethod
    def isvalid(cls,namev,phonev):
        is_name_exist=False
        is_phone_exist=False

        
        if len(phonev) != 10 or not phonev.isdigit():   
            print("\nPhone number is Invalid !!!!!!\n")
            return False
        
        
        for i in cls.number_directory:
            if phonev==i.phone:
                is_phone_exist=True
                break

        for i in cls.number_directory:
            if namev.lower()==i.name.lower():
                is_name_exist=True
                break


        if is_phone_exist:
            print(f"\nThe {phonev} number is already exists use different number\n")
            return False
        
        if is_name_exist:
            print(f"\nThe {namev} is already exist use {namev}2\n")
            return False


        return True
    

    @classmethod
    def remove_number(cls, namev):
        for i in cls.number_directory[:]:
            if i.name.lower() == namev.lower():
                cls.number_directory.remove(i)
                cls.number_of_contact -= 1
                print("----------------------")
                print(f"The {namev} is removed successfully")
                print("Name :", i.name)
                print("Phone :", i.phone)
                print("----------------------")
                return

        print("----------------------")
        print(f"The {namev} is not exist")
        print("-----------------------")



flag = True

while(flag):
    print("============MENU===============")
    print("1. Add")
    print("2. Remove")
    print("3. Search")
    print("4. Display All")
    print("5. Exit")
    print("===============================")
    ch = input(("Enter Your Choice :"))

    if ch=='1':
        name=input("Enter Name :")
        phone=input("Enter Phone :")

        if Contact.isvalid(name,phone):
            c=Contact(name,phone)
        else:
            print("Contact is not Added")

    elif ch=='2':
        name=input("Enter Name :")
        Contact.remove_number(name);
    elif ch=='3':
        name=input("Enter Name :")
        Contact.search(name)
    elif ch=='4':
        Contact.display_all()
    elif ch=='5':
        print("Thank you!!!!!!!!")
        flag = False
    else:
        print("Invalid choice !!!!!!!!!!!!")

        


