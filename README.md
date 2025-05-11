# Tutorial: Rutina de Pick and Place 
En este proyecto se realizó la simulación de una rutina de Pick and Place usando un brazo robótico modelo **ABB irb 140** con un gripper tipo **RobotiQ 2F-85** en la plataforma de simulación **RoboDK**. El objetivo de este proyecto es desarrollar una rutina automatizada que sea capaz de mover los objetos, que se realice la rutina y que estos regresen a su posición inicial.
# 📋 Requisitos previos 
Para llevar a cabo este proyecto, se recomienda:
1. Tener instalado el programa **RoboDK** el cual es un entorno de simulación y programación de robots industriales y te permite modelar estaciones de trabajo, programar trayectorias, entre otras cosas
2. Tener conocimiento básico sobre la programación en Python como lo es:
  a. Importar librerías
  b. Uso básico de objetos
  c. Sintaxis de condiciones

# 📓  Introducción 
Hoy en día, los sistemas robóticos tienen un rol esencial para poder automatizar tareas que son repetitivas, con el propósito de mejorar los sistemas en términos de eficiencia y minimizar los errores humanos. Una de las tareas consideradas de este tipo es la de *Pick-and-Place*, la cual consiste en que un brazo robótico tome una pieza, con una garra o pinza robótica, parte o caja y la mueva a otra posición definida. (Universal Robots, 2025). Es por ello que el *Pick-and-Place* es sumamente usado en líneas de producción o ensamblaje para automatizar estos procesos. Para lograrlo, este proyecto usa el robot **ABB irb 140** y simula lo siguiente:

- Definición de los puntos de paso:
  - **Home**: Posición de inicio y de fin de la rutina (en este caso es la posición 0 del robot)
  - **Pre-pick:** Posición de aproximación antes de tomar el objeto
  - **Pick:** Posición en el que el robot toma el objeto
  - **Pre-place:** Posición de aproximación antes de dejar el objeto
  - **Place:** Posición en dónde se deja el objeto
    
- Tipos de Movimientos:
  - **MoveJ**: Es un movimiento articular empleado para trasladarse de un punto a otro de manera libre (como para moverse de home a pre-pick o de pick a pre-place)
  - **MoveL**: Es un movimiento lineal que se utiliza para moverse en línea recta (como para recojer o soltar un objeto)

NOTA: Además, se usan dos programas auxiliares: *Attach* & *Detach* que permiten hacer la simulación del gripper al tomar y soltar un objeto

# 💾 Instalación necesaria:
El programa **RoboDK** se puede descargar en la siguiente liga: https://robodk.com/download
***Consideraciones:*** 
- Para sistemas operativos: Windows10, Linux y macOS
- Requiere 4GB de RAM
- Almacenamiento aproximado de 500 MB
- **Opcional**: GPU dedicada para un renderizado más fluido

# 🛠️ Instrucciones 
**🤖 Configuración del entorno de trabajo:**
1. Primero, se debe de crear y organización del espacio de trabajo en RoboDk, para ello, se debe de agregar el robot en <ins> Archivo -> Abrir </ins> y seleccionas de la carpeta el archivo *ABB-IRB-140-6-0-8.robot*.
2. Después, se debe de agregar el gripper, para ello, vas a <ins> Archivo -> Abrir </ins> y agregas el archivo *RobotiQ-2F-85-Gripper-Closed.tool* y luego este se debe de poner como el TCP del robot. Para lograrglo, vas al árbol de trabajo y con click derecho, seleccionas el gripper, se abre el menú y le das click en *Attach to* y seleccionas el últomo eslabón del robot. Así, el gripper ya está configurado como el TCP del robot ABB.
3. Una vez logrado lo anterior, se deben de agregar los otros elementos de la estación del trabajo, para ello, se debe de agregar un eje. Se debe de seleccionar el espacio de trabajo (en RoboDK, ver el árbol de trabajo y darle click a la carpeta que aparece al principio), una vez configurado esto, se selecciona este eje y le das click en <ins> Archivo -> Abrir </ins> para agregar la mesa y la caja, los cuales son fijos. Al darle doble click a cada uno de los objetos, los puedes mover y rotar en "x", "y" y "z" las unidades de medida que necesites. En este caso, la mesa se encuentra abajo del robot y la caja se encuentra al costado izquierdo.
4. Finalmente, se agregan de la misma manera que la mesa y la caja, los cubos que quieras simular, en este programa, se agregaron 3 cubos y se posicionaron a un costado derecho del robot y con una distancia en y para que este los pudiera agarrar. (OPCIONAL: Se pueden cambiar de color al apretar el botón de *more configurations* cuando trasladas y rotas el cubo)
5. En la siguiente imagen, se puede ver cómo debe de estar configurado:

**NOTA:** Todos los objetos mencionados para descargar se encuentran en este repositorio: src-> Descargables RoboDk

