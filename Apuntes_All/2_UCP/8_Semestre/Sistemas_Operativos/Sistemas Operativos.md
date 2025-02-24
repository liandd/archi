
## Clase Julio 31

La asignatura corresponde a un trabajo autónomo de 6 horas. La materia suple conocimientos y formación para los Ingenieros de Sistemas para abordar sistemas de computo, procesos, estructura y como se diseña un sistema operativo desde 0. Como los procesos de administración siendo estos Windows, Linux y Android.

> La administración de sistemas de información es el punto clave de esta materia.

La materia de Sistemas Operativos ayuda con la profundización relacionados con la administración de Hardware y Software de sistemas de computo.

Describir -> Clasificar -> Analizar, siendo los pasos que debemos de lograr.2

# Índice

## Tema 1 - Introducción
- ¿Qué es un sistema operativo?
- Conceptos y funciones básicas en Sistemas Operativos
- Tipos de sistemas operativos
- Conceptos de Hardware necesarios para los SO
## Tema 2- Gestión de Procesos
- Introducción a los procesos
- Planificación de procesos
- Comunicación entre procesos(IPC)
- Llamada de procesos por memoria compartida
- Llamada de procesos por Interrupciones
## Tema 3 - Periféricos de I/O

## Tema 4 - Administración de Memoria

## Tema 5 - Sistema de archivos

## Tema 6 - Sistemas Operativos Actuales



### Fechas

- [ ] Primer Parcial 20%(individual) (Introducción, Procesos, Hilos y Planificación).
- [ ] Segundo Parcial 20%(individual) (Dispositivos de Entrada/Salida, Administración de Memoria, Memoria Virtual, Estructura de Almacenamiento Secundario, Sistemas de Archivos)
- [ ] Talleres: 20% (grupos máximo de dos)
- [ ] Examen final: 20%(individual)
----
## Introducción
- ¿Que hace un sistema operativo?
- Organización del sistema de computo
- Arquitectura del sistema de computo
- Estructura del sistema operativo
- Operaciones del sistema operativo
- Administración de procesos

> Un programa es un proceso que antes de compilarse tiene unas líneas de código

Un proceso es un programa en ejecución, ya que antes de ejecutarse, cuando se ejecute en la CPU es un proceso, mientras no se ejecute se llama programa. *El sistema operativo es un programa* siendo un intermediario entre un usuario y el Hardware. Ya que el sistema operativo debe dar el permiso para poder realizar una acción. Todo programa debe pedir el permiso a el sistema operativo.
Objetivo primordiales
- Ejecutar los programas del usuario, brindando los recursos y los permisos
- El uso del sistema general, siendo este la optimización del uso del Hardware.

En un sistema de computo lo primordial es el Hardware, en su defecto montar un sistema operativo/máquina virtual, si este no hay una interacción entre usuario y Hardware. Si no hay sistema operativo y hay un programa instalado se llama *programa de aplicación*.

Hay diferentes sistemas de computo debido al uso (Personales, Servidores, Workstations, Moviles, Embebidos)

Un sistema embebido es una máquina controlada con un sistema especial para hacer un tipo de control, pero cumplen su función especifica.
## Punto de vista: Sistema
 El sistema mira el recurso que se esta solicitando y decide a quien dar las prioridades.
 - Administra todos los recursos.
 El sistema operativo tambien es un flujo de control, ya que este decide que proceso usa la cpu, ,si hay 20 procesos el elige entre los que hay en cola, cual usa el nucleo de la cpu. hay que decidir usando algoritmos de planificacion. Con la idea de prevenir errores.
Desde que arranca el sistema operativo hay un programa que se ejecuta todo el tiempo, administraciones de los recuros y programas.

## Organizacion del sistema de computo

Ejecucion concurrente, donde los programa compiten por el acceso a la memoria. Cuando la ram se llena  y llega un nuevo proceso le hace crear al nuevo que hay 1 proceso usando todo el ram. Aqui entra la swap.

Los procesos leen todo desde la ram.
El controlador es un programa que informa a la cpu que un proceso ha finalizado mediante algo llamado interrupcion.

## Inicio de la computadora

Hay un programado llamado boostrap guardado en la rom o en la eeprom, el encargado de correr cuando se enciende la máquina y se reinicia. Si se daña se perdio. Cuando arranca el boostrap

> Kernel programa pequeño que arranca las partes basicas.

