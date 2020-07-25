import time                                                
 
def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print("{0} took {1:0.3e} seconds".format(method.__name__, te-ts))
        return (result, te-ts)

    return timed