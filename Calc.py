"""
Calc.py
Addition (Der Benutzer gibt zwei Zahlen ein und bekommt die Summe ausgegeben)
Subtraktion
Division
Multiplikation
Mittelwert (Der Benutzer gibt mehrere Zahlen ein und bekommt den Mittelwert. Ihr könnt zuerst die Anzahl der Werte Abfragen oder einen Input abfangen, der die Eingabe der Zahlenreihe beendet)
Summe einer Liste an Zahlen
Maximum einer Liste an Zahlen
Minimum einer Liste an Zahlen
Umfang eines Kreises (bei gegebenen Radius
c bei gegebenem a^2 und b^2 nach Satz des Pythagoras (wie zieht man in Python eine Wurzel?)
"""

import streamlit as st

# Define PI as a constant. Using a numeric literal keeps us independent
PI = 3.141592653589793


# my functions for calculations (without using math or statistics modules)
def mean(nums):
    """Return the arithmetic mean of a non-empty list of numbers."""
    if len(nums) == 0:
        raise ValueError("mean requires at least one number")
    return sum(nums) / len(nums)


def circle_circumference(r):
    """Return circumference of a circle given radius r using a custom PI constant."""
    # The formula is C = 2 * pi * r.
    # We do not use Python's math module here; instead we use our own PI constant.
    return 2 * PI * r


def pythagoras(a, b):
    """Return length of hypotenuse c = sqrt(a^2 + b^2) using Newton's method."""
    return sqrt_newton(a * a + b * b)


def sqrt_newton(x, iterations=40):
    if x < 0:
        raise ValueError("Cannot compute square root of negative number")
    if x == 0:
        return 0.0
    # Start with an initial guess; x/2 is a simple choice
    guess = x / 2.0
    for _ in range(iterations):
        # Newton update for sqrt: guess = 0.5 * (guess + x / guess)
        guess = 0.5 * (guess + x / guess)
    return guess


# --- Page title and short description ---
st.title("Calculator — Ruby edition")
st.write(
    "Calculator app built for fIT in IT Python course by Ruby Claes"
)


# --- Choose operation ---
# We present a selectbox so the user picks which operation they want.
# The selected operation controls which inputs are shown and how the result
# is computed when the user clicks the Calculate button.
op = st.selectbox(
    "Choose an operation",
    (
        "+",
        "-",
        "*",
        "/",
        "Mean of list",
        "Sum of list",
        "Max of list",
        "Min of list",
        "Circumference of circle",
        "Pythagoras c = sqrt(a^2 + b^2)",
    ),
)

# --- Inputs ---
# Different operations require different inputs. For two-number operations
# (like + - * / and Pythagoras) we show two numeric inputs side-by-side.
# For list operations we show a single text input where the user types numbers
# separated by commas. For circle circumference we show a single radius input.

# Initialize variables used later
n1 = None
n2 = None
list_input = ""
radius = None

if op == "Circumference of circle":
    # Only radius is needed for circumference: C = 2 * pi * r
    radius = st.number_input("Radius", value=1.0)
elif op.startswith("Pythagoras"):
    # For Pythagoras we label the inputs `a` and `b` so it's clearer.
    col_a, col_b = st.columns(2)
    with col_a:
        n1 = st.number_input("Side a", value=3.0)
    with col_b:
        n2 = st.number_input("Side b", value=4.0)
elif "list" in op.lower():
    # List operations: ask user for comma-separated numbers (e.g. 1, 2, 3.5)
    list_input = st.text_input("Enter numbers separated by commas", "1, 2, 3")
else:
    # Default: two generic number inputs for basic arithmetic
    col1, col2 = st.columns(2)
    with col1:
        n1 = st.number_input("Number 1", value=0.0)
    with col2:
        n2 = st.number_input("Number 2", value=0.0)


# --- Helper functions ---

def parse_list(text):
    """
    Parse a comma-separated string of numbers into a list of floats.

    Example: "1, 2, 3.5" -> [1.0, 2.0, 3.5]
    We strip whitespace and ignore empty items.
    """
    parts = [s.strip() for s in text.split(",")]
    # Filter out empty strings and convert to float
    nums = [float(p) for p in parts if p != ""]
    return nums


def format_result(val, prec=6):
    """
    Format numeric results to a maximum of `prec` decimal places.
    - If the value is effectively an integer (within rounding tolerance),
      return it without a decimal point.
    - Otherwise, round to `prec` decimals and strip trailing zeros.
    """
    # Non-numeric values: fallback to str()
    try:
        # Handle integers cleanly
        if isinstance(val, int):
            return str(val)
        # For floats: check if value is very close to an integer
        if isinstance(val, float):
            if abs(val - round(val)) < 10 ** (-prec):
                return str(int(round(val)))
            # Format with fixed number of decimals then strip trailing zeros
            formatted = f"{val:.{prec}f}"
            return formatted.rstrip("0").rstrip(".")
    except Exception:
        pass
    return str(val)

# --- Calculation and error handling ---
# When the user clicks the Calculate button, we examine the selected operation
# and the inputs the user provided. We compute the result or collect an error
# message to show to the user.

result = None
error = None

if st.button("Calculate"):
    try:
        # Two-number arithmetic
        if op == "+":
            result = n1 + n2
        elif op == "-":
            result = n1 - n2
        elif op == "*":
            result = n1 * n2
        elif op == "/":
            # Guard against division by zero — this would raise an exception
            if n2 == 0:
                error = "Error: division by zero is not allowed."
            else:
                result = n1 / n2

        # List operations: parse input and apply the appropriate aggregate
        elif op.startswith("Mean"):
            nums = parse_list(list_input)
            if len(nums) == 0:
                error = "Please provide at least one number for the mean."
            else:
                result = mean(nums)
        elif op.startswith("Sum"):
            nums = parse_list(list_input)
            if len(nums) == 0:
                error = "Please provide at least one number to sum."
            else:
                result = sum(nums)
        elif op.startswith("Max"):
            nums = parse_list(list_input)
            if len(nums) == 0:
                error = "Please provide at least one number to find the maximum."
            else:
                result = max(nums)
        elif op.startswith("Min"):
            nums = parse_list(list_input)
            if len(nums) == 0:
                error = "Please provide at least one number to find the minimum."
            else:
                result = min(nums)

        # Circle circumference: only radius required
        elif op == "Circumference of circle":
            # Ensure radius is not negative — for learning, we show an error
            if radius is None:
                error = "Please enter a radius."
            elif radius < 0:
                error = "Radius cannot be negative."
            else:
                result = circle_circumference(radius)

        # Pythagoras: compute hypotenuse from sides a and b
        elif op.startswith("Pythagoras"):
            result = pythagoras(n1, n2)

        else:
            error = "Unknown operation selected."

    except ValueError:
        # Raised when float conversion fails in parse_list
        error = "Invalid numeric input — ensure numbers are formatted correctly."
    except Exception as e:
        # Catch-all for unexpected errors; show the exception message to help
        # with debugging while you are learning.
        error = f"Unexpected error: {e}"


# --- Show result or error to the user ---
if error:
    st.error(error)
elif result is not None:
    # Format result nicely so the output is easier to read.
    st.success(f"Result: {format_result(result, 6)}")
