__version__ = "1.0.0"

# Core framework components
from .framework import Component

# Integration modules
from .integrations import TailwindIntegration, BootstrapIntegration

# Make key functionality available at package level
__all__ = [
    'Component',
    'TailwindIntegration',
    'BootstrapIntegration',
]