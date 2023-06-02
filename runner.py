import signals, sample_class, time, threading

def connection_one(retrieved1):
    print(f"CONNECTION ONE: {retrieved1}")
    pass
def connection_two(retrieved1, retrieved2, retrieved3):
    print(f"CONNECTION TWO: {retrieved1}, {retrieved2}, {retrieved3}")
    pass
def connection_three():
    time.sleep(1)
    print("CONNECTION THREE")
    pass 

# make sample class and establish connections
new_sample_class = sample_class.create()

connection1 = new_sample_class.testing_signal.Connect(connection_one)
connection2 = new_sample_class.testing_signal.Connect(connection_two)
connection3 = new_sample_class.testing_signal.Connect(connection_three)

# should run all three connections
new_sample_class.fireSignal()

# disconnects
connection3.Disconnect()

# wait for all three to finish
def runAfter():
    time.sleep(2)
    new_sample_class.fireSignal()
threading.Thread(target = runAfter).start()

new_sample_class.testing_signal.WaitForFired()

print("Finished waiting for signal")