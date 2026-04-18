def daraja(n, x):
    return n ** x
```

```python
def daraja(n, x):
    if x == 0:
        return 1
    elif x < 0:
        return 1 / daraja(n, -x)
    else:
        return n * daraja(n, x - 1)
```

```python
def daraja(n, x):
    if x == 0:
        return 1
    elif x < 0:
        return 1 / daraja(n, -x)
    else:
        return n * daraja(n, x - 1)
```

```python
def daraja(n, x):
    if x == 0:
        return 1
    elif x < 0:
        return 1 / daraja(n, -x)
    else:
        return n * daraja(n, x - 1)
