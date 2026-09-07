# Gundumani's Birthday 🎉🎂

A beautiful, self-contained single-page personalized birthday website built with vanilla HTML5, CSS3, and JavaScript.

## Features ✨

- **Animated Intro Splash**: 5-second greeting with falling emoji confetti, followed by a 3 → 2 → 1 countdown sequence before revealing the main landing page.
- **Hero Section**: Animated circular photo frame showing the hero image.
- **Birthday Letter**: Styled birthday message with handwritten script signature.
- **Memory Timeline**: Vertical interactive timeline documenting favorite moments.
- **Photo Gallery**: Responsive grid with hover effects and a full-screen Lightbox photo viewer.
- **Music Card**: Built-in HTML5 `<audio>` player with support for audio files or Spotify/YouTube embeds.
- **Share & QR Code**: Auto-generated QR code of the current website URL + 1-click clipboard copy button with toast notification.
- **Responsive & Mobile Ready**: Styled using modern CSS variables with dark night-sky aesthetics (`#120A24` / `#1A1033`).

## How to Publish & Deploy 🚀

### Option 1: GitHub Pages (Free)
1. Create a repository on GitHub (e.g. `gundumani-birthday`).
2. Push this repository to GitHub:
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/gundumani-birthday.git
   git branch -M main
   git push -u origin main
   ```
3. In your GitHub repository, go to **Settings** > **Pages**.
4. Select `main` branch as the source and click **Save**.
5. Your birthday website will be live in 1–2 minutes!

### Option 2: Vercel / Netlify (Free)
- Drag and drop this folder directly into [Netlify Drop](https://app.netlify.com/drop) or deploy via [Vercel](https://vercel.com).

## Customizing Content 📝

All personal content (names, memories, signature, audio track path) is clearly marked with `<!-- EDITABLE: ... -->` HTML comments inside [`index.html`](index.html).
