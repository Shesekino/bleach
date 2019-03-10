all: clean build

clean:
	rm -rf build
	rm -rf dist
build:
	python setup.py sdist bdist_wheel

upload:
	python3 -m twine upload dist/*

