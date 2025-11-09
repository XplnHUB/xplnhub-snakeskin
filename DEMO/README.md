# Building a Landing Page with Snakeskin - Complete Tutorial

This demo shows you how to build a fully functional landing page with Snakeskin from scratch.

## What You'll Build

A modern landing page with:
- **Hero Section** with animated call-to-action button
- **Features Section** showcasing key benefits
- **Contact Form** with validation
- **Responsive Navigation Bar**
- **Footer** with social links
- **Interactive Elements** with state management

---

## Prerequisites

- Python 3.7 or higher installed
- Node.js and npm installed (for Tailwind CSS)
- Basic knowledge of Python and HTML

---

## Step 1: Installation

Install Snakeskin:

```bash
pip install snakeskin-xplnhub
```

Verify installation:

```bash
snakeskin --version
```

---

## Step 2: Create Your Project

Create a new project called `my-landing-page`:

```bash
snakeskin create my-landing-page
cd my-landing-page
```

This creates the following structure:

```
my-landing-page/
├── src/
│   └── components/    # Your UI components go here
├── dist/              # Build output directory
├── input.css          # Tailwind CSS input file
├── main.py            # Main application entry
└── tailwind.config.js # Tailwind configuration
```

---

## Step 3: Create the Navigation Component

Create `src/components/Navbar.py`:

```python
from snakeskin.framework import Component

class Navbar(Component):
    def __init__(self, **props):
        super().__init__(**props)
        self.state = {
            "mobile_menu_open": False
        }
    
    def toggle_menu(self):
        self.set_state({"mobile_menu_open": not self.state.get("mobile_menu_open", False)})
    
    def render(self):
        menu_open = self.state.get("mobile_menu_open", False)
        
        return f"""
        <nav class="bg-white shadow-lg fixed w-full top-0 z-50">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="flex justify-between h-16">
                    <div class="flex items-center">
                        <h1 class="text-2xl font-bold text-blue-600">🐍 Snakeskin</h1>
                    </div>
                    <div class="hidden md:flex items-center space-x-8">
                        <a href="#features" class="text-gray-700 hover:text-blue-600 transition">Features</a>
                        <a href="#about" class="text-gray-700 hover:text-blue-600 transition">About</a>
                        <a href="#contact" class="text-gray-700 hover:text-blue-600 transition">Contact</a>
                        <button class="bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700 transition">
                            Get Started
                        </button>
                    </div>
                </div>
            </div>
        </nav>
        """
```

---

## Step 4: Create the Hero Component

Create `src/components/Hero.py`:

```python
from snakeskin.framework import Component

class Hero(Component):
    def __init__(self, **props):
        super().__init__(**props)
        self.state = {
            "button_clicked": False,
            "email": ""
        }
    
    def handle_click(self):
        self.set_state({"button_clicked": True})
    
    def render(self):
        clicked = self.state.get("button_clicked", False)
        button_text = "🎉 Thanks for your interest!" if clicked else "Get Started Free"
        button_class = "bg-green-500 hover:bg-green-600" if clicked else "bg-blue-600 hover:bg-blue-700"
        
        return f"""
        <section class="pt-24 pb-20 bg-gradient-to-br from-blue-50 to-indigo-100 min-h-screen flex items-center">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="text-center">
                    <h1 class="text-5xl md:text-6xl font-bold text-gray-900 mb-6">
                        Build Modern Web Apps
                        <span class="text-blue-600">Venomously Fast</span>
                    </h1>
                    <p class="text-xl text-gray-600 mb-8 max-w-3xl mx-auto">
                        Snakeskin is a lightweight Python framework for building component-based 
                        web applications with Tailwind CSS integration and hot reload.
                    </p>
                    <div class="flex flex-col sm:flex-row gap-4 justify-center items-center">
                        <button 
                            onclick="handleHeroClick_{id(self)}()"
                            class="{button_class} text-white px-8 py-4 rounded-lg text-lg font-semibold transition transform hover:scale-105 shadow-lg"
                        >
                            {button_text}
                        </button>
                        <a href="#features" class="text-blue-600 px-8 py-4 rounded-lg text-lg font-semibold hover:bg-blue-50 transition">
                            Learn More →
                        </a>
                    </div>
                    <div class="mt-12">
                        <img src="https://via.placeholder.com/800x400/4F46E5/FFFFFF?text=Dashboard+Preview" 
                             alt="Dashboard Preview" 
                             class="rounded-lg shadow-2xl mx-auto"
                        />
                    </div>
                </div>
            </div>
            <script>
                function handleHeroClick_{id(self)}() {{
                    console.log("Hero button clicked!");
                    // In production, you would make an API call here
                }}
            </script>
        </section>
        """
```

---

## Step 5: Create the Features Component

Create `src/components/Features.py`:

