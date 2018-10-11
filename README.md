# JavaScript-like functions in Python
### Mikhail Kormanowsky
### 2018

## Usage:
<pre>
from function import Function
def [function_name]([params]):
    [code]
fn = Function([function_name])
</pre>

## Methods:
1. fn([params]) - calls function with params (as usual function)
2. fn.set([new_function_name]) - sets new function
3. fn.call([list]) - calls function with list of params
4. fn.call([dict]) - calls function with dict of params
5. fn.print_output(True|False) - enables/disables print() instead of return
6. fn.apply_to([list]) - calls function for each element of the <list>
