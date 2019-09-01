CC=g++
LIBS = -lglut -lGL -lGLU -lm 
CFLAGS = -g  

OBJECTS= main.o

EXEC=main

all: $(EXEC)

$(EXEC): $(OBJECTS)
	$(CC) $(OBJECTS) ${LIBS} -o $(EXEC)


main.o: main.cpp
	$(CC) ${CFLAGS} -c main.cpp  

clean:
	-rm *.o main *~; clear;