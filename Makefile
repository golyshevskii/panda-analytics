# Dependencies
init:
	poetry install --no-root

# Linting
lint:
	cd .github/lint-tests && poetry run black --config pyproject.toml ../../scripts/ ../../dags/
	cd .github/lint-tests && poetry run isort --settings-path pyproject.toml ../../scripts/ ../../dags/
	cd .github/lint-tests && poetry run flake8 --config .flake8 ../../scripts/ ../../dags

check-lint:
	cd .github/lint-tests && poetry run black --config pyproject.toml --check ../../scripts/ ../../dags/
	cd .github/lint-tests && poetry run isort --settings-path pyproject.toml --check ../../scripts/ ../../dags/
	cd .github/lint-tests && poetry run flake8 --config .flake8 ../../scripts/ ../../dags
