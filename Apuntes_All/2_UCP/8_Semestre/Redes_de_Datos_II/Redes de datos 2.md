
temas
introduccion al enrutamiento de red
protocolo de internet
taller de servicio control de traifoc
tecnologia mpls
voz sobre paquetes
seguridad en redes ip
tecnologias de acceso a banda ancha

## inreoduccion al enrutamiento de red

MOdelo osi tiene 7 capas, y el protocolo tcp/ip tiene 4 capas, se basan en protocolos para permitir en resumen compartir equipos en una red, pero los diseñadores de los modelos referencias fue iso, como creador de tcp/ip, con el proceso de enviar un paquete es complicado, no es tan facil como parece, pero cuando tenemos un problema muy grande. "iso creo las normas de referencias", se dividieron el proceso en capas, y cada capa 
1fisica
2enlace
3red
4transporte
5sesion
6presentacion
7aplicación

> la capa de red se enfrenta a un problema mas grande, para solucionar el problema de equipos de redes diferentes se pueda comunicar, enrutando.

Diferencia de tcp y udp, tcp recibe y confirma orientado a la conexion, y udp llega pero no confirma.
Hay un protocola de errores crc, crea el codigo aplica el codigo divido en paquetes y se envia por pedazos,  y verificar el archivo correcto

udp ejemplo transmision de video youtube, zoom clases virtuales consumir menor ancho de banda para evitar errorres, vigilancia requiere anchos muy grandes oporque envian bastante informacion. transmitir video es muy complicado y lo que se requiere para que funciona

ya puedo enrutar, como hago para poder crear la conexion, crear sockets, permite establecer una url y el puerto para conectarse

cors, desarrollo local y muchas veces se usan un socket 3000, todo montado sobre el mismo socket, la robustes es con 2 sockets un backend y un frontend, cors es una serie de permisos para determinar que sockets tiene accesos. cors jwt

enrutar paquetes, es con una ruta conocida llegar a una ruta que no conozco

la puerta enlace es el amigo que me ayuda a buscar a quien no conozco, preguntando y saltando llega.
porque cuando llega asi mismo se devueve.
definir como crear las rutas, preguntando preguntando preguntando, porque a simple vista si tenemos la capacidad de ver la red conozco la direccion de cada equipo, puerto conexion y direccion ip, nosotros decidimos por donde viaja nuestra nota, ejemplo conoces la ruta de viaje para llegar a nuestro hogar y sus opciones, llegando al enrutamiento estatico done ya se por donde ir y yo eligo por donde, dinamico yo poco a poco voy construyendo como enviar mis paquetes

rutamiento dinamico se hace automatico, solo se configura un parametro y los routers se encargan del resto, creando ellas solas la tabla de enrutamiento.
exmane final, se dañaron 3 enrutadores corregir el enrutamiento borrar todo porque es estatico y no cambia, y comenzar de cero.

estatico fue el primer esquema, entonce dijieron venga

en una red de comunicaciones no todos tiene el mismo ancho de banda, viaje a cartago y hay un trancon, tomar la ruta mas larga
-  esstado enlace=elige la mejor ruta dependiendo del estado de los enlaces, cuales estan encendidos para llegar
- vector distancia=mientras que este no le importa, no se fia por el enlace activo, sino por el peso de ancho banda, ya que tienen los enlaces mas grandes.
el enrutamiento calcula automatico, si se cae recalcula

investigarlos dinamicos

----
protocolos de enrutamiento estado enlace ospf,i5t5
vector distancia igrp, rip

eigrp
vlans vs lan

broadcast dominio broadcast

partir vlans es crear dominios de broadcast
dominios de broadcast, entre mas divisiones de broadcast mejor, informacion importante vlan de una, administrativa, mediante cable consola, luego el resto de usuarios regulares de la red otra vlan, importante la separacion, llamada segmentacion.

tener dominios de red es mas efiiente, y hay 2 maneras, ejemplo red 192.168.0.0/24 es una red, segementamos en 2 redes 192.168.1.0/24 o 192.168.2.0/24, o soy perezoso y dejo la misma 192.168.0.0/24, el problema de esta ultima es que se pueden enviar informacion, es un porbleam porque si hay una salida a internet a switch con un router 192.168.0.1, la segmentada vlan2 no puede ver la salida a internet.

al dividir vlan no se comunican pero se puede configurar el enrutador.

en capa 3 ya no se divide trafico de red, es trafico de enrutamiento. 4 routers, solo 2 y 2 se ven, para evitar repetir wan, se hace subneting y quedan /30

subneting ir restando de a 2, se da un nombre ip a cada interfaz, se para en un enrutador, asignar metricas 0.0.0.0 defecto, si no sirve busca la metrica 100, y si esta dañada metrica 200

tarea hacer routers,metrica en dinamico es estado enlace y vector distancas, se debe hcaer todo el enrutado en esta caso estatico para continuar, prox enrutamiento dinamico

router eigrp (motor) -> todos en el mismo motor
do show ip interface brief

colocar un motor de 100


---
mpls