**🎯 Crear los puntos de paso** 
1. Una vez que toda la estación esté lista, se deben de configurar los puntos de paso para cada uno de los objetos. En este caso que se emplearon 3 cubos, se configuraron 13 puntos de paso (1 punto de Home, 3 puntos de Prepick, 3 puntos de Pick, 3 puntos de Preplace y 3 puntos de Place)
2.   Para ello, primero le das clik al robot cargado dentro del árbol
3.   Luego, le das click al botón: *Add New Target* (el cual es una diana con una flecha) y al darle click derecho a este nuevo target, le puedes cambiar de nombre. 
    a) Como recomendación, pon la posicón y el objeto que estés manipulando para evitar posteriores confusiones.
4. Para el caso de home, le vuelves a dar click derecho y en el menú desplegable, le das click en *Teach current position*
5. Para los demás puntos de paso, se deben de crear los nuevos targets (*Add New Target* y renombrarlo). Para moverlos a otra posición, se debe de seleccionar al robot para que se manualmente se muevan en "x", "y" y "z" y en caso de ser necesario, también se configuran las rotaciones en estos 3 ejes. Una vez que la posición este hecha, se vuelve a dar click derecho y se oprime el *Teach Current Position* para poder proseguir.
6. Estos mismos pasos se deben de repetir para hacer cada punto de paso de toda la rutina.

**⌨ Programas de Attach & Detach**
1. Para realizar estos programas, primero se deben de crear los programas, para ello se da click en el botón *Add Program*  y se debe de renombrar haciendo click derecho -> Rename
2. Luego, debes de agregar una instrucción, para hacerlo, le das click al programa creado y luego en el menú de arriba, en la opción Program->Simulation Event Instruction
3. Una vez agregado, le das doble click a *Simulation Event Instruction* y se abre una pantalla, ahí, se debe de seleccionar la opción de Attach y el TCP que estés utilizando, esto hará que cuando el gripper se acerque al objeto, este se van a juntar, luego, le das click en guardar.
4. Se va a crear otro programa utilizando los pasos 1-3 de esta sección, sólamente que esta vez, en vez de seleccionar la opción de Attach, se debe de configurar como detach para que el objeto lo suelte el TCP, nuevamente, una vez configurado esto, se guarda el programa

**💻 Programa de Python**
1. En el árbol de trabajo, le das click a tu estación y agregas un script de Python, para ello le das click en Add->Program(Pyhton)
2. Una vez generado, le das click derecho al programa y en un menú desplegable, darle click en *Edit Python Program* así, podrás abrir este script y editarlo
3. Primero, se deben de agregar las librerías robolik y robomath. La primera es para tener comunicación con RoboDK y los objetos y programas que se agregaron, el segundo es para realizar las transformaciones de coordenadas y hacer las rotaciones que se configuraron en los puntos de paso:
   
    from robodk import robolink, robomath      
 
4. Luego se hace la conexión con RoboDK que permite conectar con todos los objetos:

   
   RDK = robolink.Robolink()

   
5. Luego, se obtiene el robot importado


    robot = RDK.Item('ABB IRB 140', robolink.ITEM_TYPE_ROBOT)


6. Y también se define el gripper


    tool = RDK.Item('Gripper Closed', robolink.ITEM_TYPE_TOOL)
    robot.setPoseTool(tool)


7. Luego, se debe de obtener los objetos a manipular (en este caso son los cubos)


    cubeblue = RDK.Item('Cube Blue', robolink.ITEM_TYPE_OBJECT)
    cubered = RDK.Item ('Cube Red', robolink.ITEM_TYPE_OBJECT)
    cubegreen = RDK.Item ('Cube Green', robolink.ITEM_TYPE_OBJECT)


8. Después, se deben de definir las posiciones iniciales de los cubos, esto con el objetivo de que al finalizar la rutina, estos regresen ahí:


    cubeblue_home_pose = robomath.transl(450, 140, 0) * robomath.rotx(0) * robomath.roty(0) * robomath.rotz(0)
    cubered_home_pose = robomath.transl(450, 250, 0) * robomath.rotx(0) * robomath.roty(0) * robomath.rotz(0)
    cubegreen_home_pose = robomath.transl(450, 340, 0) * robomath.rotx(0) * robomath.roty(0) * robomath.rotz(0)

NOTA: Los calores de tranlación se obtuvieron a partir de dónde se configuraron inicialmente

