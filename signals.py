import inspect, threading, time
from typing import TypeAlias
    
class _connection:
    """ Connection object. INTENDED ONLY FOR SIGNALS MODULE USE. """
    def __init__(self, function):
        self.function = function
    def Disconnect(self):
        self.function = None
        
Connection: TypeAlias = _connection

class create:
    """ Create a 'Signal' object. Contains methods used by signal. """
    def __init__(self):
        self.active_connections = []
        self.times_fired = 0
        
    def Connect(self, function) -> Connection:
        """ Connect a function to be called whenever the Signal is fired. Arguments are given through the Fire() method. """
        new_connection = _connection(function)
        self.active_connections.append(new_connection)
        return new_connection
    
    def WaitForFired(self) -> None:
        """ Yields code until the next time the Signal is fired using Fire(). """
        times_fired_when_started = self.times_fired
        while (1):
            if self.times_fired > times_fired_when_started:
                break
                        
    def Fire(self, args : tuple) -> None: 
        """ Fires the Signal. Args must be a tuple in order to provide multiple arguments. Does not yield. """
        self.times_fired += 1
        
        # if there isn't a tuple provided, convert it to one
        if not isinstance(args, tuple):
            args = [args]
        
        # loop through the active functions
        for connection in self.active_connections:
            if not connection.function:
                continue

            # number of arguments required for functions to run
            required_arg_length = len(inspect.signature(connection.function).parameters)
            given_arg_length = len(args)
            needed_none_args = 0
            
            #check for any disimilarities between needed arguments
            if given_arg_length != required_arg_length:
                # whenever more arguments are provided than needed, don't run the function
                if (given_arg_length > required_arg_length) and (not required_arg_length == 0):
                    print(f"SIGNALS: {required_arg_length} needed, {given_arg_length} was provided")
                    continue
                # if there aren't enough arguments provided, replace the needed ones with None
                elif given_arg_length < required_arg_length:
                    needed_none_args = required_arg_length - given_arg_length
                    
            # add the None arguments
            if needed_none_args > 0:
                for num in range(needed_none_args):
                    args.append(None)
                
            # run thread
            if required_arg_length > 0:
                new_thread = threading.Thread(target = connection.function, args = args)
            else:
                new_thread = threading.Thread(target = connection.function)
               
            new_thread.start()
    