# trackemathics

WIP

## example

the bill

```
>>> from trackemathics.value import Value
>>> 
>>> food = Value(2.95, 'mineral water') + Value(3.95, 'olives')
>>> total = food + (food * Value(0.15, 'service charge rate'))
>>> 
>>> total.value
7.9350000000000005
>>> 
>>> 
>>> print(total.narrate())
7.9350000000000005. from: 6.9 + 1.035
where:
1.035. from: 6.9 * 0.15
6.9. from: 2.95 + 3.95
2.95. from: mineral water
3.95. from: olives
```