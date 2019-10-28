all: build/fourier.pdf

build/fourier.pdf: fourier.tex | build
	lualatex --output-directory=build --interaction=batchmode --halt-on-error fourier.tex
	lualatex --output-directory=build --interaction=batchmode --halt-on-error fourier.tex

build:
	mkdir -p build

clean:
	rm -rf build

.PHONY: all clean