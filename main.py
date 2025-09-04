'''
Build an Arithmetic Formatter Project
Students in primary school often arrange arithmetic problems vertically to make them easier to solve. For example, "235 + 52" becomes:

Example Code
  235
+  52
-----
Finish the arithmetic_arranger function that receives a list of strings which are arithmetic problems, and returns the problems arranged vertically and side-by-side. The function should optionally take a second argument. When the second argument is set to True, the answers should be displayed.

Example
Function Call:

Example Code
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
Output:

Example Code
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
Function Call:

Example Code
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
Output:

Example Code
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
Rules
The function will return the correct conversion if the supplied problems are properly formatted, otherwise, it will return a string that describes an error that is meaningful to the user.

Situations that will return an error:
1.If there are too many problems supplied to the function. The limit is five, anything more will return: 'Error: Too many problems.' 
2.The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be: "Error: Operator must be '+' or '-'."  
3.Each number (operand) should only contain digits. Otherwise, the function will return: 'Error: Numbers must only contain digits.' 
4.Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be: 'Error: Numbers cannot be more than four digits.'
5.If the user supplied the correct format of problems, the conversion you return will follow these rules:
    a.There should be a single space between the operator and the longest of the two operands, the operator will be on the same line as the second operand, both operands will be in the same order as provided (the first will be the top one and the second will be the bottom).
    b.Numbers should be right-aligned.
    c.There should be four spaces between each problem.
    d.There should be dashes at the bottom of each problem. The dashes should run along the entire length of each problem individually. (The example above shows what this should look like.)
Note: open the browser console with F12 to see a more verbose output of the tests.
'''


def arithmetic_arranger(problems, show_answers=False):
    #TODO 1 If there are too many problems supplied to the function. The limit is five, anything more will return: 'Error: Too many problems.'
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    #TODO 2 The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be: "Error: Operator must be '+' or '-'."
    first_lines,second_lines,dashes,answers = [],[],[],[]
    # arithmetics = ''
    for problem in problems:     
        pb = problem.split(" ")   
        left,operator,right = pb
        if operator not in "+-":
            return "Error: Operator must be '+' or '-'."
    
        #TODO 3 Each number (operand) should only contain digits. Otherwise, the function will return: 'Error: Numbers must only contain digits.'
        elif not (left.isdigit() and right.isdigit()):
            return 'Error: Numbers must only contain digits.'
        
        #TODO 4 Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be: 'Error: Numbers cannot be more than four digits.'
        elif len(left) > 4 or len(right) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        # If the user supplied the correct format of problems, the conversion you return will follow these rules:
        else:
            #TODO 5 There should be a single space between the operator and the longest of the two operands, the operator will be on the same line as the second operand, both operands will be in the same order as provided (the first will be the top one and the second will be the bottom).      
            #TODO 7 c.There should be four spaces between each problem.
            max_length =  max(len(left),len(right))  
            second_line = operator + " " + (max_length - len(right))*" " + right 
            second_lines.append(second_line)
            #TODO 6 b.Numbers should be right-aligned.
            first_line = (len(second_line) - len(left))*" " + left 
            first_lines.append(first_line)
            #TODO 8 d.There should be dashes at the bottom of each problem. The dashes should run along the entire length of each problem individually.
            dash = "-" * len(second_line)
            dashes.append(dash)
            # arithmetics += first_line + second_line + dashes
            answer = int(left) + int(right) if operator =="+" else int(left) - int(right)
            answerLine = (len(second_line) - len(str(answer)))*" " + str(answer)
            answers.append(answerLine)
            
    # print(''.join(first_lines)+''.join(second_lines) )
    output = "    ".join(first_lines) +"\n"+"    ".join(second_lines)+"\n"+"    ".join(dashes)
    final_answer = "\n"+"    ".join(answers)
    # if show_answers:
    #     return   f'{"    ".join(first_lines)}\n{"    ".join(second_lines)}\n{"    ".join(dashes)}\n{"    ".join(answers)}'
    # return f'{"    ".join(first_lines)}\n{"    ".join(second_lines)}\n{"    ".join(dashes)}'
    if show_answers:
        return output + final_answer
    return output


print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["1 + 2", "1 - 9380"])}')
print(f'\n{arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])}')
