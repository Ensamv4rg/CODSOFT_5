def base_splitter(expression, target=None):
    if target is None:
        target = set('+-*/^%')
    
    bracket_count = 0  # Tracks the level of brackets
    splits = []  # To store the split parts and operators
    last_split = 0  # Index of the last split point
    
    
    for i, char in enumerate(expression):
        if char == '(':
            bracket_count += 1
        elif char == ')':
            bracket_count -= 1
        elif char in target and bracket_count == 0 and expression[i-1] not in target:
            # Append the left split and the operator
            splits.append(expression[last_split:i].strip())
            splits.append(char)
            last_split = i + 1  # Update last split to the next character after the operator
    
    # Append the final segment after the last operator
    splits.append(expression[last_split:].strip())
    if splits[0] == '': splits[0] = 0.0
    
    
    return splits

def calculate(first,operator,second):
    

    #Code to handle Negative input unproblematically
    try:
        if first == '':
            if operator == '+':
                first = 1
            elif operator == '-':
                first = -1
            else:
                raise ValueError(f'Invalid Operation {operator}{second}')
            operator = '*'          
    except:
        pass


    match operator:
        case '*':return float(first) * float(second)
        case '+':return float(first) + float(second)
        case '-':return float(first) - float(second)
        case '/':return float(first)/float(second)
        case '^':return float(first)**float(second)


    order = ['^','/','*','+','-']

def solver(expression):#Uses BODMAS
    expression=expression
    if type(expression) ==float: return expression #More or less ends the recursion
    try:
        if expression[0] == '-': return float(expression[1:])*-1 # ends the recursion to avoid problems
    except:
        raise SyntaxError(f'Misplaced/Mismatched Operators')
    #Locates all operators and returns their indexs in the list
    for index,argument in enumerate(expression):
        #Simplifies arguments with Brackets
        if '(' in str(argument):
            start = argument.index('(')
            end = len(argument) -1 
            while argument[end] != ')':
                end -=1

            expression_in_bracket = argument[start+1: end]
            expression[index] = solver(base_splitter(expression_in_bracket))[0]

    #creates a dictionary of operators(arrranged with BODMAS in mind), and thier indexes
    operators = set('+-*/^')  
    indices = {'^':[],'/':[],'*':[],'+':[], '-':[]}
    for i,char in enumerate(expression):
        if char in operators and expression[i-1] not in operators: indices[char].append(i)
    
    #Removes Blank operators 
    for operator in indices.copy():
        if not indices[operator]: del indices[operator]
    
    if indices == {}:return expression[0:] #When Indices are empty, it implies the expression is just a number.


    #Computing results
    replace_index_map = {} #dictionary containing Index to be removed

    for operator in indices:
        for index in indices[operator]:

            #Simplification of complex expressions
            
            first_number_positiion = 1
            second_number_positiion = 1

            #Looks for numbers on otherside of the operators
            while expression[index-first_number_positiion] is None:
                first_number_positiion+=1
            while expression[index+second_number_positiion] is None:
                second_number_positiion+=1

            first_number = solver(expression[index-first_number_positiion])
            second_number = solver(expression[index+second_number_positiion])


            #sets the index to be replaced in the dictionary. Removes the extra unneeded Indexes
            replace_index_map[index-first_number_positiion]= calculate(first_number,operator,second_number)#Holds the computed Value
            replace_index_map[index],replace_index_map[index+second_number_positiion] = None,None
            for key,value in replace_index_map.items(): expression[key] = value
            
        #Replace Indexes before continuing
        
        
    answer = solver(expression)
    return solver(expression)
        
   
    #Step 1. Look for brackets:(B)

    



    #return value

def error_handling(expression):
    if expression[0] in ['/','^','*']:raise SyntaxError('Expression cannot begin with an operator')
    if expression.upper() != expression.lower():raise SyntaxError('Expression should not contain letters')
    if expression.count('(') != expression.count(')'): raise SyntaxError("A '(' was not closed ")
    
    
    if expression[-1] in ['/','^','*']:expression=expression[:-1]
    if any(char in ['{','['] for char in expression):
        replace_map = {'[':'(', '{':'(', ']':')','{':')'}
        expression = ''.join(map(lambda char: replace_map.get(char, char), expression))
    
    #Code to properly handle brackets being used for multiplication
    i = len(expression) - 1
    while i >= 1:
        char = expression[i]
        if char == '(' and expression[i-1] not in ['/','^','*','(','+','-']:
            expression = expression[:i] + '*' + expression[i:]
            
        i -= 1
    expression = expression.strip()
    

    return expression

def compute(expression):
    values = solver(base_splitter(error_handling(expression)))
    value = [element for element in values if bool(element)][0]#Gets all possible Values of of it
    print(value)


expression = input("""
    Enter an expression to evalute. Standard Matehmatical operations apply.
""")
compute(expression)
