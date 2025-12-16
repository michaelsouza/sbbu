CXX := g++
CXXFLAGS := -O3 -std=c++17 -Wall -Wextra -Wpedantic -fopenmp
LDLIBS := -lboost_regex -lm

sbbu.exe: sbbu.cpp sbbu.h ddgp.h edge.h nmr.h qs.h utils.h vec3.h
	$(CXX) $(CXXFLAGS) sbbu.cpp -o $@ $(LDLIBS)

.PHONY: test_all clean

test_all: sbbu.exe
	python call_sbbu.py

clean:
	rm -f sbbu.exe
