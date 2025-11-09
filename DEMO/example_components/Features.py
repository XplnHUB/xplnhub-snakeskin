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
