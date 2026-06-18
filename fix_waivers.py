import re
with open('d:/groww/room/digital_waivers.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix CSS for waiver-hero
css_target = """    .waiver-hero {
      background: linear-gradient(rgba(15, 23, 42, 0.7), rgba(15, 23, 42, 0.9)), url('images/waiver_hero.jpg') center/cover;
      padding: 8rem 2rem 5rem;
      border-bottom: 1px solid var(--border-color);
    }"""
css_replace = css_target + """
    
    .waiver-hero .section-container {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
    }"""
text = text.replace(css_target, css_replace)

# Fix HTML order for hero
html_target = """<div class="icon-pulse"><i class="fas fa-signature"></i></div>
        <h1 class="hero-main-title">Sign Your Waiver</h1>"""
html_replace = """<h1 class="hero-main-title">Sign Your Waiver</h1>
        <div class="icon-pulse"><i class="fas fa-signature"></i></div>"""
text = text.replace(html_target, html_replace)

# Replace 'Booking' with 'Order' in specific strings
replacements = {
    'Find My Booking': 'Find My Order',
    'Attach Waiver to Booking': 'Attach Waiver to Order',
    'Enter the Booking ID': 'Enter the Order ID',
    '<label>Booking ID</label>': '<label>Order ID</label>',
    'Search Booking</button>': 'Search Order</button>',
    'No booking ID?': 'No order ID?',
    "Can't find your booking ID": "Can't find your order ID"
}

for old, new in replacements.items():
    text = text.replace(old, new)

with open('d:/groww/room/digital_waivers.html', 'w', encoding='utf-8') as f:
    f.write(text)
print('Done!')
