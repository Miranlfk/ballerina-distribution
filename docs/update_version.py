import os

markdown_file = 'docs/release_notes.md'
version_placeholder = 'version'
new_version = os.getenv('NEW_VERSION')

with open(markdown_file, 'r') as file:
    content = file.read()

updated_content = content.replace(version_placeholder, new_version)

with open(markdown_file, 'w') as file:
    file.write(updated_content)

print('Markdown file updated successfully!')
