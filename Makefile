.PHONY: dev start install lint format test type

# Dev server (hot-reload, HTTP/1.1) 
dev:
	uv run hypercorn src.main:app --reload

# Production server (no reload) 
start:
	uv run hypercorn src.main:app

# Install / sync dependencies 
install:
	uv sync

# Tests 
test:
	uv run pytest tests/ -v

# Formatting 
format:
	uv run ruff format src/ tests/

# Linting 
lint:
	uv run ruff check src/ tests/

# Type checking 
type:
	uv run ty check src/ tests/
