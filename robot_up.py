from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from colors import *
from math import pi,sin,cos
from shapes import SolidRectangle, SolidCylinder

class Robot:
    def __init__(self):
        self.legLenght        = 2.0
        self.legDiameter      = 0.3 

        self.jointSize        = 0.2

        self.feetLenght       = 0.70
        self.feetWidth        = 0.30
        self.feetHeight       = 0.15

        self.armDiameter      = 0.25
        self.forermLenght    = 1.2
        self.armLenght        = 1.2

        self.neckLenght       = 0.4
        self.neckDiameter     = 0.4

        self.headHeight       = 0.8
        self.headLenght       = 0.7

        self.torsoLenght      = 0.6
        self.torsoWidth       = 1.6
        self.torsoHeight      = 2.0

        self.rightLegFAngle   = 20.0
        self.rightLegSAngle   = 0.0
        self.leftLegFAngle    = -20.0
        self.leftLegSAngle    = 0.0

        self.rightKneeAngle   = 0.0
        self.leftKneeAngle    = 0.0

        self.rightArmFAngle   = 0.0
        self.rightArmSAngle   = 0.0
        self.leftArmFAngle    = 0.0
        self.leftArmSAngle    = 0.0

        self.rightElbowFAngle = 0.0
        self.rightElbowSAngle = 0.0
        self.leftElbowFAngle  = 0.0
        self.leftElbowSAngle  = 0.0

        

    def draw(self):
        glPushMatrix()
        glPushMatrix()
        
        # Corpo
        glColor3f(*light_gray)
        SolidRectangle(self.torsoWidth, self.torsoHeight, self.torsoLenght)

        # Cabeca
        glPushMatrix()
        glColor3f(*light_gray)
        glTranslatef(0.0, self.torsoHeight / 2.0 + self.neckLenght / 2.0, 0.0)
        SolidCylinder(self.neckDiameter / 2.0, self.neckLenght, 20)                 # Pescoco
        glTranslatef(0.0, self.neckLenght / 2.0 + self.headLenght / 2.0, 0.0)
        glColor3f(*white)
        SolidRectangle(self.headLenght, self.headHeight, self.headLenght)           # Cabeca
        glPopMatrix()

        # Perna direita
        glPushMatrix()
        glColor3f(*dark_gray)
        glTranslatef(self.torsoWidth / 2.5, -(self.torsoHeight / 2.0), 0.0)
        glutSolidSphere(self.jointSize, 25, 25)                                     # Junta quadril
        glRotatef(-self.rightLegSAngle, 0, 1, 0)
        glRotatef(self.rightLegFAngle, 1, 0, 0)
        glTranslatef(0.0, -(self.legLenght / 4.0), 0.0)
        glColor3f(*light_gray)
        SolidCylinder(self.legDiameter / 2.0, self.legLenght / 2.0, 20)             # Coxa
        glTranslatef(0.0, -(self.legLenght / 4.0), 0.0)
        glColor3f(*dark_gray)
        glutSolidSphere(self.jointSize, 25, 25)                                     # Junta joelho
        glRotatef(-self.rightKneeAngle, 1, 0, 0)
        glTranslatef(0.0, -(self.legLenght / 4.0), 0.0)
        glColor3f(*light_gray)
        SolidCylinder(self.legDiameter / 2.5, self.legLenght / 2.0, 20)             # Perna
        glTranslatef(0.0, -(self.legLenght / 4.0 + self.feetHeight / 3.0), -(self.feetLenght / 4.0))
        glRotatef(90, 0, 0, 0)
        glColor3f(*black)
        SolidRectangle(self.feetWidth, self.feetHeight, self.feetLenght)            # Pe
        glPopMatrix()

        # Perna esquerda
        glPushMatrix()
        glColor3f(*dark_gray)
        glTranslatef(-(self.torsoWidth / 2.5), -(self.torsoHeight / 2.0), 0.0)
        glutSolidSphere(self.jointSize, 25, 25)                                     # Junta quadril
        glRotatef(-self.leftLegSAngle, 0, 1, 0)
        glRotatef(self.leftLegFAngle, 1, 0, 0)
        glTranslatef(0.0, -(self.legLenght / 4.0), 0.0)
        glColor3f(*light_gray)
        SolidCylinder(self.legDiameter / 2.0, self.legLenght / 2.0, 20)             # Coxa
        glTranslatef(0.0, -(self.legLenght / 4.0), 0.0)
        glColor3f(*dark_gray)
        glutSolidSphere(self.jointSize, 25, 25)                                     # Junta joelho
        glRotatef(-self.leftKneeAngle, 1, 0, 0)
        glTranslatef(0.0, -(self.legLenght / 4.0), 0.0)
        glColor3f(*light_gray)
        SolidCylinder(self.legDiameter / 2.5, self.legLenght / 2.0, 20)             # Perna
        glTranslatef(0.0, -(self.legLenght / 4.0 + self.feetHeight / 3.0), -(self.feetLenght / 4.0))
        glRotatef(90, 0, 0, 0)
        glColor3f(*black)
        SolidRectangle(self.feetWidth, self.feetHeight, self.feetLenght)            # Pe
        glPopMatrix()

        # Quadril
        glPushMatrix()
        glTranslatef(0.0, (self.torsoHeight / 2.0), 0.0)
        glRotatef(90, 0, 0, 1)
        SolidCylinder(0.12, self.torsoWidth * 1.43, 20)                             # Eixo quadril
        glPopMatrix()

        # Braço direito
        glPushMatrix()
        glColor3f(*dark_gray)
        glTranslatef(-(self.torsoWidth * 0.7), (self.torsoHeight / 2.0), 0.0)
        glRotatef(self.rightArmSAngle, 0, 1, 0)
        glRotatef(self.rightArmFAngle, 1, 0, 0)
        glutSolidSphere(self.jointSize, 25, 25)                                     # Ombro
        glTranslatef(0.0, -(self.armLenght / 2.0), 0.0)
        glColor3f(*light_gray)
        SolidCylinder(self.armDiameter / 2.0, self.armLenght, 20)                   # Braco 1
        glTranslatef(0.0, -(self.armLenght / 2.0), 0.0)
        glColor3f(*dark_gray)
        glutSolidSphere(self.jointSize, 25, 25)                                     # Cotovelo
        glRotatef(self.rightElbowSAngle, 0, 1, 0)
        glRotatef(self.rightElbowFAngle, 1, 0, 0)
        glTranslatef(0.0, -(self.forermLenght / 2.0), 0.0)
        glColor3f(*light_gray)
        SolidCylinder(self.armDiameter / 2.5, self.forermLenght, 20)                # Braco 2
        glPopMatrix()

        # Braço esquerdo
        glPushMatrix()
        glColor3f(*dark_gray)
        glTranslatef((self.torsoWidth * 0.7), (self.torsoHeight / 2.0), 0.0)
        glRotatef(self.leftArmSAngle, 0, 1, 0)
        glRotatef(self.leftArmFAngle, 1, 0, 0)
        glutSolidSphere(self.jointSize, 25, 25)                                     # Ombro
        glTranslatef(0.0, -(self.armLenght / 2.0), 0.0)
        glColor3f(*light_gray)
        SolidCylinder(self.armDiameter / 2.0, self.armLenght, 20)                   # Braco 1
        glTranslatef(0.0, -(self.armLenght / 2.0), 0.0)
        glColor3f(*dark_gray)
        glutSolidSphere(self.jointSize, 25, 25)                                     # Cotovelo
        glRotatef(self.leftElbowSAngle, 0, 1, 0)
        glRotatef(self.leftElbowFAngle, 1, 0, 0)
        glTranslatef(0.0, -(self.forermLenght / 2.0), 0.0)
        glColor3f(*light_gray)                                                      # Braco 2
        SolidCylinder(self.armDiameter / 2.5, self.forermLenght, 20)
        glPopMatrix()
        glPopMatrix()
        glPopMatrix()

