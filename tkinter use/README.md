Una cosa a tener en cuenta es que siemrpe estaremos trabajando con widgets.

Otra es que el padx y pady, es basicamente, la ubicacion que tienen los elementos dentro de esa area.

Tambien, el .pack a algo, ya sea root u otro widget, ubicara las cosas siempre en el mismo lugar, a diferencia del grid que modifica el orden.
Por ende generalmente usamos pack cuando no nos importa mucho la posicion, pero no se puede hacer ambos digamos.

Es decir, con row=0 saldria primero o con row=1 pasaria para abajo, similar con las columnas

En cuanto a los frames, hay que tener en cuenta que hay dos diferentes padx y pady, uno es para las cosas dentro del mismo y el otro para ubicarlo al mismo.

Con los frames podemos, nuevamente, usar pack o grid, siendo que esta cualidad se haria DENTRO del elemento "frames" en cambio el pack seria del "label"