# Rotate given n characters of string to left

print("Enter a string:")
string=input()

print("\nEnter number of characters to rotate left:")
n=int(input())

print("\nNew string after rotation is:")
print(string[n:]+string[:n])
