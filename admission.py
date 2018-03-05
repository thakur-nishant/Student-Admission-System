import data
import math
"""
Most post-secondary institutions use some kind of computer system to help manage admissions. Often, these programs 
are used to handle straightforward admissions cases, freeing up human time to work on the more complex ones. 
The purpose of the system you are working on is to determine if students meet cutoffs for admission to degree 
programs and for consideration for scholarships.

Admission to degrees is based on marks in high school courses a student has taken. In our admission program, 
we are given two marks for every course in a student's application. The first mark is their grade on coursework, 
and the second is their grade on the final exam. Their final mark in the course is the average of those two marks.

In the 2016-2017 academic year, post-secondary institutions in Alberta needed to update their admissions systems 
to handle a special group of incoming students. In May 2016, out-of-control wildfires forced the evacuation of 
about 90000 people from Fort McMurray, a city in northern Alberta. This included students who were in their final 
year of high school, preparing to write final exams. Due to the evacuation, most students were 
not able to write their exams.

To accommodate students in this special situation, post-secondary institutions in Alberta changed the admission 
criteria for these students; they would be admitted based on their coursework marks up to the evacuation, 
and not on the coursework plus exam mark typically used. These special criteria were only applied to students who 
came from particular schools in the affected year. This accommodation works as follows:
1) If a student is not a special case, then his/her admission mark is the average of term mark and final 
mark for the course. A special case is a student form an affected city, starting final year in 2016.
2) Else, his/her admission mark for a course is his/her term mark.
Example 1: 
John is a special case. He has earned 80 in the term work for course 1, 70 for course 2, and 60 for course 3.
Then his average mark is (80+70+60)/3=70.
Example 2:
Mary is not a special case. She has earned 80 in term work for course 1, 70 for course 2, and 60 for course 3.
She has also earned 80 in final for course 1, 90 for course 2, and 100 for course 3. Then her average mark is
((80+80)/2+(70+90)/2+(60+100)/2)/3=80.
If cutoff=75, then John is not admitted and Mary is admitted.
You are not allowed to import packages other than the packages imported above.
"""


def is_special_case_school(school_name):
    """
    :param school_name: a string, representing a school name
    :return: True, if school_name is a Fort McMurray school. Otherwise return False.
    Please do not change this function.
    """
    return school_name in data.setup_school_list()


def is_special_admission_case(school_name, year):
    """
    :param school_name: a string, representing a school name
    :param year: a positive integer
    :return: True, if school_name is a special case school, and year is the starting calendar year of
    academic year 2016-2017. 
    To earn full marks, you must call is_special_case_school in your implementation.
    """
    return is_special_case_school(school_name) and year == 2016


def get_final_course_mark(student_id, school_name, year, course_num):
    """
    :param student_id: A positive integer, student ID
    :param school_name: A string, students's school name
    :param year: A positive integer, year
    :param course_num: An integer from 1 to 3
    :return: An int, the student_id mark for the course course_num to be used for admission
    """
    final_marks = data.final_marks()
    term_marks = data.term_marks()
    student_final_mark = final_marks[student_id][year][course_num]
    student_term_mark = term_marks[student_id][year][course_num]
    # Compute and return student's admission mark
    # If a student is a special admission case (call is_special_admission_case function for full marks!)
    # then his/her final_course_mark matches his/her student_term_mark.
    # Else his/her final_course_mark mark is the average of student_term_mark and student_final_mark.
    # Hint: Average of two numbers si computed by adding them and dividing the result by 2.
    # Please use math.ceil to round up decimal results
    if is_special_admission_case(school_name, year):
        final_course_mark = student_term_mark
    else:
        final_course_mark = (student_term_mark + student_final_mark) / 2

    return math.ceil(final_course_mark)


def compute_average_mark(student_id, school_name, year):
    """
    :param student_id: A positive integer, student ID
    :param school_name: A string, students's school name
    :param year: A positive integer, year 
    :return: student's average mark for courses 1,2 and 3
    Your may use a for loop or while loop. Your choice will not affect your grade, as long as your code is correct.
    Please make sure to call get_admission_mark. Else you will get a zero mark in this function.
    Hint: The average of three numbers can be computed by summing up the given numbers and diving their sum by 3.
    After computing the average, please round up the result by using the function math.ceil.
    For example, math.ceil(3.2) returns 4.
    """
    total = 0
    for course_num in range(1, 4):
        total += get_final_course_mark(student_id, school_name, year, course_num)

    average = total / 3
    return math.ceil(average)


def is_admitted(student_id, school_name, year, cutoff):
    """
    :param student_id: A positive integer, student ID
    :param school_name: A string, students's school name
    :param year: A positive integer, year 
    :param cutoff: a positive integer
    :return: a boolean, True indicates the student is admitted, False otherwise
    The student is admitted iff his average mark (computed using the function compute_average_mark) is greater or
    equal to cutoff mark. Please make sure to call compute_average_mark. Else you will get a zero mark in this function.
    """
    avg = compute_average_mark(student_id, school_name, year)

    if avg >= cutoff:
        return True
    else:
        return False

