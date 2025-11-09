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
