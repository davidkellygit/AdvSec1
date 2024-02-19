## Advanced Security
## Assignment 1

## David Kelly
## 16/Oct/2023

## Qs. 6 - Hill Cipher

key = [1, 0,
       10, 4] # BAKE
messageArr = [0, 0,
              0, 0] # AAAA
alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
textArr = []
finalArr = [0, 0,
            0, 0]


# Prompt the user for a 4-letter word.
print("\nThis program will encrypt any 4-letter word using the Hill Cipher method.\n")
userText = input("Enter your 4-letter word:\n")
userText = userText.lower()

# Error checking - Ensure it's exactly 4 letters.
while len(userText) != 4:

    print("\nError: Must have exactly 4 letters.")
    userText = input("Try again:\n")
    userText = userText.lower()

# Convert string to array.
for char in userText:
    textArr.append(char)


# Create the user's message Array.
for i in range(len(messageArr)):

    for j in range(len(alph)):
        
        if textArr[i] == alph[j]:
            
            messageArr[i] = j

# Show the user what their matrices look like
print("\nThe key (BAKE) is", key)
print("Your message is", messageArr)

# Cross multiply the arrays like matrices.
finalArr[0] = ((key[0] * messageArr[0]) + (key[1] * messageArr[2])) % 26
finalArr[1] = ((key[0] * messageArr[1]) + (key[1] * messageArr[3])) % 26
finalArr[2] = ((key[2] * messageArr[0]) + (key[3] * messageArr[2])) % 26
finalArr[3] = ((key[2] * messageArr[1]) + (key[3] * messageArr[3])) % 26

# Display the resulting array.

print("\nYour encrypted matrix is:")
print("[",finalArr[0],",",finalArr[1],",")
print(finalArr[2],",",finalArr[3],"]\n")