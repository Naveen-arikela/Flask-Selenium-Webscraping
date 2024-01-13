from selenium import webdriver

CHOROME_DRIVER_LOCAL_HOST_PORT = 8989
def get_local_chrome_driver_connection():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("debuggerAddress", f"localhost:{CHOROME_DRIVER_LOCAL_HOST_PORT}")
    chrome_driver = webdriver.Chrome(options=chrome_options)
    return chrome_driver
