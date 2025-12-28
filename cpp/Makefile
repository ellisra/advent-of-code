CXX = clang++
CXXFLAGS = -std=c++23 -Wall -I.
COMMON = utils.cpp

all:
	@echo "Usage: make run YEAR=2015 DAY=1"

all-days:
	@for year in 2015 2025; do \
		for day in $$year/day*.cpp; do \
			daynum=$$(basename $$day .cpp | sed 's/day0*//'); \
			echo "Building $$year day $$daynum"; \
			$(CXX) $(CXXFLAGS) $$day $(COMMON) -o target/$$year-day$$daynum.o || true; \
		done \
	done

run:
	$(CXX) $(CXXFLAGS) $(YEAR)/day$(shell printf "%02d" $(DAY)).cpp $(COMMON) -o target/day$(DAY).o && ./target/day$(DAY).o

build:
	$(CXX) $(CXXFLAGS) $(YEAR)/day$(shell printf "%02d" $(DAY)).cpp $(COMMON) -o target/day$(DAY).o

clean:
	rm -f target/*

.PHONY: all run build clean
