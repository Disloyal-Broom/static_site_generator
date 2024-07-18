import unittest
from extract_markdown_links import *

class TestExtractMarkdownLinks(unittest.TestCase):
    def test_two_links(self):
        test_case = extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)")
        expected_results = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(test_case,expected_results)

    def test_one_link(self):
        test_case = extract_markdown_links("This is text. [Link](https://google.com)")
        expected_results = [("Link","https://google.com")]
        self.assertEqual(test_case,expected_results)
        
    def test_no_links(self):
        test_case = extract_markdown_links("this is just some text")
        expected_results = None
        self.assertEqual(test_case,expected_results)
        
    def test_invalid_format(self):
        test_case = extract_markdown_links("[link](google.com")
        expected_results = None
        self.assertEqual(test_case,expected_results)
        
if __name__ == '__main__':
    unittest.main()