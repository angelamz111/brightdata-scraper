# Bright Data Playwright Scraper

This repo demonstrates how to scrape public web pages using **Playwright** routed through **Bright Data's Web Unlocker proxies**.
- Edit `main.py` to add your scraping logic.
- Credentials come from GitHub Secrets: `BRIGHTDATA_USERNAME` and `BRIGHTDATA_PASSWORD`.

To run locally:

```bash
pip install -r requirements.txt
python -m playwright install chromium
python main.py
