import os

Contacts = []
AddOption = 0
AddMultipleOption = 1
RemoveOption = 2
RemoveMultipleOption = 3
RemoveAllOption = 4
ViewAllContactsOption = 5
ViewAllNamesOption = 6
LookUpOption = 7
CheckContactOption = 8
NumContactsOption = 9
ChangeNameOption = 10
ChangeHomePhoneOption = 11
ChangeCellPhoneOption = 12
ChangeWorkPhoneOption = 13
ChangeAddressOption = 14
ChangeRelationshipOption = 15
QuitOption = 16
validOptions = ["a", "am", "r", "rm", "ra", "v", "vn", "l", "ca", "gm", "cn", "ch", "cc", "cw", "ca", "cr", "q"]

def CommandOptions():
	print("--------------------------------------")
	print("Command Options:")
	print("")
	print("Enter ({0:s}-{1:s}) to add contact".format(validOptions[AddOption], validOptions[AddOption].upper()))
	print("Enter ({0:s}-{1:s}) to add multiple contacts".format(validOptions[AddMultipleOption], validOptions[AddMultipleOption].upper()))
	print("Enter ({0:s}-{1:s}) to remove contact".format(validOptions[RemoveOption], validOptions[RemoveOption].upper()))
	print("Enter ({0:s}-{1:s}) to remove multiple contacts".format(validOptions[RemoveMultipleOption], validOptions[RemoveMultipleOption].upper()))
	print("Enter ({0:s}-{1:s}) to remove all contacts".format(validOptions[RemoveAllOption], validOptions[RemoveAllOption].upper()))
	print("Enter ({0:s}-{1:s}) to view all contacts".format(validOptions[ViewAllContactsOption], validOptions[ViewAllContactsOption].upper()))
	print("Enter ({0:s}-{1:s}) to view all names".format(validOptions[ViewAllNamesOption], validOptions[ViewAllNamesOption].upper()))
	print("Enter ({0:s}-{1:s}) to look up contact".format(validOptions[LookUpOption], validOptions[LookUpOption].upper()))
	print("Enter ({0:s}-{1:s}) to check if contact is in contacts".format(validOptions[CheckContactOption], validOptions[CheckContactOption].upper()))
	print("Enter ({0:s}-{1:s}) to get number of contacts".format(validOptions[NumContactsOption], validOptions[NumContactsOption].upper()))
	print("Enter ({0:s}-{1:s}) to change contact name".format(validOptions[ChangeNameOption], validOptions[ChangeNameOption].upper()))
	print("Enter ({0:s}-{1:s}) to change contact home phone number".format(validOptions[ChangeHomePhoneOption], validOptions[ChangeHomePhoneOption].upper()))
	print("Enter ({0:s}-{1:s}) to change contact cell phone number".format(validOptions[ChangeCellPhoneOption], validOptions[ChangeCellPhoneOption].upper()))
	print("Enter ({0:s}-{1:s}) to change contact work phone number".format(validOptions[ChangeWorkPhoneOption], validOptions[ChangeWorkPhoneOption].upper()))
	print("Enter ({0:s}-{1:s}) to change contact address".format(validOptions[ChangeAddressOption], validOptions[ChangeAddressOption].upper()))
	print("Enter ({0:s}-{1:s}) to change contact relationship".format(validOptions[ChangeRelationshipOption], validOptions[ChangeRelationshipOption].upper()))
	print("Enter ({0:s}-{1:s}) to quit".format(validOptions[QuitOption], validOptions[QuitOption].upper()))
	print("--------------------------------------\n")
	
def MoveFile():
	if os.path.exists("C:\\Users\\earlj\\Desktop\\PasswordManager\\contacts.txt"):
		os.remove("C:\\Users\\earlj\\Desktop\\PasswordManager\\contacts.txt")
	os.rename("C:\\Users\\earlj\\Desktop\\PasswordManager\\newFile.txt", "C:\\Users\\earlj\\Desktop\\PasswordManager\\contacts.txt")
	
def WriteAccountsToFile():
	tempFile = open("C:\\Users\\earlj\\Desktop\\PasswordManager\\newFile.txt", "w")
	for contact in Contacts:
		for index in range(len(contact)):
			tempFile.write(contact[index] + ";")
		tempFile.write("\n")
	tempFile.close()
	
