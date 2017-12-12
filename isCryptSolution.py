#A cryptarithm is a mathematical puzzle for which the goal is to find the correspondence between letters and digits,
#such that the given arithmetic equation consisting of letters holds true when the letters are converted to digits.
#You have an array of strings crypt, the cryptarithm, and an an array containing the mapping of letters and digits,
#solution. The array crypt will contain three non-empty strings that follow the structure: [word1, word2, word3], 
#which should be interpreted as the word1 + word2 = word3 cryptarithm.
#If crypt, when it is decoded by replacing all of the letters in the cryptarithm with digits using the mapping in
#solution, becomes a valid arithmetic equation containing no numbers with leading zeroes, the answer is true. If it
#does not become a valid arithmetic solution, the answer is false.

def isCryptSolution(crypt, solution):

    word3len=len(crypt[2])
    num1 = []
    num2 = []
    num3 = []

    def wordgrab(crypt, solution):
    #here i pull a single word from crypt and pass it to wordtonum. I also pass which # word i'm sending
        word_count=0
        for word in crypt:
            word_count=word_count+1
            word_letter(word,word_count, solution)

    
    def word_letter(word, word_count, solution):
        #here i will pass in a single word and this will pull out each letter #in turn and pass it to letter_num
        letter_count=0
        for letter in word:
            letter_count+=1
            letter_num(letter, word_count, solution,letter_count)

        
    def letter_num(letter, word_count, solution,letter_count):
        # here i take a letter and use solution to translate the letter to a #num and create num1-3
        for list in solution:
            if letter == list[0] and word_count==1:
                num1.append(list[1])
            elif letter == list[0] and word_count==2:
                num2.append(list[1])
            elif letter == list[0] and word_count==3:
                num3.append(list[1])
                
        if word_count==3 and letter_count==word3len:
            global answer
            answer = output(num1, num2, num3)
        
    def output(num1, num2, num3):

        if num1[0]=='0' and len(num1)>1:
            return False
        elif num2[0]=='0' and len(num2)>1:
            return False
        elif num3[0]=='0' and len(num3)>1:
            return False
        number1=int("".join(num1))
        number2=int("".join(num2))
        number3=int("".join(num3))
        if number1 + number2==number3:
            return True
        else:
            return False
        
    wordgrab(crypt, solution)
    return(answer)
