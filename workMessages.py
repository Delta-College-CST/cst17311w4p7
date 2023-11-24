# This program performs simple tests of the CodedMessage
# class by encrypting and decrypting messages

from CodedMessage import CodedMessage 

testMessage1 = "DELTA COLLEGE"
messageObj1 = CodedMessage(testMessage1)
print(testMessage1)
print(messageObj1.encrypt(3))

print()

testMessage2 = "WSJXAEVI HIZIPSTIVW EVI GSSP"
messageObj2 = CodedMessage(testMessage2)
print(testMessage2)
print(messageObj2.decrypt(4))

