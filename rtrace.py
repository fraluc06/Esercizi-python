
def trace(pause=False):
    class TraceRecursion:
        """ A decorator class to trace the recursive function calls.
            To enable it, type the following import statement
              from rtrace import trace
            and prepend
              @trace()
            to the functions you want to monitor.
            The pause argument allows stopping at each call/exit
        """
        def __init__(self, f):
            self.f = f
            self.pause = pause
            self.traceP = False
            self.countP = False
            self.indent = 0
            self.callsNum = 0

        def count(self, *args, **kargs):
            self.traceP = False
            self.countP = True
            self.callsNum = 0
            answer = self.__call__(*args, **kargs)
            print('Num calls:', self.callsNum)
            self.countP = False
            return answer

        def trace(self, *args, **kargs):
            self.traceP = True
            self.countP = True
            self.indent = 0
            self.callsNum = 0
            print('------------------- Starting recursion -------------------')
            answer = self.__call__(*args, **kargs)
            print('-------------------- Ending recursion --------------------')
            print('Num calls:', self.callsNum)
            self.countP = False
            self.traceP = False
            return answer

        def __call__(self, *args, **kargs):
            """Counts and traces (if requested) the function calls"""
            if self.traceP:
                indent     = '|--'*self.indent
                callString = self.f.__name__
                if args : callString += str(args)
                if kargs: callString += str(kargs)
                if self.pause: 
                    input(f"{indent} entering\t{callString} ")
                else:
                    print(indent+" entering", callString, sep='\t')
                self.indent += 1
            if self.countP:
                self.callsNum += 1
            answer = self.f(*args, **kargs)
            if self.traceP:
                self.indent -= 1
                if self.pause: 
                    input(f"{indent} exiting\t{callString}\treturns\t{answer} ")
                else:
                    print(indent+' exiting ', callString, "returns", answer, sep='\t')
            return answer
    return TraceRecursion


# +
from functools import wraps

def traced(pause=False):
    "Decoratore che traccia l'entrata/uscita da una funzione o da un metodo ed eventuali errori"
    def my_trace(func):
        indent = 0
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal indent    # per accedere alla variabile indent
            print_fn = input if pause else print
            call_str=f"{'|--'*indent} %s \t{func.__name__}({args}, {kwargs or ''})"
            if args and getattr(args[0],func.__name__, False):
                # se è una chiamata a un metodo lo scrivo come X.metodo
                call_str=f"{'|--'*indent} %s \t{args[0]}.{func.__name__}({args[1:]}, {kwargs or ''})"
            print_fn(call_str%'entering:')
            indent += 1
            try:
                ret = func(*args, **kwargs)
            except Exception:  # se c'è una eccezione
                indent -= 1    # sistemo l'indent
                raise          # e faccio continuare l'eccezione
            indent -= 1
            print_fn(call_str%'exiting:')
            return ret
        return wrapper
    return my_trace
