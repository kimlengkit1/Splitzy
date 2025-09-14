# Splitzy

"Because math is hard"

AI-powered receipt reader and bill-splitting app to make group payments effortless. Just snap a photo or upload a screenshot of your receipt, and it will itemize every purchase using AI. No more typing line by line because everything is extracted automatically.

## What is it?
Instead of squinting at crumpling paper or fighting over who ordered guac, just snap a pic of the receipt and let our AI do the work.

## How it works:
**Step 1**: Upload a picture of the receipt.

**Step 2**: Splitzy reads the receipt and itemizes everything.

**Step 3**: Choose your payment style. Either evenly split everything, split it based on items (you get your fries, I'll take my boba), or smart split (AI will help you do all the brain work).

## The Goal
Make splitting receipts fast, fair, and fun, so you can go back to enjoying the company of your friends and loved ones, not the calculator.

# Other Notes 

## Installation instruction

I ran this using the isolated environment instead of my system Python. To create a virtual environment: ``python -m venv .venv``

Need to activate it every time a new terminal is open, so use ``source .venv/bin/activate``. 

To install the dependencies, use ``pip install -r requirements.txt``.

As a sanity check, run ``pip list`` and look for google-generativeai, pillow, and python-dotenv.

Type ``deactivate`` when ready to exit.

To run the program, type ``python main.py`` or ``python3 main.py``.


You will need a key, make a .env file in the root of the repo, and add "API_KEY=[keys]" for Gemini to work.
[Click to get an API key for Gemini ](https://aistudio.google.com/app/apikey)