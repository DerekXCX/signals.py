# signals

Short python module intended for the creation of function connections to objects. Signals are fired on an object to run connected functions. One of my first ever projects, might be vulnerable to memory-leaks or optimizations. If any are spotted, please let me know.

# DOCUMENTATION : Creating new Signal Objects

``signals.create() -> signal``

Creates a signal object, contains following methods.

``signal.Connect(function) -> Connection``

Connect a function to be called whenever the Signal is fired. Arguments are given through the Fire() method.

``signal.WaitForFired() -> None``

Yields code until the next time the Signal is fired using Fire().

``signal.Fire(args : tuple) -> None``

Fires the Signal. Args must be a tuple in order to provide multiple arguments. Does not yield.

# EXAMPLE USAGE

--> Sample class
```python
import signals

class create:
    def __init__(self):
        self.testing_signal = signals.create()
    def fireSignal(self):
        self.testing_signal.Fire("Fired connection")
```

--> Sample signal
```python
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

print("Finished yielding")

```
--> Output
```
CONNECTION ONE: Fired connection

CONNECTION TWO: Fired connection, None, None

CONNECTION THREE

Finished waiting for signal

CONNECTION ONE: Fired connection

CONNECTION TWO: Fired connection, None, None

```
