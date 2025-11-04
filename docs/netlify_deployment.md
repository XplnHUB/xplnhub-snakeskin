# Deploying Snakeskin Projects to Netlify

This guide explains how to deploy a Snakeskin project to Netlify.

## Prerequisites

1. A Snakeskin project that builds successfully with `snakeskin build`
2. A [Netlify](https://netlify.com) account
3. [Netlify CLI](https://docs.netlify.com/cli/get-started/) installed (optional)

## Option 1: Deploy via Git Integration

1. Push your Snakeskin project to GitHub, GitLab, or Bitbucket
2. Log in to your Netlify account
3. Click "New site from Git"
4. Select your repository
5. Configure the build settings:
   - Build Command: `pip install snakeskin && snakeskin build`
   - Publish Directory: `dist`
6. Click "Deploy site"

## Option 2: Deploy via Netlify CLI

1. Install Netlify CLI:
   ```bash
   npm install -g netlify-cli
   ```

2. Log in to Netlify:
   ```bash
   netlify login
   ```

3. Navigate to your Snakeskin project directory:
   ```bash
   cd my-snakeskin-project
   ```

4. Initialize Netlify:
   ```bash
   netlify init
   ```

5. Deploy to Netlify:
   ```bash
   netlify deploy --prod
   ```

## Configuration

The `netlify.toml` file in your project configures how Netlify builds and serves your project:

```toml
[build]
  publish = "dist"
  command = "pip install snakeskin && snakeskin build"

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200
```

## Troubleshooting

- **Build Environment**: Netlify uses a Linux environment, so ensure your build works on Linux
- **Python Version**: Specify the Python version in a `runtime.txt` file if needed
- **Dependencies**: Add any Python dependencies to a `requirements.txt` file
- **Build Timeout**: If your build takes too long, optimize it or increase the build timeout in Netlify settings

## Notes

- Netlify primarily supports JavaScript frameworks, so you're using it as a static file host
- The build process runs `snakeskin build` to generate static files
- For more complex setups, consider using Netlify Functions to run serverless Python code
