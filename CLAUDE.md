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
│   ├── content/
│   │   └── changelog/  # Changelog entries (Markdown with frontmatter)
│   ├── data/
│   │   └── version.json # Current version and lastUpdated date
│   ├── layouts/        # Page layouts
│   └── pages/          # Route pages
├── astro.config.mjs    # Astro configuration
├── package.json        # Dependencies and scripts
└── tsconfig.json       # TypeScript configuration
```

## Development Guidelines

### IMPORTANT: Always Run Linting Before Commits

**Before pushing any commit, you MUST run:**

```bash
npm run lint-all
```

This command runs both Prettier formatting and ESLint fixes. CI will fail if code is not properly formatted or has linting errors. Always run this after making changes to validate they were made correctly.

### Pull Request Guidelines

- When creating a PR that fixes a GitHub issue, include `Closes #xxx` in the PR description (where `xxx` is the issue number). This automatically closes the issue when the PR is merged.
- Consolidate related small PRs into a single PR when possible to simplify review.
- Avoid creating multiple PRs that all modify `src/data/version.json` simultaneously; coordinate version bumps to prevent merge conflicts.

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

### Changelog & Versioning

- Changelog entries are Markdown files in `src/content/changelog/`, named `YYYY-MM-DD-vX-Y-Z.md`
- Each file has frontmatter: `version`, `date`, `prNumber`, `prUrl`
- `src/data/version.json` tracks the current `version` and `lastUpdated` date; update it with each release
- On the Updates page, changelog entries are grouped by day, showing the highest version number for that day as the header with all bullet points combined
- PR references within grouped entries display as a concise, comma-separated list
- Use `import.meta.glob` with `eager: true` to load changelog files for display

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

## Zelda: Developmental Editor

The `zelda/` directory contains Zelda Felfenlagger, the AI developmental editor for _Boss at Work | Intern at Home: Redeploy Your Competence_. She's a system prompt + methodology + book context package designed for use with Claude Projects, Claude Code, or the API. See `zelda/README.md` for usage instructions. `zelda/BOOK_CONTEXT.md` should be updated after major editorial decisions.

## Ghostwriter: Voice-Matched Copywriter

The `ghostwriter/` directory contains a voice-matched copywriter for _Boss at Work | Intern at Home: Redeploy Your Competence_. It drafts and revises chapter prose in Danvers Fleury's natural voice (the labnotes register — confessional, structurally funny, specific). It takes chapter briefs and Zelda's revision directives and produces publication-ready prose. See `ghostwriter/README.md` for usage instructions.

**Workflow:** Zelda analyzes -> Author approves directives -> Ghostwriter writes -> Author refines -> Zelda scores if needed.

## Notes for Future Development

- Logo placeholder should be replaced with actual LifeBuild.me logo
- Consider adding more pages (about, features, etc.)
- May need to update Buttondown form action URL with actual username
- Keep design consistent with minimalist approach
