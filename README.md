# Project Name

This project provides a tool to review code diffs using a custom script and a Makefile target.

## Prerequisites

- Python 3.x
- Make
- Ollama

## Installation

1. Clone the repository:
   ```bash
   git clone git@github.com:ragan/cr.git
   cd cr
   ```

2. Ensure you have Python 3.x installed on your system.

## Ollama Installation

To use the `qwen2.5-coder` model, you need to install Ollama. Follow these steps:

1. Download and install Ollama from the [official website](https://ollama.com/download).
2. Once installed, open a terminal and run the following command to install the `qwen2.5-coder` model:
   ```bash
   ollama install qwen2.5-coder
   ```

## Usage

To run the code review tool, execute the following command:

```bash
make run-review
```

This command will run the `cr.py` script with the `diff.diff` file as input, using the `run-review` target defined in the Makefile.

## Running the Script Directly

You can also run the `cr.sh` script to review the current changes in your working directory against the last commit. This script will execute the `git diff` command and pipe the output to `cr.py`:

```bash
./cr.sh
```

This is useful for reviewing changes that have not yet been committed to the repository.

- `cr.py`: The main script that processes the diff file and provides code review suggestions.
- `diff.diff`: The diff file containing the code changes to be reviewed.
- `Makefile`: Contains the `run-review` target to execute the review process.

## License

This project is licensed under the terms of the LICENSE file.
