all: build/lock_in.pdf

build/lock_in.pdf: lock_in.tex | build
	lualatex --output-directory=build --interaction=batchmode --halt-on-error lock_in.tex
	lualatex --output-directory=build --interaction=batchmode --halt-on-error lock_in.tex

build:
	mkdir -p build

clean:
	rm -rf build

.PHONY: all clean