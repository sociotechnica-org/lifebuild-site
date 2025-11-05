# Claude Development Notes

This document contains notes and guidelines for Claude when working on this project.

## Project Overview

LifeBuild.me is a simple landing page built with Astro, similar to WorkSquared.ai. The site features:

- Clean, centered layout
- Newsletter subscription via Buttondown
- Links to GitHub and SocioTechnica
- Responsive design
- Cloudflare Pages deployment

## Technology Stack

- **Framework**: Astro 5.x
- **UI Library**: React 19.x (for future interactive components)
- **Styling**: Scoped CSS within Astro components
- **Deployment**: Cloudflare Pages
- **Newsletter**: Buttondown email service

## Project Structure

```
/
├── public/             # Static assets
├── src/
│   ├── components/     # Astro/React components
│   ├── layouts/        # Page layouts
│   └── pages/          # Route pages
├── astro.config.mjs    # Astro configuration
├── package.json        # Dependencies and scripts
└── tsconfig.json       # TypeScript configuration
```

## Development Guidelines

### Code Style

- Use TypeScript strict mode
- Follow ESLint rules configured in eslint.config.js
- Format with Prettier (configured in .prettierrc)
- Use functional components for React
- Prefer Astro components for static content

### Component Guidelines

- Keep components focused and single-purpose
- Use scoped styles within components
- Follow responsive design patterns (mobile-first)
- Ensure accessibility (semantic HTML, ARIA labels)

### Newsletter Integration

The site uses Buttondown for email subscriptions. The form is configured in:

- `src/components/LifeBuild.astro`
- Form action points to Buttondown API
- Success message displays after submission

### Deployment

- Automatic deployments via Cloudflare Pages
- Triggered by pushes to main branch
- Build command: `npm run build`
- Output directory: `dist`

## Common Tasks

### Adding New Pages

1. Create new `.astro` file in `src/pages/`
2. Import and use the Layout component
3. Add your content

### Updating Styles

- Global styles: `src/layouts/Layout.astro`
- Component styles: Within each component's `<style>` block
- Use CSS custom properties for theme values

### Testing Locally

```bash
npm install
npm run dev
```

### Building for Production

```bash
npm run build
npm run preview
```

## Notes for Future Development

- Logo placeholder should be replaced with actual LifeBuild.me logo
- Consider adding more pages (about, features, etc.)
- May need to update Buttondown form action URL with actual username
- Keep design consistent with minimalist approach
