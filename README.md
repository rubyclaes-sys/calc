# Calculator — Ruby Edition

A simple yet powerful calculator web app built with [Streamlit](https://streamlit.io/), created for the fIT in IT Python course by Ruby Claes.

## Features

This calculator supports the following operations:

### Basic Arithmetic
- **Addition (+)**: Add two numbers together
- **Subtraction (-)**: Subtract the second number from the first
- **Multiplication (*)**: Multiply two numbers
- **Division (/)**: Divide the first number by the second (with zero-division protection)

### List Operations
- **Mean of list**: Calculate the average of multiple numbers
- **Sum of list**: Add all numbers in a list together
- **Max of list**: Find the largest number in a list
- **Min of list**: Find the smallest number in a list

### Geometry
- **Circumference of circle**: Calculate the circumference given a radius using the formula C = 2πr
- **Pythagoras c = sqrt(a² + b²)**: Calculate the hypotenuse of a right triangle given sides a and b

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/rubyclaes-sys/calc.git
cd calc
```

2. Install Streamlit:
```bash
pip install streamlit
```

## Usage

### Running the App

Start the application by running:
```bash
streamlit run Calc.py
```

The app will open in your default web browser at `http://localhost:8501`

### How to Use

1. **Select an operation** from the dropdown menu at the top
2. **Enter your input(s)**:
   - For arithmetic and Pythagoras: Enter two numbers in the input fields
   - For list operations: Enter comma-separated numbers (e.g., `1, 2, 3, 4.5`)
   - For circle circumference: Enter the radius value
3. **Click the "Calculate" button**
4. **View your result** displayed below the button

### Examples

#### Addition
- Select: `+`
- Number 1: `5`
- Number 2: `3`
- Result: `8`

#### Mean of List
- Select: `Mean of list`
- Enter numbers: `10, 20, 30, 40`
- Result: `25`

#### Circle Circumference
- Select: `Circumference of circle`
- Radius: `5`
- Result: `31.415927` (approximately)

#### Pythagoras
- Select: `Pythagoras c = sqrt(a² + b²)`
- Side a: `3`
- Side b: `4`
- Result: `5`

## Implementation Notes

- **No external math library**: All calculations (including square roots and PI) are implemented without using Python's `math` or `statistics` modules
- **Error handling**: The app validates inputs and provides helpful error messages
- **Precise formatting**: Results are formatted to remove unnecessary trailing zeros while maintaining accuracy

## Technical Details

### Key Functions

- `mean(nums)`: Calculates the arithmetic mean of a list
- `circle_circumference(r)`: Calculates circle circumference
- `pythagoras(a, b)`: Calculates the hypotenuse using the Pythagorean theorem
- `sqrt_newton(x)`: Computes square roots using Newton's method
- `parse_list(text)`: Parses comma-separated numbers from text input
- `format_result(val, prec)`: Formats numeric results for clean display

## Error Handling

The app includes validation for:
- Division by zero
- Empty lists for list operations
- Negative radius values for circle calculations
- Invalid numeric input formats

## License

This project is part of the fIT in IT Python course.
