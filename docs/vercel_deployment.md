# Deploying Snakeskin Projects to Vercel

This guide explains how to deploy a Snakeskin project to Vercel.

## Prerequisites

1. A Snakeskin project that builds successfully with `snakeskin build`
2. A [Vercel](https://vercel.com) account
3. [Vercel CLI](https://vercel.com/docs/cli) installed (optional)

## Option 1: Deploy via Git Integration

1. Push your Snakeskin project to GitHub, GitLab, or Bitbucket
2. Log in to your Vercel account
3. Click "New Project"
4. Import your repository
5. Configure the project:
   - Build Command: `pip install snakeskin-xplnhub && snakeskin build`
   - Output Directory: `dist`
6. Click "Deploy"

## Option 2: Deploy via Vercel CLI

1. Install Vercel CLI:
   ```bash
   npm i -g vercel
   ```

2. Log in to Vercel:
   ```bash
   vercel login
   ```

3. Navigate to your Snakeskin project directory:
   ```bash
   cd my-snakeskin-project
   ```

4. Deploy to Vercel:
   ```bash
   vercel
   ```

5. Follow the prompts to configure your deployment

## Configuration

The `vercel.json` file in your project configures how Vercel builds and serves your project:

```json
{
  "version": 2,
  "builds": [
    {
      "src": "dist/**",
      "use": "@vercel/static"
    }
  ],
  "routes": [
    { "handle": "filesystem" },
    { "src": "/(.*)", "dest": "/dist/index.html" }
  ],
  "buildCommand": "snakeskin build"
}
```

## Troubleshooting

- **Build Fails**: Make sure your project builds locally with `snakeskin build`
- **Missing Dependencies**: Add any Python dependencies to a `requirements.txt` file
- **404 Errors**: Check that your routes in `vercel.json` are correctly configured

## Notes

- Vercel primarily supports JavaScript frameworks, so you're using it as a static file host
- The build process runs `snakeskin build` to generate static files
- For more complex setups, consider using a serverless function to run Python code
