import os
from playwright.sync_api import sync_playwright, expect

def run_verification():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Get absolute path for the HTML files
        current_dir = os.path.abspath(os.getcwd())
        index_path = f"file://{os.path.join(current_dir, 'index.html')}"
        homepage_path = f"file://{os.path.join(current_dir, 'homepage.html')}"

        # 1. Verify the initial landing page (index.html)
        page.goto(index_path)

        # Set viewport for mobile and desktop screenshots
        # Desktop
        page.set_viewport_size({"width": 1280, "height": 800})
        page.screenshot(path="jules-scratch/verification/01_landing_page_desktop.png")

        # Mobile
        page.set_viewport_size({"width": 375, "height": 667})
        page.screenshot(path="jules-scratch/verification/02_landing_page_mobile.png")

        # 2. Verify the door opening and navigation
        door_locator = page.locator('.door')

        # Click the door on the mobile view
        door_locator.click()

        # Wait for navigation to homepage.html
        expect(page).to_have_url(homepage_path)

        # 3. Verify the homepage (homepage.html)
        # Desktop
        page.set_viewport_size({"width": 1280, "height": 800})
        page.screenshot(path="jules-scratch/verification/03_homepage_desktop.png")

        # Mobile
        page.set_viewport_size({"width": 375, "height": 667})
        page.screenshot(path="jules-scratch/verification/04_homepage_mobile.png")

        browser.close()

if __name__ == "__main__":
    run_verification()