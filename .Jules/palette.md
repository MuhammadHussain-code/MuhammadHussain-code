## 2024-12-16 - Dark Mode Contrast and GitHub READMEs
**Learning:** GitHub's README renderer strips `opacity` from inline styles, making it hard to create subtle text that works in both Light and Dark modes. Using `#666` (medium gray) fails WCAG AA contrast on GitHub's dark theme (#0d1117).
**Action:** Use `#767676` (Magic Gray) instead. It passes WCAG AA contrast ratios (4.5:1) on both pure white and pure black backgrounds, ensuring accessibility for all users.
