import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class TestApp(unittest.TestCase):

    def setUp(self):
        # Start the Flask app (make sure it's already running)
        self.driver = webdriver.Chrome()  # Use the appropriate WebDriver for your browser

    def tearDown(self):
        # Close the browser window
        self.driver.close()

    def test_generate_story(self):
        # Open the app in the browser
        self.driver.get("http://127.0.0.1:5000/")

        # Fill in the form
        genre_select = self.driver.find_element("name", "genre")
        genre_select.send_keys("superhero")

        prompt_input = self.driver.find_element("name", "prompt")
        prompt_input.send_keys("Batman was hunting down")

        story_length_slider = self.driver.find_element("name", "story_length")
        story_length_slider.send_keys(Keys.ARROW_RIGHT)  # Adjust the slider to a different value if needed

        # Submit the form
        generate_button = self.driver.find_element("tag name", "button")
        generate_button.click()

        # Wait for the generated story to appear
        time.sleep(5)

        # Check if the generated story is present on the page
        generated_story = self.driver.find_element("class name", "generated-story")
        self.assertTrue(generated_story.is_displayed())

if __name__ == "__main__":
    unittest.main()
