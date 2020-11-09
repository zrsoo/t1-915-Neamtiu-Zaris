# Source code for Test 1 program. Success!

# UI Section

def start_console():
    dict_functions = {}

    while True:
        str_input = input("Type your command: ")

        if str_input == "exit":
            return

        li_input = str_input.split()
        user_command = li_input[0]
        mamba_function = li_input[1]

        # print(li_input)
        li_command = format_input(mamba_function) # = ['function_name', 'function_name(p1,p2,...,pn)=p1(+|-)p2(+|-)p3(+|-)...(+|-)pn']
        # print(li_command)
        if user_command == "add":
            str_command = format_command(li_command[1])
            # print(str_command)
            li_command[1] = str_command
            add_function(dict_functions, li_command)
            # print(dict_functions)
        elif user_command == "list":
            try:
                print(dict_functions[li_input[1]])
            except KeyError:
                print("The command you are trying to list was not previously defined.")
        elif user_command == "eval":
            # print(dict_functions[li_input[1]])
            # print(li_input)
            # print(li_command)
            try:
                str_exec = dict_functions[li_command[0]] + "\nprint(" + li_command[1] + ")"
            except Exception as ex:
                print("The command you are trying to evaluate contains syntax errors, " + ex)
            # print(str_exec)
            exec(str_exec)


# Functions section
def add_function(dict_functions, li_function):
    """
    Adds to the dictionary of commands the pair 'function_name': 'function_code'
    example {'alternate_sum': 'def alternate_sum(first,second,third,fourth): return first-second+third-fourth'}
    :param dict_functions: the dictionary of commands.
    :param li_function: the list containing the respective strings of the command.
    :return:
    """
    dict_functions[li_function[0]] = li_function[1]


def format_input(str_function):
    """Returns a list containing the name of the function on the first position and the user input on the second one"""
    paranthesis_index = str_function.find('(')
    function_name = str_function[:paranthesis_index]
    return [function_name, str_function]


def format_command(str_command):
    str_command = "def " + str_command
    str_command = str_command.replace("=", ": return ")
    return str_command


# Start
start_console()

