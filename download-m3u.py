import time
import tempfile
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Temporary Chrome profile (avoids user-data-dir issues)
temp_profile = tempfile.TemporaryDirectory()

# Chrome options
options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument(f"--user-data-dir={temp_profile.name}")
options.binary_location = "/usr/bin/chromium"  # or "/usr/bin/chromium-browser"

# Set driver path (you can also use `which chromedriver` result here)
driver = webdriver.Chrome(
    service=Service("/usr/bin/chromedriver"),  # or output of `which chromedriver`
    options=options
)

try:
    driver.get("https://freeiptv2023-d.ottc.xyz/")
    time.sleep(20)

    # Click the create button
    create_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Create IPTV Account')]"))
    )
    create_btn.click()

    # Wait for M3U input to appear
    m3u_input = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "m3uLink"))
    )

    # Extract the value
    m3u_url = m3u_input.get_attribute("value")
    print("✅ M3U Link:", m3u_url)

finally:
    driver.quit()
    temp_profile.cleanup()
