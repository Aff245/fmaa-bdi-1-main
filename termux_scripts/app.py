#!/usr/bin/env python3
"""
FMAA BDI v1 - Main Application Entry Point
Optimized for Vercel deployment
"""

import os
import sys

# Add the termux_scripts directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'termux_scripts'))

from bdi_master import master_agent

# Export the Flask app for Vercel
app = master_agent.app

if __name__ == '__main__':
    # For local development
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)