```python
from snakeskin.framework import Component

class Features(Component):
    def __init__(self, **props):
        super().__init__(**props)
        self.features = [
            {
                "icon": "⚡",
                "title": "Lightning Fast",
                "description": "Build and deploy web applications in minutes, not hours."
            },
            {
                "icon": "🎨",
                "title": "Beautiful UI",
                "description": "Integrated with Tailwind CSS for stunning, responsive designs."
            },
            {
                "icon": "🔧",
                "title": "Easy to Use",
                "description": "Simple Python syntax with powerful component-based architecture."
            },
            {
                "icon": "🔥",
                "title": "Hot Reload",
                "description": "See your changes instantly with built-in development server."
            },
            {
                "icon": "📦",
                "title": "Component-Based",
                "description": "Build reusable components with state management and lifecycle hooks."
            },
            {
                "icon": "🚀",
                "title": "Deploy Anywhere",
                "description": "Deploy to Vercel, Netlify, or any static hosting platform."
            }
        ]
    
    def render(self):
        features_html = ""
        for feature in self.features:
            features_html += f"""
            <div class="bg-white p-8 rounded-xl shadow-lg hover:shadow-xl transition transform hover:-translate-y-2">
                <div class="text-5xl mb-4">{feature['icon']}</div>
                <h3 class="text-xl font-bold text-gray-900 mb-3">{feature['title']}</h3>
                <p class="text-gray-600">{feature['description']}</p>
            </div>
            """
        
        return f"""
        <section id="features" class="py-20 bg-white">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="text-center mb-16">
                    <h2 class="text-4xl font-bold text-gray-900 mb-4">Why Choose Snakeskin?</h2>
                    <p class="text-xl text-gray-600">Everything you need to build modern web applications</p>
                </div>
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                    {features_html}
                </div>
            </div>
        </section>
        """
```

---

## Step 6: Create the Contact Form Component

Create `src/components/ContactForm.py`:

```python
from snakeskin.framework import Component

class ContactForm(Component):
    def __init__(self, **props):
        super().__init__(**props)
        self.state = {
            "name": "",
            "email": "",
            "message": "",
            "submitted": False,
            "errors": {}
        }
    
    def validate_form(self):
        errors = {}
        if not self.state.get("name"):
            errors["name"] = "Name is required"
        if not self.state.get("email"):
            errors["email"] = "Email is required"
        elif "@" not in self.state.get("email", ""):
            errors["email"] = "Invalid email format"
        if not self.state.get("message"):
            errors["message"] = "Message is required"
        return errors
    
    def render(self):
        submitted = self.state.get("submitted", False)
        
        if submitted:
            return f"""
            <section id="contact" class="py-20 bg-gradient-to-br from-blue-50 to-indigo-100">
                <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
                    <div class="bg-white rounded-xl shadow-lg p-12 text-center">
                        <div class="text-6xl mb-4">✅</div>
                        <h3 class="text-3xl font-bold text-gray-900 mb-4">Thank You!</h3>
                        <p class="text-xl text-gray-600">We'll get back to you soon.</p>
                    </div>
                </div>
            </section>
            """
        
        return f"""
        <section id="contact" class="py-20 bg-gradient-to-br from-blue-50 to-indigo-100">
            <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="text-center mb-12">
                    <h2 class="text-4xl font-bold text-gray-900 mb-4">Get In Touch</h2>
                    <p class="text-xl text-gray-600">Have questions? We'd love to hear from you.</p>
                </div>
                <div class="bg-white rounded-xl shadow-lg p-8">
                    <form onsubmit="handleSubmit_{id(self)}(event)" class="space-y-6">
                        <div>
                            <label class="block text-gray-700 font-semibold mb-2">Name</label>
                            <input 
                                type="text" 
                                name="name"
                                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                                placeholder="Your name"
                                required
                            />
                        </div>
                        <div>
                            <label class="block text-gray-700 font-semibold mb-2">Email</label>
                            <input 
                                type="email" 
                                name="email"
                                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                                placeholder="your.email@example.com"
                                required
                            />
                        </div>
                        <div>
                            <label class="block text-gray-700 font-semibold mb-2">Message</label>
                            <textarea 
                                name="message"
                                rows="5"
                                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                                placeholder="Tell us what you're thinking..."
                                required
                            ></textarea>
                        </div>
                        <button 
                            type="submit"
                            class="w-full bg-blue-600 text-white px-8 py-4 rounded-lg text-lg font-semibold hover:bg-blue-700 transition transform hover:scale-105"
                        >
                            Send Message
                        </button>
                    </form>
                </div>
            </div>
            <script>
                function handleSubmit_{id(self)}(event) {{
                    event.preventDefault();
                    const formData = new FormData(event.target);
                    console.log("Form submitted:", Object.fromEntries(formData));
                    alert("Thank you for your message! We'll get back to you soon.");
                    event.target.reset();
                }}
            </script>
        </section>
        """
```

---

## Step 7: Create the Footer Component

Create `src/components/Footer.py`:

