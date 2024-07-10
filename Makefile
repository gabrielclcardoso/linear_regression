VPATH = .venv/bin/

.venv:
	python -m venv .venv

setup: .venv
	$(VPATH)pip install -r requirements.txt

install: .venv
	$(VPATH)pip install $(pkg) && $(VPATH)pip freeze > requirements.txt;

hello: .venv
	echo "print('hello world')" | $(VPATH)python

.PHONY: hello install setup
