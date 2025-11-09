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
