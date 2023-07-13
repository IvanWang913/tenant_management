def login_menu():
    import datetime
    time = datetime.datetime.now().strftime("%x %X")

    username = 'Bryan0066'
    password = 'Abc12345'

    while True:
        x = input("Enter Username: ")
        y = input("Enter Password: ")

        if x == username:
            if y == password:
                print(f"Welcome {username}")
                main_menu()

        else:
            print("Login Failed!!! Please try again")
            print(time)
        break

#Bryan
def main_menu():

    options = input("1. Tenant details\n2. Apartment details\n3. Pass tenant details\n4. Exit\nChoose option: ")
    while True:
        if options == '1':
                tenant = input("1. Add Tenant details\n2. See Tenant records\n3. Modify data\n4. Delete records\nPlease select 1,2,3,4: ")

                if tenant == '1':
                    tenants_details()

                elif tenant == '2':
                    readfile()

                elif tenant == '3':
                    modifyDta()

                elif tenant == '4':
                    removeData()

                else:
                    print("Error....Try again!!!!!!!!!")
                    main_menu()
                    break

        elif options == '2':
            apartment_menu()


        elif options == '3':
            pasttenant_menu()


        elif options == '4':
            print("Logout successfully!!!!!!")
            quit()

        else:
            print("Please try again later")


        print("Continue Press any key button....")
        print("Exit Press[E]")
        select = input("Press: ")
        if select == 'E':
            break

        return main_menu()


#Bryan
def validphone(mphone):
    if len(mphone) >10:
        return False

    while not mphone.isdigit():
        return False

    return True

#Bryan
def validname(mname):

    if len(mname) > 50:
        return False

    while not mname.isalpha():
        return False

    return True
#Bryan
def validic(mIc):
    for number in mIc:
        if not number.isdigit():
            return False

    if len(mIc) > 20:
        return False

    return True

#Bryan
def validpob(pob):
    if not pob.isalpha():
        return False
    elif len(pob) > 20:
        return False

    return True

#Bryan
def validcity(mcity):
    for character in mcity:
        if not character.isalpha():
            return False
        elif len(mcity) < 1:
            return False
    return True

#Bryan
def validwork(mwork):
    if not mwork.lower().upper().isalpha():
        return False
    for character in mwork:
        if len(character) > 20:
            return False
    return True

#Bryan
def validemployer(memployer):
    while memployer.isdigit():
        return False
    if len(memployer) >20:
        return False
    return True

#Bryan
def tenants_details():
    loadlist = []
    mlist = []

    while True:
        tenant_name = input("Enter name: ")
        if validname(tenant_name):
            pass
        else:
            print("Invalid name.....Please try again")
            option = input("1.Continue\n2.Exit\nSelect option: ")
            if option == '2':
                break
            else:
                continue

        phone_number = input("Enter phone number: ")
        if validphone(phone_number):
            pass
        else:
            print("Invalid number......Please try again")
            option = input("1.Continue\n2.Exit\nSelect option: ")
            if option == '2':
                break
            else:
                continue

        id_number = input("Enter IC number: ")
        if validic(id_number):
            pass
        else:
            print("Invalid number.....Please try again")
            option = input("1.Continue\n2.Exit\nSelect option: ")
            if option == '2':
                break
            else:
                continue

        place_of_birth = input("Enter Place of Birth: ")
        if validpob(place_of_birth):
            pass
        else:
            print("Invalid place")
            option = input("1.Continue\n2.Exit\nSelect option: ")
            if option == '2':
                break
            else:
                continue

        city_of_birth = input("Enter City of Birth: ")
        if validcity(city_of_birth):
            pass
        else:
            print("Invalid city.....")
            option = input("1.Continue\n2.Exit\nSelect option: ")
            if option == '2':
                break
            else:
                continue

        work_history = input("Enter work history: ")
        if validwork(work_history):
            pass
        else:
            print("Invalid work_history")
            option = input("1.Continue\n2.Exit\nSelect option: ")
            if option == '2':
                break
            else:
                continue

        current_employer = input("Enter current employer: ")
        if validemployer(current_employer):
            pass
        else:
            print("Invalid....Please try again")
            option = input("1.Continue\n2.Exit\nSelect option: ")
            if option == '2':
                break
            else:
                continue

        mlist.append(tenant_name)
        mlist.append(phone_number)
        mlist.append(id_number)
        mlist.append(place_of_birth)
        mlist.append(city_of_birth)
        mlist.append(work_history)
        mlist.append(current_employer)
        loadlist.append(mlist)
        print(loadlist)
        break


    with open("Tenant details.txt", "a") as tenant_files:
        for record in loadlist:
            for collections in record:
                tenant_files.write(collections)
                tenant_files.write(",")
        tenant_files.write("\n")

