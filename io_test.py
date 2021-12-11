import pytest
import io.py

def io_test():
    input_values = ["1","5"]
    input_values_stored = ["-1","25","55","65","79","80","95","105"]
    output = []

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)

    io.input = mock_input
    io.print = lambda s : output.append(s)
    io.main()

    io.input = mock_input
    io.print = lambda s : output.append(s)
    io.main()

 
    assert [output[0],output[1]] == ["Give points [0-100]:","Grade: impossible!"]
    assert [output[2],output[3]] == ["Give points [0-100]:","Grade: failed"]
 
