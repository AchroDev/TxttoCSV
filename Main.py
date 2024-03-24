#Define the list to hold records from the data file.
recordsList = []
recordCount = 0

#Learn to Program with Python: #Chapter 9 File Input/Output - Defining a Path to a File / File Handle

#Open the file and read data into the list variable then close the file
file = open("C:\PATHTO\Data.txt", 'r')

for line in file:
    #Append record to the end of the list and strip the whitespace
    recordsList.append(line.strip())
#Close the file
file.close()

#Append new record to the list
recordsList.append("5,Brady,Bobby,4222 Clinton Way,Los Angeles,CA")

#Open New CSV file for writing
file = open("C:\PATHTO\PromoCredit.csv", 'w') #  w for writing
#Write file header to file
file.write("Customer ID, Last Name, First Name, Address, City, State, Promo Credit\n")
#file.write("\n")

#Write each record in the list to file and add a new comma separated value to the end of each record to reflect promotional credit
for record in recordsList:
    file.write(record)
    file.write(",$500\n")
    recordCount = recordCount+1
#Close the File
file.close()

print("There were", recordCount, "records written to the promo credits csv file.")