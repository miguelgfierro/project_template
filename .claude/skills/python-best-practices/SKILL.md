---
name: python-best-practices
description: Python code quality rules and conventions. Use this skill when reviewing Python code for style, structure, or common mistakes.
user-invocable: false
metadata:
  version: 1.0.0
---

# Python Best Practices

Apply these rules when reviewing Python code.

## Philosophy

- Explicit is better than implicit. Each function name should tell the caller exactly what it does, with no hidden behavior based on input type or format. Prefer specific functions over generic ones that branch internally.

```python
# Bad: implicit — the caller does not know what format will be read,
# and the function hides branching logic based on the file extension.
def read(filename):
    ...

# Good: explicit — each function does one thing and the name says exactly what.
def read_csv(filename):
    ...

def read_json(filename):
    ...
```

## Style

- Follow PEP 8 for naming and formatting.
- Use type hints on function signatures.
- Keep functions under 30 lines. Extract helpers when they grow.

## Imports

- All imports at the top of the file, never inline.
- Group imports: stdlib, third-party, local. Separate each group with a blank line.
- No wildcard imports (`from module import *`).

## Functions

- Each function should do one thing.
- Prefer returning early over deep nesting.
- Use keyword arguments for functions with more than three parameters.

## Error Handling

- Catch specific exceptions, never bare `except:`.
- Do not silence exceptions without logging.
- Validate inputs at system boundaries (user input, external APIs), not internally.

## Testing

- Use plain functions with `pytest`, no classes.
- One assertion per test when possible.
- Name tests `test_<what>_<expected_behavior>`.

## Common Mistakes to Flag

- Mutable default arguments (`def f(x=[])`).
- Using `==` to compare with `None` (use `is None`).
- Catching `Exception` instead of a specific type.
- F-strings or `.format()` in logging calls (use lazy `%` formatting).
- Unused imports or variables.