robo = Robot()
angle = 300.0
angle_arms=300.0
spin = True
turn_h = 1
up_arms = False

def keyboard(key,x,y):
    global spin, turn_h, angle, up_arms

    key = ord(key)
    # Esc para sair
    if key==27:
        exit(0)
    elif key==ord('s'):
        spin = not spin
    elif key==ord('a'):
        turn_h = -1
    elif key==ord('d'):
        turn_h = 1
    elif key==ord('u'):
        up_arms = True
    else:
        return
        

def display():
    global spin, angle, up_arms, angle_arms

    glMatrixMode(GL_MODELVIEW)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(*blue_sky)
    glLoadIdentity()

    gluLookAt(-6.0, 4.0, -6.0,
                0.0, 2.9,  0.0,
                0.0, 1.0,  0.0)
    
    # Controle de camera
    if spin:
        angle += turn_h*0.5
    angle %= 360

    if up_arms:
        angle_arms += turn_h*0.5
    angle_arms %= 360

    robo.rightLegFAngle = cos(angle / 180.0 * 4.0 * pi) * 22.5
    robo.rightKneeAngle = (-sin(angle / 180.0 * 4.0 * pi) + 1) * 30.0
    robo.leftLegFAngle = cos((angle + 180.0) / 180.0 * 4.0 * pi) * -22.5
    robo.leftKneeAngle = (sin((angle + 90.0) / 180.0 * 4.0 * pi) + 1) * 30.0
    robo.rightLegSAngle = (sin(angle / 180.0 * 4.0 * pi) + 1) * 5.0
    robo.leftLegSAngle = (sin(angle / 180.0 * 4.0 * pi) + 1) * -5.0
    
    if up_arms:
        if robo.rightArmFAngle<0.0:
            up_arms = False
        robo.rightArmFAngle = abs(cos(angle_arms / 180.0 * 4.0 * pi) * 150)-1
        #robo.rightArmSAngle = (sin(angle_arms / 180.0 * 4.0 * pi) + 1) * 0.0
        #robo.rightElbowFAngle = abs((-sin(angle_arms / 180.0 * 4.0 * pi)) * 15.0)
        robo.leftArmFAngle = abs(cos((angle_arms + 180.0) / 180.0 * 4.0 * pi) * 150)-1
        #robo.leftArmSAngle = (sin(angle_arms / 180.0 * 4.0 * pi) + 1) * -0.0
        #robo.leftElbowFAngle = abs((-sin((angle_arms + 90.0) / 180.0 * 4.0 * pi)) * 15.0)
        
        
    glRotatef(angle, 0, 1, 0)

    
    # Base
    glPushMatrix()
    glColor3f(*grass)
    glNormal3f(0.0, 1.0, 0.0)
    glBegin(GL_QUADS)
    glVertex3f(-30.0, 0.0, -30.0)
    glVertex3f(-30.0, 0.0,  30.0)
    glVertex3f( 30.0, 0.0,  30.0)
    glVertex3f( 30.0, 0.0, -30.0)
    glEnd()

    # Robo
    glTranslatef(0.0, 3.5, 0.0)
    robo.draw()
    glPopMatrix()

    glFlush()
    glutSwapBuffers()


