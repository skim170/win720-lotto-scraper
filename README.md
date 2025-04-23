![image](https://github.com/user-attachments/assets/a2d80f81-d301-47f3-83ca-9d653d433f9e)

# 🎰 Win720 Lotto Scraper

This Python script scrapes the latest 50 rounds of **Win720** lottery results from the official Korean lottery mobile website ([m.dhlottery.co.kr](https://m.dhlottery.co.kr)).

## 📌 Features

- Automatically fetches the most recent **Win720** draw number.
- Crawls draw results for the last 50 rounds.
- Extracts:
  - Draw number (회차)
  - Winning numbers (당첨 번호 6개)
  - Jo number (조 번호)

## 🚀 How to Use

### Requirements

Make sure you have Python 3 and the following packages installed:

```bash
pip install requests beautifulsoup4
```

Run the Script
```bash
python pension_lotto_scraper.py
```

### 🔍 Example Output
Each list contains:
- The Jo (조) number in the format '103조'
- The 6 winning numbers as strings

### 📌 Note
- This script is intended for educational and data-processing purposes.
- Make sure to respect the website’s terms of use when scraping.
