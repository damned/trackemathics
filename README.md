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
i am 7.9350000000000005. from: 6.9 + 1.035
where:
i am 1.035. from: 6.9 * 0.15
i am 6.9. from: 2.95 + 3.95
i am 2.95. from: mineral water
i am 3.95. from: olives
```