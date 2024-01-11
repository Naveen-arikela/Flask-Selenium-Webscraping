from selenium import webdriver

# Remote debugging port
remote_debugging_port = 8989

# Connect to the existing Chrome session
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("debuggerAddress", f"localhost:{remote_debugging_port}")

# Initialize Chrome WebDriver
chrome_driver = webdriver.Chrome(options=chrome_options)

# Perform actions on the existing Chrome window (e.g., open a URL)
makes_url = "https://www.thelancet.com/journals/laneur/article/PIIS1474-4422(23)00358-7/fulltext"
amazon_url = "https://www.amazon.com/"
chrome_driver.execute_script(f'''window.open("{makes_url}","_blank");''')
chrome_driver.execute_script(f'''window.open("{amazon_url}","_blank");''')

# chrome_driver.switch_to.window(chrome_driver.window_handles[-1])
# chrome_driver.get("http://makes.org.in/")

# # Open the second URL in a new tab
# chrome_driver.execute_script("window.open('','_blank');")
# chrome_driver.switch_to.window(chrome_driver.window_handles[-1])
# chrome_driver.get("https://www.amazon.com/")

# Close the WebDriver instance
# chrome_driver.quit()
