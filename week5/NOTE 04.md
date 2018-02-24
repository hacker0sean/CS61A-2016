```python
>>> chinese = ['coin', 'string', 'myriad']
>>> suits = chinese
>>> suits.pop()
'myriad'
>>> suits.remove('string')
>>> suits.append('cup')
>>> suits.extend(['sword', 'club'])
>>> suits[2] = 'spade'
>>> suits[0:2] = ['heart', 'diamond']
>>> nest = list(suits)
>>> nest
['heart', 'diamond', 'spade', 'club']
>>> nest[0] = suits
>>> nest
[['heart', 'diamond', 'spade', 'club'], 'diamond', 'spade', 'club']
>>> suits.insert(2, 'Joker')
>>> nest
[['heart', 'diamond', 'Joker', 'spade', 'club'], 'diamond', 'spade', 'club']
>>> nest[0].pop(2)
'Joker'
>>> suits
['heart', 'diamond', 'spade', 'club']

```

