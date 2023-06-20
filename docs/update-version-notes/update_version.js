const fs = require('fs');

const markdownFile = 'release_notes.md';
const versionPlaceholder = /{{ version }}/g;
const newVersion = process.env.NEW_VERSION;

fs.readFile(markdownFile, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }

  const updatedContent = data.replace(versionPlaceholder, newVersion);

  fs.writeFile(markdownFile, updatedContent, 'utf8', (err) => {
    if (err) {
      console.error(err);
      return;
    }

    console.log('Markdown file updated successfully!');
  });
});