#Bryan

def readfile():
    with open("Tenant details.txt", "r") as tenant_files:
        for record in tenant_files:
            print(record.rstrip().rstrip(","))

#Bryan


def modifyDta():
    list = []
    search = input("Enter data to search: ")
    with open("Tenant details.txt","r") as files:
        for data in files:
            data = data.rstrip('\n').split(',')
            list.append(data)
            if data[0] == search:
                print(f'''data1 :{data[0]}
data2 :{data[1]}
data3 :{data[2]}
data4 :{data[3]}
data5 :{data[4]}
data6 :{data[5]}
data7 :{data[6]}''')

    option = int(input("Select which data replace: "))
    newData = input("Enter new Data: ")
    with open("Tenant details.txt","w") as modify:
        for index, data in enumerate(list):
            if data[0] == search:
                data[option] = newData
                list[index] = data

        for records in list:
            for collection in records:
                modify.write(collection)
                modify.write(',')
            modify.write('\n')

#Bryan


def removeData():
    import os
    search = input("Enter name to search: ")
    with open("Tenant details.txt","r") as ipt:
        with open("Delete.txt","w") as opt:
            for line in ipt:
                if search not in line.strip('\n'):
                    opt.write(line)

    os.replace('Delete.txt','Tenant details.txt')

#Bryan



def apartment_menu():
    choice = input(
        "Welcome to the apartment menu! Please enter: " + "\n" + "1) Read" + "\n" + "2) Insert" + "\n" + "3) Modify" + "\n" + "4) Delete" + "\n" + "5) Quit" + "\n" + "What would you like to do?: ")

    if choice == "1":
        apartment_read()
    elif choice == "2":
        apartment_insert()
    elif choice == "3":
        apartment_modify()
    elif choice == "4":
        apartment_delete()
    elif choice == "5":
        return main_menu()
    else:
        print("Error! Enter only 1/2/3/4/5")

def apartment_read():
  try:
    file = open('apartment.txt', 'r')
    read = file.readlines()
    modified = []

    for line in read:
      modified.append(line.strip())

    print(modified)

  except:
    print("Apartment text file has not been created")


#Ivan


def apartment_insert() :
    open("apartment.txt", "a")
    file = open('apartment.txt', 'r+')

    apartment_id = input("Please enter new apartment ID (eg. A001): ")


    if len(apartment_id) > 0:
        DOA = input("Please enter new date of acquisition (DD/MM/YYYY): ")
        square_footage = int(input("Please enter new square footage (ft2): "))
        expected_rent = int(input("Please enter new expected rent (RM): "))
        ICNo = input("Please enter new past tenant's IC No. (eg. 012345-02-0123): ")
        Name = input("Please enter new past tenant's name (eg. Adam Tan): ")
        file.write(apartment_id + "," + DOA + "," + str(square_footage) + "," + str(expected_rent) + "," + ICNo + "," + Name + "\n")
    else:
        print("Please enter a valid apartment ID! Try again!")


    file.close()



#Ivan


def apartment_modify():
    import os
    try:
        #read the existing file and writing data to a new file
        fh_r = open("apartment.txt", "r")
        fh_w = open("temp.txt", "w")

        apartment_id = input("Enter apartment ID to replace record: ")

        s = ' '
        while(s):
            s=fh_r.readline()
            L=s.split(",")
            if len(s)>0:
                if (L[0])==apartment_id:
                    apartment_id = input("Please enter new apartment ID: ")
                    DOA = input("Please enter new date of acquisition: ")
                    square_footage = input("Please enter new square footage: ")
                    expected_rent = input("Please enter new expected rent: ")
                    ICNo = input("Please enter new past tenant's IC No.: ")
                    Name = input("Please enter new past tenant's name: ")
                    fh_w.write(apartment_id+","+DOA+","+square_footage+","+expected_rent+","+ICNo+","+Name+"\n")
                else:
                    fh_w.write(s)


        fh_w.close()
        fh_r.close()
        os.remove("apartment.txt")
        os.rename("temp.txt", "apartment.txt")

    except:
        print("Apartment text file does not exist")


