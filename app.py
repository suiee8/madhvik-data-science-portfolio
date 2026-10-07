import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(
    page_title="Madhvik Rashmin Panchal – Data Scientist",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Madhvik Rashmin Panchal – Data Scientist</title>
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=Syne:wght@400;500;600;700&display=swap" rel="stylesheet" />
    <style>
      :root {
        --bg: #000;
        --ink: #f8f7f4;
        --ink-dim: rgba(248, 247, 244, 0.58);
        --card: #141414;
        --card-2: #1b1b1b;
        --line: rgba(248, 247, 244, 0.1);
        --display: "Syne", sans-serif;
        --mono: "IBM Plex Mono", ui-monospace, monospace;
      }

      * { box-sizing: border-box; margin: 0; padding: 0; }
      html { scroll-behavior: auto; }
      body {
        background: var(--bg);
        color: var(--ink);
        font-family: var(--display);
        overflow-x: hidden;
        letter-spacing: -0.02em;
      }
      body::before {
        content: "";
        position: fixed;
        inset: 0;
        background: linear-gradient(rgba(255,255,255,0.02), rgba(255,255,255,0));
        pointer-events: none;
        z-index: 1;
      }
      a { color: inherit; text-decoration: none; }
      button { font: inherit; color: inherit; background: none; border: none; cursor: pointer; }
      img { max-width: 100%; display: block; }

      .logo {
        position: fixed;
        top: 28px;
        left: 50%;
        transform: translateX(-50%);
        z-index: 40;
        letter-spacing: 0.28em;
        font-size: 13px;
        font-weight: 700;
      }

      .blob {
        position: fixed;
        inset: 18% 18% auto;
        height: 62vh;
        pointer-events: none;
        z-index: 0;
        background:
          radial-gradient(closest-side at 48% 42%, #2a2a2a 0%, transparent 72%),
          radial-gradient(closest-side at 58% 55%, #1a1a1a 0%, transparent 70%),
          radial-gradient(closest-side at 40% 60%, #222 0%, transparent 68%);
        filter: blur(8px);
        opacity: 0.9;
        animation: blob 14s ease-in-out infinite;
      }
      @keyframes blob {
        0%, 100% { transform: scale(1) rotate(0deg); }
        50% { transform: scale(1.08) rotate(8deg); }
      }

      .dock {
        position: fixed;
        left: 50%;
        bottom: 22px;
        transform: translateX(-50%);
        z-index: 50;
        display: flex;
        gap: 22px;
        padding: 14px 22px;
        border: 1px solid var(--line);
        border-radius: 999px;
        background: rgba(18, 18, 18, 0.72);
        backdrop-filter: blur(18px);
        box-shadow: 0 12px 30px rgba(0,0,0,0.22);
      }
      .dock a {
        position: relative;
        font-size: 12px;
        letter-spacing: 0.12em;
        color: var(--ink-dim);
      }
      .dock a.active, .dock a:hover { color: var(--ink); }
      .dock a.active::after {
        content: "";
        position: absolute;
        left: 50%;
        bottom: -8px;
        width: 4px;
        height: 4px;
        border-radius: 50%;
        background: var(--ink);
        transform: translateX(-50%);
      }

      .hero {
        position: relative;
        z-index: 2;
        min-height: 100vh;
        padding: 140px 24px 80px;
        text-align: center;
      }
      .scramble {
        font-size: clamp(3.2rem, 11vw, 10.4rem);
        line-height: 0.88;
        letter-spacing: -0.05em;
        font-weight: 500;
        white-space: pre-line;
      }
      .hero-sub {
        margin: 36px auto 0;
        max-width: 420px;
        font-size: 13px;
        letter-spacing: 0.16em;
        line-height: 1.5;
      }

      .device-stage {
        position: relative;
        z-index: 2;
        margin: 54px auto 0;
        width: min(860px, 88vw);
      }
      .device {
        border-radius: 42px;
        padding: 18px;
        background: linear-gradient(180deg, #6d5cff, #4a34d6);
        box-shadow: 0 40px 80px rgba(0, 0, 0, 0.45);
        transform: translateY(0);
        transition: transform 0.45s ease, box-shadow 0.45s ease;
      }
      .device:hover { transform: translateY(-4px); box-shadow: 0 46px 90px rgba(0,0,0,0.5); }
      .device.cream { background: linear-gradient(180deg, #eceaf3, #d9d5e4); }
      .device.slate { background: linear-gradient(180deg, #2b2b33, #17171c); }
      .device.wine { background: linear-gradient(180deg, #f4f1ea, #e8e2d6); }
      .device.mint { background: linear-gradient(180deg, #c9f3df, #8ad7b8); }
      .device-inner {
        overflow: hidden;
        border-radius: 28px;
        min-height: 420px;
        background: #0c1020;
        position: relative;
      }
      .work {
        position: relative;
        z-index: 2;
        height: 420vh;
      }
      .work-sticky {
        position: sticky;
        top: 0;
        height: 100vh;
        display: grid;
        place-items: center;
        padding: 90px 24px 110px;
      }
      .work-meta {
        position: absolute;
        left: 6vw;
        right: 6vw;
        bottom: 110px;
        display: flex;
        justify-content: space-between;
        align-items: baseline;
        gap: 24px;
      }
      .work-title {
        font-size: 26px;
        font-weight: 500;
      }
      .work-title span {
        display: inline-block;
        margin-left: 8px;
        opacity: 0.7;
      }
      .work-tags {
        font-family: var(--mono);
        font-size: 12px;
        letter-spacing: 0.12em;
        color: var(--ink-dim);
        text-transform: uppercase;
      }

      .screen {
        height: 460px;
        padding: 36px 42px;
        color: #fff;
        transition: transform 0.6s ease, box-shadow 0.6s ease;
      }
      .screen h3 {
        font-size: clamp(2rem, 4vw, 3.4rem);
        letter-spacing: -0.04em;
        max-width: 420px;
      }
      .screen p {
        margin-top: 14px;
        max-width: 280px;
        font-size: 13px;
        color: rgba(255, 255, 255, 0.7);
        line-height: 1.5;
      }
      .screen-art {
        position: absolute;
        right: 8%;
        top: 22%;
        width: 220px;
        height: 220px;
      }
      .north { background: radial-gradient(circle at 80% 30%, #7a3dff, transparent 40%), #0b1024; }
      .lumen { background: #f4f0e8; color: #1d1a16; }
      .lumen h3, .lumen p { color: #1d1a16; }
      .meridian { background: linear-gradient(160deg, #101014, #26222d); }
      .atlas { background: #d9d5cf; color: #6a1f32; }
      .atlas h3, .atlas p { color: #6a1f32; }
      .helix { background: #111; }
      .shape {
        width: 100%;
        height: 100%;
        background: linear-gradient(135deg, #ff4de1, #6d5cff 50%, #45e0ff);
        clip-path: polygon(20% 10%, 90% 20%, 80% 90%, 10% 70%);
        filter: drop-shadow(0 20px 30px rgba(109, 92, 255, 0.5));
        animation: spin 16s linear infinite;
      }
      @keyframes spin { to { transform: rotate(360deg); } }

      .section {
        position: relative;
        z-index: 2;
        padding: 120px 6vw 80px;
      }
      .about-top {
        display: grid;
        grid-template-columns: 0.7fr 1.3fr;
        gap: 24px;
        align-items: start;
      }
      .section-title {
        font-size: clamp(3.4rem, 7vw, 5.4rem);
        letter-spacing: -0.05em;
        font-weight: 500;
      }
      .stats {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 14px;
      }
      .stat {
        background: var(--card);
        border-radius: 22px;
        min-height: 180px;
        padding: 22px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
      }
      .stat strong {
        font-size: clamp(2.6rem, 5vw, 4.4rem);
        font-weight: 500;
        letter-spacing: -0.05em;
      }
      .stat span {
        font-family: var(--mono);
        font-size: 12px;
        letter-spacing: 0.14em;
        color: var(--ink-dim);
        text-align: right;
      }
      .bio-row {
        display: grid;
        grid-template-columns: 180px 1fr;
        gap: 24px;
        margin-top: 90px;
      }
      .label {
        font-family: var(--mono);
        font-size: 12px;
        letter-spacing: 0.16em;
        color: var(--ink-dim);
      }
      .bio {
        max-width: 720px;
        font-family: var(--mono);
        font-size: clamp(16px, 2vw, 24px);
        line-height: 1.55;
        text-transform: uppercase;
      }
      .testimonials {
        display: grid;
        grid-template-columns: 180px 1fr;
        gap: 24px;
        margin-top: 90px;
      }
      .t-track {
        position: relative;
        min-height: 240px;
      }
      .t-card {
        position: absolute;
        inset: 0 auto auto 0;
        width: min(640px, 100%);
        background: var(--card-2);
        border-radius: 24px;
        padding: 28px;
        opacity: 0;
        transform: translateX(24px);
        transition: 0.5s ease;
      }
      .t-card.active {
        opacity: 1;
        transform: none;
        z-index: 2;
      }
      .t-who {
        display: flex;
        gap: 12px;
        align-items: center;
        margin-bottom: 18px;
      }
      .avatar {
        width: 42px;
        height: 42px;
        border-radius: 12px;
        display: grid;
        place-items: center;
        font-size: 14px;
        background: #6d5cff;
      }
      .t-who small {
        display: block;
        color: var(--ink-dim);
        font-family: var(--mono);
        font-size: 11px;
        letter-spacing: 0.08em;
      }
      .t-card p {
        font-size: 22px;
        line-height: 1.4;
        letter-spacing: -0.02em;
      }

      .services-head {
        display: flex;
        justify-content: space-between;
        gap: 24px;
        align-items: end;
        margin-bottom: 48px;
      }
      .services-copy {
        max-width: 320px;
        text-align: right;
        font-family: var(--mono);
        font-size: 13px;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        line-height: 1.6;
        color: var(--ink-dim);
      }
      .service-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 16px;
      }
      .service {
        background: var(--card);
        border-radius: 28px;
        padding: 28px 24px 18px;
        min-height: 520px;
        display: flex;
        flex-direction: column;
        border: 1px solid transparent;
        transition: transform 0.35s ease, border-color 0.35s ease, box-shadow 0.35s ease;
      }
      .service:hover {
        transform: translateY(-6px);
        border-color: var(--line);
        box-shadow: 0 20px 38px rgba(0,0,0,0.26);
      }
      .price {
        display: inline-flex;
        border: 1px solid var(--line);
        border-radius: 8px;
        padding: 4px 8px;
        font-family: var(--mono);
        font-size: 12px;
      }
      .service h3 {
        margin-top: 28px;
        font-size: 34px;
        letter-spacing: -0.04em;
        font-weight: 500;
        line-height: 1.05;
      }
      .service > p {
        margin-top: 16px;
        color: var(--ink-dim);
        line-height: 1.5;
      }
      .service ul {
        list-style: none;
        margin-top: 28px;
      }
      .service li {
        padding: 12px 0;
        border-top: 1px solid var(--line);
        color: var(--ink-dim);
        font-size: 14px;
      }
      .service li::before { content: "—  "; }
      .service li.hidden { display: none; }
      .service.open li.hidden { display: block; }
      .service-actions {
        margin-top: auto;
        display: flex;
        justify-content: space-between;
        padding-top: 18px;
      }
      .ghost {
        border: 1px solid var(--line);
        border-radius: 999px;
        padding: 10px 14px;
        font-size: 12px;
        letter-spacing: 0.08em;
      }

      .contact {
        padding-bottom: 140px;
        text-align: center;
      }
      .marquee-wrap {
        display: block;
        overflow: hidden;
        border: 1px solid var(--line);
        border-radius: 999px;
        padding: 20px 0;
        background: rgba(255,255,255,0.03);
        position: relative;
        box-shadow: inset 0 0 0 1px rgba(255,255,255,0.02);
      }
      .marquee-wrap::before,
      .marquee-wrap::after {
        content: "";
        position: absolute;
        top: 0;
        bottom: 0;
        width: 12%;
        z-index: 2;
        pointer-events: none;
      }
      .marquee-wrap::before {
        left: 0;
        background: linear-gradient(90deg, rgba(0,0,0,1), rgba(0,0,0,0));
      }
      .marquee-wrap::after {
        right: 0;
        background: linear-gradient(270deg, rgba(0,0,0,1), rgba(0,0,0,0));
      }
      .marquee {
        display: flex;
        gap: 28px;
        width: max-content;
        font-size: clamp(2.4rem, 7vw, 5.4rem);
        letter-spacing: -0.04em;
        font-weight: 500;
        white-space: nowrap;
        animation: marquee 20s linear infinite;
      }
      .marquee span { display: inline-block; }
      @keyframes marquee {
        from { transform: translateX(0); }
        to { transform: translateX(-50%); }
      }
      .mail-row {
        display: flex;
        justify-content: center;
        gap: 28px;
        margin-top: 28px;
        font-family: var(--mono);
        font-size: 13px;
        letter-spacing: 0.12em;
      }
      .mail-row a, .mail-row button { transition: opacity 0.25s ease, transform 0.25s ease; }
      .mail-row a:hover, .mail-row button:hover { opacity: 0.8; transform: translateY(-1px); }
      .footer {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-top: 64px;
        font-family: var(--mono);
        font-size: 11px;
        letter-spacing: 0.1em;
        color: var(--ink-dim);
      }
      .socials { display: flex; gap: 10px; }
      .socials a {
        width: 42px;
        height: 42px;
        border: 1px solid var(--line);
        border-radius: 50%;
        display: grid;
        place-items: center;
      }
      .toast {
        position: fixed;
        right: 24px;
        bottom: 86px;
        z-index: 60;
        background: var(--ink);
        color: #111;
        padding: 10px 14px;
        border-radius: 999px;
        font-size: 12px;
        opacity: 0;
        transform: translateY(8px);
        pointer-events: none;
        transition: 0.3s ease;
      }
      .toast.show { opacity: 1; transform: none; }

      @media (max-width: 960px) {
        .about-top, .bio-row, .testimonials, .service-grid { grid-template-columns: 1fr; }
        .work-meta { flex-direction: column; align-items: flex-start; }
        .services-head { flex-direction: column; align-items: flex-start; }
        .services-copy { text-align: left; }
        .stats { grid-template-columns: 1fr; }
        .footer { flex-direction: column; gap: 16px; }
        .device-inner, .screen { min-height: 320px; height: auto; }
      }
    </style>
  </head>
  <body>
    <a class="logo" href="#top">MADHVIK</a>
    <div class="blob" aria-hidden="true"></div>

    <nav class="dock" aria-label="Primary">
      <a href="#work">WORK</a>
      <a href="#about">ABOUT</a>
      <a href="#services">SERVICES</a>
      <a href="#contact">CONTACT</a>
    </nav>

    <main id="top">
      <section class="hero">
        <h1 class="scramble" data-phrases="DATA SCIENTIST|AI ANALYST|ML ENTHUSIAST">DATA SCIENTIST</h1>
        <p class="hero-sub">I TURN DATA INTO DECISIONS, MODELS, AND IMPACT</p>
        <div class="device-stage">
          <div class="device">
            <div class="device-inner north">
              <article class="screen">
                <h3>WHAT ARE WE ANALYZING?</h3>
                <p>Predictive systems, business insights, and data products that turn messy information into clear decisions.</p>
                <div class="screen-art"><div class="shape"></div></div>
              </article>
            </div>
          </div>
        </div>
      </section>

      <section class="work" id="work">
        <div class="work-sticky">
          <div class="device-stage">
            <div class="device" id="work-device">
              <div class="device-inner" id="work-screen"></div>
            </div>
          </div>
          <div class="work-meta">
            <h2 class="work-title" id="work-title">SignalIQ <span>↗</span></h2>
            <p class="work-tags" id="work-tags">Machine Learning / Forecasting / Insights</p>
          </div>
        </div>
      </section>

      <section class="section" id="about">
        <div class="about-top">
          <h2 class="section-title">ABOUT</h2>
          <div class="stats">
            <article class="stat"><strong>20</strong><span>YEARS<br />OLD</span></article>
            <article class="stat"><strong>IND</strong><span>COUNTRY<br />INDIA</span></article>
            <article class="stat"><strong>AHM</strong><span>CITY<br />AHMEDABAD</span></article>
          </div>
        </div>

        <div class="bio-row">
          <p class="label">../PARAGRAPH</p>
          <p class="bio">My name is Madhvik Rashmin Panchal, a data scientist based in Ahmedabad, Gujarat, India. I build analytical models, uncover actionable insights, and design data-driven solutions that create measurable business impact.</p>
        </div>

        <div class="testimonials">
          <p class="label">../TESTIMONIALS</p>
          <div class="t-track" id="testimonials"></div>
        </div>
      </section>

      <section class="section" id="services">
        <div class="services-head">
          <h2 class="section-title">SERVICES</h2>
          <p class="services-copy">Purposeful designs blend beauty and functionality, resulting in cohesive and impactful outcomes.</p>
        </div>
        <div class="service-grid">
          <article class="service">
            <span class="price">$$$</span>
            <h3>Data Analysis &amp; Insights</h3>
            <p>I help teams make sense of complex data and turn it into focused, high-impact business decisions.</p>
            <ul>
              <li>Data Analysis</li>
              <li class="hidden">Business Intelligence</li>
              <li class="hidden">KPI Tracking</li>
              <li class="hidden">Trend Research</li>
              <li class="hidden">Decision Support</li>
              <li class="hidden">Pattern Discovery</li>
              <li class="hidden">Custom Reporting</li>
            </ul>
            <div class="service-actions">
              <a class="ghost" href="#contact">CONTACT ME</a>
              <button class="ghost more" type="button">SHOW MORE +</button>
            </div>
          </article>

          <article class="service">
            <span class="price">$$</span>
            <h3>Machine Learning &amp; Predictive Modeling</h3>
            <p>From forecasting to experimentation, I build models that translate raw data into practical predictions and measurable value.</p>
            <ul>
              <li>Predictive Modeling</li>
              <li class="hidden">Classification &amp; Regression</li>
              <li class="hidden">Forecasting</li>
              <li class="hidden">Feature Engineering</li>
              <li class="hidden">Model Evaluation</li>
              <li class="hidden">A/B Test Insights</li>
            </ul>
            <div class="service-actions">
              <a class="ghost" href="#contact">CONTACT ME</a>
              <button class="ghost more" type="button">SHOW MORE +</button>
            </div>
          </article>

          <article class="service">
            <span class="price">$</span>
            <h3>Data Visualization &amp; Storytelling</h3>
            <p>I turn output into clear narratives by designing dashboards and visuals that make your insights easy to understand and act on.</p>
            <ul>
              <li>Interactive Dashboards</li>
              <li class="hidden">Data Storytelling</li>
              <li class="hidden">Visualization Design</li>
              <li class="hidden">Executive Reporting</li>
            </ul>
            <div class="service-actions">
              <a class="ghost" href="#contact">CONTACT ME</a>
              <button class="ghost more" type="button">SHOW MORE +</button>
            </div>
          </article>
        </div>
      </section>

      <section class="section contact" id="contact">
        <a class="marquee-wrap" href="mailto:themadhvik@gmail.com" aria-label="Email Madhvik">
          <div class="marquee">
            <span>THEMADHVIK@GMAIL.COM • THEMADHVIK@GMAIL.COM • THEMADHVIK@GMAIL.COM • </span>
            <span>THEMADHVIK@GMAIL.COM • THEMADHVIK@GMAIL.COM • THEMADHVIK@GMAIL.COM • </span>
          </div>
        </a>
        <div class="mail-row">
          <a href="mailto:themadhvik@gmail.com">[ THEMADHVIK@GMAIL.COM ]</a>
          <button type="button" id="copy-email">[ COPY EMAIL ]</button>
        </div>
        <div class="footer">
          <p>©2026 MADHVIK RASHMIN PANCHAL.<br />ALL RIGHTS RESERVED.</p>
          <div class="socials">
            <a href="https://www.linkedin.com/in/madhvikpanchal/" target="_blank" rel="noreferrer" aria-label="LinkedIn">in</a>
            <a href="https://github.com/suiee8" target="_blank" rel="noreferrer" aria-label="GitHub">Gh</a>
            <a href="mailto:themadhvik@gmail.com" aria-label="Email">Mail</a>
            <a href="https://www.linkedin.com/in/madhvikpanchal/" target="_blank" rel="noreferrer" aria-label="Profile">Li</a>
          </div>
        </div>
      </section>
    </main>

    <div class="toast" id="toast">Email copied</div>

    <script>
      const GLYPHS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789$€+/";
      const projects = [
        { name: "SignalIQ", tags: "Machine Learning / Forecasting / Insights", skin: "purple", html: '<article class="screen north"><h3>WHAT ARE WE MODELING?</h3><p>Turning business signals into accurate predictions and clear, actionable intelligence.</p><div class="screen-art"><div class="shape"></div></div></article>' },
        { name: "InsightFlow", tags: "Analytics / Data Pipelines / Reporting", skin: "cream", html: '<article class="screen lumen"><h3>Data, translated into clarity.</h3><p>Dashboards and analytics systems designed to guide faster, smarter decisions.</p></article>' },
        { name: "TrendFrame", tags: "Predictive Modeling / Research / Automation", skin: "slate", html: '<article class="screen meridian"><h3>Patterns, surfaced.</h3><p>Clean forecasting workflows that uncover the story hidden in large datasets.</p></article>' },
        { name: "Atlas Metrics", tags: "Experimentation / Data Storytelling / Analysis", skin: "wine", html: '<article class="screen atlas"><h3>BY THE NUMBERS</h3><p>Analytical decisions built from evidence, testing, and sharp communication.</p></article>' },
        { name: "Data Canvas", tags: "Product Analytics / ML / Visualization", skin: "mint", html: '<article class="screen helix"><h3>Insight-first systems.</h3><p>Structured data experiences that make complex analysis feel intuitive and useful.</p></article>' }
      ];

      const quotes = [
        { who: "Aarav K.", org: "Research Team", text: "Madhvik brings sharp analytical thinking and a calm, practical approach to complex data challenges.", mark: "AK" },
        { who: "Riya S.", org: "Product Ops", text: "He turns messy datasets into clear storylines and useful decisions without overcomplicating the process.", mark: "RS" },
        { who: "Nikhil P.", org: "Business Insights", text: "One of the most reliable people I’ve worked with — thoughtful, fast, and deeply detail-oriented.", mark: "NP" },
        { who: "Sana M.", org: "Analytics Studio", text: "Madhvik understands the business context quickly and builds models that are both technically strong and easy to act on.", mark: "SM" }
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
        const el = document.querySelector('.scramble');
        const phrases = el.dataset.phrases.split('|');
        let i = 0;
        setInterval(() => {
          i = (i + 1) % phrases.length;
          scrambleTo(el, phrases[i]);
        }, 3200);
      }

      function renderWork(index) {
        const project = projects[index];
        const device = document.getElementById('work-device');
        const screen = document.getElementById('work-screen');
        const title = document.getElementById('work-title');
        const tags = document.getElementById('work-tags');
        const skins = ['', 'cream', 'slate', 'wine', 'mint'];
        device.className = `device ${skins[index] || ''}`;
        screen.innerHTML = project.html;
        title.innerHTML = `${project.name} <span>↗</span>`;
        tags.textContent = project.tags;
      }

      function initWork() {
        const section = document.getElementById('work');
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
        window.addEventListener('scroll', onScroll, { passive: true });
      }

      function initTestimonials() {
        const root = document.getElementById('testimonials');
        root.innerHTML = quotes.map((q, i) => `
          <article class="t-card ${i === 0 ? 'active' : ''}">
            <div class="t-who">
              <div class="avatar">${q.mark}</div>
              <div>
                <strong>${q.who}</strong>
                <small>${q.org}</small>
              </div>
            </div>
            <p>${q.text}</p>
          </article>
        `).join('');

        let i = 0;
        setInterval(() => {
          const cards = [...root.querySelectorAll('.t-card')];
          cards[i].classList.remove('active');
          i = (i + 1) % cards.length;
          cards[i].classList.add('active');
        }, 4200);
      }

      function initDock() {
        const links = [...document.querySelectorAll('.dock a')];
        const ids = ['work', 'about', 'services', 'contact'];
        const onScroll = () => {
          let active = 'work';
          for (const id of ids) {
            const el = document.getElementById(id);
            if (el.getBoundingClientRect().top < window.innerHeight * 0.55) active = id;
          }
          links.forEach(link => { link.classList.toggle('active', link.getAttribute('href') === `#${active}`); });
        };
        onScroll();
        window.addEventListener('scroll', onScroll, { passive: true });
      }

      function initAnchorNavigation() {
        document.addEventListener('click', (event) => {
          const link = event.target.closest('a[href^="#"]');
          if (!link) return;
          const target = document.querySelector(link.getAttribute('href'));
          if (!target) return;
          event.preventDefault();
          target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        });
      }

      function initServices() {
        document.querySelectorAll('.service .more').forEach((btn) => {
          btn.addEventListener('click', () => {
            const card = btn.closest('.service');
            card.classList.toggle('open');
            btn.textContent = card.classList.contains('open') ? 'SHOW LESS −' : 'SHOW MORE +';
          });
        });
      }

      function initCopy() {
        const toast = document.getElementById('toast');
        document.getElementById('copy-email').addEventListener('click', async () => {
          await navigator.clipboard.writeText('themadhvik@gmail.com');
          toast.classList.add('show');
          setTimeout(() => toast.classList.remove('show'), 1600);
        });
      }

      initScramble();
      initWork();
      initTestimonials();
      initDock();
      initAnchorNavigation();
      initServices();
      initCopy();
    </script>
  </body>
</html>
"""

st.markdown(
    """
    <style>
      .stApp { padding: 0 !important; }
      .block-container { padding: 0 !important; max-width: 100% !important; }
      iframe { border: none; width: 100%; }
      body { margin: 0; }
    </style>
    """,
    unsafe_allow_html=True,
)

html(HTML_PAGE, height=700, scrolling=True)
