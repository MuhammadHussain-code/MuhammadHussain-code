# Palette Journal

## 2026-02-12 - Accessibility of Hardcoded Colors in READMEs
**Learning:** Hardcoding colors (e.g., `#666`) in `README.md` inline styles creates poor contrast in GitHub's Dark Mode, making text unreadable. GitHub does not support CSS classes or variables in READMEs.
**Action:** Use `opacity` (e.g., `opacity: 0.8`) on the default text color instead of hardcoded hex values to create visual hierarchy (dimmed text) that adapts automatically to both Light and Dark modes.
