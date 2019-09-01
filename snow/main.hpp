#ifndef MAIN_HPP_
#define MAIN_HPP_
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <GL/glut.h>
#include <GL/gl.h>
#include <time.h>
#define QTDFLOCOS 1000
int loop;

typedef struct {
	bool viva;
	float vida;
	float desaparecer;
	float xPos;
	float yPos;
	float zPos;
	float vel;
	float gravidade;
} structFloco;
#endif /* MAIN_HPP_ */
