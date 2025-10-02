
class RuleBased:

    def __init__(self, input, dictionary):
        self.input=input
        self.dictionary=dictionary

    
    def response(self):
        output="Hi!!"
        if self.input.lower() in self.dictionary:
            output=self.dictionary[self.input.lower()]
        return output
    
    
    

