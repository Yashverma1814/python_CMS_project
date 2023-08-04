import os
import csv
import datetime

#menu for CMS

def title():
    title = "\nContact Management System"
    print(title)
    deisgn = "------------------------------>>"
    print(deisgn);
    print('')

class contact_management:
    contact_field = ['Name', 'Number', 'Email','Address']
    contact_datafile = 'data.csv'
    contact_data = []

    #creator function
    def create(self):
        os.system('cls')
        title()
        print('Create Contact')
        #getting input from user one by one 
        for field in self.contact_field:
            self.contact_detail = input('Enter '+field+':\t')
            print("")
            self.contact_data.append(self.contact_detail)
        
        # entering data to csv file
        with open(self.contact_datafile,'a') as file:
            write = csv.writer(file)
            write.writerows([self.contact_data])

        self.contact_data=[]

        print('\n Success \n')

    #viewer function
    def view(self):
        os.system('cls')
        title()

        print('All Contacts')
        
        count = 0

        #getting data out of CSV file
        with open(self.contact_datafile,'r') as file:
            read = csv.reader(file)
            for data1 in read:
                if len(data1)>0:
                    count += 1

            print('Total Contacts: ',count)
        
        #display data
        with open(self.contact_datafile,'r') as file:
            read = csv.reader(file)
            if os.path.getsize(self.contact_datafile) == 0:
                print("EMPTY")
            else:
                for fields in self.contact_field:
                    print('{0:10}'.format(fields),end="\t\t")
                print("")

                for data in read:
                    for item in data:
                        print('{0:<10}'.format(item),end='\t\t')
                    print("")
        print('\n')
        input("Press enter to exit")
        os.system('cls')


    #Search Functionality
    def search(self):
        os.system('cls')
        title()

        print('Search Contacts\n')

        self.contact_match = 'false'
        search_value = ''
        search_by = input('type N for Search by Name or type M for Search by Number: \t').lower()
        if search_by=='n':
            search_value = input('Enter Name: \t')
        elif search_by == 'm':
            search_value = input('Enter Number: \t')        

        for fields in self.contact_field:
            print('{0:10}'.format(fields),end="\t\t")
        print("")

        with open(self.contact_datafile,'r') as file:
            read = csv.reader(file)
            for data in read:
                if len(data)>0:
                    if search_value ==data[0] or search_value == data[1]:
                        self.contact_match = 'true'
                        print('{:<10}\t\t{:<10}\t\t{:<10}\t\t{:<10}'.format(data[0],data[1],data[2],data[3]))
        if(self.contact_match == 'false'):
            print('\n Not Found\n')
        
        exit = input('press enter to exit')

    #delete functionality
    def delete(self):
        os.system('cls')
        title()

        print('Delete Contacts\n')

        self.contact_match = 'false'
        delete_value = input('Enter Name: \t')
        update_list = []

        with open(self.contact_datafile,'r') as file:
            read = csv.reader(file)
            for data in read:
                if len(data)>0:
                    if delete_value != data[0]:
                        update_list.append(data)
                    else:
                        self.contact_match = 'true'

        if self.contact_match == 'true':
            with open(self.contact_datafile,'w') as file:
                write = csv.writer(file)
                write.writerows(update_list)
                print('\ndeleted successfully\n')
        if self.contact_match == 'false':
            print('\nThe data you want to delete is not found!!\n')
    
        exit= input('press enter to exit')


contact_class = contact_management()

os.system('cls')
title()

while True:
    print("1. View contacts")
    print("2. Search contact")
    print("3. Create contact")
    print("4. Delete contact")
    print("5. Exit software \n")

    option = int(input("Enter your Option : \t"));

    if option==1:
        contact_class.view()
        title()
    
    if option==2:
        contact_class.search()
        os.system('cls')
        title()

    if option==3:
        contact_class.create()
        os.system('cls')
        title()

    if option==4:
        contact_class.delete()
        os.system('cls')
        title()

    if option==5 :
        break

    if option>5 or option<1:
        print('\nInvalid Option!!\n');
        input('Press enter to continue again');
        os.system('cls')
        title()

    


