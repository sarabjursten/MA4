from numba import njit
from person import Person 
from time import perf_counter as pc
import matplotlib.pyplot as plt
import numpy as np

#Python
def fib_py(n):
	if n <= 1:
		return n
	else:
		return fib_py(n-1) + fib_py(n-2)

#Python with numba
@njit	
def fib_py_numba(n):
	if n <= 1:
		return n
	else:
		return fib_py_numba(n-1) + fib_py_numba(n-2)
	
#C++
p = Person(1)
def fib_cpp(n):
	p.setAge(n)
	return p.fib()

def timing(fun, n):
	t0 = pc()
	fun(n)
	t1 = pc()
	return t1-t0

def main():
    #python and numba for age = 20,...,30
    #age_list = np.linspace(20, 30)
    #time_py = [timing(fib_py, age) for age in age_list]
    #time_numba= [timing(fib_py_numba, age) for age in age_list]
 
    #plt.figure()
    #plt.plot(age_list, time_py, label = 'Python')
    #plt.plot(age_list, time_numba, label = 'Numba')
    #plt.legend()
    #plt.xlabel('n')
    #plt.ylabel('Time (s)')
    #plt.title('Time for Fibonacci') 
    #plt.savefig('time_for_fib.png')

    #large n
    #age_list = list(range(30, 45))
    #time_py = [timing(fib_py, age) for age in age_list]
    #time_numba = [timing(fib_py_numba, age) for age in age_list]    
    #time_cpp = [timing(fib_cpp, age) for age in age_list]

    #plt.figure()
    #plt.plot(age_list, time_py, label = 'Python')
    #plt.plot(age_list, time_numba, label = 'Numba')
    #plt.plot(age_list, time_cpp, label = 'C++')
    #plt.legend()
    #plt.xlabel('n')
    #plt.ylabel('Time [s]')
    #plt.title('Time for Fibonacci') 
    #plt.savefig('time_for_fib_large.png')

    print(f'Time for Fibonacci for n = 47: Numba: {timing(fib_py_numba, 47)} and C++: {timing(fib_cpp, 47)}')
        #Time for n = 47: Numba: 20.745637145999808 and C++: 20.90136755200001, min dator
        
        
if __name__ == "__main__":
    main()

	
	


	    
	    
	    
    

