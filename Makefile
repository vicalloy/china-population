gen:
	python -m chinapopulation.main

init-pre-commit:
	git config --global url."https://".insteadOf git://
	pre-commit install
	pre-commit run --all-files

update-pre-commit:
	pre-commit autoupdate
