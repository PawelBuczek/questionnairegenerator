import pytest

# there are probably other tests that we could think of here, but these 3 will be good for our learning purposes.

# to run all these test, simply type  "pytest"  in the console (may require to kill it and open again)
# to run only specific test, for example:  pytest -k 'test_indicators_are_correctly_added'


def test_indicators_are_correctly_added():
    pass  # delete this line
    # purpose of this test is to check `add_indicators` method from file `b_add_indicators` (will require import).
    # for this we don't really need to care about any text file.
    # that's because this method takes in string and returns string.

    # so we may just pass some text to this method, try for example: "Test\nX 1st line\nX 2nd line"
    # and assert if what was returned is the same as expected, for example: "Test\n:regional_indicator_a: 1st line\n:regional_indicator_b: 2nd line"


def test_questionnaire_is_generated_for_Jul2023():
    pass  # delete this line
    # this test can be for any month, Jul2023 is just an example. (Yes, checking one random month should should is sufficient for our needs.)
    # first of all - try to run method `generate_questionnaire` from file `a_generate_questionnaire` with correct text for given month passed (will require import).
    # then run this test and check manually if it works. Was file `questionnaire.txt` populated?
    # after that is done, try to check if the file is ok.

    # this can be done in a few ways, but I would recommend copying generated file with a different name (something like `test_Jul2023_questionnaire.txt`).
    # and then in this test asserting if newly generated file is the same as our saved copy (copy will not be modified, unless business requirements change).
    # with this approach we just need to manually check generated file once, then test is asserting that no changes to the logic are made.


def test_questionnaire_generation_and_indicators_adding_work_together():
    pass  # delete this line
    # final test. Some would say this is not needed since we already checked pretty much everything, but for learning purposes let's roll with it.
    # Here we need to first run `generate_questionnaire` from file `a_generate_questionnaire` with correct text passed as a parameter.
    # then we need to modify `questionnaire.txt` file, for example by removing lines 10 through 20.
    # then we run `add_indicators_to_file` method from file `b_add_indicators`.
    # and finally we check if what was created is what was expected. Here, to make it a bit different from the previous test, let's change our tactic.
    # instead of comparing txt file with a saved copy, lets make 3 assertions:
    # - is `questionnaire.txt` file third line starting with ":regional_indicator_b"
    # - is `questionnaire.txt` file first line NOT starting with ":regional_indicator"
    # - is `questionnaire.txt` file NOT ending with an empty line (the last character is not '\n')
