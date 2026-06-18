const fs = require('fs');

const files = [
  "book_rooms.html", 
  "Contact.html", 
  "digital_waivers.html", 
  "home2.html", 
  "navbar.html", 
  "packages.html", 
  "Safety Demos.html", 
  "team_rosters.html"
];

const indexHtml = fs.readFileSync('index.html', 'utf8');

const navMatch = indexHtml.match(/<nav class="navbar">[\s\S]*?<\/nav>/);
const footerMatch = indexHtml.match(/<footer id="contact" class="footer">[\s\S]*?<\/footer>/);

if (navMatch && footerMatch) {
  for (const file of files) {
    let content = fs.readFileSync(file, 'utf8');
    content = content.replace(/<nav class="navbar">[\s\S]*?<\/nav>/, navMatch[0]);
    content = content.replace(/<footer class="footer">[\s\S]*?<\/footer>/, footerMatch[0]);
    fs.writeFileSync(file, content, 'utf8');
    console.log(`Updated ${file}`);
  }
} else {
  console.log("Could not find nav or footer in index.html");
}
