create-env:
	@cp .env.example .env
	@echo "Created .env file. Please edit it with your configuration."

install:
	python3 -m venv venv
	. venv/bin/activate && pip install --upgrade pip
	. venv/bin/activate && pip install -r requirements.txt
	python3 -m playwright install chromium

setup: create-env install

run:
	. venv/bin/activate && python3 main.py

clean:
	rm -rf venv
	rm -f .env

help:
	@echo "Available targets:"
	@echo "  setup   - Create .env file and install dependencies"
	@echo "  install - Create virtual environment and install dependencies"
	@echo "  run     - Run the main application"
	@echo "  clean   - Remove virtual environment and .env file"
	@echo "  help    - Show this help message"
