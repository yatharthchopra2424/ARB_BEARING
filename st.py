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

# Fixed dimensions based on the provided values
width = 1300
height = 750
total_width = 1400
total_height = 1000  # Adjusted for nav-tab (44px), padding-top (20px), and margin-top (-5px)

# Top Navigation Bar (nav-tab) Configuration Variables
nav_width = 1300  # Width of the navigation bar in pixels
nav_height = 44   # Height of the navigation bar in pixels
nav_background_color = "rgba(0, 32, 84, 0.92)"  # Dark blue with transparency
nav_glow_color = "rgba(65, 137, 255, 0.7)"     # Blue glow effect color
nav_shadow = "0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24)"  # Box shadow
nav_padding = "8px 16px"  # Padding inside the nav bar
nav_border_radius = "4px 4px 0 0"  # Rounded corners (top only)
nav_blur = "8px"  # Backdrop blur effect

# Logo Configuration
logo_height = 26  # Height of the logo in pixels
logo_margin_right = 12  # Margin between logo and title in pixels

# Title Configuration
title_font_size = 16  # Font size of the title in pixels
title_font_weight = 500  # Font weight of the title
title_color = "white"  # Text color of the title
title_text_shadow = "0 0 10px rgba(65, 137, 255, 0.8)"  # Text shadow effect

# Scatter Particle Configuration
particle_count_nav = 5  # Number of scatter particles in nav
particle_size = 4  # Size of particles in pixels
particle_color = "rgba(65, 137, 255, 0.6)"  # Particle color
particle_blur = "1px"  # Blur effect on particles

# Control Panel Position Configuration
control_panel_right = 300  # Distance from right edge in pixels
control_panel_bottom = 200  # Distance from bottom edge in pixels

