all: clean build

clean:
	rm -rf build
	rm -rf dist
build:
	PYTHONPATH=py python3 setup.py sdist bdist_wheel

upload:
	twine upload dist/*

