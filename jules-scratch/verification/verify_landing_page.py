import os
from playwright.sync_api import sync_playwright, Page, expect

def verify_landing_page(page: Page):
    """
    This test verifies that the landing page is displayed correctly.
    """
    # 1. Arrange: Go to the index.html page.
    # The file path must be absolute.
    file_path = os.path.abspath("index.html")
    page.goto(f"file://{file_path}")

    # 2. Assert: Check if the door element is visible.
    door = page.locator(".door")
    expect(door).to_be_visible()

    # 3. Assert: Check if the note with "Welcome!" is visible.
    note_text = page.locator(".note p")
    expect(note_text).to_have_text("Welcome!")

    # 4. Screenshot: Capture the final result for visual verification.
    page.screenshot(path="jules-scratch/verification/verification.png")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    verify_landing_page(page)
    browser.close()