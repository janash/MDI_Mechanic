# make tests target that runs pytest
test:
	export TESTING="true"
	pytest -v --cov=mdimechanic
