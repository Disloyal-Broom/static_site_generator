import unittest
from extract_markdown_images import *

class TestExtractMarkdownImages(unittest.TestCase):
    def test_valid_image(self):
        test_case = extract_markdown_images("Text with ![a thing](https://google.com/an_image_for_sure/)")
        expected_result = [("a thing","https://google.com/an_image_for_sure/")]
        self.assertEqual(test_case,expected_result)
    
    def test_two_valid_images(self):
        test_case = extract_markdown_images("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)")
        expected_result = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(test_case,expected_result)
        
    def test_no_valid_images(self):
        test_case = extract_markdown_images("nothing to be found here")
        expected_results = None
        self.assertEqual(test_case,expected_results)
        
    def test_invalid_format(self):
        test_case = extract_markdown_images("![this is something](almost simliar to an image tag")
        expected_results = None
        self.assertEqual(test_case,expected_results)
        
if __name__ == "__main__":
    unittest.main()