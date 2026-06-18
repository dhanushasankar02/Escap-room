import re

with open('index.html', 'r', encoding='utf-8') as f:
    indexHtml = f.read()

with open('Contact.html', 'r', encoding='utf-8') as f:
    contactHtml = f.read()

headStart = re.search(r'(<!DOCTYPE html>[\s\S]*?<\/style>)', indexHtml).group(1)

contactCSS = """
    /* Contact Page Specific Styles */
    .main-content-contact { width: 100%; padding-top: 80px; background: var(--bg-color); }
    section { padding: 5rem 2rem; position: relative; }
    .section-container { max-width: 1200px; margin: 0 auto; }
    .text-center { text-align: center; }
    .mx-auto { margin-left: auto; margin-right: auto; }
    .w-100 { width: 100%; }
    .mt-2 { margin-top: 1rem; }
    .section-title { font-size: 2.5rem; font-weight: 700; margin-bottom: 1rem; color: var(--text-primary); }
    .section-desc { color: var(--text-secondary); font-size: 1.1rem; max-width: 700px; margin-bottom: 3rem; line-height: 1.6; }
    .btn-primary, .btn-outline { display: inline-block; padding: 0.8rem 1.8rem; border-radius: 30px; font-weight: 600; text-decoration: none; transition: var(--transition); cursor: pointer; border: none; font-family: inherit; }
    .btn-large { padding: 1rem 2.5rem; font-size: 1.2rem; }
    .btn-primary { background: var(--accent-color); color: #fff; }
    .btn-primary:hover { background: var(--accent-hover); transform: translateY(-3px); }
    .btn-outline { background: transparent; color: var(--text-primary); border: 2px solid var(--accent-color); }
    .btn-outline:hover { background: var(--accent-color); color: #fff; }
    .split-layout { display: flex; align-items: stretch; gap: 3rem; }
    .split-layout.reverse { flex-direction: row-reverse; align-items: center; }
    .split-text { flex: 1; }
    .split-image { flex: 1; border-radius: 20px; overflow: hidden; box-shadow: 0 20px 40px var(--shadow-color); position: relative; }
    .split-image img { width: 100%; height: 100%; object-fit: cover; display: block; }
    .contact-hero { background: linear-gradient(rgba(15, 23, 42, 0.8), rgba(15, 23, 42, 0.95)), url('images/contact_hero.jpg') center/cover; padding: 8rem 2rem 5rem; border-bottom: 1px solid var(--border-color); }
    .hero-icon { font-size: 4rem; color: #38bdf8; margin-bottom: 1.5rem; }
    .hero-main-title { font-size: 3.5rem; font-weight: 800; margin-bottom: 1rem; color: #fff; }
    .hero-main-desc { font-size: 1.2rem; color: #e2e8f0; max-width: 600px; margin: 0 auto 2.5rem; }
    .info-grid-section { background: var(--bg-color); margin-top: -3rem; }
    .contact-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 2rem; max-width: 1000px; margin: 0 auto; position: relative; z-index: 10; }
    .contact-card { background: var(--dropdown-bg); border: 1px solid var(--border-color); border-radius: 15px; padding: 2.5rem 1.5rem; text-align: center; box-shadow: 0 10px 30px var(--shadow-color); transition: transform 0.3s; }
    .contact-card:hover { transform: translateY(-5px); }
    .contact-card i { font-size: 2.5rem; color: var(--accent-color); margin-bottom: 1rem; }
    .contact-card h3 { font-size: 1.2rem; margin-bottom: 0.5rem; color: var(--text-primary); }
    .contact-card p { font-size: 1.1rem; font-weight: bold; color: var(--text-primary); margin-bottom: 0.5rem; }
    .contact-card span { font-size: 0.9rem; color: var(--text-secondary); }

    /* 3. Interactive Map (Fix to be full section) */
    .map-section { background: var(--dropdown-bg); padding-bottom: 0 !important; }
    .map-full-container { position: relative; width: 100%; height: 450px; overflow: hidden; }
    .map-full-container iframe { display: block; position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0; }
    @media (max-width: 991px) { .map-full-container { height: 400px; } }
    @media (max-width: 680px) { .map-full-container { height: 350px; } }

    /* 4. Raven Form */
    .raven-form-section { background: var(--bg-color); }
    .raven-icon { font-size: 5rem; color: #a855f7; margin-top: 2rem; }
    .split-form { flex: 1; background: var(--dropdown-bg); border: 1px solid var(--border-color); border-radius: 15px; padding: 3rem; box-shadow: 0 20px 40px var(--shadow-color); }
    .custom-form .form-group { margin-bottom: 1.5rem; text-align: left; }
    .custom-form label { display: block; margin-bottom: 0.5rem; color: var(--text-primary); font-weight: 500; font-size: 0.95rem; }
    .custom-form input, .custom-form select, .custom-form textarea { width: 100%; padding: 1rem; background: var(--bg-color); border: 1px solid var(--border-color); border-radius: 8px; color: var(--text-primary); font-family: inherit; font-size: 1rem; transition: border-color 0.3s; }
    .custom-form input:focus, .custom-form select:focus, .custom-form textarea:focus { outline: none; border-color: var(--accent-color); }

    /* 5. Event Inquiry */
    .event-inquiry-section { background: var(--dropdown-bg); }

    /* 6. Parking */
    .parking-directions-section { background: var(--bg-color); }
    .parking-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 2rem; margin-top: 2rem; }
    .p-card { background: var(--dropdown-bg); padding: 2rem; border-radius: 15px; border: 1px solid var(--border-color); }
    .p-card i { font-size: 2.5rem; color: #f59e0b; margin-bottom: 1rem; }
    .p-card h4 { font-size: 1.2rem; color: var(--text-primary); margin-bottom: 0.5rem; }
    .p-card p { color: var(--text-secondary); font-size: 0.95rem; line-height: 1.5; }

    /* 7. Social Hub */
    .social-hub-section { background: linear-gradient(135deg, #1e1b4b 0%, #0f172a 100%); }
    .social-hub-section .section-title, .social-hub-section .section-desc { color: #fff; }
    .social-links-big { display: flex; justify-content: center; gap: 2rem; margin-top: 2rem; }
    .s-link { width: 80px; height: 80px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 2.5rem; color: #fff; background: rgba(255, 255, 255, 0.1); transition: all 0.3s; text-decoration: none; }
    .s-link:hover { transform: translateY(-10px); }
    .s-link.ig:hover { background: #e1306c; box-shadow: 0 10px 20px rgba(225, 48, 108, 0.4); }
    .s-link.tt:hover { background: #00f2fe; box-shadow: 0 10px 20px rgba(0, 242, 254, 0.4); color: #000; }
    .s-link.fb:hover { background: #1877f2; box-shadow: 0 10px 20px rgba(24, 119, 242, 0.4); }

    /* 8. Contact FAQ */
    .contact-faq-section { background: var(--dropdown-bg); }
    .faq-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 2rem; text-align: left; }
    .faq-item { background: var(--bg-color); padding: 2rem; border-radius: 12px; border: 1px solid var(--border-color); }
    .faq-item h4 { font-size: 1.2rem; margin-bottom: 1rem; color: var(--text-primary); }
    .faq-item p { color: var(--text-secondary); line-height: 1.6; margin: 0; }

    /* Responsive */
    @media (max-width: 991px) {
      .split-layout, .split-layout.reverse { flex-direction: column; }
      .hero-main-title { color: #fff; font-size: 2.8rem; }
      .split-form { padding: 2rem; }
    }
    @media (max-width: 680px) {
      section { padding: 4rem 1.5rem; }
      .contact-card { padding: 1.5rem; }
      .s-link { width: 60px; height: 60px; font-size: 1.8rem; }
    }
  </style>
  <link rel="stylesheet" href="mobile.css">
  <link rel="icon" href="favicon.svg" type="image/svg+xml">
"""

