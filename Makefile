install:
	pip install --upgrade pip && \
	pip install -r requirements.txt && \
	python -m textblob.download_corpora

test:
	python -m pytest -vv --cov=wukiphrases --cov=nlp_logic testnlp.py

lint:
	pylint --disable=R,C *.py nlp_logic/*.py

format:
	black *.py nlp_logic	

all: install lint test