# This class manages a string message and includes methods to both
# encrypt and decrypt a message


class CodedMessage:

    # Constructor
    def __init__(self, msgIn):
        self.message = msgIn

    # Encrypt a message.  Assumes message is in clear text.
    # Parameter 'shift' indicates the positions alphabetic positions
    # forward to shift the message characters.
    def encrypt(self, shift):
        length = len(self.message)
        encrypted = ""
        for i in range(length):
            if self.message[i].isalpha() == True:
                newChar = self.message[i].upper()
                newCharInt = ord(newChar) + shift
                if newCharInt > ord("Z"):
                    newCharInt = newCharInt - 26
                encrypted += chr(newCharInt)
            else:
                encrypted += self.message[i]
        return encrypted

    # Decrypt a message.  Assumes message is coded.
    # Parameter 'shift' indicates the positions alphabetic positions
    # backward to shift the message characters.
    def decrypt(self, shift):
        length = len(self.message)
        decrypted = ""
        for i in range(length):
            if self.message[i].isalpha() == True:
                newChar = self.message[i].upper()
                newCharInt = ord(newChar) - shift
                if newCharInt < ord("A"):
                    newCharInt = newCharInt + 26
                decrypted += chr(newCharInt)
            else:
                decrypted += self.message[i]
        return decrypted
