import unittest
import src.greeting as greeting

'''
Do not modify this file. Run it in the same directory as your source code.
'''

class Test_Greeting(unittest.TestCase):
    def input_replacement(self, prompt):
        self.inputed_prompts.append(prompt)
        value = self.responses[self.index]
        self.index +=1
        self.count +=1
        if self.index >= len(self.responses):
            self.index = 0
        return value

    def print_replacement(self, *text):
        line = " ".join(text) + "\n"
        self.printed_lines.append(line)
        return
    
    def setUp(self) -> None:
        self.printed_lines = []
        self.inputed_prompts = []
        self.responses = ["John", "", "Mary", "Ellison"]
        self.index = 0
        self.count = 0
        greeting.print = self.print_replacement
        greeting.input = self.input_replacement

        return
    
    def test_001GreetingExists(self):
        self.assertTrue("Greeting" in dir( greeting ), 'Function "Greeting" is not defined. Please check your spelling.')
        return
    
    def test_002GreetingPrompted(self):
        greeting.Greeting()

        expected = ["Hi, what is your name? "]
        self.assertListEqual(self.inputed_prompts, expected)
        self.index = 0
        self.inputed_prompts = []
        return
    
    def test_003GreetingOutput(self):
        for i in range(len(self.responses)):
            greeting.Greeting()
            expected = ["Nice to meet you " + self.responses[i] + "!\n"]
            self.assertListEqual(expected, self.printed_lines)
            self.printed_lines = []
    


if __name__ == "__main__":
    unittest.main()
