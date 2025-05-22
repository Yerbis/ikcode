from ikcode_gtconnect import runGUI, CheckInfo, Help

@CheckInfo
def run_gui():
    import time
    print("Running GUI test...")
    time.sleep(2)
    print("GUI test completed.")
    e = 2

    class Test:
        def __init__(self):
            self.name = "Test"
            self.value = 0



    runGUI()



print(Help())

