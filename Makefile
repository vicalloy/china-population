gen:
	python -m chinapopulation.main

init-pre-commit:
	git config --global url."https://".insteadOf git://
	pre-commit install
	pre-commit run --all-files

update-pre-commit:
	pre-commit autoupdate

docker-gen:
	docker run -v `pwd`:/app --rm python:3.10 \
		bash -c \
		"cd /app; pip install -i https://mirrors.bfsu.edu.cn/pypi/web/simple/ plotly==5.24.0; make gen"
