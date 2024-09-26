document.addEventListener('DOMContentLoaded', (event) => {
    const asciiMaze = 
`
+---+---+---+---+---+
| S |   |   |   |   |
+   +   +---+---+   +
|   |   |       |   |
+   +---+   +   +   +
|           |   |   |
+---+---+   +   +   +
|           |   |   |
+   +---+---+   +   +
| P |           | E |
+---+---+---+---+---+
`;

    document.getElementById('ascii-maze').textContent = asciiMaze;

    // Smooth scrolling for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Add animation to features on scroll
    const features = document.querySelectorAll('.feature');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate');
            }
        });
    }, { threshold: 0.5 });

    features.forEach(feature => {
        observer.observe(feature);
    });
});
