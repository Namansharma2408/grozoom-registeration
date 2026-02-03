# Grozoom User Registration Automation

A Python-based automation tool that uses Playwright to register multiple users on the Grozoom platform.

## Prerequisites

- Python 3.8 or higher
- Make
- Google Chrome or Chromium browser

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd grozoom
```

2. Run the setup command to create the environment and install dependencies:
```bash
make setup
```

3. Edit the `.env` file with your configuration:
```bash
nano .env
```

## Configuration

Edit the `.env` file to configure the application:

| Variable | Description | Default |
|----------|-------------|---------|
| `BASE_URL` | The base URL of the application | `http://51.195.24.179:8000` |
| `HEADLESS` | Run browser in headless mode | `false` |
| `SLOW_MO` | Add delay between actions (ms) | `0` |

## User Data

Edit the `user_data.json` file to configure the users to be registered. The file contains an array of user objects with the following structure:

```json
[
    {
        "username": "user1",
        "email": "user1@example.com",
        "password": "Test@1234"
    }
]
```

## Usage

Run the application:
```bash
make run
```

## Available Make Targets

| Target | Description |
|--------|-------------|
| `setup` | Create .env file and install all dependencies |
| `install` | Create virtual environment and install dependencies |
| `run` | Run the main application |
| `clean` | Remove virtual environment and .env file |
| `help` | Show available targets |

## Project Structure

```
grozoom/
├── main.py          # Main application script
├── Makefile         # Build and automation targets
├── requirements.txt # Python dependencies
├── .env.example     # Environment variables template
├── .env             # Environment variables (created on setup)
└── user_data.json   # User credentials for registration
```

## Development

To set up the development environment:

```bash
make setup
```

To clean up:

```bash
make clean
```

## License

MIT License