def ReadAccountsFromFile():
	if os.path.exists("C:\\Users\\earlj\\Desktop\\PasswordManager\\contacts.txt") and os.path.getsize("C:\\Users\\earlj\\Desktop\\PasswordManager\\contacts.txt") > 0:
		contactsFile = open("contacts.txt", "a+")
		contactsFile.seek(0, 0)
		lines = contactsFile.readlines()
		if len(lines) > 0:
			for line in lines:
				line = line.strip('\n')
				contactsInfo = line.split(";")
				Contacts.append([contactsInfo[0], contactsInfo[1], contactsInfo[2], contactsInfo[3], contactsInfo[4], contactsInfo[5]])
		contactsFile.close()

ReadAccountsFromFile()
CommandOptions()
userChoice = input("Enter command option> ")
userChoice = userChoice.lower()

while userChoice != validOptions[QuitOption]:
	while userChoice not in validOptions:
		print("Not a valid command option. Please enter a valid command option.")
		userChoice = input("Enter command option> ")
		userChoice = userChoice.lower()
	if userChoice == validOptions[AddOption]:
		found = False
		contactName = input("Enter contact name> ")
		for contact in Contacts:
			if contactName in Contacts:
				changeAccount = input("{0:s} account already exists. Would you like to change the contact details for {0:s} account (y/Y)/(n/N)?".format(serviceName))
				changeAccount = changeAccount.lower()
				if changeAccount == "y":
					changeType = input("Enter 'cn' to change contact name, 'ch' to change home phone number, 'cc' to change cell phone number, 'cw' to change work phone number, 'ca' to change contact address, \
					'cr' to change contact relationship.")
					changeType = changeType.lower()
					if changeType == "cn":
						newContactName = input("Enter a new contact name> ")
						while newContactName == "":
							newContactName = input("You entered an empty contact name.\nPlease enter a valid contact name> ")
						accounts[serviceName] = (newUserName, password)
						if accounts[serviceName] == (newUserName, password):
							print("Successfully changed contact name to {0:s}\n".format(newContactName))
					elif changeType == "ch":
						newHomePhoneNumber = accounts[contactName][0]
						newHomePhoneNumber = input("Enter a home phone number> ")
						while newPassword == "":
							newPassword = input("You entered an empty phone number.\nPlease enter a valid phone number> ")
						accounts[serviceName] = (userName, newPassword)
						if accounts[serviceName] == (userName, newPassword):
							print("Successfully changed {0:s} phone number to {1:s}\n".format(serviceName, newPassword))
					elif changeType == "cc":
						cellPhoneNumber = accounts[serviceName][0]
						newCellPhoneNumber = input("Enter a new cell phone password> ")
						while newPassword == "":
							newPassword = input("You entered an empty cell phone number.\nPlease enter a valid cell phone number ")
						accounts[serviceName] = (userName, newPassword)
						if accounts[serviceName] == (userName, newPassword):
							print("Successfully changed account password for {0:s} to {1:s}\n".format(serviceName, newPassword))
					elif changeType == "cw":
						userName = accounts[serviceName][0]
						newPassword = input("Enter a new password> ")
						while newPassword == "":
							newPassword = input("You entered an empty password.\nPlease enter a valid password> ")
						accounts[serviceName] = (userName, newPassword)
						if accounts[serviceName] == (userName, newPassword):
							print("Successfully changed account password for {0:s} to {1:s}\n".format(serviceName, newPassword))
					elif changeType == "ca":
						userName = accounts[serviceName][0]
						newPassword = input("Enter a new password> ")
						while newPassword == "":
							newPassword = input("You entered an empty password.\nPlease enter a valid password> ")
					elif changeType == "cr":
						userName = accounts[serviceName][0]
						newPassword = input("Enter a new password> ")
						while newPassword == "":
							newPassword = input("You entered an empty password.\nPlease enter a valid password> ")
		verification = input("Is {0:s} the correct contact name? ".format(contactName))
		if verification.lower() == "y":
			homePhone = input("Enter home phone for {0:s} contact> ".format(contactName))
			verification = input("Is {0:s} the correct home phone number for {1:s} contact? ".format(homePhone, contactName))
			if verification.lower() == "y":
				cellPhone = input("Enter cell phone number for {0:s} contact> ".format(contactName))
				verification = input("Is {0:s} the correct cell phone number for {1:s} contact? ".format(cellPhone, contactName))
				if verification.lower() == "y":
					workPhone = input("Enter work phone number for {0:s} contact> ".format(contactName))
					verification = input("Is {0:s} the correct work phone number for {1:s} contact? ".format(workPhone, contactName))
					if verification.lower() == "y":
						address = input("Enter address for {0:s} contact> ".format(contactName))
						verification = input("Is {0:s} the correct address for {1:s} contact? ".format(address, contactName))
						if verification.lower() == "y":
							relationship = input("Enter relationship for {0:s} contact> ".format(contactName))
							verification = input("Is {0:s} the correct relationship for {1:s} contact? ".format(relationship, contactName))
						else:
							pass
					else:
						pass
				else:
					pass
			else:
				pass
		else:
			pass
		contactToAdd = [contactName, homePhone, cellPhone, workPhone, address, relationship]
		Contacts.append([contactName, homePhoneNumber, cellPhoneNumber, workPhoneNumber, contactAddress, contactRelationship])
		if contactToAdd in Contacts:
			print("Successfully added contact {0:s} to database\n".format(contactName))
		else:
			print("Contact {0:s} could not be added to the database at this time\n".format(contactName))
	elif userChoice == validOptions[AddMultipleOption]:
		found = False
		index = 0
		contactName = input("Enter contact name (e to end)> ")
		while contactName != "e":
			for contact in Contacts:
				if contact[0] == contactName:
					found = True
					break
				index += 1
			if found == True:
				changeContact = input("{0:s} contact already exists. Would you like to change the home phone, cell phone, work phone, address, or relationship for {1:s} contact (y/Y)/(n/N)?".format(contactName, contactName))
				changeContact = changeContact.lower()
				if changeContact == "y":
					changeType = input("Enter 'hp' to change home phone, 'cp' to change cell phone, 'wp' to change work phone, 'ca' to change address, or 'cr' to change relationship.")
					changeType = changeType.lower()
					if changeType == "hp":
						newHomePhoneNumber = input("Enter a new home phone number> ")
						while newHomePhoneNumber == "":
							newHomePhoneNumber = input("You entered an empty home phone number.\nPlease enter a valid home phone number> ")
						Contacts[index][1] = newHomePhoneNumber
						if Contacts[index][1] == newHomePhoneNumber:
							print("Successfully changed contact home phone number for {0:s} to {1:s}\n".format(contactName, newHomePhoneNumber))
						else:
							print("Unsuccessfully changed contact home phone number for {0:s} to {1:s}\n".format(contactName, newHomePhoneNumber))
					elif changeType == "cp":
						newCellPhoneNumber = input("Enter a new cell phone number> ")
						while newCellPhoneNumber == "":
							newCellPhoneNumber = input("You entered an empty cell phone number.\nPlease enter a valid cell phone number> ")
						Contacts[index][2] = newCellPhoneNumber
						if Contacts[index][2] == newCellPhoneNumber:
							print("Successfully changed contact cell phone number for {0:s} to {1:s}\n".format(contactName, newCellPhoneNumber))
						else:
							print("Unsuccessfully changed contact cell phone number for {0:s} to {1:s}\n".format(contactName, newCellPhoneNumber))
					elif changeType == "wp":
						newWorkPhoneNumber = input("Enter a new work phone number> ")
						while newWorkPhoneNumber == "":
							newWorkPhoneNumber = input("You entered an empty work phone number.\nPlease enter a valid work phone number> ")
						Contacts[index][3] = newWorkPhoneNumber
						if Contacts[index][3] == newWorkPhoneNumber:
							print("Successfully changed contact work phone number for {0:s} to {1:s}\n".format(contactName, newWorkPhoneNumber))
						else:
							print("Unsuccessfully changed contact work phone number for {0:s} to {1:s}\n".format(contactName, newWorkPhoneNumber))
					elif changeType == "ca":
						newAddress = input("Enter a new address> ")
						while newAddress == "":
							newAddress = input("You entered an empty address.\nPlease enter a valid address> ")
						Contacts[index][4] = newAddress
						if Contacts[index][4] == newAddress:
							print("Successfully changed contact address for {0:s} to {1:s}\n".format(contactName, newAddress))
						else:
							print("Unsuccessfully changed contact address for {0:s} to {1:s}\n".format(contactName, newAddress))
					elif changeType == "cr":
						newRelationship = input("Enter a new relationship> ")
						while newRelationship == "":
							newRelationship = input("You entered an empty relationship.\nPlease enter a valid relationship> ")
						Contacts[index][5] = newRelationship
						if Contacts[index][5] == newRelationship:
							print("Successfully change contact relationship for {0:s} to {1:s}\n".format(contactName, newRelationship))
						else:
							print("Unsuccessfully changed contact relationship for {0:s} to {1:s}\n".format(contactName, newRelationship))
			else:
				verification = input("Is {0:s} the correct contact name? ".format(contactName))
				if verification.lower() == "y":
					homePhone = input("Enter home phone for {0:s} contact> ".format(contactName))
					verification = input("Is {0:s} the correct home phone number for {1:s} contact? ".format(homePhone, contactName))
					if verification.lower() == "y":
						cellPhone = input("Enter cell phone number for {0:s} contact> ".format(contactName))
						verification = input("Is {0:s} the correct cell phone number for {1:s} contact? ".format(cellPhone, contactName))
						if verification.lower() == "y":
							workPhone = input("Enter work phone number for {0:s} contact> ".format(contactName))
							verification = input("Is {0:s} the correct work phone number for {1:s} contact? ".format(workPhone, contactName))
							if verification.lower() == "y":
								address = input("Enter address for {0:s} contact> ".format(contactName))
								verification = input("Is {0:s} the correct address for {1:s} contact? ".format(address, contactName))
								if verification.lower() == "y":
									relationship = input("Enter relationship for {0:s} contact> ".format(contactName))
									verification = input("Is {0:s} the correct relationship for {1:s} contact? ".format(relationship, contactName))
								else:
									pass
							else:
								pass
						else:
							pass
					else:
						pass
				else:
					pass
				contactToAdd = [contactName, homePhone, cellPhone, workPhone, address, relationship]
				Contacts.append([contactName, homePhoneNumber, cellPhoneNumber, workPhoneNumber, contactAddress, contactRelationship])
				if contactToAdd in Contacts:
					print("Successfully added contact {0:s} to database\n".format(contactName))
				else:
					print("Contact {0:s} could not be added to the database at this time\n".format(contactName))
			contactName = input("Enter contact name (e to end)> ")
	elif userChoice == validOptions[RemoveOption]:
		found = False
		index = 0
		if len(Contacts) <= 0:
			print("No contacts available to remove. Add contacts prior to removing them from the list.\n")
		else:
			contactName = input("Enter contact name> ")
			while not found:
				for contact in Contacts:
					if contact[0] == contactName:
						found = True
						index += 1
						break
				if found == False:
					print("Contact name not in database. Please enter a contact name that is in the accounts list")
					contactName = input("Enter contact name> ")
			remove = input("You have choosen to remove the {0:s} contact from the database! Are you sure you would like to do this (y/Y)/(n/N)? ".format(serviceName))
			remove = remove.lower()
			if remove == "y":
				Contacts.remove(Contacts[index])
			elif remove == "n":
				print("Contact removal cancelled by user.\n")
			if Contacts.find(Contacts[index]) == -1:
				print("Contact {0:s} successfully removed from database!")
			else:
				print("Contact {0:s} not successfully removed from database!")
	elif userChoice == validOptions[RemoveMultipleOption]:
		found = False
		missing = True
		index = 0
		if len(Contacts) <= 0:
			print("No contacts available to remove. Add contacts prior to removing them from the database.\n")
		else:
			contactName = input("Enter contact name (e to end)> ")
			while contactName != "e":
				while found == False:
					for contact in Contacts:
						if contact[0] == contactName:
							found = True
							break
						index += 1
					if found == False:
						print("Contact name not in database. Please enter a contact that is in the accounts list.")
						contactName = input("Enter contact name> ")
				remove = input("You have choosen to remove the {0:s} contact from the database! Are you sure you would like to do this (y/Y)/(n/N)? ".format(contactName))
				remove = remove.lower()
				if remove == "y":
					Contacts.remove(Contacts[index])
					for contact in Contacts:
						if contact == Contacts[index]:
							missing = False
					if missing == False:
						print("{0:s} contact was successfully removed from the database.\n".format(contactName))
					else:
						print("Failed to remove {0:s} contact from the database.\n".format(contactName))
				elif remove == "n":
					print("Contact removal cancelled by user.\n")
				contactName = input("Enter contact name (e to end)> ")
	elif userChoice == validOptions[RemoveAllOption]:
		if len(Contacts) <= 0:
			print("No contacts available to remove. Add contacts prior to removing them from the list.\n")
		else:
			remove = input("You have choosen to remove all contacts! Are you sure you would like to do this (y/Y)/(n/N)? ")
			remove = remove.lower()
			if remove == "y":
				Contacts = [[]]
				if len(Contacts) <= 0:
					print("All contacts have successfully been removed!\n")
				else:
					print("Not all contacts were successfully removed! Please try again.")
					print("{0:d} contacts were not successfully removed.\n".format(len(Contacts)))
			elif remove == "n":
				print("Accounts removal cancelled by user.\n")
	elif userChoice == validOptions[ViewAllContactsOption]:
		counter = 1
		if len(Contacts) <= 0:
			print("No contacts to display! Please add contacts to view all contacts.\n")
		else:
			print("\nAll Contacts View\n")
			for contact in Contacts:
				print("Contact {0:d}: ".format(counter))
				print("\tContact Name: {0:s}".format(contact[0]))
				print("\tHome: {0:s}".format(contact[1]))
				print("\tCell: {0:s}".format(contact[2]))
				print("\tWork: {0:s}".format(contact[3]))
				print("\tAddress: {0:s}".format(contact[4]))
				print("\tRelationship: {0:s}\n".format(contact[5]))
				counter += 1
			counter = 1
			print("")
	elif userChoice == validOptions[ViewAllNamesOption]:
		numberOfContacts = 1
		if len(Contacts) <= 0:
			print("No contacts to display! Please add contacts to view all contacts.\n")
		else:
			print("\nAll Contacts View\n")
			for contact in Contacts:
				print("\tContact {0:d}: {1:s}".format(counter, contact[0]))
				counter += 1
			counter = 1
			print("")
	elif userChoice == validOptions[LookUpOption]:
		found = False
		index = 0
		if len(Contacts) <= 0:
			print("No contacts to display! Please add contacts to look up account.\n")
		else:
			contactName = input("Enter contact name> ")
			while found == False:
				for contact in Contacts:
					if contact[0] == contactName:
						found = True
				if found == False:
					print("Contact name {0:s} not in contacts. Please enter a valid contact name that is in contact list".format(contactName))
					contactName = input("Enter contact name> ")
				index += 1
			homePhone = Contacts[index][1]
			cellPhone = Contacts[index][2]
			workPhone = Contacts[index][3]
			address = Contacts[index][4]
			relationship = Contacts[index][5]
			print("\t{0:s} Home Phone Number: {1:s}".format(contactName, homePhone))
			print("\t{0:s} Cell Phone Number: {1:s}".format(contactName, cellPhone))
			print("\t{0:s} Work Phone Number: {1:s}".format(contactName, workPhone))
			print("\t{0:s} Address: {1:s}".format(contactName, address))
			print("\t{0:s} Relationship: {1:s}\n".format(contactName, relationship))
	elif userChoice == validOptions[CheckContactOption]:
		found = False
		contactName = input("Enter contact name> ")
		for contact in Contacts:
			if contact[0] == contactName:
				found = True
		if found == True:
			print("Contact name {0:s} is in the contacts.".format(contactName))
		elif found == False:
			print("Contact name {0:s} is not in the contacts.".format(contactName))
	elif userChoice == validOptions[NumContactsOption]:
		print("Number of contacts: {0:d}\n".format(len(Contacts)))
	elif userChoice == validOptions[ChangeNameOption]:
		if len(Contacts) <= 0:
			print("No contacts saved! Please add contacts before attempting to change a name.\n")
		else:
			serviceName = input("Enter service name> ")
			while serviceName not in accounts:
				print("Service name {0:s} not in accounts list. Please enter a valid service name that is in accounts list".format(serviceName))
				serviceName = input("Enter service name> ")
			userName = input("Enter current username> ")
			password = accounts[serviceName][1]
			while userName != accounts[serviceName][0]:
				userName = input("Incorrect user name! Please enter the correct username for {0:s}".format(serviceName))
			print("User name has been verified!\n")
			newUserName = input("Enter a new username> ")
			if newUserName != "":
				accounts[serviceName] = (newUserName, password)
			if accounts[serviceName] == (newUserName, password):
				print("Successfully changed account user name for {0:s} to {1:s}\n".format(serviceName, newUserName))
	elif userChoice == validOptions[ChangeHomePhoneOption]:
		if len(accounts) <= 0:
			print("No accounts stored in list! Please add accounts before attempting to change a password.\n")
		else:
			serviceName = input("Enter service name> ")
			while serviceName not in accounts:
				print("Service name {0:s} not in accounts list. Please enter a valid service name that is in accounts list".format(serviceName))
				serviceName = input("Enter service name> ")
			userName = accounts[serviceName][0]
			password = input("Enter current password> ")
			while password != accounts[serviceName][1]:
				password = input("Incorrect password! Please enter the correct password for {0:s}".format(serviceName))
			print("Password has been verified!\n")
			newPassword = input("Enter a new password> ")
			if newPassword != "":
				accounts[serviceName] = (userName, newPassword)
			if accounts[serviceName] == (userName, newPassword):
				print("Successfully changed account password for {0:s} to {1:s}\n".format(serviceName, newPassword))
	elif userChoice == validOptions[ChangeCellPhoneOption]:
		if len(accounts) <= 0:
			print("No accounts stored in list! Please add accounts before attempting to change a password.\n")
		else:
			serviceName = input("Enter service name> ")
			while serviceName not in accounts:
				print("Service name {0:s} not in accounts list. Please enter a valid service name that is in accounts list".format(serviceName))
				serviceName = input("Enter service name> ")
			userName = accounts[serviceName][0]
			password = input("Enter current password> ")
			while password != accounts[serviceName][1]:
				password = input("Incorrect password! Please enter the correct password for {0:s}".format(serviceName))
			print("Password has been verified!\n")
			newPassword = input("Enter a new password> ")
			if newPassword != "":
				accounts[serviceName] = (userName, newPassword)
			if accounts[serviceName] == (userName, newPassword):
				print("Successfully changed account password for {0:s} to {1:s}\n".format(serviceName, newPassword))
	elif userChoice == validOptions[ChangeWorkPhoneOption]:
		if len(accounts) <= 0:
			print("No accounts stored in list! Please add accounts before attempting to change a password.\n")
		else:
			serviceName = input("Enter service name> ")
			while serviceName not in accounts:
				print("Service name {0:s} not in accounts list. Please enter a valid service name that is in accounts list".format(serviceName))
				serviceName = input("Enter service name> ")
			userName = accounts[serviceName][0]
			password = input("Enter current password> ")
			while password != accounts[serviceName][1]:
				password = input("Incorrect password! Please enter the correct password for {0:s}".format(serviceName))
			print("Password has been verified!\n")
			newPassword = input("Enter a new password> ")
			if newPassword != "":
				accounts[serviceName] = (userName, newPassword)
			if accounts[serviceName] == (userName, newPassword):
				print("Successfully changed account password for {0:s} to {1:s}\n".format(serviceName, newPassword))
	elif userChoice == validOptions[ChangeAddressOption]:
		if len(accounts) <= 0:
			print("No accounts stored in list! Please add accounts before attempting to change a password.\n")
		else:
			serviceName = input("Enter service name> ")
			while serviceName not in accounts:
				print("Service name {0:s} not in accounts list. Please enter a valid service name that is in accounts list".format(serviceName))
				serviceName = input("Enter service name> ")
			userName = accounts[serviceName][0]
			password = input("Enter current password> ")
			while password != accounts[serviceName][1]:
				password = input("Incorrect password! Please enter the correct password for {0:s}".format(serviceName))
			print("Password has been verified!\n")
			newPassword = input("Enter a new password> ")
			if newPassword != "":
				accounts[serviceName] = (userName, newPassword)
			if accounts[serviceName] == (userName, newPassword):
				print("Successfully changed account password for {0:s} to {1:s}\n".format(serviceName, newPassword))
	elif userChoice == validOptions[ChangeRelationshipOption]:
		if len(accounts) <= 0:
			print("No accounts stored in list! Please add accounts before attempting to change a password.\n")
		else:
			serviceName = input("Enter service name> ")
			while serviceName not in accounts:
				print("Service name {0:s} not in accounts list. Please enter a valid service name that is in accounts list".format(serviceName))
				serviceName = input("Enter service name> ")
			userName = accounts[serviceName][0]
			password = input("Enter current password> ")
			while password != accounts[serviceName][1]:
				password = input("Incorrect password! Please enter the correct password for {0:s}".format(serviceName))
			print("Password has been verified!\n")
			newPassword = input("Enter a new password> ")
			if newPassword != "":
				accounts[serviceName] = (userName, newPassword)
			if accounts[serviceName] == (userName, newPassword):
				print("Successfully changed account password for {0:s} to {1:s}\n".format(serviceName, newPassword))
	CommandOptions()
	userChoice = input("Enter command option> ")
	userChoice = userChoice.lower()
	
WriteAccountsToFile()

MoveFile()
	
exit()
