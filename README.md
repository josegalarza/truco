![Build Status](https://github.com/josegalarza/truco/workflows/python-app/badge.svg)

# truco
Truco Argentino

Goal: create a bot that could beat a human playing Truco.

## Classes

### Carta

```py
>>> from carta import Carta
>>>
>>> c = carta.Carta(numero=7, palo="espadas")
>>> c.get_truco()
3
>>> c.get_evido()
7
>>> print(c)
'7e'
```

### Mazo

```py
>>> from mazo import Mazo
>>>
>>> # Cartas vienen ordenadas
>>> m = Mazo()
>>> carta = m.pop_carta()
>>> print(carta)
'1e'
>>>
>>> m.mezclar()
>>> carta_random = m.pop_carta()
'10c'
>>> 
>>> # Repartir lista de cartas a 2 jugadores
>>> jujgador1, jugador2 = m.repartir_cartas(jugadores=2)
```


### Jugador

```py
from jugador import Jugador

jose = Jugador(nombre="Jose")
fran = Jugador(nombre="Fran")
```
