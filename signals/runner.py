import signals, sample_class, time, threading

def functionOne(retrieved1):
    print(f"CONNECTION ONE: {retrieved1}")
    pass
def functionTwo(retrieved1, retrieved2, retrieved3):
    print(f"CONNECTION TWO: {retrieved1}, {retrieved2}, {retrieved3}")
    pass
def functionThree():
    time.sleep(1)
    print("CONNECTION THREE")
    pass 

# make sample class and establish connections
new_sample_class = sample_class.create()

connection_1 = new_sample_class.testing_signal.Connect(functionOne)
connection_2 = new_sample_class.testing_signal.Connect(functionTwo)
connection_3 = new_sample_class.testing_signal.Connect(functionThree)

# should run all three connections
new_sample_class.fireSignal()

# disconnects
connection_3.Disconnect()

# wait for all three to finish
def runAfter():
    time.sleep(2)
    new_sample_class.fireSignal()
threading.Thread(target = runAfter).start()

new_sample_class.testing_signal.WaitForFired()

print("Finished waiting for signal")
