import string

def is_precedence(char):
    if char == '|':
        return 1
    if char == '.':
        return 2
    if char == '>' or char == '<' or char == '=' or char == '#':
        return 3
    if char == '-' or char == '+':
        return 4
    if char == '*' or char == '/':
        return 5
    if char == '^':
        return 6
    return 0


def is_operators(char):
    return (char == '|' or char == '.' or char == '>' or char == '<' or
            char == '=' or char == '#' or char == '+' or char == '-' or
            char == '*' or char == '/' or char == '^' or char == '(' or
            char == ')')


def is_operands(char):
    return (char in string.ascii_lowercase or
            char in string.ascii_uppercase or
            char in string.digits)


def is_lexical_error(exp):
    error = False
    try:
        for a_char in exp:
            print(a_char)
            if not is_operands(a_char) and not is_operators(a_char) and a_char != '(' and a_char != ')':
                error = True
                break
        if error is True:
            raise Exception('Lexical error occurred.')
    except Exception as e:
        print(e)
    finally:
        return error


def is_parantheses_error(exp):
    stack = []
    error = False
    try:
        for a_char in exp:
            if a_char == '(':
                stack.append(a_char)
            else:
                if len(stack) == 0:
                    error = True
                if '(' != stack.pop():
                    error = True
        if len(stack) == 0:
            error = False
        else:
            error = True
        if error is True:
            raise Exception('Lexical error occurred.')
    except Exception as e:
        print(e)
    finally:
        return error


def is_syntax_error(exp):
    error = False
    try:
        for an_idx in range(len(exp)):
            if is_operators(exp[an_idx]) and is_operators(exp[an_idx+1]):
                error = True
                break
            elif is_operands(exp[an_idx]) and is_operands(exp[an_idx+1]):
                error = True
                break
            if is_operators(exp[an_idx]) and (exp[an_idx+1]) == None:
                error = True
                break
        if error is True:
            raise Exception('Lexical error occurred.')
    except Exception as e:
        print(e)
    finally:
        return error


def infix_to_postfix(exp): 
    stack = [] 
    postfix = '' 
    for a_char in exp:
        if not is_operators(a_char):
            postfix += a_char
        elif a_char == '(':
            stack.append('(')
        elif a_char ==')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] != '(' and is_precedence[a_char] <= is_precedence[stack[-1]]:
                postfix += stack.pop() 
            stack.append(a_char) 
    while stack:
        postfix += stack.pop()
    return postfix  

def lexsim():
    #exp = "(A+B)*c"
    exp = "(a+b)/2"
    is_lexical_error(exp)
    is_parantheses_error(exp)
    is_syntax_error(exp)
    print('\ninfix expression: ',exp) 
    print('postfix expression: ',infix_to_postfix(exp))

if __name__ == "__main__":
    lexsim()