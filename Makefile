CC=gcc
CFLAGS=-Wall -Wextra -std=c11 -O2 -fPIC
LDFLAGS=-lm

all: main libfixed_point.so

main: main.o fixed_point.o
	$(CC) -o $@ main.o fixed_point.o $(LDFLAGS)

fixed_point.o: fixed_point.c fixed_point.h
	$(CC) $(CFLAGS) -c fixed_point.c

main.o: main.c fixed_point.h
	$(CC) $(CFLAGS) -c main.c

libfixed_point.so: fixed_point.o
	$(CC) -shared -o $@ fixed_point.o $(LDFLAGS)

clean:
	rm -f *.o main libfixed_point.so