```python
from snakeskin.framework import Component

class Footer(Component):
    def render(self):
        return f"""
        <footer class="bg-gray-900 text-white py-12">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="grid grid-cols-1 md:grid-cols-4 gap-8">
                    <div>
                        <h3 class="text-xl font-bold mb-4">🐍 Snakeskin</h3>
                        <p class="text-gray-400">
                            A modern Python framework for building beautiful web applications.
                        </p>
                    </div>
                    <div>
                        <h4 class="font-semibold mb-4">Product</h4>
                        <ul class="space-y-2 text-gray-400">
                            <li><a href="#features" class="hover:text-white transition">Features</a></li>
                            <li><a href="#" class="hover:text-white transition">Pricing</a></li>
                            <li><a href="#" class="hover:text-white transition">Documentation</a></li>
                        </ul>
                    </div>
                    <div>
                        <h4 class="font-semibold mb-4">Company</h4>
                        <ul class="space-y-2 text-gray-400">
                            <li><a href="#about" class="hover:text-white transition">About</a></li>
                            <li><a href="#" class="hover:text-white transition">Blog</a></li>
                            <li><a href="#contact" class="hover:text-white transition">Contact</a></li>
                        </ul>
                    </div>
                    <div>
                        <h4 class="font-semibold mb-4">Connect</h4>
                        <div class="flex space-x-4">
                            <a href="#" class="text-gray-400 hover:text-white transition text-2xl">🐦</a>
                            <a href="#" class="text-gray-400 hover:text-white transition text-2xl">💼</a>
                            <a href="#" class="text-gray-400 hover:text-white transition text-2xl">📧</a>
                        </div>
                    </div>
                </div>
                <div class="border-t border-gray-800 mt-8 pt-8 text-center text-gray-400">
                    <p>&copy; 2024 Snakeskin. Built with 🐍 and ❤️</p>
                </div>
            </div>
        </footer>
        """
```

---

## Step 8: Update main.py

Replace the content of `main.py` with:

```python
from src.components.Navbar import Navbar
from src.components.Hero import Hero
from src.components.Features import Features
from src.components.ContactForm import ContactForm
from src.components.Footer import Footer

# Initialize components
navbar = Navbar()
hero = Hero()
features = Features()
contact = ContactForm()
footer = Footer()

# Mount components to activate lifecycle hooks
navbar.mount()
hero.mount()
features.mount()
contact.mount()
footer.mount()

# Create HTML content
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Snakeskin - Modern Python Web Framework</title>
    <link href="tailwind.css" rel="stylesheet">
    <style>
        html {{
            scroll-behavior: smooth;
        }}
    </style>
</head>
<body class="bg-gray-50">
    {navbar.render()}
    {hero.render()}
    {features.render()}
    {contact.render()}
    {footer.render()}
</body>
</html>
"""

# Write to file
with open("dist/index.html", "w") as f:
    f.write(html_content)

print("✅ Build complete! Open dist/index.html to view your landing page.")
```

---

## Step 9: Build Your Project

Build the project to generate the HTML and CSS:

```bash
snakeskin build
```

This will:
1. Run `main.py` to generate `dist/index.html`
2. Process Tailwind CSS to generate `dist/tailwind.css`
3. Optimize all assets

---

## Step 10: Run the Development Server

Start the development server with hot reload:

```bash
snakeskin dev
```

The browser will automatically open to `http://localhost:3000/dist/index.html`

Any changes you make to your components will automatically reload the page!

---

## Step 11: Customize Your Landing Page

### Change Colors

Edit `tailwind.config.js` to customize colors:

```javascript
module.exports = {
  content: ["./src/components/**/*.py", "./main.py"],
  theme: {
    extend: {
      colors: {
        primary: '#3B82F6',
        secondary: '#8B5CF6',
      },
    },
  },
  plugins: [],
};
```

### Add More Sections

Create new components in `src/components/` and import them in `main.py`.

### Add Interactivity

Use the component state system:

```python
def __init__(self, **props):
    super().__init__(**props)
    self.state = {
        "count": 0
    }

def increment(self):
    self.set_state({"count": self.state["count"] + 1})
```

---

## Step 12: Deploy Your Landing Page

### Deploy to Netlify

```bash
# Install Netlify CLI
npm install -g netlify-cli

# Login
netlify login

# Deploy
netlify deploy --prod
```

### Deploy to Vercel

```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel
```

---

## Troubleshooting

### Tailwind CSS not working?

Make sure Node.js is installed and run:

```bash
npx tailwindcss -i ./input.css -o ./dist/tailwind.css
```

### Hot reload not working?

Install websockets:

```bash
pip install snakeskin-xplnhub[dev]
```

### Port 3000 already in use?

Kill the process:

```bash
lsof -i :3000
kill -9 <PID>
```

---

## Next Steps

1. **Add a database** - Connect to PostgreSQL, MongoDB, or SQLite
2. **Add authentication** - Implement user login/signup
3. **Add API integration** - Connect to external APIs
4. **Add animations** - Use CSS animations or JavaScript libraries
5. **Optimize performance** - Minimize CSS, compress images

---

## Resources

- [Full Documentation](../docs/getting_started.md)
- [Component Guide](../docs/component_guide.md)
- [API Reference](../docs/api_reference.md)
- [GitHub Repository](https://github.com/XplnHUB/xplnhub-snakeskin)

---

## Support

Need help? Open an issue on GitHub or check the troubleshooting guide.

Happy building! 🐍✨
