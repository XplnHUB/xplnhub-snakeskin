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
                    <p>&copy; 2025 Snakeskin via XplnHUB. Built with 🐍 and ❤️</p>
                </div>
            </div>
        </footer>
        """