9. Luego se deben de obtener los puntos de paso y los programas de Attach/Detach


      homecubeblue = RDK.Item('Home', robolink.ITEM_TYPE_TARGET)
      prepickcubeblue = RDK.Item('Prepick_CubeBlue', robolink.ITEM_TYPE_TARGET)
      pickcubeblue = RDK.Item('Pick_CubeBlue', robolink.ITEM_TYPE_TARGET)
      preplacecubeblue = RDK.Item('Preplace_CubeBlue', robolink.ITEM_TYPE_TARGET)
      placecubeblue = RDK.Item('Place_CubeBlue', robolink.ITEM_TYPE_TARGET)
   
      prog_attachcubeblue = RDK.Item('Attach Cube Blue', robolink.ITEM_TYPE_PROGRAM)
      prog_detachcubeblue = RDK.Item('Detach Cube Blue', robolink.ITEM_TYPE_PROGRAM)


10. Después se deben de definir el tipo de movimiento (Ya sea MoveJ o Move L) dependiendo de lo que se requiera y se selecciona el target a realizar:


    robot.MoveJ(homecubeblue)
    robot.MoveJ(prepickcubeblue)
    robot.MoveL(pickcubeblue)
    prog_attachcubeblue.RunProgram()
    robot.MoveL(prepickcubeblue)
    robot.MoveJ(preplacecubeblue)
    robot.MoveL(placecubeblue)
    prog_detachcubeblue.RunProgram()
    robot.MoveJ(homecubeblue)

    La rutina a seguir es: **Home -> Prepick -> Pick -> Prepick -> Preplace -> Place -> Home**
    
12. Finalmente, se regresa el cubo a su posición original


    cubeblue.setPoseAbs(cubeblue_home_pose)


**NOTA**:Este es el script general, en caso de querer agregar más objetos a manipular, se puede utilizar esto como base

13. Una vez terminado, le das click en *Save* o *Ctrl + S*
14. Para ejecutarlo, das click derecho en el programa de Pyhton, y en el menú desplegable, le das click en <ins>*Run Python Script*</ins>, con esto, el programa corre

# ▶️ Video:
https://www.youtube.com/watch?v=yUIlx9siYtE

# 🏗️ Conclusiones y Poaibles Mejoras
Este proyecto permitó comprender la función y cómo se puede automatizar una rutina básica de Pick-and-Place con un brazo robótico industrial en uns simulación en RoboDK a tarvés de un programa en Python. Es por ello que como conlcusiones tenemos:
- Se puede ver la facilidad de la automatización al implementar este programa, ya que permitió la creación y modificación de los procesos simulados.
- Se comprendió el entorno de RoboDK para poder escalar a proyectos más complejos que involucren sensores o múltiples robots operando juntos.
- En cuanto a la importancia del control, se tiene la creación de puntos de paso y los programas auxiliares que señala la relevancia de mantener una planeación ordenada y precisa
- También, está que gracias a la lógica utilizada, esto se puede aplicar en la industria en líneas de ensamblaje o clasificación de productos.
- Finalmente, el realizar un códgio en Python demostró la versatilidad para poder conectarse a los robots y a los elementos a manipular.

A pesar de que este proyecto se desarrolló en un ambiente simulado, hay grandes opciones de mejora, las cuales no se pudieron realizar por falta de tiempo, sin embargo, estas son algunas propuestas para mejorar este proyecto:
1. Si se realiza una simulación:
    a) Se puede mejorar el proyecto a través de agregar sensores virtuales o lógicos, lo que permite hacer condicionales en base al estado del sensor (por ejemplo: si un cubo está presente o si el cubo se dejó de manera correcta)
   b) Detectar errores, es decir, que dentro del programa de Python se pongan consicionales en caso de que un cubo no esté en su lugar o que haga un parado de emergencia

2. Pasar del plano simulado a conectarlo con un robot ABB Real
Debido a que RoboDK permite exportar los programas a robots físicos, esto se puede lograr utilizando un controlador tipo *IRC5*, para ello se deberá verificar la compatibilidad del robot, luego instalar un driver de comunicación (considerar que el ABB usa el lenguaje *RAPID*) o el *RoboDK Driver for ABB* para conectar la computadora al robot por vía Ethernet y luego cargar el código

Estas son sólamente sugerencias, ya que el proyecto demuestra las múltiples aplicaciones que se pueden generar a partir de una simulación.

# 📖 Referencias y Recursos Adicionales
Librería de RoboDK (en caso de querer buscar más elementos u otros robots): https://robodk.com/es/library

Sistema pick and place: qué es, funcionamiento y principales aplicaciones. (s.f.). https://www.universal-robots.com/mx/blog/sistema-pick-and-place-qu%C3%A9-es-funcionamiento-y-principales-aplicaciones/ 

Repositorio sobre la documentación de RoboDK- Python: https://github.com/RoboDK/RoboDK-API/blob/master/Python/readme.md

# 📞 Contacto
Para preguntas o sugerencias: 

- Asesor encargado de la página: Dr. César Martínez Torres
    - 📥Correo electrónico:
      cesar.martinez@udlap.mx
    
- Redctor del tutorial: Paulina Gómez Olvera Carpinteyro
    - 📥Correo electrónico:
      paulinagoc@outlook.com 
