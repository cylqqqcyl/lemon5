.DEFAULT_GOAL := help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

target_dirs := tests

test:	## run tests.
	nose2 -F -v -B --with-coverage --coverage app tests

test_tts:	## run tests for text-to-speech.
	nose2 -F -v -B --with-coverage --coverage app tests.tts_tests

test_vc:	## run tests for voice conversion.
	:

test_sr:	## run tests for speech recognition.
	:

test_chat:	## run tests for chatting.
	:

style:	## update code style.
	black ${target_dirs}
	isort ${target_dirs}

lint:	## run pylint linter.
	pylint ${target_dirs}
	black ${target_dirs} --check
	isort ${target_dirs} --check-only

deps:	## install dependencies.
	pip install -r requirements.txt

doc-deps:	## install dependencies for docs.
	pip install -r docs/requirements.txt

build-docs:	# build docs.
	cd docs && make clean && make build