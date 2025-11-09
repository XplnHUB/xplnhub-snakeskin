# Customization Guide

Learn how to customize your landing page to match your brand.

## Table of Contents

1. [Changing Colors](#changing-colors)
2. [Updating Text Content](#updating-text-content)
3. [Adding Images](#adding-images)
4. [Modifying Layout](#modifying-layout)
5. [Adding New Sections](#adding-new-sections)
6. [Custom Fonts](#custom-fonts)

---

## Changing Colors

### Method 1: Tailwind Config (Recommended)

Edit `tailwind.config.js`:

```javascript
module.exports = {
  content: ["./src/components/**/*.py", "./main.py"],
  theme: {
    extend: {
      colors: {
        // Add your brand colors
        brand: {
          primary: '#FF6B6B',
          secondary: '#4ECDC4',
          accent: '#FFE66D',
        },
      },
    },
  },
  plugins: [],
};
```

Then use in components:

```python
<button class="bg-brand-primary hover:bg-brand-secondary">
    Click Me
</button>
```

### Method 2: Direct Class Changes

In your component files, replace color classes:

```python
# Before
class="bg-blue-600 hover:bg-blue-700"

# After
class="bg-purple-600 hover:bg-purple-700"
```

Available Tailwind colors:
- `gray`, `red`, `yellow`, `green`, `blue`, `indigo`, `purple`, `pink`
- Shades: `50`, `100`, `200`, `300`, `400`, `500`, `600`, `700`, `800`, `900`

---

## Updating Text Content

### Hero Section

Edit `src/components/Hero.py`:

```python
# Change the main headline
<h1 class="text-5xl md:text-6xl font-bold text-gray-900 mb-6">
    Your Amazing Product
    <span class="text-blue-600">Changes Everything</span>
</h1>

# Change the subtitle
<p class="text-xl text-gray-600 mb-8 max-w-3xl mx-auto">
    Your compelling value proposition goes here. 
    Explain why your product is amazing.
</p>

# Change button text
button_text = "Start Free Trial" if clicked else "Get Started Now"
```

### Features Section

Edit `src/components/Features.py`:

```python
self.features = [
    {
        "icon": "🚀",  # Change emoji
        "title": "Your Feature",  # Change title
        "description": "Your feature description"  # Change description
    },
    # Add more features...
]
```

### Navigation

Edit `src/components/Navbar.py`:

```python
# Change brand name
<h1 class="text-2xl font-bold text-blue-600">Your Brand</h1>

# Change menu items
<a href="#pricing">Pricing</a>
<a href="#testimonials">Testimonials</a>
<a href="#faq">FAQ</a>
```

---

## Adding Images

### Replace Placeholder Image

In `Hero.py`, replace the placeholder:

```python
# Before
<img src="https://via.placeholder.com/800x400/4F46E5/FFFFFF?text=Dashboard+Preview" 

# After - Using local image
<img src="assets/hero-image.png" 

# After - Using external URL
<img src="https://yourdomain.com/images/hero.jpg"
```

### Add Logo

In `Navbar.py`:

```python
<div class="flex items-center">
    <img src="assets/logo.png" alt="Logo" class="h-8 w-8 mr-2" />
    <h1 class="text-2xl font-bold text-blue-600">Your Brand</h1>
</div>
```

### Store Images

Create an assets folder:

```bash
mkdir -p src/assets
# Copy your images there
cp ~/Downloads/logo.png src/assets/
```

Update `snakeskin/utils.py` to copy assets during build (already configured).

---

## Modifying Layout

### Change Section Order

In `main.py`, rearrange the components:

```python
# Before
{navbar.render()}
{hero.render()}
{features.render()}
{contact.render()}
{footer.render()}

# After - Different order
{navbar.render()}
{hero.render()}
{contact.render()}  # Contact moved up
{features.render()}
{footer.render()}
```

### Adjust Spacing

Change padding/margin classes:

```python
# Less spacing
<section class="py-10">  # Instead of py-20

# More spacing
<section class="py-32">  # Instead of py-20

# Different spacing for mobile vs desktop
<section class="py-10 md:py-20">
```

### Grid Layouts

Change the features grid:

```python
# 2 columns on all screens
<div class="grid grid-cols-2 gap-8">

# 1 column mobile, 2 tablet, 4 desktop
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
```

---

## Adding New Sections

### Create a Testimonials Section

Create `src/components/Testimonials.py`:

```python
from snakeskin.framework import Component

class Testimonials(Component):
    def __init__(self, **props):
        super().__init__(**props)
        self.testimonials = [
            {
                "name": "John Doe",
                "role": "CEO, Company",
                "text": "This product changed my life!",
                "avatar": "https://via.placeholder.com/100"
            },
            # Add more...
        ]
    
    def render(self):
        testimonials_html = ""
        for t in self.testimonials:
            testimonials_html += f"""
            <div class="bg-white p-6 rounded-lg shadow-lg">
                <p class="text-gray-600 mb-4">"{t['text']}"</p>
                <div class="flex items-center">
                    <img src="{t['avatar']}" class="w-12 h-12 rounded-full mr-4" />
                    <div>
                        <p class="font-bold">{t['name']}</p>
                        <p class="text-sm text-gray-500">{t['role']}</p>
                    </div>
                </div>
            </div>
            """
        
        return f"""
        <section class="py-20 bg-gray-50">
            <div class="max-w-7xl mx-auto px-4">
                <h2 class="text-4xl font-bold text-center mb-12">
                    What Our Customers Say
                </h2>
                <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                    {testimonials_html}
                </div>
            </div>
        </section>
        """
```

Add to `main.py`:

```python
from src.components.Testimonials import Testimonials

testimonials = Testimonials()
testimonials.mount()

# In HTML
{testimonials.render()}
```

### Create a Pricing Section

Create `src/components/Pricing.py`:

```python
from snakeskin.framework import Component

class Pricing(Component):
    def render(self):
        return f"""
        <section id="pricing" class="py-20 bg-white">
            <div class="max-w-7xl mx-auto px-4">
                <h2 class="text-4xl font-bold text-center mb-12">
                    Simple, Transparent Pricing
                </h2>
                <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                    <!-- Free Plan -->
                    <div class="border-2 border-gray-200 rounded-lg p-8">
                        <h3 class="text-2xl font-bold mb-4">Free</h3>
                        <p class="text-4xl font-bold mb-6">$0<span class="text-lg">/mo</span></p>
                        <ul class="space-y-3 mb-8">
                            <li>✓ Feature 1</li>
                            <li>✓ Feature 2</li>
                            <li>✓ Feature 3</li>
                        </ul>
                        <button class="w-full bg-gray-200 text-gray-800 py-3 rounded-lg">
                            Get Started
                        </button>
                    </div>
                    
                    <!-- Pro Plan -->
                    <div class="border-4 border-blue-600 rounded-lg p-8 transform scale-105">
                        <div class="bg-blue-600 text-white text-sm font-bold px-3 py-1 rounded-full inline-block mb-4">
                            POPULAR
                        </div>
                        <h3 class="text-2xl font-bold mb-4">Pro</h3>
                        <p class="text-4xl font-bold mb-6">$29<span class="text-lg">/mo</span></p>
                        <ul class="space-y-3 mb-8">
                            <li>✓ Everything in Free</li>
                            <li>✓ Advanced Feature 1</li>
                            <li>✓ Advanced Feature 2</li>
                            <li>✓ Priority Support</li>
                        </ul>
                        <button class="w-full bg-blue-600 text-white py-3 rounded-lg hover:bg-blue-700">
                            Start Free Trial
                        </button>
                    </div>
                    
                    <!-- Enterprise Plan -->
                    <div class="border-2 border-gray-200 rounded-lg p-8">
                        <h3 class="text-2xl font-bold mb-4">Enterprise</h3>
                        <p class="text-4xl font-bold mb-6">Custom</p>
                        <ul class="space-y-3 mb-8">
                            <li>✓ Everything in Pro</li>
                            <li>✓ Custom Integration</li>
                            <li>✓ Dedicated Support</li>
                            <li>✓ SLA</li>
                        </ul>
                        <button class="w-full bg-gray-800 text-white py-3 rounded-lg hover:bg-gray-900">
                            Contact Sales
                        </button>
                    </div>
                </div>
            </div>
        </section>
        """
```

---

## Custom Fonts

### Method 1: Google Fonts

Add to `main.py` in the `<head>` section:

```python
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Your Site</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
    <link href="tailwind.css" rel="stylesheet">
    <style>
        body {{
            font-family: 'Inter', sans-serif;
        }}
    </style>
</head>
```

### Method 2: Tailwind Config

Update `tailwind.config.js`:

```javascript
module.exports = {
  content: ["./src/components/**/*.py", "./main.py"],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
        heading: ['Poppins', 'sans-serif'],
      },
    },
  },
  plugins: [],
};
```

Use in components:

```python
<h1 class="font-heading text-4xl">Heading Text</h1>
<p class="font-sans">Body text</p>
```

---

## Quick Tips

### Responsive Design

Use Tailwind's responsive prefixes:

```python
# Mobile first approach
<div class="text-sm md:text-base lg:text-lg">
    # Small on mobile, medium on tablet, large on desktop
</div>

<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3">
    # 1 column mobile, 2 tablet, 3 desktop
</div>
```

### Hover Effects

```python
<button class="bg-blue-600 hover:bg-blue-700 hover:scale-105 transition">
    Hover Me
</button>
```

### Animations

```python
<div class="transform transition hover:scale-110 hover:rotate-3">
    Animated Card
</div>
```

---

## Need More Help?

- Check the [Tailwind CSS Documentation](https://tailwindcss.com/docs)
- See the [Component Guide](../docs/component_guide.md)
- Review the [API Reference](../docs/api_reference.md)

Happy customizing! 🎨
