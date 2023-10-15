import unittest
import src.total_ages as total_ages

class TestTotalAges(unittest.TestCase):
    def input_replacement(self, prompt):
        self.inputed_prompts.append(prompt)
        r = self.test_inputs[self.index]
        self.index += 1
        return r
    
    def print_replacement(self, *text):
        line = " ".join(map(str, text)) + "\n"
        self.printed_lines.append(line)




    def setUp(self):
        self.inputed_prompts = []
        self.test_inputs = [5,7]
        self.printed_lines = []
        self.index = 0
        total_ages.print = self.print_replacement
        total_ages.input = self.input_replacement
    
    def test_001TotalAgesExists(self):
        self.assertTrue("TotalAges" in dir( total_ages ), 'Function "TotalAges" is not defined. Please check your spelling.')
        return
    
    def test_002TotalAgesPrompts(self):
        '''
        Prelude
        '''
        expected = ["Age 1? ", "Age 2? "]
        total_ages.TotalAges()
        
        '''
        Running tests
        '''
        self.assertListEqual(self.inputed_prompts, expected)

        '''
        postlude
        '''
        self.inputed_prompts = []
        self.printed_lines = []
        self.index = 0
        self.bin = 0
    
    def test_003TotalAgesOutputs(self):
        expected = ["12\n"]
        total_ages.TotalAges()
        self.assertListEqual(expected, self.printed_lines)

if __name__ == "__main__":
    unittest.main()