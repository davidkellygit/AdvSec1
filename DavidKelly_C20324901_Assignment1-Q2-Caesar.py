## Advanced Security
## Assignment 1

## David Kelly
## 10/Oct/2023

## Qs. 2 - Caesar Cipher

# A. Program asks user if they want to (1) Encrypt, or (2) Decrypt.
# B. User inputs their message.
# C. The characters are shifted up/down the alphabet 3 places.
# D. The new message is printed to the user.

again = 'y'
alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
key = ['d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c']


print("\nThis is a Caeser Cipher program that can encrypt or decrypt your message.\n")



# Function to convert an array of characters into a string.
def ArrayToString(s): 

	# initialization of string to "" 
	new = "" 

	# traverse in the string 
	for x in s: 
		new += x 

	# return string 
	return new

# End Functions



# Loop the program in case the user wants to try again.
while again == 'y':

    userText = ""
    userOption = 1
    userArr = []
    finalArr = []
    i = 0
    j = 0

    # User enters message
    userText = input("Enter your message here:\n")
    
    # Convert any upper case to lower case
    userText = userText.lower()
    
    # Ask user to choose encryption or decryption.
    userOption = int(input("\nDo you want to Encrypt or Decrypt this message?\nEncrypt (1)\nDecrypt (2)\n"))    


    # -----------------------Encryption-----------------------
    
    if userOption == 1:

        # Convert their string text into separated characters in an array, e.g., "hello" => [h,e,l,l,o]

        for char in userText:
            userArr.append(char)

        ## Debugging...
        #print("Your new array is:", userArr)

        # Find each letter from the message in the alphabet array.
        while i < len(userArr):
            j = 0
            
            while j < len(alph):

                # If the letter is found,
                if userArr[i] == alph[j]:

                    # Overwrite it with the corresponding 'key' array letter (3 letters down).
                    userArr[i] = key[j]

                    ## Debugging...
                    #print("Pass", i,", your new array is:", userArr)

                    break

                else:
                    pass

                j = j + 1
            # End inner while

            i = i + 1
        # End outer while

        # Display the message to the user.   
        print("\nYour encrypted message is:\n" + ArrayToString(userArr))

    # End if


    # -----------------------Decryption-----------------------
    
    elif userOption == 2:
        
        # Convert their string text into separated characters in an array, e.g., "hello" => [h,e,l,l,o]

        for char in userText:
            userArr.append(char)

        ## Debugging...
        #print("Your new array is:", userArr)

        # Find each letter from the message in the alphabet array.
        while i < len(userArr):
            j = 0
            
            while j < len(alph):

                # If the letter is found,
                if userArr[i] == key[j]:

                    # Overwrite it with the corresponding 'alph' array letter (3 letters down).
                    userArr[i] = alph[j]

                    ## Debugging...
                    #print("Pass", i,", your new array is:", userArr)

                    break

                else:
                    pass

                j = j + 1
            # End inner while

            i = i + 1
        # End outer while

        # Display the message to the user.   
        print("\nYour decrypted message is:\n" + ArrayToString(userArr))
                

    # End elif

    else:
        print("\nError: This is an invalid option. Please choose either 1 to encrypt or 2 to decrypt.")

    # End else

    # Give user the option to try again.
    again = input("\nWould you like to try again? (y/n): ")

# End while

print("\nGoodbye\n")