# Main
width  = 800
height = 600
glutInit()
glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(width, height)
glutCreateWindow("Robo - Menderson e Vinicius")

glutDisplayFunc(display)
glutIdleFunc(display)
glutKeyboardFunc(keyboard)

glViewport(0, 0, width, height)
glLoadIdentity()
glMatrixMode(GL_PROJECTION)
aspect = width / height
gluPerspective(45, aspect, .01, 100.0)
glMatrixMode(GL_MODELVIEW)
glShadeModel(GL_SMOOTH)
glClearDepth(1.0)
glEnable(GL_DEPTH_TEST)
glDepthFunc(GL_LEQUAL)
glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)
glClearColor(0.0, 0.0, 0.0, 1.0)

mat_shininess  = [ 32.0 ]
mat_specular   = [ 0.75, 0.75, 0.75, 0.75 ]
light_ambient  = [ 0.4, 0.4, 0.4, 1.0]
light_diffuse  = [ 0.8, 0.8, 0.8, 0.9]
light_specular = [ 1.0, 1.0, 1.0, 0.1]
light_position = [ 6.0, 6.0, 2.0, 0.0]

glMaterialfv(GL_FRONT, GL_SPECULAR,  mat_specular)
glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)

glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)

glLightfv(GL_LIGHT0, GL_POSITION, light_position)

glEnable(GL_LIGHTING)
glEnable(GL_LIGHT0)

glEnable(GL_COLOR_MATERIAL)

glLightModeli(GL_LIGHT_MODEL_TWO_SIDE, GL_TRUE)

glutMainLoop()
