# LifeBuild.me

A simple landing page for LifeBuild.me, built with Astro and deployed on Cloudflare Pages.

## 🚀 Project Structure

```
/
├── public/
│   └── favicon.svg
├── src/
│   ├── components/
│   │   └── LifeBuild.astro
│   ├── layouts/
│   │   └── Layout.astro
│   └── pages/
│       └── index.astro
├── astro.config.mjs
├── package.json
└── tsconfig.json
```

## 🧞 Commands

All commands are run from the root of the project, from a terminal:

| Command                   | Action                                           |
| :------------------------ | :----------------------------------------------- |
| `npm install`             | Installs dependencies                            |
| `npm run dev`             | Starts local dev server at `localhost:4321`      |
| `npm run build`           | Build your production site to `./dist/`          |
| `npm run preview`         | Preview your build locally, before deploying     |
| `npm run lint`            | Run ESLint to check code quality                 |
| `npm run lint:fix`        | Run ESLint and automatically fix issues          |
| `npm run format`          | Format code with Prettier                        |
| `npm run format:check`    | Check code formatting without making changes     |

## 🌐 Deployment to Cloudflare Pages

This site is configured for deployment on Cloudflare Pages. Here's how to set it up:

### Prerequisites
- A Cloudflare account
- GitHub repository connected to your Cloudflare account

### Cloudflare Pages Configuration

1. **Log in to Cloudflare Dashboard**
   - Go to Workers & Pages
   - Click "Create application"
   - Select "Pages" tab
   - Click "Connect to Git"

2. **Connect Your Repository**
   - Select your GitHub account
   - Choose the `life-build-site` repository
   - Click "Begin setup"

3. **Configure Build Settings**
   - **Project name**: `lifebuild` (or your preferred name)
   - **Production branch**: `main` (or your default branch)
   - **Build command**: `npm run build`
   - **Build output directory**: `dist`
   - **Environment variables**: None required for basic setup

4. **Deploy**
   - Click "Save and Deploy"
   - Cloudflare will build and deploy your site
   - Future commits to the main branch will automatically trigger new deployments

### Custom Domain Setup

1. **Add Custom Domain**
   - In Cloudflare Pages, go to your project
   - Click "Custom domains" tab
   - Click "Set up a custom domain"
   - Enter `lifebuild.me`
   - Follow the DNS setup instructions

2. **DNS Configuration**
   - If domain is registered elsewhere (e.g., Namecheap):
     - Add CNAME record pointing to your Cloudflare Pages URL
   - If using Cloudflare Registrar:
     - DNS records will be configured automatically

## 📧 Newsletter Integration

The site includes a newsletter subscription form powered by [Buttondown](https://buttondown.email/).

To configure your own newsletter:
1. Create a Buttondown account at https://buttondown.email/
2. Update the form action URL in `src/components/LifeBuild.astro`:
   ```html
   <form action="https://buttondown.com/api/emails/embed-subscribe/YOUR-USERNAME" ...>
   ```
3. Replace `YOUR-USERNAME` with your Buttondown username

## 🔗 Links

- GitHub Repository: Update the link in `src/components/LifeBuild.astro`
- SocioTechnica: https://sociotechnica.org

## 📝 Customization

### Logo
The logo is currently a placeholder. To add your own logo:
1. Place your logo image in the `public/` directory
2. Update the logo section in `src/components/LifeBuild.astro`

### Styling
All styles are contained within the component files. Modify the `<style>` blocks in:
- `src/layouts/Layout.astro` for global styles
- `src/components/LifeBuild.astro` for component-specific styles

### Content
Edit the text content in `src/components/LifeBuild.astro` to customize:
- Headline
- Tagline
- Footer links
