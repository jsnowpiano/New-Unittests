import unittest
import questions_3

'''
Do not edit this file. Run this file in the same directory as your source code.
'''

class TestQuestions3(unittest.TestCase):
    def input_replacement(self, prompt):
        self.input_prompt.append(prompt)
        while(True):
            if self.ternarySwitch == 0:
                self.results.append(self.integers[self.index])
                self.ternarySwitch += 1
                return self.integers[self.index]
            elif self.ternarySwitch == 1:
                self.results.append(self.colors[self.index])
                self.ternarySwitch += 1
                return self.colors[self.index]
            elif self.ternarySwitch == 2:
                self.results.append(self.numbers[self.index])
                self.ternarySwitch += 1
                return self.numbers[self.index]
            elif self.ternarySwitch > 2:
                self.ternarySwitch = 0
                self.index +=1
            

    
        
    def print_replacement(self, *text):
        line = " ".join(text) + "\n"
        self.printed_lines.append(line)
        return
    
    def setUp(self) -> None:
        self.printed_lines = []
        self.input_prompt = []
        self.integers = [7,6,3,5,7,8,9,0]
        self.colors = ["Gray", "Green", "Red", "Scarlet", "Violet", "Indigo", "Blue", ""]
        self.numbers = [1.6, 87.6, 44.89, 6.6, 7.8, 190.456, 7.7, 0.0]
        self.results = []
        self.index = 0
        self.ternarySwitch = 0
        questions_3.print = self.print_replacement
        questions_3.input = self.input_replacement
        return
    
    def test_001Questions3Exists(self):
        '''
        Checking if Questions_3 exists
        '''
        self.assertTrue("Questions_3" in dir( questions_3 ), 'Function "Questions_3" is not defined. Please check your spelling.')
        return
    
    def test_002Questions3Prompts(self):
        '''
        Prelude
        '''
        questions_3.Questions_3()

        '''
        Testing expected with actual
        '''

        expected = [
                    "What is your favorite integer? ",
                    "What is your favorite color? ",
                    "What is your favorite number? "
                    ]
        
        self.assertListEqual(expected, self.input_prompt)
        '''
        Postlude
        '''
        self.index = 0
        self.input_prompt = []
        self.printed_lines = []

    def test_003Questions3Outputs(self):
        '''
        Prelude
        '''
        expected = []
        actual = self.results
        for i in range(len(self.numbers)):
            questions_3.Questions_3()
            expected.append(self.integers[i])
            expected.append(self.colors[i])
            expected.append(self.numbers[i])

        '''
        Testing expected with actual
        '''
        self.assertListEqual(actual, expected)

        '''
        Postlude
        '''


if __name__ == "__main__":
    unittest.main()