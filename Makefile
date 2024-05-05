# Dependencies
init:
	poetry install --no-root

# Linting & Formatting
lint:
	cd .github/lint-tests && poetry run black --config pyproject.toml ../../core/scripts/ ../../core/dags/
	cd .github/lint-tests && poetry run isort --settings-path pyproject.toml ../../core/scripts/ ../../core/dags/
	cd .github/lint-tests && poetry run flake8 --config .flake8 ../../core/scripts/ ../../core/dags

format:
	cd .github/lint-tests && poetry run black --config pyproject.toml ../../core/scripts/ ../../core/dags/
	cd .github/lint-tests && poetry run isort --settings-path pyproject.toml ../../core/scripts/ ../../core/dags/

check-lint:
	cd .github/lint-tests && poetry run black --config pyproject.toml --check ../../core/scripts/ ../../core/dags/
	cd .github/lint-tests && poetry run isort --settings-path pyproject.toml --check ../../core/scripts/ ../../core/dags/
	cd .github/lint-tests && poetry run flake8 --config .flake8 ../../core/scripts/ ../../core/dags

# Docker
up:
	docker-compose up

up-b:
	docker-compose up --build

down:
	docker-compose down
