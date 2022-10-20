import nltk
import re

program = input("Enter the given string: ")

count = 0

Identifiers= []
Keywords= []
Punctuations= []
Arithmetic_Operators= []
Logical_Operators =[]
Constants= []
Parenthesis=[]

def remove_Spaces(program):
    scanned_Program = []
    for line in prog:
        if (line.strip() != ''):
            scanned_Program.append(line.strip())
    return scanned_Program

def remove_Comments(program):
    program_Multi_Comments_Removed = re.sub("/\*[^*]*\*+(?:[^/*][^*]*\*+)*/", "", program)
    program_Single_Comments_Removed = re.sub("//.*", "", program_Multi_Comments_Removed)
    program_Comments_removed = program_Single_Comments_Removed
    return program_Comments_removed

assign_Keywords = "auto|break|case|char|const|continue|default|do|double|else|enum|extern|float|for|goto|if|int|long|register|return|short|signed|sizeof|static|struct|switch|typedef|union|unsigned|void|volatile|while|string|class|struc|include"
assign_Arrithmetic_Operators = "(\+)|(-)|(=)|(\*)|(/)|(%)"
assign_Logical_Operators = "(\--)|(<=)|(>=)"
assign_Constants = "^(\d+)$"
assign_Punctuations = "[\[@&~!#$\^\|{}\]:;<>?,\.']|\(\)|\(|\)|{}|\[\]|\""
assign_Identifiers = "^[a-zA-Z_]+[a-zA-Z0-9_]*"
assign_Parenthesis ="\{}|\[]|\(\)"

program_Comments_removed = remove_Comments(program)
prog = program_Comments_removed.split('\n')

scanned_Prog = remove_Spaces(prog)
scanned_Program = '\n'.join([str(elem) for elem in scanned_Prog])

scanned_Program_lines = scanned_Program.split('\n')
match_counter = 0


Source_Code=[]
for line in scanned_Program_lines:
        Source_Code.append(line)

display_counter = 0
for line in Source_Code:
    count = count + 1
    if(line.startswith("#include")):
        tokens = nltk.word_tokenize(line)
    else:
        tokens = nltk.wordpunct_tokenize(line)
    for token in tokens:
        if(re.findall(assign_Keywords, token)):
            Keywords.append(token)
        elif (re.findall(assign_Arrithmetic_Operators, token)):
            Arithmetic_Operators.append(token)
        elif (re.findall(assign_Constants,token)):
            Constants.append(token)
        elif (re.findall(assign_Punctuations, token)):
            Punctuations.append(token)
        elif (re.findall(assign_Identifiers, token)):
            Identifiers.append(token)
        elif (re.findall(assign_Logical_Operators, token)):
           Logical_operators.append(token)
        elif (re.findall(assign_Parenthesis, token)):
           Parenthesis.append(token)

print("Keywords","(",len(Keywords),"):",Keywords)
print("\n")

print("Arithmetic Operators","(",len(Arithmetic_Operators),"):",Arithmetic_Operators)
print("\n")

print("Constants","(",len(Constants),"):",Constants)
print("\n")

print("Punctuations","(",len(Punctuations),"):",Punctuations)
print("\n")

print("Identifiers","(",len(Identifiers),"):",Identifiers)
print("\n")

print("Logical Operators","(",len(Logical_Operators),"):",Logical_Operators)
print("\n")

print("Parenthesis","(",len(Parenthesis),"):",Parenthesis)
print("\n")