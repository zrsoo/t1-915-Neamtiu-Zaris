# Source code for Test 1 program. Success!

# UI Section

def start_console():
    dict_functions = {}

    while True:
        str_input = input("Type your command: ")

        li_input = str_input.split()
        user_command = li_input[0]
        mamba_function = li_input[1]

        # print(li_input)
        li_command = format_input(mamba_function)

        if li_input[0] == "add":
            add_function(dict_functions, li_command)
            # print(dict_functions)
        elif li_input[0] == "list":
            pass


# Functions section
def add_function(dict_functions, li_function):
    """
    Appends the function string, of the form ("function_name(p1,p2,...,pn)=p1(+/-)....pn) to the dictionary of functions
    :param li_functions: The dictionary of functions
    :param function: The string containing the specifications of the function
    :return: The list
    """
    dict_functions[li_function[0]] = li_function[1]


def format_input(str_function):
    """Returns a list containing the name of the function on the first position and the user input on the second one"""
    paranthesis_index = str_function.find('(')
    function_name = str_function[:paranthesis_index]
    return [function_name, str_function]





# Start
start_console()

