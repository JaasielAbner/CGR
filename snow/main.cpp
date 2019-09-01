#include "main.hpp"
structFloco Floco[QTDFLOCOS];

void iniciaFloco(int i) {
	Floco[i].viva = true;
	Floco[i].vida = 1.5;
	Floco[i].desaparecer = float(rand() % 100) * 0.001;
	Floco[i].xPos = (float) (rand() % 100)/15;
	Floco[i].yPos = 5; //altura de onde começa os Flocos
	Floco[i].zPos = (float) (rand() % 100)/15;
	Floco[i].vel = 0;
	Floco[i].gravidade = -0.0005;
}

void init() {
	for (loop = 0; loop < QTDFLOCOS; loop++) {
		iniciaFloco(loop);
	}
}

void criaChuva() {
	float x, y, z;
	for (loop = 0; loop < QTDFLOCOS; loop = loop + 2) {
		if (Floco[loop].viva == 1) {
			x = Floco[loop].xPos;
			y = Floco[loop].yPos;
			z = Floco[loop].zPos - 25;
			glBegin(GL_LINES);
			glVertex3f(x , y, z); //faz as linhas ficarem em 90º com o x-1
			glVertex3f(x, y + 0.1, z); //Tamanho do Floco é o 1
			glEnd();
			Floco[loop].yPos += Floco[loop].vel;
			Floco[loop].vel += Floco[loop].gravidade;
			Floco[loop].vida -= Floco[loop].desaparecer;
			if (Floco[loop].vida < 0.0) {
				iniciaFloco(loop);
			}
		}
	}
}

void drawScene() {
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();
	glRotatef(0.0, 0.0, 1.0, 0.0);
	glRotatef(0.0, 1.0, 0.0, 0.0);
	glEnd();
	criaChuva();
	glutSwapBuffers();
}

void reshape(int w, int h) {
	glViewport(0, 0, w, h);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluPerspective(55, (float) w / (float) h, .1, 200);
	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();
}

void idle() {
	glutPostRedisplay();
}

int main(int argc, char** argv) {
	srand(time(NULL));
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_DEPTH | GLUT_RGB | GLUT_DOUBLE);
	glutInitWindowSize(640, 480); //tamanho da tela
	glutCreateWindow("Neve");
	init(); //inicia o glut
	glutDisplayFunc(drawScene); //callback, qual função vai ser chamada para mostrar
	glutReshapeFunc(reshape);
	glutIdleFunc(idle);
	glutMainLoop();
	return 0;
}
