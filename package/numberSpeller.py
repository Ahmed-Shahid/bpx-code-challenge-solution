from .integerSpeller import integerSpeller


class numberSpeller:

    '''
    This class is meant to provide methods to spell out full numbers,
    regardless of whether they are integers, decimals, or negative
    '''

    
    
    
    def __init__(self):
        pass
        
        
    def spellNumber(self, n_str):
    
        intSpell = integerSpeller()
        
        #TODO: Build out functionality
        
        return intSpell.spellInteger(n_str)