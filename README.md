# balance-equation
Balance a chemical reaction equation using brute force.

## Installation

From PyPI:

```zsh
$ pip install balance-equation
```

## Command line usage

Use the `balance` command:

```zsh
$ balance "H2SO4 + NaOH" "Na2SO4 + H2O"
Multipliers: 1 2 1 2
Equation: ('H2SO4+2NaOH', 'Na2SO4+2H2O')
```

It takes the left side and right side of the equation as arguments.

It will output the multipliers, and the two sides of the balanced equation.

## Python usage

Use `balance.balance`:

```python
from balance import balance
print(balance("H2SO4 + NaOH", "Na2SO4 + H2O"))
```

Output:

```python
('H2SO4+2NaOH', 'Na2SO4+2H2O')
```

It takes the left side and right side of the equation as arguments.
It will output the two sides of the balanced equation.
