# test_morse_codecd.py


"""
Powershell statements for setting up the pytest library
    Use within root folder (best if it is a 'test' folder) for each project

pip install pytest

Base testing line: python -m pytest
Gives help screen with list of modules: python -m pytest -h
For more detailed feedback: pytest -v
    -v increases the verbosity
To execute the tests from a specific file: pytest <filename> -v

Markers are used to set various features/attributes to test functions. 
    Pytest provides many inbuilt markers such as xfail, skip and parametrize. 
    Apart from that, users can create their own marker names. 

Markers are applied on the tests using the syntax given below −
    @pytest.mark.<markername>

To use markers, we have to import pytest module in the test file. 
    Define marker names to the tests and run the tests having those marker names.

To run the marked tests, we can use the following syntax −
    pytest -m <markername> -v
    -m <markername> represents the marker name of the tests to be executed

To execute the tests containing a string in its name we can use the following syntax −
    pytest -k <substring> -v
    -k <substring> represents the substring to search for in the test names
"""

# Have morse_code.py declared as a class object
import morse_code as mc

def test_interpreter():
    #assert encode_morse_code("hello/world") == ".... . .-.. .-.. ---/.-- --- .-. .-.. -.."
    #assert decode_morse_code(".... . .-.. .-.. ---/.-- --- .-. .-.. -..") == "HELLO WORLD"
    arg_array = [None, 1, ".-"]
    #assert morse_code_interpreter(arg_array) == "A"
    assert mc.morse_code_interpreter(arg_array) == "A"
    
    