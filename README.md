# trackemathics

WIP

## example

the bill

```
>>> from trackemathics.value import Value
>>> 
>>> total = Value(2.95, 'mineral water') + Value(2.50, 'service charge')
>>> 
>>> total.value
5.45
>>> 
>>> total.value / 2
2.725
>>> 
>>> print(total.narrate())
i am 5.45. from: 2.95 + 2.5
where:
i am 2.95. from: mineral water
i am 2.5. from: service charge
```