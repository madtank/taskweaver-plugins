# hello_world.py
from taskweaver.plugin import Plugin, register_plugin

@register_plugin
class HelloWorldPlugin(Plugin):
    def __call__(self, name="World"):
        """Simple Hello World plugin implementation."""
        greeting_message = f"Hello, {name}!"
        return greeting_message  # Return only the greeting message
