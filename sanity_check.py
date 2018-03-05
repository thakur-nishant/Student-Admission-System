import builtins
import admission

# Please do not change anything is this file!
# Also, please do not submit this file.
# Check for use of functions print and input.
# IMPORTANT!
# If you are getting this error message here:
# line xx, in <module>
#     our_print = print
# invalid syntax: <string>, line xx, pos yy
# Then you are using the wrong version of Python! Make sure you have Python 3!
our_print = print
our_input = input


def disable_print(*args):
    raise Exception("You must not call print anywhere in your code!")


def disable_input(*args):
    raise Exception("You must not call input anywhere in your code!")

builtins.print = disable_print
builtins.input = disable_input

# Type check admission.is_special_admission_case
result = admission.is_special_admission_case('Test 123', 2015)
assert isinstance(result, bool), \
       '''admission.is_special_admission_case should return a bool, but returned {0}
       '''.format(type(result))

# Type check admission.get_final_course_mark
result = admission.get_final_course_mark(100, 'Fort McMurray High', 2016, 1)
assert isinstance(result, int), \
       '''admission.get_final_course_mark should return an int, but returned {0}
       '''.format(type(result))

# Type check admission.compute_average_mark
result = admission.compute_average_mark(100, 'Fort McMurray High', 2016)
assert isinstance(result, int), \
       '''admission.compute_average_mark should return an int, but returned {0}
       '''.format(type(result))

# Type check admission.is_admitted
result = admission.is_admitted(100, 'Fort McMurray High', 2016, 81)
assert isinstance(result, bool), \
       '''admission.is_admitted should return a bool, but returned {0}
       '''.format(type(result))

our_print("""
Hooray! The type checker passed!
This does NOT necessarily mean that your functions are correct!

It does mean that the functions in admission.py:
- are named correctly,
- take the correct number of arguments, and
- return the correct types.  

Be sure to thoroughly test your functions yourself before submitting.""")

builtins.print = our_print
builtins.input = our_input
