import pytest
import b_add_indicators
import a_generate_questionnaire

# to run all these test, simply type  "pytest"  in the console (may require to kill it and open again)

def test_indicators_are_correctly_added():
    my_input = "Test\nX 1st line\nX 2nd line"  # preparing text as our input
    my_desired_output = "Test\n:regional_indicator_a: 1st line\n:regional_indicator_b: 2nd line"  # preparing our desired output
    
    my_actual_output = b_add_indicators.add_indicators(my_input)  # running the method, passing our input as parameter, and saving it as output
    
    assert(my_desired_output == my_actual_output)  # asserting if our output is what we exptected

    # note: we could also do all of the above in one line (though it may be less clear) like below:
    # assert("Test\n:regional_indicator_a: 1st line\n:regional_indicator_b: 2nd line" == b_add_indicators.add_indicators("Test\nX 1st line\nX 2nd line"))


def test_questionnaire_is_generated_for_Jul2023():
    with open("test_Jul2023_questionnaire.txt", "r", encoding="utf-8") as f:
        my_desired_output = f.read()  # reading our stored copy into variable

    my_date_in_text_format = "2023-07-01"  # date for our chosen month, could be any day of the month really
    a_generate_questionnaire.generate_questionnaire(my_date_in_text_format)  # generating questionnaire for a given month

    with open("questionnaire.txt", "r", encoding="utf-8") as f:
        my_actual_output = f.read()  # reading created output into variable

    assert(my_desired_output == my_actual_output)  # asserting if our output is what we exptected


def test_questionnaire_generation_and_indicators_adding_work_together():
    my_date_in_text_format = "2031-12-01"
    a_generate_questionnaire.generate_questionnaire(my_date_in_text_format)

    # removing the lines in the next 7 code lines, resource link: https://www.tutorialspoint.com/how-to-delete-specific-line-from-a-text-file-in-python
    with open("questionnaire.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    with open("questionnaire.txt", "w", encoding="utf-8") as f:
        for number, line in enumerate(lines):
            if number < 10 or number > 20:
                f.write(line)
    
    b_add_indicators.add_indicators_to_file()

    with open("questionnaire.txt", "r", encoding="utf-8") as f:
        my_output_lines = f.readlines()  # reading output as lines will make it easier for us to work with them

    assert(my_output_lines[2].startswith(":regional_indicator_b"))
    assert(not my_output_lines[0].startswith(":regional_indicator"))  # we can add 'not' to our assertions to make them easier
    assert(not my_output_lines[-1].endswith("\n"))  # [-1] means last element of the list, last line of our file in this example
