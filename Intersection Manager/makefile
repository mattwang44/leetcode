all: build clean 
	
build : main.o
	g++ -fno-use-linker-plugin -O3 -o build main.o
	
main.o: main.cpp
	g++ -std=c++17 -g -c -O3 main.cpp

.PHONY:clean	

clean : 
	rm -rf *.o
