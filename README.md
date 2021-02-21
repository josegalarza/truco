![Build Status](https://github.com/josegalarza/truco/workflows/pytest/badge.svg)

# truco
Truco Argentino

Goal: create a bot that could beat a human playing Truco.

## Classes

### Carta

```py
from carta import Carta
c = Carta(numero=7, palo="espadas")
c.get_truco()  # 3
c.get_evido()  # 7
c.get_id()  # '7e'
```

### Mazo

```py
from mazo import Mazo

# Cartas vienen ordenadas
m = Mazo()
m.pop_carta().get_id()  # '1e'

m.mezclar()
m.pop_carta().egt_id()  # '10c'

# Repartir lista de cartas a 2 jugadores
j1, j2 = m.repartir_cartas(jugadores=2)
len(j1)  # 3
len(j2)  # 3
```
