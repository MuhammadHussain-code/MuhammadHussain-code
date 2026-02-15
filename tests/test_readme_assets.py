import unittest
import os
import re

class TestReadmeAssets(unittest.TestCase):
    def test_local_images_exist(self):
        """Verify that local image references in README.md exist."""
        readme_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'README.md')

        if not os.path.exists(readme_path):
             self.fail(f"README.md not found at {readme_path}")

        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Regex to find src="something"
        matches = re.findall(r'src=["\']([^"\']+)["\']', content)

        # Filter for local files (start with ./ or just filename, not http)
        local_images = [m for m in matches if not m.startswith('http') and not m.startswith('//')]

        for image_path in local_images:
            # Resolve path relative to README location
            full_path = os.path.join(os.path.dirname(readme_path), image_path)
            self.assertTrue(os.path.exists(full_path), f"Image {image_path} not found at {full_path}")

if __name__ == '__main__':
    unittest.main()
