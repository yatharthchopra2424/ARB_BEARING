import streamlit as st
from streamlit.components.v1 import html
import time

# Page configuration
st.set_page_config(
    page_title="ARB BEARING - Power BI Report Viewer",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items=None
)

# Fixed dimensions based on the provided iframe
width = 1140
height = 541.25

# Add a loading state
with st.spinner("Loading ARB Bearing Dashboard..."):
    # Simulate loading for better UX
    time.sleep(0.5)

# Generate iframe HTML with updated styling
iframe_code = f"""
<style>
    /* Reset and base styles */
    * {{
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }}
    
    body {{
        font-family: 'Segoe UI', Arial, sans-serif;
        background: transparent;
    }}

    /* Hide Streamlit elements */
    #MainMenu {{visibility: hidden;}}
    header {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    .block-container {{
        padding: 0 !important;
        max-width: 100% !important;
        margin-top: 0 !important;
    }}
    
    /* Remove sidebar and adjust main content */
    .css-1d391kg {{
        visibility: hidden;
        width: 0;
    }}
    
    .main .block-container {{
        padding: 0 !important;
        max-width: 100% !important;
    }}
    
    /* Main container to center content */
    .dashboard-container {{
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-start;
        padding-top: 20px;
        background: transparent;
        position: relative;
    }}
    
    /* Navigation Tab Styling - DARK BLUE with matching glow */
    .nav-tab-container {{
        position: relative;
        width: {width}px;
        z-index: 1000;
    }}
    
    /* Edge lighting for nav tab */
    .nav-edge-lighting {{
        position: absolute;
        top: -5px;
        left: -5px;
        width: calc(100% + 10px);
        height: calc(100% + 10px);
        border-radius: 4px 4px 0 0;
        z-index: 0;
        overflow: visible;
        pointer-events: none;
    }}
    
    /* Nav tab glow effect */
    .nav-glow-effect {{
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: transparent;
        border: 5px solid rgba(65, 137, 255, 0.7);
        border-radius: 4px 4px 0 0;
        box-shadow: 
            0 0 35px 8px rgba(65, 137, 255, 0.5),
            inset 0 0 18px rgba(65, 137, 255, 0.4);
        animation: breathe 8s infinite ease-in-out;
    }}
    
    /* Nav scatter particles - NEW */
    .nav-scatter-container {{
        position: absolute;
        top: -10px;
        left: -10px;
        width: calc(100% + 20px);
        height: calc(100% + 10px);
        pointer-events: none;
        overflow: visible;
        z-index: 0;
    }}
    
    .nav-scatter-particle {{
        position: absolute;
        width: 4px;
        height: 4px;
        border-radius: 50%;
        background-color: rgba(65, 137, 255, 0.6);
        filter: blur(1px);
        animation: float 5s infinite ease-out;
    }}
    
    .nav-scatter-particle:nth-child(1) {{ top: -10px; left: 10%; animation-delay: 0.1s; }}
    .nav-scatter-particle:nth-child(2) {{ top: -8px; left: 30%; animation-delay: 0.5s; }}
    .nav-scatter-particle:nth-child(3) {{ top: -12px; left: 50%; animation-delay: 0.9s; }}
    .nav-scatter-particle:nth-child(4) {{ top: -9px; left: 70%; animation-delay: 1.3s; }}
    .nav-scatter-particle:nth-child(5) {{ top: -11px; left: 90%; animation-delay: 1.7s; }}
    
    .nav-tab {{
        width: 100%;
        background-color: rgba(0, 32, 84, 0.92);
        padding: 8px 16px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
        border-radius: 4px 4px 0 0;
        height: 44px;
        position: relative;
        z-index: 1;
    }}
    
    /* Brand Section with Logo and Title */
    .nav-brand {{
        display: flex;
        align-items: center;
        height: 100%;
    }}
    
    .nav-logo {{
        height: 26px;
        margin-right: 12px;
        vertical-align: middle;
        transition: transform 0.3s ease, filter 0.3s ease;
    }}
    
    .nav-logo:hover {{
        transform: scale(1.05);
        filter: drop-shadow(0 0 5px rgba(65, 137, 255, 0.7));
    }}
    
    .nav-title {{
        font-family: 'Segoe UI', 'Helvetica Neue', sans-serif;
        font-size: 16px;
        font-weight: 500;
        color: white;
        letter-spacing: 0.3px;
        text-shadow: 0 0 10px rgba(65, 137, 255, 0.8);
    }}
    
    /* Navigation Menu */
    .nav-menu {{
        display: flex;
        align-items: center;
        gap: 15px;
    }}
    
    .nav-menu-item {{
        color: rgba(255, 255, 255, 0.85);
        font-size: 14px;
        cursor: pointer;
        transition: all 0.2s ease;
        padding: 4px 8px;
        border-radius: 4px;
        text-shadow: 0 0 8px rgba(65, 137, 255, 0.6);
        position: relative;
        overflow: hidden;
    }}
    
    /* NEW: Ripple effect on menu click */
    .nav-menu-item::after {{
        content: '';
        position: absolute;
        top: 50%;
        left: 50%;
        width: 5px;
        height: 5px;
        background: rgba(255, 255, 255, 0.7);
        opacity: 0;
        border-radius: 100%;
        transform: scale(1, 1) translate(-50%, -50%);
        transform-origin: 50% 50%;
    }}
    
    .nav-menu-item:focus:not(:active)::after {{
        animation: ripple 0.8s ease-out;
    }}
    
    @keyframes ripple {{
        0% {{ opacity: 1; transform: scale(0, 0); }}
        20% {{ transform: scale(8, 8); }}
        100% {{ opacity: 0; transform: scale(15, 15); }}
    }}
    
    .nav-menu-item:hover {{
        color: white;
        background-color: rgba(65, 137, 255, 0.2);
        box-shadow: 0 0 10px rgba(65, 137, 255, 0.3);
    }}
    
    .nav-menu-item.active {{
        color: white;
        background-color: rgba(65, 137, 255, 0.3);
        box-shadow: 0 0 15px rgba(65, 137, 255, 0.4);
    }}
    
    /* Power BI container styling */
    .power-bi-container {{
        width: {width}px;
        display: flex;
        flex-direction: column;
        align-items: center;
        background: transparent;
        position: relative;
        margin-top: -5px;
    }}
    
    /* Loading animation */
    .loading-container {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        background-color: rgba(0, 32, 84, 0.9);
        z-index: 5;
        border-radius: 0 0 4px 4px;
        transition: opacity 0.5s ease-out;
    }}
    
    .loading-spinner {{
        width: 60px;
        height: 60px;
        margin-bottom: 20px;
        border: 5px solid rgba(65, 137, 255, 0.3);
        border-radius: 50%;
        border-top-color: rgba(65, 137, 255, 0.9);
        animation: spin 1s linear infinite;
    }}
    
    .loading-text {{
        color: white;
        font-size: 16px;
        text-align: center;
        text-shadow: 0 0 10px rgba(65, 137, 255, 0.8);
    }}
    
    @keyframes spin {{
        0% {{ transform: rotate(0deg); }}
        100% {{ transform: rotate(360deg); }}
    }}
    
    /* Power BI frame styling */
    .power-bi-frame {{
        border: none;
        border-radius: 0 0 4px 4px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1), 0 1px 3px rgba(0, 0, 0, 0.08);
        width: {width}px;
        height: {height}px;
        background: transparent;
        position: relative;
        z-index: 1;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }}

    /* Hover effect for the frame */
    .power-bi-frame:hover {{
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15), 0 3px 6px rgba(0, 0, 0, 0.1);
    }}

    /* Edge lighting container */
    .edge-lighting {{
        position: absolute;
        top: -5px;
        left: -5px;
        width: calc(100% + 10px);
        height: calc(100% + 10px);
        border-radius: 0 0 5px 5px;
        z-index: 0;
        overflow: visible;
        pointer-events: none;
    }}
    
    /* Glowing effect */
    .glow-effect {{
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: transparent;
        border: 5px solid rgba(65, 137, 255, 0.7);
        border-radius: 0 0 5px 5px;
        box-shadow: 
            0 0 35px 8px rgba(65, 137, 255, 0.5),
            inset 0 0 18px rgba(65, 137, 255, 0.4);
        animation: breathe 8s infinite ease-in-out;
    }}
    
    /* Light scatter particles */
    .scatter-container {{
        position: absolute;
        top: -10px;
        left: -10px;
        width: calc(100% + 20px);
        height: calc(100% + 20px);
        pointer-events: none;
        overflow: visible;
    }}
    
    .scatter-particle {{
        position: absolute;
        width: 4px;
        height: 4px;
        border-radius: 50%;
        background-color: rgba(65, 137, 255, 0.6);
        filter: blur(1px);
        animation: float 5s infinite ease-out;
    }}
    
    /* Position particles around edges */
    .scatter-particle:nth-child(1) {{ top: 10%; left: -10px; animation-delay: 0s; }}
    .scatter-particle:nth-child(2) {{ top: 30%; left: -8px; animation-delay: 0.4s; }}
    .scatter-particle:nth-child(3) {{ top: 50%; left: -12px; animation-delay: 0.8s; }}
    .scatter-particle:nth-child(4) {{ top: 70%; left: -9px; animation-delay: 1.2s; }}
    .scatter-particle:nth-child(5) {{ top: 90%; left: -11px; animation-delay: 1.6s; }}
    
    .scatter-particle:nth-child(6) {{ bottom: -10px; left: 20%; animation-delay: 0.2s; }}
    .scatter-particle:nth-child(7) {{ bottom: -12px; left: 40%; animation-delay: 0.6s; }}
    .scatter-particle:nth-child(8) {{ bottom: -8px; left: 60%; animation-delay: 1s; }}
    .scatter-particle:nth-child(9) {{ bottom: -10px; left: 80%; animation-delay: 1.4s; }}
    
    .scatter-particle:nth-child(10) {{ top: 15%; right: -10px; animation-delay: 0.3s; }}
    .scatter-particle:nth-child(11) {{ top: 35%; right: -8px; animation-delay: 0.7s; }}
    .scatter-particle:nth-child(12) {{ top: 55%; right: -12px; animation-delay: 1.1s; }}
    .scatter-particle:nth-child(13) {{ top: 75%; right: -9px; animation-delay: 1.5s; }}
    
    .scatter-particle:nth-child(14) {{ top: -10px; left: 10%; animation-delay: 0.1s; }}
    .scatter-particle:nth-child(15) {{ top: -8px; left: 30%; animation-delay: 0.5s; }}
    .scatter-particle:nth-child(16) {{ top: -12px; left: 50%; animation-delay: 0.9s; }}
    .scatter-particle:nth-child(17) {{ top: -9px; left: 70%; animation-delay: 1.3s; }}
    .scatter-particle:nth-child(18) {{ top: -11px; left: 90%; animation-delay: 1.7s; }}

    /* Particle floating animation */
    @keyframes float {{
        0% {{
            opacity: 0;
            transform: translate(0, 0) scale(0.8);
        }}
        20% {{
            opacity: 0.8;
            transform: translate(calc(var(--direction-x, -1) * 6px), calc(var(--direction-y, -1) * 6px)) scale(1.2);
        }}
        100% {{
            opacity: 0;
            transform: translate(calc(var(--direction-x, -1) * 12px), calc(var(--direction-y, -1) * 12px)) scale(0.8);
        }}
    }}

    /* Enhanced breathing animation keyframes with fade-out effect */
    @keyframes breathe {{
        0% {{ 
            opacity: 0.3;
            border-color: rgba(65, 137, 255, 0.4);
            box-shadow: 
                0 0 15px 3px rgba(65, 137, 255, 0.3),
                inset 0 0 8px rgba(65, 137, 255, 0.2);
        }}
        25% {{ 
            opacity: 0.7;
            border-color: rgba(65, 137, 255, 0.6);
            box-shadow: 
                0 0 25px 6px rgba(65, 137, 255, 0.5),
                inset 0 0 12px rgba(65, 137, 255, 0.3);
        }}
        50% {{ 
            opacity: 1;
            border-color: rgba(65, 137, 255, 0.8);
            box-shadow: 
                0 0 40px 10px rgba(65, 137, 255, 0.6),
                inset 0 0 20px rgba(65, 137, 255, 0.5);
        }}
        75% {{ 
            opacity: 0.7;
            border-color: rgba(65, 137, 255, 0.6);
            box-shadow: 
                0 0 25px 6px rgba(65, 137, 255, 0.5),
                inset 0 0 12px rgba(65, 137, 255, 0.3);
        }}
        100% {{ 
            opacity: 0.3;
            border-color: rgba(65, 137, 255, 0.4);
            box-shadow: 
                0 0 15px 3px rgba(65, 137, 255, 0.3),
                inset 0 0 8px rgba(65, 137, 255, 0.2);
        }}
    }}
    
    /* Fullscreen view mode */
    .control-panel {{
        position: absolute;
        right: 10px;
        bottom: 10px;
        display: flex;
        gap: 5px;
        z-index: 10;
        opacity: 0.7;
        transition: opacity 0.3s ease;
    }}
    
    .control-panel:hover {{
        opacity: 1;
    }}
    
    .control-button {{
        background-color: rgba(0, 32, 84, 0.7);
        color: white;
        border: none;
        border-radius: 4px;
        padding: 5px 10px;
        font-size: 12px;
        cursor: pointer;
        transition: all 0.2s ease;
        display: flex;
        align-items: center;
        gap: 5px;
    }}
    
    .control-button:hover {{
        background-color: rgba(65, 137, 255, 0.8);
    }}
    
    .fullscreen-icon {{
        width: 12px;
        height: 12px;
        border: 1px solid white;
        position: relative;
    }}
    
    /* NEW: Refresh button icon */
    .refresh-icon {{
        width: 12px;
        height: 12px;
        position: relative;
        border: 1px solid transparent;
    }}
    
    .refresh-icon::before {{
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 8px;
        height: 8px;
        border: 1px solid white;
        border-bottom-color: transparent;
        border-left-color: transparent;
        border-radius: 50%;
    }}
    
    .refresh-icon::after {{
        content: '';
        position: absolute;
        top: 4px;
        right: 0;
        width: 0;
        height: 0;
        border-style: solid;
        border-width: 3px 0 0 3px;
        border-color: white transparent transparent white;
        transform: rotate(45deg);
    }}
    
    /* Media queries for responsiveness */
    @media (max-width: 1200px) {{
        .dashboard-container {{
            transform: scale(0.9);
            transform-origin: top center;
        }}
    }}
    
    @media (max-width: 992px) {{
        .dashboard-container {{
            transform: scale(0.8);
            transform-origin: top center;
        }}
    }}
    
    @media (max-width: 768px) {{
        .dashboard-container {{
            transform: scale(0.7);
            transform-origin: top center;
        }}
        .nav-menu-item {{
            font-size: 12px;
            padding: 3px 6px;
        }}
    }}
    
    /* Error message styling */
    .error-message {{
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background-color: rgba(220, 53, 69, 0.9);
        color: white;
        padding: 20px;
        border-radius: 8px;
        text-align: center;
        max-width: 80%;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
        z-index: 10;
        display: none;
    }}
    
    /* NEW: Tooltip styling */
    .tooltip {{
        position: relative;
    }}
    
    .tooltip .tooltip-text {{
        visibility: hidden;
        width: 120px;
        background-color: rgba(0, 32, 84, 0.9);
        color: white;
        text-align: center;
        border-radius: 4px;
        padding: 5px;
        position: absolute;
        z-index: 1;
        bottom: 125%;
        left: 50%;
        transform: translateX(-50%);
        opacity: 0;
        transition: opacity 0.3s;
        font-size: 11px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    }}
    
    .tooltip .tooltip-text::after {{
        content: "";
        position: absolute;
        top: 100%;
        left: 50%;
        margin-left: -5px;
        border-width: 5px;
        border-style: solid;
        border-color: rgba(0, 32, 84, 0.9) transparent transparent transparent;
    }}
    
    .tooltip:hover .tooltip-text {{
        visibility: visible;
        opacity: 1;
    }}
</style>

<div class="dashboard-container">
    <div class="nav-tab-container">
        <div class="nav-edge-lighting">
            <div class="nav-glow-effect"></div>
            <div class="nav-scatter-container">
                <div class="nav-scatter-particle"></div>
                <div class="nav-scatter-particle"></div>
                <div class="nav-scatter-particle"></div>
                <div class="nav-scatter-particle"></div>
                <div class="nav-scatter-particle"></div>
            </div>
        </div>
        <div class="nav-tab">
            <div class="nav-brand">
                <img src="https://arb-easternbearings.com/wp-content/uploads/2021/08/arb-bearings-logo-300x192-1.jpg" alt="ARB Logo" class="nav-logo">
                <span class="nav-title">ARB Bearing Dashboard</span>
            </div>

        </div>
    </div>

    <div class="power-bi-container">
        <div class="edge-lighting">
            <div class="glow-effect"></div>
            <div class="scatter-container">
                <div class="scatter-particle" style="--direction-x: -1; --direction-y: -1;"></div>
                <div class="scatter-particle" style="--direction-x: -1; --direction-y: -1;"></div>
                <div class="scatter-particle" style="--direction-x: -1; --direction-y: -1;"></div>
                <div class="scatter-particle" style="--direction-x: -1; --direction-y: -1;"></div>
                <div class="scatter-particle" style="--direction-x: -1; --direction-y: -1;"></div>
                <div class="scatter-particle" style="--direction-x: 0; --direction-y: 1;"></div>
                <div class="scatter-particle" style="--direction-x: 0; --direction-y: 1;"></div>
                <div class="scatter-particle" style="--direction-x: 0; --direction-y: 1;"></div>
                <div class="scatter-particle" style="--direction-x: 0; --direction-y: 1;"></div>
                <div class="scatter-particle" style="--direction-x: 1; --direction-y: -1;"></div>
                <div class="scatter-particle" style="--direction-x: 1; --direction-y: -1;"></div>
                <div class="scatter-particle" style="--direction-x: 1; --direction-y: -1;"></div>
                <div class="scatter-particle" style="--direction-x: 1; --direction-y: -1;"></div>
                <div class="scatter-particle" style="--direction-x: 0; --direction-y: -1;"></div>
                <div class="scatter-particle" style="--direction-x: 0; --direction-y: -1;"></div>
                <div class="scatter-particle" style="--direction-x: 0; --direction-y: -1;"></div>
                <div class="scatter-particle" style="--direction-x: 0; --direction-y: -1;"></div>
                <div class="scatter-particle" style="--direction-x: 0; --direction-y: -1;"></div>
            </div>
        </div>
        
        <!-- Loading spinner overlay -->
        <div class="loading-container" id="loadingOverlay">
            <div class="loading-spinner"></div>
            <div class="loading-text">Loading dashboard data...</div>
        </div>
        
        <!-- Error message -->
        <div class="error-message" id="errorMessage">
            Failed to load the dashboard. Please check your connection and try again.
        </div>
        
        <iframe 
            class="power-bi-frame"
            id="powerBiFrame"
            title="5 Years Analysis" 
            width="{width}" 
            height="{height}" 
            src="https://app.powerbi.com/reportEmbed?reportId=dc8ab23e-fe0c-4032-9069-da6948bbf75d&autoAuth=true&ctid=c393e2ef-9c24-4bfc-bf28-c48ac7208f2e" 
            frameborder="0" 
            allowFullScreen="true"
            onload="document.getElementById('loadingOverlay').style.opacity = 0; setTimeout(() => document.getElementById('loadingOverlay').style.display = 'none', 500);"
            onerror="document.getElementById('errorMessage').style.display = 'block'; document.getElementById('loadingOverlay').style.display = 'none';">
        </iframe>
        
        <div class="control-panel">
            <button class="control-button tooltip" onclick="refreshReport()">
                <div class="refresh-icon"></div>
                <span>Refresh</span>
                <span class="tooltip-text">Reload the latest data</span>
            </button>
            
            <button class="control-button tooltip" onclick="toggleFullscreen()">
                <div class="fullscreen-icon"></div>
                <span>Fullscreen</span>
                <span class="tooltip-text">View in fullscreen mode</span>
            </button>
        </div>
    </div>
</div>

<script>
    // Handle menu navigation
    document.querySelectorAll('.nav-menu-item').forEach(item => {{
        item.addEventListener('click', function() {{
            // Remove active class from all menu items
            document.querySelectorAll('.nav-menu-item').forEach(menuItem => {{
                menuItem.classList.remove('active');
            }});
            
            // Add active class to clicked item
            this.classList.add('active');
            
            // You could add page navigation here in a full implementation
            // For now, just show a loading effect
            document.getElementById('loadingOverlay').style.display = 'flex';
            document.getElementById('loadingOverlay').style.opacity = 1;
            
            // Hide loading after 1 second (simulating page change)
            setTimeout(() => {{
                document.getElementById('loadingOverlay').style.opacity = 0;
                setTimeout(() => document.getElementById('loadingOverlay').style.display = 'none', 500);
            }}, 1000);
        }});
    }});
    
    // NEW: Refresh report functionality
    function refreshReport() {{
        document.getElementById('loadingOverlay').style.display = 'flex';
        document.getElementById('loadingOverlay').style.opacity = 1;
        
        // Reload the iframe
        const iframe = document.getElementById('powerBiFrame');
        const src = iframe.src;
        iframe.src = '';
        
        setTimeout(() => {{
            iframe.src = src;
        }}, 300);
    }}
    
    // Fullscreen functionality
    function toggleFullscreen() {{
        const iframe = document.getElementById('powerBiFrame');
        
        if (!document.fullscreenElement) {{
            if (iframe.requestFullscreen) {{
                iframe.requestFullscreen();
            }} else if (iframe.mozRequestFullScreen) {{ /* Firefox */
                iframe.mozRequestFullScreen();
            }} else if (iframe.webkitRequestFullscreen) {{ /* Chrome, Safari & Opera */
                iframe.webkitRequestFullscreen();
            }} else if (iframe.msRequestFullscreen) {{ /* IE/Edge */
                iframe.msRequestFullscreen();
            }}
        }} else {{
            if (document.exitFullscreen) {{
                document.exitFullscreen();
            }} else if (document.mozCancelFullScreen) {{
                document.mozCancelFullScreen();
            }} else if (document.webkitExitFullscreen) {{
                document.webkitExitFullscreen();
            }} else if (document.msExitFullscreen) {{
                document.msExitFullscreen();
            }}
        }}
    }}
    
    // Error handling
    window.addEventListener('error', function(e) {{
        // Only show error message if it's related to the iframe
        if (e.target.tagName === 'IFRAME') {{
            document.getElementById('errorMessage').style.display = 'block';
            document.getElementById('loadingOverlay').style.display = 'none';
        }}
    }}, true);
</script>
"""

# Display the report
html(iframe_code, height=700, scrolling=False)