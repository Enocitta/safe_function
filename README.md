

<p style='font-size:160%; text-align:center'><img  src="doc/SF-escudo.jpg" alt="Safe Function" width="100px"/></p>
<div style='font-size:160%; text-align:center;text-decoration: overline; vertical-align:baseline; font-family:courier;'>Safe Function</div>


## Function decorator for debugging Type Errors in runtime calls.

The following Project is a simple development to control that the variables that are entered in the functions correspond
to the specifications declared in the prototype of the function, if not, it avoids the execution of the decorated function and performs error reporting by log


**Table of Contents**  

  - [Description](#function-decorator-for-debugging-type-errors-in-runtime-calls)
  - [Example](#example)
  - [Installation](#installation)
  - [Tests](#tests)
  - [Style conventions](#convenciones-de-estilo)
  - [License](#license)



## Example

This section shows how to use the package with a simple example.

```python
import safe_function as Sf

@Sf
def funcInt(A: int, B: int ) -> int:
  return A+B

funcInt(1,3) --> "OK ,silent log pass ,the function runs normally"
funcInt(1,"error") --> "the decorator checks for the type error and stops execution"

```

The decorator can be added to a function that needs to be inspected, preventing its execution if it does not comply.
the invocation requirements, if used in an object that is not a function it will send a `python TypeError`

```python
import safe_function as Sf

@Sf
class myclass:
    pass

ins1 = myclass --> "TypeError"
```

## Installation

This section lists the steps required to install the package.

- Install Python 3 at least (it is recommended to install the most recent version)


## Tests

Remember that the tests depend on the `nose` module
If you don't have it, install it with... 

`pip install nose`


In the library there is the file `test_safe_function.py` which contains the execution tests
in the `PyCharm` terminal for example you can run
- `nosetests` (runs all tests)
```...........
----------------------------------------------------------------------
Ran 11 tests in 0.003s

OK
```
 
## Style conventions

This project follows the conventions of the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html).

See a complete example of [using docstrings in python according to Google's guide](http://sphinxcontrib-napoleon.readthedocs.org/en/latest/example_google.html#example-google)
## License
[GPL](https://www.gnu.org/licenses/gpl-3.0.html)
