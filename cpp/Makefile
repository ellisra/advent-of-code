CXX = clang++
CXXFLAGS = -std=c++20 -Wall -I.
COMMON = utils.cpp

all:
	@echo "Usage: make run YEAR=2015 DAY=1"

run:
	$(CXX) $(CXXFLAGS) $(YEAR)/day$(shell printf "%02d" $(DAY)).cpp $(COMMON) -o target/day$(DAY).o && ./target/day$(DAY).o

build:
	$(CXX) $(CXXFLAGS) $(YEAR)/day$(shell printf "%02d" $(DAY)).cpp $(COMMON) -o target/day$(DAY).o

clean:
	rm -f target/*

.PHONY: all run build clean
