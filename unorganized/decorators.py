#example of decorator without arguments

def decorator_function(func):
    ''' Receives the function being decorated as first argument'''
    
    def actual_decorator(*args, **kwargs): 
        '''function that actually performs the decorated logic '''
        
        # do something, before original logic
        
        #call the original function
        
        func(*args,**kwargs)
        
        # and/or do something after. 
        
        #return result 
    
    #return the actual decorator so it gets called by calling context . 
    return actual_decorator    
    
        
def decorator_function(a, b):
    ''' Receives the decorator arguments'''
    
    def additional_wrapper(func):
        ''' receivs the function (and its arguments) being decorated '''
    
        def actual_decorator(*args, **kwargs): 
            '''function that actually performs the decorated logic '''
            
            #arguments a and b passed from outer fuction are in scope but read only. 
               if a > b:
                   pass         
            # do something, before original logic
                      
            
            #call the original function            
            func(*args,**kwargs)
            
            # and/or do something after. 
            
            #return result
        
        # return function to calling context (so that it gets executed).    
        return actual_decorator   

    #return fuction to calling context (so that it gets executed).
    return additional_wrapper


