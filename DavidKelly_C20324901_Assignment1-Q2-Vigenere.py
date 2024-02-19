## Advanced Security
## Assignment 1

## David Kelly
## 15/Oct/2023

## Qs. 2 - Vigenere Cipher

# 1. User enters their message.
# 2. User enters key.
# 3. Message and key string converted to array of chars.
# 4. Program creates key array as long as the message.
#    e.g. key = [pencil]
#         message = [cerealcomesbeforemilk]
#         key string = [pencilpencilpencilpen]
# 5. Message is encrypted/decrypted using the Vigenere cipher algorithm.
# 6. Resulting message is displayed to the user.
# 7. Ask if they want to go again.


userMessage = ""
key = ""
userOption = 1
alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
newIndex = 0
finalMessage = ""
again = 'y'


# Function to convert an array of characters into a string.
def ArrayToString(s): 

	# Initialization of string to "" 
	new = "" 

	# Traverse in the string.
	for x in s: 
		new += x 

	# Return string.
	return new


# Loop the program in case the user wants to try again.
while again == 'y':
    
    messageArr = []
    keyArr = []
    finalArr = []
    
    # Prompt the user to input their message and their key
    print("\nThis program will encrypt or decrypt your message using the Vigenere Cipher method.\n")
    userMessage = input("Enter your message here:\n")
    key = input("\nEnter your key:\n")

    # Ask user to choose encryption or decryption.
    userOption = int(input("\nDo you want to Encrypt or Decrypt this message?\nEncrypt (1)\nDecrypt (2)\n"))

    # Convert the user's message and key to lower case
    userMessage = userMessage.lower()
    key = key.lower()

    # Convert the user's message from string to array of chars. E.g., "hello" => ['h','e','l','l','o']

    for char in userMessage:
        messageArr.append(char)



    # This creates the recursive key. E.g., "pencil" => "pencilpencilpencilpen...(etc.)" 

    for x in range(len(messageArr)):    # Continue for the length of the message.
        
        for y in key:
        
            # Check if the key array length is shorter than the message.
            if len(keyArr) < len(messageArr):

                # Add each next letter to the key array.            
                keyArr.append(y)

            else:
                break



    # Vigenere cipher algorithm.

    # Identify each letter in the key array.
    for i in range(len(keyArr)):

        for j in range(len(alph)):

            # If the key letter is found:
            if keyArr[i] == alph[j]:
                
                # Identify each letter in the user's message.
                for k in range(len(alph)):
                    
                    # If the message letter is found:
                    if messageArr[i] == alph[k]:

                        # ENCRYPTION
                        if userOption == 1:
                            # To get the encrypted letter's index, add the previous indexes together, and then modulo 26.
                            newIndex = (j + k) % 26
                        
                        # DECRYPTION
                        elif userOption == 2:
                            # To get the decrypted letter's index, subtract the previous indexes together, and then modulo 26.
                            newIndex = (k - j) % 26

                        # Error: user entered neither 1 or 2
                        else:
                            pass
                        
                        
                        # Add this encrypted letter to the final array.
                        finalArr.append(alph[newIndex])

                        break
                                            
                    # This handles any characters not in the alphabet. E.g. space, comma, colon, etc.
                    elif messageArr[i] not in alph:
                        finalArr.append(messageArr[i])
                        break

                    else:
                        pass

            else:
                pass


    # Convert the final array into a string (to make it easier for the user to read).
    finalMessage = ArrayToString(finalArr)

    if userOption == 1:

        # Display the encrypted message to the user.
        print("\nYour encrypted message is:\n"+finalMessage)

    elif userOption == 2:

        # Display the decrypted message to the user.
        print("\nYour decrypted message is:\n"+finalMessage)
    
    else:
        print("\nError: Invalid Option. Choose only 1 to encrypt, or 2 to decrypt.")

    # Give user the option to try again.
    again = input("\nWould you like to try again? (y/n): ")

# End while loop

print("\nGoodbye\n")