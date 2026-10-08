import os
import threading
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from functools import partial

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="session")
def base_url():
    webapp_dir = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "webapp")
    )
    handler = partial(SimpleHTTPRequestHandler, directory=webapp_dir)
    server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()

    url = f"http://127.0.0.1:{server.server_port}"
    yield url

    server.shutdown()
    server.server_close()


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--window-size=1400,1000")
    # Uncomment for headless execution:
    # options.add_argument("--headless=new")

    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()