## Interrupciones
Los procesos se ejecutan por nucleo de cpu, cuando un disposito i/o manda mensaje, el cpu corta el proceso que se esta ejecutando corta el proceso "se interrumpe" analiza el impulso de la entrada y luego reaunuda el proceso de nuevo.

Es mucho mas optimo trabajar con interrupciones. Transfiere el control a la rutina de servicio de la misma. Mediante vectores de interrupciones guardado en memoria ram -> instrucciones y datos.

No se puede interrumpir una interrupcion, se deshabilita.
**Un sistema operativo es manejado por las interrupciones** optimizando el uso de la cpu

Manejo de las interupciones
- Registros -> Datos reciente de lo que se va a ejecutar
- Contador de programa -> guarda la direcciones de la siguiente instruccion que se va ejecutar
Sincrono -> espera
asincorno -> no espera

## introduccion dma
direct memory access, algunas funciones no necesitan hacer saltos para ir de una parte a otra.

controlador escribe directamente en la ram si pasar or la cpu.

## Estructura de almacenamiento

ram como memoria principal donde la cpu solo escribe en la ram, siendo secundarios lo qu eno sea ram.

multiprogramacion: tirar varias tareas y en teoria ejecutar al mismo tiempo, un  proceso por nucleo al mismo tiempo
el sistema operativo para ejecutar varias tareas al mismo tiempo, hay un espacio reservado solo para la memoria ram que no puede tocar ningun otro programa, siendo todo proceso partido en 2(código y datos), al hacer una tarea son separados, de tal manera que un trabajo siempre se esta ejecutando, dependiendo del numero de nucleos ejecuto los procesos al mismo tiempo. Se utiliza una estructura de tipo cola, no todos los procesos se cargan porque la ram se llena. una tarea se selecciona y se ejecuta, planificadores. para escojer la siguiente tarea que ejecutara el cpu.
el so se encarga de la administracion de los procesos asegurarando que este el tiempo de la cpu este al 100%, para aprovecharlo

tiempo compartido: los procesos comparten tiempo de cpu, cuando un proceso se ejecuta, no se le da el tiempo y se interrumpe, ya que se comparte. el tiempo de respuesta deberia ser < a 1 segundo.

todas las tareas listas deben entrar en una cola y se debe escoger el siguiente, cuando la ram se llena se hace swap. el archivo de paginacion pesa correspondiente al tamaño asignado de swap en disco.

memoria virtual permite la ejecucion de procesos no completo en ram, es decir instrucciones o datos en ram o en disco. cuando no la encuentra en ram busca en disco, pero si no lo encuentra pantalla azul.

el sistema operativo esta controlado por el hardware en las entradas y salidas generando interurrupciones, hay algunos errores que se llaman excepciones o trap. puede suceder que un proceso escribe en la memoria de otro proceso

todas las operaciones se hacen en modo dual, modo usuario o kernel siendo el kernel el que cuenta con todos los permisos, y el modo usuario esta restringido.

el timer es el tiempo que se da para el acceso a los recursos.

llamada al sistema es una peticion a modo de funcion o metodo. Siempre se pide permiso al sistema operativo

el programa es una entidad pasiva, cuando se pone a correr se vuelve un proceso porque hace uso de los recursos del equipo
el proceso necesita
cpu
memoria
archivos
inicializar datos

cuando se acaba un proceso debe retornar los recursos.

ahora cualquier sistema tiene muchos proceso ejecutandose al mismo tiempo y es concurrente, un sistema operativo manejo un concepto llamado concurrencia de varios procesos al mismo tiempo y darle ese efecto al usuario, multiplexado.

el so con los procesos los crea y los elimina como administrador del sistema. suspencion o reactivacion de procesos. y debe proveer mecanimos de sincronizacion para decidir que proceso usa los recursos y los demas procesos quedan en cola, y solo 1 se ejecuta. Interbloqueo en el intercambio de recursos

memoria.
todos los datos deben recidir en memoria antes y despues del procesamiento, si no esta en memoria no se puede ejecutar si no esta en disco pantalla azul.
se busca en memoria que hay, para saber que se debe optimizar y el tiempo de respuesta. Para saber quien usa o no usa cpu buscando que siempre este ocupada. crea tabla para llevar registro de que poner en memoria ram, ocupa y desocupa.

el so sabe que hay programas que controlan el acceso a las unidades de almacenamiento

cache, es una memoria intermedia hay una cache de registros y de la memoria principal