scriptAndNavMatch = re.search(r'(<script>[\s\S]*?<\/nav>)', indexHtml)
scriptAndNav = scriptAndNavMatch.group(1)

bodyStart = """
  <main class="main-content-contact">
    <!-- 1. Contact Hero Section -->
    <section class="contact-hero text-center">
      <div class="section-container">
        <div class="hero-icon"><i class="fas fa-headset"></i></div>
        <h1 class="hero-main-title">We're Here to Help</h1>
        <p class="hero-main-desc">Got a question? Need to change a booking? Our dedicated support team is ready to assist you on your adventure.</p>
      </div>
    </section>

    <!-- 2. Contact Info Quick-Grid -->
    <section class="info-grid-section">
      <div class="section-container">
        <div class="contact-grid">
          <div class="contact-card">
            <i class="fas fa-phone-alt fa-flip-horizontal"></i>
            <h3>Call Us</h3>
            <p>1-800-ESCAPE-NOW</p>
            <span>Mon-Sun: 10AM - 10PM</span>
          </div>
          <div class="contact-card">
            <i class="fas fa-envelope"></i>
            <h3>Email Us</h3>
            <p>hello@venuedash.com</p>
            <span>Average response: 2 hrs</span>
          </div>
          <div class="contact-card">
            <i class="fas fa-map-marker-alt"></i>
            <h3>Visit Us</h3>
            <p>123 Adventure Lane</p>
            <span>Downtown District</span>
          </div>
        </div>
      </div>
    </section>

    <!-- 3. "Send a Raven" Message Form -->
    <section id="message" class="raven-form-section">
      <div class="section-container split-layout">
        <div class="split-text">
          <h2 class="section-title">Send a Raven</h2>
          <p class="section-desc">Drop us a line and our Game Masters will get back to you faster than you can say 'checkmate'.</p>
          <div style="margin-top: 2rem; margin-bottom: 2rem; text-align: left;">
            <p style="font-size: 1.1rem; color: var(--text-primary); display: flex; align-items: center; gap: 15px;">
              <i class="fas fa-phone-alt fa-flip-horizontal" style="color: var(--accent-color); font-size: 1.5rem; width: 24px; text-align: center;"></i> 
              <strong>1-800-ESCAPE-NOW</strong>
            </p>
          </div>
          <div style="border-radius: 15px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.3); margin-top: 1rem; max-width: 450px;">
            <img src="images/raven_illustration.png" alt="Send a Raven" style="width: 100%; height: auto; display: block;">
          </div>
        </div>
        <div class="split-form">
          <form class="custom-form">
            <div class="form-group">
              <label>What is this regarding?</label>
              <select>
                <option>General Question</option>
                <option>Change My Booking</option>
                <option>Lost and Found</option>
                <option>Feedback</option>
              </select>
            </div>
            <div class="form-group">
              <label>Your Name</label>
              <input type="text" placeholder="John Doe">
            </div>
            <div class="form-group">
              <label>Your Email</label>
              <input type="email" placeholder="john@example.com">
            </div>
            <div class="form-group">
              <label>Contact Number</label>
              <input type="tel" placeholder="+1 (555) 000-0000">
            </div>
            <div class="form-group">
              <label>Message</label>
              <textarea rows="4" placeholder="How can we help?"></textarea>
            </div>
            <button type="button" class="btn-primary w-100">Send Message <i class="fas fa-paper-plane"></i></button>
          </form>
        </div>
      </div>
    </section>

    <!-- 4. Interactive Map -->
    <section class="map-section">
      <div class="section-container" style="padding-bottom: 2rem;">
        <h2 class="section-title text-center" style="margin-bottom: 0;">Find Your Way</h2>
      </div>
      <div class="map-full-container">
        <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d193595.2527998699!2d-74.14448766782414!3d40.69766374878486!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c24fa5d33f083b%3A0xc80b8f06e177fe62!2sNew%20York%2C%20NY%2C%20USA!5e0!3m2!1sen!2s!4v1700000000000!5m2!1sen!2s" width="100%" height="100%" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Google Map Location"></iframe>
      </div>
    </section>

    <!-- 5. Private Event Inquiry -->
    <section class="event-inquiry-section">
      <div class="section-container split-layout reverse">
"""

restMatch = re.search(r'<div class="split-text">[\s\S]*', contactHtml)

if restMatch:
    newContent = headStart + contactCSS + '</head>\n<body>\n' + scriptAndNav + '\n' + bodyStart + restMatch.group(0)
    with open('Contact.html', 'w', encoding='utf-8') as f:
        f.write(newContent)
    print("Restored successfully")
else:
    print("Failed to match structure")