# Add a loading state
with st.spinner("Loading ARB Bearing Dashboard..."):
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
    
    html, body {{
        width: {total_width}px;
        height: {total_height}px;
        margin: 0 auto;
        font-family: 'Segoe UI', Arial, sans-serif;
        background: transparent;
        overflow: hidden;
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
    
    .css-1d391kg {{
        visibility: hidden;
        width: 0;
    }}
    
    .main .block-container {{
        padding: 0 !important;
        max-width: 100% !important;
    }}
    
    .dashboard-container {{
        width: {total_width}px;
        height: {total_height}px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-start;
        padding-top: 20px;
        background: transparent;
        position: relative;
        overflow: hidden;
    }}
    
    .nav-tab-container {{
        position: relative;
        width: {nav_width}px;
        z-index: 1000;
    }}
    
    .nav-edge-lighting {{
        position: absolute;
        top: -5px;
        left: -5px;
        width: calc(100% + 10px);
        height: calc(100% + 10px);
        border-radius: {nav_border_radius};
        z-index: 0;
        pointer-events: none;
    }}
    
    .nav-glow-effect {{
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: transparent;
        border: 5px solid {nav_glow_color};
        border-radius: {nav_border_radius};
        box-shadow: 
            0 0 35px 8px rgba(65, 137, 255, 0.5),
            inset 0 0 18px rgba(65, 137, 255, 0.4);
        animation: breathe 8s infinite ease-in-out;
    }}
    
    .nav-scatter-container {{
        position: absolute;
        top: -10px;
        left: -10px;
        width: calc(100% + 20px);
        height: calc(100% + 10px);
        pointer-events: none;
        z-index: 0;
    }}
    
    .nav-scatter-particle {{
        position: absolute;
        width: {particle_size}px;
        height: {particle_size}px;
        border-radius: 50%;
        background-color: {particle_color};
        filter: blur({particle_blur});
        animation: float 5s infinite ease-out;
    }}
    
    .nav-scatter-particle:nth-child(1) {{ top: -10px; left: 10%; animation-delay: 0.1s; }}
    .nav-scatter-particle:nth-child(2) {{ top: -8px; left: 30%; animation-delay: 0.5s; }}
    .nav-scatter-particle:nth-child(3) {{ top: -12px; left: 50%; animation-delay: 0.9s; }}
    .nav-scatter-particle:nth-child(4) {{ top: -9px; left: 70%; animation-delay: 1.3s; }}
    .nav-scatter-particle:nth-child(5) {{ top: -11px; left: 90%; animation-delay: 1.7s; }}
    
    .nav-tab {{
        width: 100%;
        background-color: {nav_background_color};
        padding: {nav_padding};
        display: flex;
        align-items: center;
        justify-content: space-between;
        box-shadow: {nav_shadow};
        backdrop-filter: blur({nav_blur});
        -webkit-backdrop-filter: blur({nav_blur});
        border-radius: {nav_border_radius};
        height: {nav_height}px;
        position: relative;
        z-index: 1;
    }}
    
    .nav-brand {{
        display: flex;
        align-items: center;
        height: 100%;
    }}
    
    .nav-logo {{
        height: {logo_height}px;
        margin-right: {logo_margin_right}px;
        vertical-align: middle;
        transition: transform 0.3s ease, filter 0.3s ease;
    }}
    
    .nav-logo:hover {{
        transform: scale(1.05);
        filter: drop-shadow(0 0 5px rgba(65, 137, 255, 0.7));
    }}
    
    .nav-title {{
        font-family: 'Segoe UI', 'Helvetica Neue', sans-serif;
        font-size: {title_font_size}px;
        font-weight: {title_font_weight};
        color: {title_color};
        letter-spacing: 0.3px;
        text-shadow: {title_text_shadow};
    }}
    
    .power-bi-container {{
        width: {width}px;
        height: {height}px;
        position: relative;
        margin-top: -5px;
        overflow: visible; /* Allow glow to extend beyond container */
        z-index: 10;
    }}
    
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
        z-index: 1001;
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
    
    .power-bi-frame {{
        border: none;
        border-radius: 0 0 4px 4px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1), 0 1px 3px rgba(0, 0, 0, 0.08);
        width: {width}px;
        height: {height}px;
        background: transparent;
        position: relative;
        z-index: 1; /* Above glow effect */
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }}

    .power-bi-frame:hover {{
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15), 0 3px 6px rgba(0, 0, 0, 0.1);
    }}

    /* Hide Power BI navigation and filter panes */
    .power-bi-frame + div,
    .power-bi-frame ~ div[class*="report-navigation"],
    .power-bi-frame ~ div[class*="page-navigation"],
    div[class*="filter-pane"],
    div[class*="filters-container"],
    div[role="complementary"],
    div[aria-label*="Filters"] {{
        display: none !important;
    }}

    .edge-lighting {{
        position: absolute;
        top: -5px;
        left: -5px;
        width: calc(100% + 10px);
        height: calc(100% + 10px);
        border-radius: 0 0 5px 5px;
        z-index: 0;
        pointer-events: none;
    }}
    
    .glow-effect {{
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: transparent;
        border: 5px solid rgba(65, 137, 255, 0.7); /* Matching nav glow */
        border-radius: 0 0 5px 5px;
        box-shadow: 
            0 0 35px 8px rgba(65, 137, 255, 0.5), /* Matching nav glow */
            inset 0 0 18px rgba(65, 137, 255, 0.4); /* Matching nav glow */
        animation: breathe 8s infinite ease-in-out; /* Matching nav glow */
        z-index: 0;
    }}
    
    .scatter-container {{
        position: absolute;
        top: -10px;
        left: -10px;
        width: calc(100% + 20px);
        height: calc(100% + 20px);
        pointer-events: none;
        z-index: 0;
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

    @keyframes float {{
        0% {{ opacity: 0; transform: translate(0, 0) scale(0.8); }}
        20% {{ opacity: 0.8; transform: translate(calc(var(--direction-x, -1) * 6px), calc(var(--direction-y, -1) * 6px)) scale(1.2); }}
        100% {{ opacity: 0; transform: translate(calc(var(--direction-x, -1) * 12px), calc(var(--direction-y, -1) * 12px)) scale(0.8); }}
    }}

    @keyframes breathe {{
        0% {{ opacity: 0.3; border-color: rgba(65, 137, 255, 0.4); box-shadow: 0 0 15px 3px rgba(65, 137, 255, 0.3), inset 0 0 8px rgba(65, 137, 255, 0.2); }}
        50% {{ opacity: 1; border-color: rgba(65, 137, 255, 0.8); box-shadow: 0 0 40px 10px rgba(65, 137, 255, 0.6), inset 0 0 20px rgba(65, 137, 255, 0.5); }}
        100% {{ opacity: 0.3; border-color: rgba(65, 137, 255, 0.4); box-shadow: 0 0 15px 3px rgba(65, 137, 255, 0.3), inset 0 0 8px rgba(65, 137, 255, 0.2); }}
    }}

    .control-panel {{
        position: fixed;
        right: {control_panel_right}px;
        bottom: {control_panel_bottom}px;
        display: flex;
        gap: 10px;
        z-index: 1002;
        opacity: 0.7;
        transition: opacity 0.3s ease;
        pointer-events: auto;
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

    @media (max-width: 1400px) {{
        .dashboard-container {{ transform: scale(0.9); transform-origin: top center; }}
    }}

    @media (max-width: 1200px) {{
        .dashboard-container {{ transform: scale(0.8); transform-origin: top center; }}
    }}

    @media (max-width: 992px) {{
        .dashboard-container {{ transform: scale(0.7); transform-origin: top center; }}
    }}

    @media (max-width: 768px) {{
        .dashboard-container {{ transform: scale(0.6); transform-origin: top center; }}
    }}

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
        z-index: 1003;
        display: none;
    }}

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
        z-index: 1004;
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
                {' '.join(['<div class="nav-scatter-particle"></div>' for _ in range(particle_count_nav)])}
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
        
        <div class="loading-container" id="loadingOverlay">
            <div class="loading-spinner"></div>
            <div class="loading-text">Loading dashboard data...</div>
        </div>
        
        <div class="error-message" id="errorMessage">
            Failed to load the dashboard. Please check your connection and try again.
        </div>
        
        <iframe 
            class="power-bi-frame"
            id="powerBiFrame"
            title="5 Years Analysis" 
            width="{width}" 
            height="{height}" 
            src="https://app.powerbi.com/reportEmbed?reportId=d364d848-ed99-4175-9fec-dedc6ca1cb09&autoAuth=true&ctid=c393e2ef-9c24-4bfc-bf28-c48ac7208f2e&navContentPaneEnabled=false&filterPaneEnabled=false" 
            frameborder="0" 
            allowFullScreen="true"
            onload="document.getElementById('loadingOverlay').style.opacity = 0; setTimeout(() => document.getElementById('loadingOverlay').style.display = 'none', 500);"
            onerror="document.getElementById('errorMessage').style.display = 'block'; document.getElementById('loadingOverlay').style.display = 'none';">
        </iframe>
    </div>

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

<script>
    function refreshReport() {{
        document.getElementById('loadingOverlay').style.display = 'flex';
        document.getElementById('loadingOverlay').style.opacity = 1;
        const iframe = document.getElementById('powerBiFrame');
        const src = iframe.src;
        iframe.src = '';
        setTimeout(() => {{ iframe.src = src; }}, 300);
    }}
    
    function toggleFullscreen() {{
        const iframe = document.getElementById('powerBiFrame');
        if (!document.fullscreenElement) {{
            if (iframe.requestFullscreen) {{ iframe.requestFullscreen(); }}
            else if (iframe.mozRequestFullScreen) {{ iframe.mozRequestFullScreen(); }}
            else if (iframe.webkitRequestFullscreen) {{ iframe.webkitRequestFullscreen(); }}
            else if (iframe.msRequestFullscreen) {{ iframe.msRequestFullscreen(); }}
        }} else {{
            if (document.exitFullscreen) {{ document.exitFullscreen(); }}
            else if (document.mozCancelFullScreen) {{ document.mozCancelFullScreen(); }}
            else if (document.webkitExitFullscreen) {{ document.webkitExitFullscreen(); }}
            else if (document.msExitFullscreen) {{ document.msExitFullscreen(); }}
        }}
    }}
    
    window.addEventListener('error', function(e) {{
        if (e.target.tagName === 'IFRAME') {{
            document.getElementById('errorMessage').style.display = 'block';
            document.getElementById('loadingOverlay').style.display = 'none';
        }}
    }}, true);
</script>
"""

# Display the report
html(iframe_code, height=total_height, scrolling=False)
