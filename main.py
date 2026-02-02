from playwright.sync_api import sync_playwright, TimeoutError
import time
import json
import os
from dotenv import load_dotenv
load_dotenv()
BASE_URL = os.getenv("BASE_URL", "http://51.195.24.179:8000")
HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
SLOW_MO = int(os.getenv("SLOW_MO", "0"))
USER_DATA_FILE = "user_data.json"

def load_user_data():
    """Load user credentials array from JSON file."""
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, 'r') as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                return [data]  
    else:
        raise FileNotFoundError(f"User data file '{USER_DATA_FILE}' not found")
USERS = load_user_data()
def register_user(context, user_data, user_index):
    """Register a single user and close tab on completion."""
    username = user_data["username"]
    email = user_data["email"]
    password = user_data["password"]
    page = context.new_page()
    try:
        page.goto(BASE_URL, wait_until="networkidle")
        page.click("text=Register")
        page.wait_for_load_state("networkidle")
        page.wait_for_selector("input", timeout=15000)
        page.fill("input[type='text'], input[name*='username'], input[placeholder*='username']", username)
        page.fill("input[type='email'], input[name*='mail'], input[placeholder*='mail']", email)
        page.fill("input[type='password']", password)
        try:
            with page.expect_response(
                lambda r: ("/api/v1/complete_registration" in r.url or "signup" in r.url) and r.status in (200, 201),
                timeout=15000
            ) as resp_info:
                page.click("button[type='submit']")
        except TimeoutError:
            pass
        page.wait_for_load_state("networkidle")
    except Exception:
        pass
    finally:
        page.close()
with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=HEADLESS,
        args=["--start-minimized"],
        slow_mo=SLOW_MO
    )
    context = browser.new_context(locale="en-US")
    try:
        total_users = len(USERS)
        for index, user_data in enumerate(USERS):
            register_user(context, user_data, index)
            print(f"Progress: {index + 1}/{total_users} users completed")
            time.sleep(1)      
    finally:
        browser.close()
