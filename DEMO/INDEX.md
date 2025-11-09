# 🐍 Snakeskin Landing Page Demo

Welcome to the Snakeskin Landing Page Demo! This folder contains everything you need to build a professional landing page in minutes.

![Snakeskin Demo](https://img.shields.io/badge/Snakeskin-Demo-blue?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Ready-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

---

## 📚 Documentation Files

### 1. **[QUICKSTART.md](QUICKSTART.md)** ⚡
**Start here if you want to get running in 5 minutes!**

Quick commands to get your landing page up and running with minimal setup.

### 2. **[README.md](README.md)** 📖
**Complete step-by-step tutorial**

Comprehensive guide covering:
- Installation and setup
- Creating all components (Navbar, Hero, Features, Contact, Footer)
- Building and running your project
- Deployment instructions
- Troubleshooting

### 3. **[CUSTOMIZATION.md](CUSTOMIZATION.md)** 🎨
**Make it your own!**

Learn how to:
- Change colors and fonts
- Update text content
- Add images and logos
- Modify layouts
- Add new sections (Testimonials, Pricing, etc.)
- Responsive design tips

---

## 📁 Example Components

The `example_components/` folder contains ready-to-use component files:

```
example_components/
├── Navbar.py          # Responsive navigation bar
├── Hero.py            # Hero section with CTA
├── Features.py        # Features showcase grid
├── ContactForm.py     # Contact form with validation
├── Footer.py          # Footer with links
└── main.py            # Main application file
```

**How to use:**
1. Create a new project: `snakeskin create my-landing-page`
2. Copy all `.py` files from `example_components/` to your project's `src/components/`
3. Copy `main.py` to your project root
4. Run: `snakeskin build && snakeskin dev`

---

## 🚀 Quick Start Commands

```bash
# Install Snakeskin
pip install snakeskin-xplnhub

# Create a new project
snakeskin create my-landing-page
cd my-landing-page

# Copy example components
cp ../DEMO/example_components/*.py src/components/
cp ../DEMO/example_components/main.py .

# Build and run
snakeskin build
snakeskin dev
```

Your browser will open automatically at `http://localhost:3000/dist/index.html`

---

## 🎯 What You'll Build

A modern, responsive landing page with:

✅ **Navigation Bar** - Fixed header with smooth scrolling  
✅ **Hero Section** - Eye-catching headline with CTA button  
✅ **Features Grid** - Showcase 6 key features with icons  
✅ **Contact Form** - Functional form with validation  
✅ **Footer** - Links and social media icons  
✅ **Responsive Design** - Works on mobile, tablet, and desktop  
✅ **Interactive Elements** - Buttons with state management  
✅ **Modern UI** - Built with Tailwind CSS  

---

## 📋 Prerequisites

- Python 3.7 or higher
- Node.js and npm (for Tailwind CSS)
- Basic knowledge of Python and HTML

---

## 🛠️ Customization Options

After building the basic landing page, you can:

1. **Change Colors** - Update Tailwind config or component classes
2. **Add Sections** - Testimonials, Pricing, FAQ, etc.
3. **Modify Layout** - Adjust spacing, grid columns, etc.
4. **Add Images** - Replace placeholders with your own
5. **Custom Fonts** - Integrate Google Fonts
6. **Add Animations** - Use Tailwind transitions and transforms

See [CUSTOMIZATION.md](CUSTOMIZATION.md) for detailed instructions.

---

## 📦 Project Structure

After creating your project, you'll have:

```
my-landing-page/
├── src/
│   └── components/
│       ├── Navbar.py
│       ├── Hero.py
│       ├── Features.py
│       ├── ContactForm.py
│       └── Footer.py
├── dist/                    # Build output
│   ├── index.html
│   └── tailwind.css
├── input.css                # Tailwind input
├── main.py                  # Application entry
└── tailwind.config.js       # Tailwind config
```

---

## 🚢 Deployment

Deploy your landing page to popular platforms:

### Netlify
```bash
netlify deploy --prod
```

### Vercel
```bash
vercel
```

See the main [README.md](README.md) for detailed deployment instructions.

---

## 🆘 Need Help?

1. **Check the docs**: Start with [QUICKSTART.md](QUICKSTART.md)
2. **Customization**: See [CUSTOMIZATION.md](CUSTOMIZATION.md)
3. **Full tutorial**: Read [README.md](README.md)
4. **Troubleshooting**: Check [../docs/troubleshooting.md](../docs/troubleshooting.md)
5. **GitHub Issues**: [Open an issue](https://github.com/XplnHUB/xplnhub-snakeskin/issues)

---

## 🎓 Learning Path

**Beginner?** Follow this path:

1. Read [QUICKSTART.md](QUICKSTART.md) - Get familiar with the basics
2. Build the demo - Copy the example components and run
3. Experiment - Change colors, text, and images
4. Read [README.md](README.md) - Understand how everything works
5. Customize - Use [CUSTOMIZATION.md](CUSTOMIZATION.md) to make it yours
6. Deploy - Push your site live!

**Experienced?** Jump straight to:

1. Copy `example_components/` to your project
2. Customize using [CUSTOMIZATION.md](CUSTOMIZATION.md)
3. Deploy!

---

## 💡 Tips

- **Hot Reload**: Changes auto-refresh in dev mode
- **Component-Based**: Each section is a reusable component
- **State Management**: Components can manage their own state
- **Tailwind CSS**: Use utility classes for rapid styling
- **Python Power**: Leverage Python for dynamic content

---

## 🌟 Features Showcase

### Interactive Components
```python
# Buttons with state
self.state = {"clicked": False}

# Form validation
def validate_form(self):
    errors = {}
    # Validation logic
    return errors
```

### Responsive Design
```python
# Mobile-first responsive classes
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3">
```

### Modern UI
```python
# Tailwind utility classes
<button class="bg-blue-600 hover:bg-blue-700 transform hover:scale-105">
```

---

## 📞 Support

- **Documentation**: [../docs/](../docs/)
- **GitHub**: [https://github.com/XplnHUB/xplnhub-snakeskin](https://github.com/XplnHUB/xplnhub-snakeskin)
- **PyPI**: [https://pypi.org/project/snakeskin-xplnhub/](https://pypi.org/project/snakeskin-xplnhub/)

---

## 📄 License

MIT License - Feel free to use this demo for your projects!

---

**Ready to build?** Start with [QUICKSTART.md](QUICKSTART.md) now! 🚀
