# EMOJI_TO_TEXT 😀➡️📝

A simple **command-line Python application** for working with emojis in text.
Built using the [`demoji`](https://pypi.org/project/demoji/) library.

## Features

| Option | Description |
|--------|-------------|
| 1 | **Remove emoji** from the text |
| 2 | **Replace emoji with description** (e.g. 😀 → `grinning face`) |
| 3 | **Detect emojis** in the text (shows each emoji with its description) |
| 4 | **Change the input text** without restarting the app |
| 5 | **Exit** the application |

## Requirements

- Python **3.10 or higher** (the code uses `match` / `case`)
- `demoji` (listed in `requirements.txt`)

## Installation

```bash
# 1. Clone the repository
git clone https://github.com/sarveshkamdi7-collab/emoji-to-text.git
cd emoji-to-text

# 2. (Optional) create a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

## Usage

```bash
python emoji_to_text.py
```

1. Enter the text you want to work on.
2. Choose an option from the menu (1-5).
3. Choose option 4 to change the text, or 5 to exit.

## Example

```
Please enter a text Hello 😀 World 🌍
______________________________________
1:Remove emoji from text
2:Replace emoji with description
3:Detect emojis in string
4:Change the input text
5:exit
______________________________________
Please enter a choice (1-5)1
Hello  World

Please enter a choice (1-5)2
Hello grinning face World globe showing Europe-Africa

Please enter a choice (1-5)3
{'😀': 'grinning face', '🌍': 'globe showing Europe-Africa'}
```

## Concepts Used

- `while` loops for a repeating menu
- `try` / `except` for input handling
- `match` / `case` (structural pattern matching)
- Third-party libraries with `pip`

## Project Structure

```
emoji-to-text/
├── emoji_to_text.py    # main program
├── requirements.txt    # dependencies
├── README.md           # project documentation
├── LICENSE             # MIT license
└── .gitignore          # files Git should ignore
```

## License

This project is licensed under the [MIT License](LICENSE).
