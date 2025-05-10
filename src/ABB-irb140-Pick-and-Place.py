from robodk import robolink, robomath

# Conexión con RoboDK
RDK = robolink.Robolink()

# Obtener el robot
robot = RDK.Item('ABB IRB 140', robolink.ITEM_TYPE_ROBOT)

# Definición de la Herramienta (Gripper)
tool = RDK.Item('Gripper Closed', robolink.ITEM_TYPE_TOOL)
robot.setPoseTool(tool)

# Definición de los Cubos
cubeblue = RDK.Item('Cube Blue', robolink.ITEM_TYPE_OBJECT)
cubered = RDK.Item ('Cube Red', robolink.ITEM_TYPE_OBJECT)
cubegreen = RDK.Item ('Cube Green', robolink.ITEM_TYPE_OBJECT)

# Definir la Pose inicial de los cubos
cubeblue_home_pose = robomath.transl(450, 140, 0) * robomath.rotx(0) * robomath.roty(0) * robomath.rotz(0)
cubered_home_pose = robomath.transl(450, 250, 0) * robomath.rotx(0) * robomath.roty(0) * robomath.rotz(0)
cubegreen_home_pose = robomath.transl(450, 340, 0) * robomath.rotx(0) * robomath.roty(0) * robomath.rotz(0)


# Targets/ Puntos de paso a hacer
homecubeblue = RDK.Item('Home', robolink.ITEM_TYPE_TARGET)
prepickcubeblue = RDK.Item('Prepick_CubeBlue', robolink.ITEM_TYPE_TARGET)
pickcubeblue = RDK.Item('Pick_CubeBlue', robolink.ITEM_TYPE_TARGET)
preplacecubeblue = RDK.Item('Preplace_CubeBlue', robolink.ITEM_TYPE_TARGET)
placecubeblue = RDK.Item('Place_CubeBlue', robolink.ITEM_TYPE_TARGET)

homecubered = RDK.Item('Home', robolink.ITEM_TYPE_TARGET)
prepickcubered = RDK.Item('Prepick_CubeRed', robolink.ITEM_TYPE_TARGET)
pickcubered = RDK.Item('Pick_CubeRed', robolink.ITEM_TYPE_TARGET)
preplacecubered = RDK.Item('Preplace_CubeRed', robolink.ITEM_TYPE_TARGET)
placecubered = RDK.Item('Place_CubeRed', robolink.ITEM_TYPE_TARGET)

homecubegreen = RDK.Item('Home', robolink.ITEM_TYPE_TARGET)
prepickcubegreen = RDK.Item('Prepick_CubeGreen', robolink.ITEM_TYPE_TARGET)
pickcubegreen = RDK.Item('Pick_CubeGreen', robolink.ITEM_TYPE_TARGET)
preplacecubegreen = RDK.Item('Preplace_CubeGreen', robolink.ITEM_TYPE_TARGET)
placecubegreen = RDK.Item('Place_CubeGreen', robolink.ITEM_TYPE_TARGET)

# Programas de Attach/Detach de cada cubo
prog_attachcubeblue = RDK.Item('Attach Cube Blue', robolink.ITEM_TYPE_PROGRAM)
prog_detachcubeblue = RDK.Item('Detach Cube Blue', robolink.ITEM_TYPE_PROGRAM)

prog_attachcubered = RDK.Item('Attach Cube Red', robolink.ITEM_TYPE_PROGRAM)
prog_detachcubered = RDK.Item('Detach Cube Red', robolink.ITEM_TYPE_PROGRAM)

prog_attachcubegreen = RDK.Item('Attach Cube Green', robolink.ITEM_TYPE_PROGRAM)
prog_detachcubegreen = RDK.Item('Detach Cube Green', robolink.ITEM_TYPE_PROGRAM)

# --------------------------- Movimientos -----------------------------#

# --------------------------- Bloque Azul ------------------------------#
robot.MoveJ(homecubeblue)
robot.MoveJ(prepickcubeblue)
robot.MoveL(pickcubeblue)

prog_attachcubeblue.RunProgram()  #Correr programa para agarrar cubo azul

robot.MoveL(prepickcubeblue)
robot.MoveJ(preplacecubeblue)
robot.MoveL(placecubeblue)

prog_detachcubeblue.RunProgram()  # Correr programa para soltar cubo azul

robot.MoveL(preplacecubeblue)

# --------------------------- Bloque Rojo ------------------------------#
robot.MoveJ(homecubered)
robot.MoveJ(prepickcubered)
robot.MoveL(pickcubered)

prog_attachcubered.RunProgram()  # Correr programa para agarrar cubo rojo

robot.MoveL(prepickcubered)
robot.MoveJ(preplacecubered)
robot.MoveL(placecubered)

prog_detachcubered.RunProgram()  # Correr programa para soltar cubo rojo


robot.MoveL(preplacecubered)

# --------------------------- Bloque Verde ------------------------------#
robot.MoveJ(homecubegreen)
robot.MoveJ(prepickcubegreen)
robot.MoveL(pickcubegreen)

prog_attachcubegreen.RunProgram()  # Correr programa para agarrar cubo verde

robot.MoveL(prepickcubegreen)
robot.MoveJ(preplacecubegreen)
robot.MoveL(placecubegreen)

prog_detachcubegreen.RunProgram()  # Correr programa para soltar cubo verde

robot.MoveL(preplacecubered)

# Regresar a home 
robot.MoveJ(homecubeblue)

# ----- Poner el cubo a su lugar -----
cubeblue.setPoseAbs(cubeblue_home_pose)
cubered.setPoseAbs(cubered_home_pose)
cubegreen.setPoseAbs(cubegreen_home_pose)

#print("✔️ Secuencia completada y cubo restablecido a posición original.")
