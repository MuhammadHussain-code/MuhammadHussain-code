## 2026-02-11 - [Dark Mode Contrast in READMEs]
**Learning:** Hardcoded text colors (like #666) in README.md files can become illegible in GitHub's Dark Mode, as the background changes but the inline style forces the text color.
**Action:** Avoid inline `color` styles for text in READMEs. Rely on default Markdown rendering which adapts to the user's theme (Light/Dark mode) automatically.
