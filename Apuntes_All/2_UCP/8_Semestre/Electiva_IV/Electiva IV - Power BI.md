## Clase 30 Julio

La asignatura se centra en la analítica de datos. Mediante la aplicación *PowerBi*, seguidamente se trabajaran con distintas fuentes de datos las cuales no se reducen a las _Bases de Datos_, por tanto, la idea es entender los diferentes tipos de datos, todo miente la conexión a diferentes tipos de datos. Cuando tenemos acceso a una fuente de datos se presenta una diferencias entre datos locales y compartidos. **La idea es equivocarse lo menos posible** con el tratamiento de datos.

> Popularmente la información se pueden encontrar en distintos formatos.

La asignatura tiene un enfoque génerico.

# Índice

#### Semana 1
- Socialización Plan de Asignatura
- Políticas Evaluativas
- 
#### Semana 2
- 
- 
#### Semana 3
- ¿Qué es transformar datos?
- Tipos de datos en Power Bi
- Modificación de tipos de datos
- Errores comunes
- Power Query
- Pivote
- Combinación de Tablas
- Fusión de fuentes de datos
#### Semana 4 - 5
- Carga de datos
- Proceso ETL
- Perfilar datos
- Datos Erróneos
- Power Query y Consultas
#### Semanas 6
- *Primer Parcial de la Asignatura*
#### Semana 7
Aquí se comienza a trabajar el modelado de datos, como el modelo estructural. El *Modelo en Estrella* y *Modelo Copo de Nieve*, buscando una buena representación de los datos para representarlos en esquemas.
- Conceptos de Modelo de Datos
- Esquemas planos
- Normalización y Desnormalización
- Esquema Star -> Modelo en Estrella
- Esquema SnowFlake -> Modelo Copo de Nieve
#### Semana 8
- Funciones estadísticas básicas
- Crossfiltrer
- Calcular
- User Relationship
#### Semana 9 - 10
- Rendimiento en Power BI
- Optimización en Power Bi
- DirectQuery
- Agregación
#### Semana 11
- *Segundo Parcial dela Asignatura*

#### Semana 12
- Visualizaciones
- Informes de venta
- Gráficos
#### Semana 13
- Formato Condicional
- Jerarquías 
- Clasificación
- Cortadoras
- Botones
- Marcadores
- Filtros  DAX
#### Semana 14 - 15 - 16
- **Ejercicio Final de la Asignatura**.
La temática para el trabajo final de la asignatura contará como *Examen final*.

> Las políticas evaluativas son las siguientes:

- [ ] Primer Parcial 20% - (%15 trabajo - %5 Parcial)
- [ ] Segundo Parcial 20% - (%15 trabajo - %5 Parcial)
- [ ] Tercer Parcial 20%
- [ ] Examen Final 20% - (%15 trabajo - %5 Parcial)
- [ ] Trabajos en Clase 20% - (%5 Asistencia - %15 Quizes y Trabajos)

----
Introuduccion, trabajar con origines de datos, siendo estos datos digitales salidos de bases de datos, archivos, apis, sitios  web ya que muestran tendencias, pdf archivos de word, archivos de texto como fuentes de datos, siendo los origenes locales o en la nube, donde se debe consultar a los administradores para poder extraer la informacions, el origen de datos es de donde proviene la informacion

origen de dato clasico, excel, archivos csv, xml, json, pdfs

-----
Clase 13 agosto

Se trabajará la carga de datos durante la clase. Todo es compatible entre tecnologías Microsoft. SE utiliza sql server manager para la carga de datos

Se obtienen datos y se selecciona base de datos sql server y se conecta, siendo el servidor. y se elige la base de datos de ejemplo adventure works. Importante tener en cuenta las columnas de relación para la realización de informes, incluir las columnas de relaciones. Es importante ya que ayuda a saber que tablas tienen o no tienen relación. Y encontrara una cantidad de tablas. Es más fácil la conexión directa ya que no utilizamos nada localmente. para el modo dual requerimos de una red montada en propiedades avanzado para activar el modo DUAL para hacer filtros y traer los datos a mi equipo.

Tema transformacion de datos usando power bi

hay que conocer que power bi, excel y demas herramientas de analisis tiene el power query que permite hacer consultas en bases de datos de tipo Microsoft. A través de powerQuery como similitud a excel para realizar tareas.

se ingrese por transformar datos, hay diferentes tipos de errores debido a datos no cargados, algunos casos no tienen datos relacionados.. La mayoria de los errores es porque los datos no están diligenciados. en transformar se remplazan los valores(error) y se cambia por un número.

los pasos aplicados son los cambios a el trabajo que hemos realizado. se pueden deshacer las acciones y cambiar de orden. muestra las operaciones o transformaciones a los datos aplicados a power query

PIVOTS

Se elige una o unas columnas para consolidarse en un Tipo PIVOT y se llama columna dinámica y en opciones avanzadas elegir la operación para crear las distinciones.