#Ivan

def apartment_delete():
    import os
    try:
        # read the existing file and writing data to a new file
        fh_r = open("apartment.txt", "r")
        fh_w = open("temp.txt", "w")

        apartment_id = input("Enter apartment ID to delete record: ")

        s = ' '
        while (s):
            s = fh_r.readline()
            L = s.split(",")
            if len(s) > 0:
                if (L[0]) != apartment_id:
                    fh_w.write(s)

        fh_w.close()
        fh_r.close()
        os.remove("apartment.txt")
        os.rename("temp.txt", "apartment.txt")

    except:
        print("Apartment file does not exist")

#Ivan

def pasttenant_menu():
    choice = input("Welcome to the past tenant menu! Please enter: "+"\n"+"1) Read"+"\n"+"2) Insert"+"\n"+"3) Modify"+"\n"+"4) Delete"+"\n"+"5) Quit"+"\n"+"What would you like to do?: ")

    if choice=="1":
        pasttenant_read()
    elif choice=="2":
        pasttenant_insert()
    elif choice =="3":
        pasttenant_modify()
    elif choice =="4":
        pasttenant_delete()
    elif choice =="5":
        return main_menu()
    else:
        print("Error! Enter only 1/2/3/4/5")


#Ivan

def pasttenant_read():
  try:
    file = open('pasttenant.txt', 'r')
    read = file.readlines()
    modified = []

    for line in read:
      modified.append(line.strip())

    print(modified)
  except:
    print("Past tenant text file has not been created")



#Ivan

def pasttenant_insert() :
    open("pasttenant.txt", "a")
    file = open('pasttenant.txt', 'r+')

    ICNo = input("Please enter past tenant's IC no. (eg. 012345-02-0123): ")


    if len(ICNo) > 0:
        name = input("Please enter past tenant's name. (eg. Adam Tan): ")
        phoneNo = input("Please enter past tenant's phone no. (eg. 012-3456789): ")
        email = input("Please enter past tenant's email. (eg. adam@gmail.com): ")
        address = input("Please enter past tenant's address (eg. 3, Lorong Merah...): ")
        placeofbirth = input("Please enter past tenant's place of birth (eg. Kuala Lumpur): ")
        occupation = input("Please enter past tenant's occupation (eg. Manager): ")
        file.write(ICNo + "," + name + "," + phoneNo + "," + email+ "," + address + "," + placeofbirth + "," + occupation + "\n")
    else:
        print("Please enter a valid IC no.: ")


    file.close()



#Ivan

def pasttenant_modify():
    import os
    try:
        #read the existing file and writing data to a new file
        fh_r = open("pasttenant.txt", "r")
        fh_w = open("temp.txt", "w")

        ICNo = input("Enter past tenant's IC No to replace record: ")

        s = ' '
        while(s):
            s=fh_r.readline()
            L=s.split(",")
            if len(s)>0:
                if (L[0])==ICNo:
                    ICNo = input("Please enter past tenant's IC no.: ")
                    name = input("Please enter past tenant's name.: ")
                    phoneNo = input("Please enter past tenant's phone no.: ")
                    email = input("Please enter past tenant's email.: ")
                    address = input("Please enter past tenant's address: ")
                    placeofbirth = input("Please enter past tenant's place of birth: ")
                    occupation = input("Please enter past tenant's occupation: ")
                    fh_w.write(ICNo+","+name+","+phoneNo+","+email+","+address+","+placeofbirth+","+occupation+"\n")
                else:
                    fh_w.write(s)


        fh_w.close()
        fh_r.close()
        os.remove("pasttenant.txt")
        os.rename("temp.txt", "pasttenant.txt")
    except:
      print("Past tenant text file has not been created")



#Ivan

def pasttenant_delete():
    import os
    try:
        #read the existing file and writing data to a new file
        fh_r = open("pasttenant.txt", "r")
        fh_w = open("temp.txt", "w")

        ICNo = input("Enter past tenant IC No to delete record: ")

        s = ' '
        while(s):
            s=fh_r.readline()
            L=s.split(",")
            if len(s)>0:
                if (L[0])!=ICNo:
                    fh_w.write(s)

        fh_w.close()
        fh_r.close()
        os.remove("pasttenant.txt")
        os.rename("temp.txt", "pasttenant.txt")

    except:
      print("Past tenant text file has not been created")


#Ivan

login_menu()







































