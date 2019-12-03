all: build/graph.pdf build/lock_in.pdf

build/graph.pdf: lock_in.py | build
	python lock_in.py

build/lock_in.pdf: lock_in.tex | build
	lualatex --output-directory=build --interaction=batchmode --halt-on-error lock_in.tex
	lualatex --output-directory=build --interaction=batchmode --halt-on-error lock_in.tex

build:
	mkdir -p build

clean:
	rm -rf build

.PHONY: all clean