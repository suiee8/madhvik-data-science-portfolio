const EMAIL = "themadhvik@gmail.com";
const GLYPHS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789$€+/";

const projects = [
  {
    name: "SignalIQ",
    tags: "Machine Learning / Forecasting / Insights",
    skin: "purple",
    html: `<article class="screen north"><h3>WHAT ARE WE MODELING?</h3><p>Turning business signals into accurate predictions and clear, actionable intelligence.</p><div class="screen-art"><div class="shape"></div></div></article>`,
  },
  {
    name: "InsightFlow",
    tags: "Analytics / Data Pipelines / Reporting",
    skin: "cream",
    html: `<article class="screen lumen"><h3>Data, translated into clarity.</h3><p>Dashboards and analytics systems designed to guide faster, smarter decisions.</p></article>`,
  },
  {
    name: "TrendFrame",
    tags: "Predictive Modeling / Research / Automation",
    skin: "slate",
    html: `<article class="screen meridian"><h3>Patterns, surfaced.</h3><p>Clean forecasting workflows that uncover the story hidden in large datasets.</p></article>`,
  },
  {
    name: "Atlas Metrics",
    tags: "Experimentation / Data Storytelling / Analysis",
    skin: "wine",
    html: `<article class="screen atlas"><h3>BY THE NUMBERS</h3><p>Analytical decisions built from evidence, testing, and sharp communication.</p></article>`,
  },
  {
    name: "Data Canvas",
    tags: "Product Analytics / ML / Visualization",
    skin: "mint",
    html: `<article class="screen helix"><h3>Insight-first systems.</h3><p>Structured data experiences that make complex analysis feel intuitive and useful.</p></article>`,
  },
];

const quotes = [
  {
    who: "Aarav K.",
    org: "Research Team",
    text: "Madhvik brings sharp analytical thinking and a calm, practical approach to complex data challenges.",
    mark: "AK",
  },
  {
    who: "Riya S.",
    org: "Product Ops",
    text: "He turns messy datasets into clear storylines and useful decisions without overcomplicating the process.",
    mark: "RS",
  },
  {
    who: "Nikhil P.",
    org: "Business Insights",
    text: "One of the most reliable people I’ve worked with — thoughtful, fast, and deeply detail-oriented.",
    mark: "NP",
  },
  {
    who: "Sana M.",
    org: "Analytics Studio",
    text: "Madhvik understands the business context quickly and builds models that are both technically strong and easy to act on.",
    mark: "SM",
  },
];

function scrambleTo(el, next) {
  const length = Math.max(el.textContent.length, next.length);
  let frame = 0;
  const ticks = 18;
  const id = setInterval(() => {
    el.textContent = Array.from({ length }, (_, i) => {
      if (frame / ticks > i / length) return next[i] || "";
      return GLYPHS[Math.floor(Math.random() * GLYPHS.length)];
    }).join("");
    frame += 1;
    if (frame > ticks) {
      el.textContent = next;
      clearInterval(id);
    }
  }, 32);
}

function initScramble() {
  const el = document.querySelector(".scramble");
  const phrases = el.dataset.phrases.split("|");
  let i = 0;
  setInterval(() => {
    i = (i + 1) % phrases.length;
    scrambleTo(el, phrases[i]);
  }, 3200);
}

function renderWork(index) {
  const project = projects[index];
  const device = document.getElementById("work-device");
  const screen = document.getElementById("work-screen");
  const title = document.getElementById("work-title");
  const tags = document.getElementById("work-tags");
  const skins = ["", "cream", "slate", "wine", "mint"];
  device.className = `device ${skins[index] || ""}`;
  screen.innerHTML = project.html;
  title.innerHTML = `${project.name} <span>↗</span>`;
  tags.textContent = project.tags;
}

function initWork() {
  const section = document.getElementById("work");
  let current = -1;
  const onScroll = () => {
    const rect = section.getBoundingClientRect();
    const total = section.offsetHeight - window.innerHeight;
    const progressed = Math.min(Math.max(-rect.top / total, 0), 0.999);
    const index = Math.floor(progressed * projects.length);
    if (index !== current) {
      current = index;
      renderWork(index);
    }
  };
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });
}

function initTestimonials() {
  const root = document.getElementById("testimonials");
  root.innerHTML = quotes
    .map(
      (q, i) => `
      <article class="t-card ${i === 0 ? "active" : ""}">
        <div class="t-who">
          <div class="avatar">${q.mark}</div>
          <div>
            <strong>${q.who}</strong>
            <small>${q.org}</small>
          </div>
        </div>
        <p>${q.text}</p>
      </article>`
    )
    .join("");
  let i = 0;
  setInterval(() => {
    const cards = [...root.querySelectorAll(".t-card")];
    cards[i].classList.remove("active");
    i = (i + 1) % cards.length;
    cards[i].classList.add("active");
  }, 4200);
}

function initDock() {
  const links = [...document.querySelectorAll(".dock a")];
  const ids = ["work", "about", "services", "contact"];
  const onScroll = () => {
    let active = "work";
    for (const id of ids) {
      const el = document.getElementById(id);
      if (el.getBoundingClientRect().top < window.innerHeight * 0.55) active = id;
    }
    links.forEach((link) => {
      link.classList.toggle("active", link.getAttribute("href") === `#${active}`);
    });
  };
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });
}

function initServices() {
  document.querySelectorAll(".service .more").forEach((btn) => {
    btn.addEventListener("click", () => {
      const card = btn.closest(".service");
      card.classList.toggle("open");
      btn.textContent = card.classList.contains("open") ? "SHOW LESS −" : "SHOW MORE +";
    });
  });
}

function initCopy() {
  const toast = document.getElementById("toast");
  document.getElementById("copy-email").addEventListener("click", async () => {
    await navigator.clipboard.writeText(EMAIL);
    toast.classList.add("show");
    setTimeout(() => toast.classList.remove("show"), 1600);
  });
}

initScramble();
initWork();
initTestimonials();
initDock();
initServices();
initCopy();
