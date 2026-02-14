## 2024-05-22 - Magic Gray for Light/Dark Mode Accessibility
**Learning:** Text with color `#666` fails WCAG AA contrast on dark backgrounds (like GitHub Dark Mode). However, `#767676` passes WCAG AA on both pure white (4.54:1) and pure black (4.62:1) backgrounds, making it an excellent "safe" gray for text that must be visible on both themes without media queries.
**Action:** Use `#767676` instead of `#666` for secondary text in Markdown files where CSS variables or media queries are unavailable.
