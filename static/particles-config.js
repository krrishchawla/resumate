// static/particles-config.js

particlesJS("particles-container", {
    particles: {
      number: { value: 80, density: { enable: true, value_area: 800 } },
      color: { value: ["#00183f", "#0077cc", "#43c3ff"] },
      shape: {
        type: "circle",
        stroke: { width: 0, color: "#000" },
        polygon: { nb_sides: 5 },
      },
      opacity: { value: 1, random: false, anim: { enable: false, speed: 1, opacity_min: 0.1, sync: false } },
      size: { value: 3, random: true, anim: { enable: false, speed: 40, size_min: 0.1, sync: false } },
      line_linked: { enable: true, distance: 150, color: "#0077cc", opacity: 0.3, width: 1 },
      move: {
        enable: true,
        speed: 1,
        direction: "none",
        random: false,
        straight: false,
        out_mode: "out",
        bounce: false,
      },
    },
    interactivity: {
      detect_on: "canvas",
      events: { onhover: { enable: true, mode: "repulse" }, onclick: { enable: true, mode: "push" }, resize: true },
    },
    retina_detect: true,
  });
  