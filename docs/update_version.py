import re
import os

markdown_file = 'release_notes.md'
version_placeholder = r'{{Version}}'
new_version = os.environ.get('NEW_VERSION')

with open(markdown_file, 'r', encoding='utf8') as file:
    data = file.read()

updated_content = re.sub(version_placeholder, new_version, data)

with open(markdown_file, 'w', encoding='utf8') as file:
    file.write(updated_content)

print('Markdown file updated successfully!')
