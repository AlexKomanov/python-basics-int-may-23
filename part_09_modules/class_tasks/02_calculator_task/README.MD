# Building a Simple Calculator in Python
In this project, you will create a basic calculator that can perform addition, subtraction, multiplication, and division. 
The calculator will be split into two Python files: `calculator_module.py` for the calculator's core functions, and `main.py` for the user interface.

## Instructions
Follow these steps to build and use the calculator.

### Step 1: Create `calculator_module.py`

In this step, you will create a Python module named calculator_module.py that contains the core calculator functions.

* Create a new Python file named `calculator_module.py`.


* Add the following functions to `calculator_module.py`:

    * `_add(x, y)`: This private function takes two numbers x and y as input and returns their sum.
    * `_subtract(x, y)`: This private function takes two numbers x and y as input and returns their difference.
    * `_multiply(x, y)`: This private function takes two numbers x and y as input and returns their product.
    * `_divide(x, y)`: This private function takes two numbers x and y as input and returns their quotient. It includes error handling to prevent division by zero. 
    * `calculate(x, y, operation)`: This public function takes two numbers x and y, as well as a string operation representing the desired mathematical operation ('+', '-', '*', '/'). It uses a match statement to determine the operation to perform and calls the appropriate private function. If the operation is invalid, it raises a **ValueError**.

### Step 2: Create `main.py`

In this step, you will create a Python script named `main.py` that interacts with the user and uses the calculator functions from `calculator_module.py`.

* Create a new Python file named `main.py`.


* Write a program that calls **ONLY** to the `calculate()` function from the `calculator_module.py`.


* Validate a correct behavior in case of the valid and invalid operations.


* You can perform an attempt to wrap the code inside the `try-except` block to catch a `ValueError` in case of invalid operation.


### Step 3: Run the Calculator

* Open your terminal.

* Navigate to the directory where you saved calculator_module.py and main.py.

* Run the calculator by executing `main.py` with the following command:
`
python main.py
`

* Follow the on-screen prompts to enter two numbers and a math operation. The calculator will display the result.
