from ikcode_devtools import runGUI, CheckInfo, getVersion

@CheckInfo
@getVersion
def test():
    print("e")
    e = 2
    class A:
        test = 1

    def p():
        print("test")
        return 1
    
    import time 


runGUI()