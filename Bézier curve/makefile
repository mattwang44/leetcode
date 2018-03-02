all: build clean 

build : main.o
	g++ -fno-use-linker-plugin -O3 -o build main.o

main.o: main.cpp
	g++ -std=c++17 -g -c -O3 main.cpp

noGraph: build_noGraph clean

build_noGraph : main_noGraph.o
	g++ -fno-use-linker-plugin -O3 -o build main_noGraph.o

main_noGraph.o: main_noGraph.cpp
	g++ -std=c++17 -g -c -O3 main_noGraph.cpp

.PHONY:clean

clean : 
	rm -rf *.o
