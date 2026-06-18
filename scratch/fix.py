import codecs

with codecs.open('d:/groww/room/admin_dashboard.html', 'r', 'utf-8') as f:
    lines = f.readlines()

new_lines = []
skip = False
for i, line in enumerate(lines):
    if '<div class="nav-section">' in line and i+1 < len(lines) and '<div class="nav-title">Finance & Reporting</div>' in lines[i+1]:
        new_lines.append("""    <div class="nav-section">
      <div class="nav-title">Finance & Reporting</div>
      <ul class="nav-list">
        <li class="nav-item"><a href="#" class="nav-link" data-target="payment-mgmt"><i class="fas fa-credit-card"></i> Payments</a></li>
        <li class="nav-item"><a href="#" class="nav-link" data-target="revenue-reports"><i class="fas fa-chart-pie"></i> Revenue Reports</a></li>
      </ul>
    </div>

    <div class="nav-section">
      <div class="nav-title">System</div>
      <ul class="nav-list">
        <li class="nav-item"><a href="#" class="nav-link" data-target="notifications"><i class="fas fa-bell"></i> Notifications</a></li>
        <li class="nav-item"><a href="#" class="nav-link" data-target="settings"><i class="fas fa-cog"></i> Settings</a></li>
      </ul>
    </div>
  </aside>

  <!-- MAIN WRAPPER -->
  <div class="main-wrapper">
    <!-- Top Bar -->
    <header class="topbar">
      <!-- Navbar Logo -->
      <a href="index.html" class="navbar-logo" style="display: flex; align-items: center; gap: 10px; text-decoration: none;">
        <i class="fas fa-cube" style="color: #6366f1; font-size: 1.8rem; filter: drop-shadow(0 0 8px #6366f1);"></i>
        <span style="font-weight: 800; font-size: 1.5rem; background: linear-gradient(90deg, #6366f1, #9d00ff); -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-transform: uppercase;">NEXUS</span>
      </a>

      <div style="flex: 1;"></div>
      <div class="user-actions">
        <!-- Theme & RTL Buttons -->
        <button class="action-btn icon-btn" id="theme-toggle" title="Toggle Theme" style="margin-right: 12px;"><i class="fas fa-sun" id="theme-icon"></i></button>
        <button class="action-btn icon-btn" id="rtl-toggle" title="Toggle RTL" style="margin-right: 12px;"><i class="fas fa-arrows-left-right"></i></button>

        <button class="action-btn icon-btn" onclick="document.querySelector('[data-target=\\'notifications\\']').click()">
          <i class="fas fa-envelope"></i><span class="badge">4</span>
        </button>
        <div class="admin-profile-btn" onclick="document.querySelector('[data-target=\\'admin-profile\\']').click()">
          <span style="font-size: 0.85rem; font-weight: 500;">Admin_Root</span>
          <div class="avatar"><i class="fas fa-crown"></i></div>
        </div>
      </div>
      <button class="mobile-toggle hamburger" id="mobile-toggle" style="margin-inline-start: 1rem;"><i class="fas fa-bars"></i></button>
    </header>

    <!-- CONTENT AREA -->
    <main class="content-area">

      <!-- 1. DASHBOARD OVERVIEW -->
      <section id="dashboard-overview" class="section-panel active">
        <div class="section-header">
          <h1 class="section-title">Dashboard Overview</h1>
          <button class="btn btn-primary"><i class="fas fa-download"></i> Export Daily Log</button>
        </div>
        
        <div class="metric-grid">
""")
        skip = True
        continue
        
    if skip:
        if '<div class="metric-card amber">' in line:
            skip = False
            new_lines.append(line)
        continue
        
    new_lines.append(line)

with codecs.open('d:/groww/room/admin_dashboard.html', 'w', 'utf-8') as f:
    f.writelines(new_lines)
