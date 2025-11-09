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
