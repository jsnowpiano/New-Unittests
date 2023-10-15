import unittest
import total_ages

class TestTotalAges(unittest.TestCase):
    def input_replacement(self, prompt):
        self.inputed_prompts.append(prompt)
        r = self.test_inputs[self.index][self.bin]
        self.index += 1
        self.bin +=1
        if self.index >= len(self.test_inputs):
            self.index = 0
        if self.bin > 1:
            self.bin = 0
        return r
    
    def print_replacement(self, *text):
        line = " ".join(text) + "\n"
        self.printed_lines.append(line)
        print(text)




    def setUp(self):
        self.inputed_prompts = []
        self.test_inputs = [["5","6"], ["7","67"],["88","34"]]
        self.printed_lines = []
        self.index = 0
        self.bin = 0
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
        '''
        Prelude
        '''
        expected = []
        for i in range(len(self.test_inputs)):
            total = int(self.test_inputs[i][0]) + int(self.test_inputs[i][1])
            expected.append(str(total) + "\n" )
            total_ages.TotalAges()
        print(self.printed_lines)
        '''
        Running tests
        '''
        self.assertListEqual(self.printed_lines, expected)

        '''
        Postlude
        '''

if __name__ == "__main__":
    unittest.main()