buildproject:
	python setup.py sdist bdist_wheel

test:
	python setup.py test

install:
	pip install dist/minfinder-0.0.1-py3-none-any.whl
