name: Run Menu Bot

on:
  schedule:
    - cron: "30 13 * * 1-5"  # 9:30 AM EST weekdays

jobs:
  run:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Install Python
        uses: actions/setup-python@v4
      - name: Install dependencies
        run: pip install requests beautifulsoup4
      - name: Run script
        run: python menu.py
