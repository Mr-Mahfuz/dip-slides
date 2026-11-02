# -*- coding: utf-8 -*-
import json
from slides_def import slides_data

print("Generating mobile-first light-themed presentation HTML...")

html_template = """<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, viewport-fit=cover">
<title>DIP Slide Deck | Slides 7 & 8 | Frequency Domain & Image Restoration</title>
<meta name="description" content="Slide-by-slide interactive study guide for Digital Image Processing: Frequency Domain Filtering (Slide 7) and Image Restoration & Noise Removal (Slide 8).">

<!-- Mobile App Capable Meta Tags -->
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="theme-color" content="#ffffff" id="theme-color-meta">

<!-- Google Fonts -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600;700&family=Outfit:wght@500;600;700;800&display=swap" rel="stylesheet">

<!-- MathJax for TeX rendering -->
<script>
MathJax = {
  tex: {
    inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
    displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']],
    tags: 'ams'
  },
  svg: { fontCache: 'global' }
};
</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js" id="MathJax-script"></script>

<style>
/* ─── LIGHT THEME (DEFAULT) ─── */
:root {
  --bg-primary: #f8fafc;
  --bg-secondary: #f1f5f9;
  --bg-card: #ffffff;
  --bg-card-hover: #fcfdfe;
  --bg-subtle: #f8fafc;
  
  --text-primary: #0f172a;
  --text-secondary: #334155;
  --text-muted: #64748b;
  --text-inverted: #ffffff;
  
  --border: #e2e8f0;
  --border-subtle: #edf2f7;
  --border-strong: #cbd5e1;
  --border-glow: rgba(37, 99, 235, 0.25);
  
  --accent-blue: #2563eb;
  --accent-blue-light: #eff6ff;
  --accent-blue-border: #bfdbfe;
  --accent-blue-text: #1d4ed8;
  
  --accent-purple: #7c3aed;
  --accent-purple-light: #faf5ff;
  --accent-purple-border: #e9d5ff;
  --accent-purple-text: #6d28d9;
  
  --accent-cyan: #0284c7;
  --accent-cyan-light: #f0f9ff;
  --accent-cyan-border: #bae6fd;
  
  --accent-green: #059669;
  --accent-green-light: #ecfdf5;
  --accent-green-border: #a7f3d0;
  --accent-green-text: #047857;
  
  --accent-orange: #d97706;
  --accent-orange-light: #fffbeb;
  --accent-orange-border: #fde68a;
  --accent-orange-text: #b45309;
  
  --accent-pink: #e11d48;
  --accent-pink-light: #fff1f2;
  --accent-pink-border: #fecdd3;
  --accent-pink-text: #be123c;
  
  --shadow-sm: 0 1px 3px rgba(15, 23, 42, 0.06), 0 1px 2px rgba(15, 23, 42, 0.04);
  --shadow-md: 0 4px 14px rgba(15, 23, 42, 0.06), 0 2px 6px rgba(15, 23, 42, 0.04);
  --shadow-lg: 0 10px 25px -3px rgba(15, 23, 42, 0.08), 0 4px 6px -4px rgba(15, 23, 42, 0.04);
}

/* ─── OPTIONAL DARK THEME ─── */
[data-theme="dark"] {
  --bg-primary: #0a0c16;
  --bg-secondary: #111424;
  --bg-card: #181d33;
  --bg-card-hover: #1f2644;
  --bg-subtle: #13172c;
  
  --text-primary: #f0f4ff;
  --text-secondary: #9daabf;
  --text-muted: #5e6a84;
  --text-inverted: #0a0c16;
  
  --border: #232b47;
  --border-subtle: #1c233c;
  --border-strong: #333d63;
  --border-glow: rgba(79, 142, 247, 0.3);
  
  --accent-blue: #4f8ef7;
  --accent-blue-light: rgba(79, 142, 247, 0.12);
  --accent-blue-border: rgba(79, 142, 247, 0.3);
  --accent-blue-text: #70a5f9;
  
  --accent-purple: #a259ff;
  --accent-purple-light: rgba(162, 89, 255, 0.12);
  --accent-purple-border: rgba(162, 89, 255, 0.3);
  --accent-purple-text: #b87cff;
  
  --accent-cyan: #00d4ff;
  --accent-cyan-light: rgba(0, 212, 255, 0.12);
  --accent-cyan-border: rgba(0, 212, 255, 0.3);
  
  --accent-green: #39e079;
  --accent-green-light: rgba(57, 224, 121, 0.12);
  --accent-green-border: rgba(57, 224, 121, 0.3);
  --accent-green-text: #5fe695;
  
  --accent-orange: #ff8c42;
  --accent-orange-light: rgba(255, 140, 66, 0.12);
  --accent-orange-border: rgba(255, 140, 66, 0.3);
  --accent-orange-text: #ffa264;
  
  --accent-pink: #ff4fa3;
  --accent-pink-light: rgba(255, 79, 163, 0.12);
  --accent-pink-border: rgba(255, 79, 163, 0.3);
  --accent-pink-text: #ff72b7;
  
  --shadow-sm: 0 2px 6px rgba(0,0,0,0.3);
  --shadow-md: 0 4px 16px rgba(0,0,0,0.4);
  --shadow-lg: 0 12px 32px rgba(0,0,0,0.5);
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  background: var(--bg-primary);
  color: var(--text-primary);
  font-family: 'Plus Jakarta Sans', 'Inter', -apple-system, sans-serif;
  line-height: 1.65;
  min-height: 100vh;
  overflow-x: hidden;
  transition: background-color 0.2s ease, color 0.2s ease;
  -webkit-font-smoothing: antialiased;
  -webkit-tap-highlight-color: transparent;
}

/* ─── TOP PROGRESS BAR ─── */
.slide-progress-bar {
  position: fixed;
  top: 0;
  left: 0;
  height: 4px;
  background: linear-gradient(90deg, #0284c7, #2563eb, #7c3aed, #db2777);
  width: 0%;
  z-index: 1000;
  transition: width 0.25s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 0 1px 4px rgba(37, 99, 235, 0.3);
}

/* ─── FIXED TOP CONTROL BAR ─── */
.top-control-bar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: 60px;
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border-bottom: 1px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 16px;
  z-index: 900;
  box-shadow: var(--shadow-sm);
  transition: background-color 0.2s ease, border-color 0.2s ease;
}
[data-theme="dark"] .top-control-bar {
  background: rgba(17, 20, 36, 0.95);
}

.top-bar-left {
  display: flex;
  align-items: center;
  gap: 10px;
  min-width: 0;
}

.brand-badge {
  font-family: 'Outfit', sans-serif;
  font-weight: 800;
  font-size: 15px;
  background: linear-gradient(135deg, #1d4ed8, #7c3aed);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  display: flex;
  align-items: center;
  gap: 5px;
  cursor: pointer;
  white-space: nowrap;
}

.category-pill {
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: 0.5px;
  padding: 3px 8px;
  border-radius: 20px;
  text-transform: uppercase;
  white-space: nowrap;
}
.s7-tag {
  background: var(--accent-blue-light);
  color: var(--accent-blue-text);
  border: 1px solid var(--accent-blue-border);
}
.s8-tag {
  background: var(--accent-purple-light);
  color: var(--accent-purple-text);
  border: 1px solid var(--accent-purple-border);
}

.top-bar-center {
  display: flex;
  align-items: center;
  gap: 8px;
}

.slide-counter-badge {
  font-family: 'Outfit', sans-serif;
  font-size: 13.5px;
  font-weight: 700;
  color: var(--text-primary);
  background: var(--bg-secondary);
  padding: 5px 12px;
  border-radius: 20px;
  border: 1px solid var(--border-strong);
  white-space: nowrap;
  cursor: pointer;
}
.slide-counter-badge:hover {
  border-color: var(--accent-blue);
  background: var(--accent-blue-light);
  color: var(--accent-blue-text);
}

.jump-form {
  display: flex;
  align-items: center;
  gap: 4px;
  background: var(--bg-card);
  padding: 2px 6px;
  border-radius: 8px;
  border: 1px solid var(--border-strong);
  box-shadow: 0 1px 2px rgba(0,0,0,0.03);
}
.jump-form label {
  font-size: 11.5px;
  font-weight: 600;
  color: var(--text-muted);
}
.jump-input {
  width: 40px;
  background: transparent;
  border: none;
  color: var(--text-primary);
  font-family: 'JetBrains Mono', monospace;
  font-size: 13px;
  font-weight: 700;
  text-align: center;
  outline: none;
}
.jump-input::-webkit-inner-spin-button,
.jump-input::-webkit-outer-spin-button {
  -webkit-appearance: none;
  margin: 0;
}
.jump-btn {
  background: var(--accent-blue);
  color: #fff;
  border: none;
  padding: 4px 8px;
  border-radius: 5px;
  font-size: 11px;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.15s ease;
}
.jump-btn:hover {
  background: #1d4ed8;
}

.top-bar-right {
  display: flex;
  align-items: center;
  gap: 6px;
}

.nav-icon-btn {
  background: var(--bg-card);
  border: 1px solid var(--border-strong);
  color: var(--text-primary);
  padding: 6px 12px;
  border-radius: 8px;
  font-size: 12.5px;
  font-weight: 600;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 5px;
  transition: all 0.15s ease;
  box-shadow: var(--shadow-sm);
  white-space: nowrap;
}
.nav-icon-btn:hover {
  background: var(--bg-secondary);
  border-color: var(--accent-blue);
  color: var(--accent-blue);
  transform: translateY(-1px);
}
.nav-icon-btn:disabled {
  opacity: 0.35;
  cursor: not-allowed;
  transform: none;
  box-shadow: none;
}

.nav-icon-btn.primary {
  background: linear-gradient(135deg, #2563eb, #7c3aed);
  border: none;
  color: white;
  box-shadow: 0 2px 6px rgba(37, 99, 235, 0.3);
}
.nav-icon-btn.primary:hover {
  opacity: 0.95;
  transform: translateY(-1px);
}

.theme-toggle-btn {
  background: var(--bg-secondary);
  border: 1px solid var(--border-strong);
  color: var(--text-primary);
  width: 34px;
  height: 34px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 15px;
  cursor: pointer;
  transition: all 0.15s ease;
  flex-shrink: 0;
}
.theme-toggle-btn:hover {
  border-color: var(--accent-blue);
  background: var(--bg-card);
}

/* ─── SLIDE CONTAINER ─── */
.presentation-container {
  margin-top: 60px;
  min-height: calc(100vh - 60px);
  padding-bottom: 74px;
  touch-action: pan-y;
}

.presentation-slide {
  display: none;
  max-width: 1040px;
  margin: 0 auto;
  padding: 32px 20px 40px 20px;
  animation: slideFadeIn 0.2s cubic-bezier(0.16, 1, 0.3, 1);
}

.presentation-slide.active-slide {
  display: block;
}

@keyframes slideFadeIn {
  from {
    opacity: 0;
    transform: translateY(6px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* In scroll/continuous mode */
body.mode-scroll .presentation-slide {
  display: block !important;
  border-bottom: 2px dashed var(--border);
  padding-bottom: 50px;
  margin-bottom: 40px;
}

/* ─── SLIDE HEADER BLOCK ─── */
.slide-title-block {
  margin-bottom: 20px;
}

.slide-meta-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 6px;
}

.slide-num-pill {
  font-family: 'Outfit', sans-serif;
  font-size: 11.5px;
  font-weight: 700;
  color: var(--text-muted);
  letter-spacing: 0.5px;
}

.slide-h2 {
  font-family: 'Outfit', sans-serif;
  font-size: 26px;
  font-weight: 800;
  color: var(--text-primary);
  line-height: 1.3;
}

.slide-subtitle {
  font-size: 14px;
  color: var(--text-secondary);
  margin-top: 4px;
  line-height: 1.5;
}

/* ─── CARDS & COMPONENTS ─── */
.card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 14px;
  padding: 22px 26px;
  box-shadow: var(--shadow-sm);
  margin-bottom: 18px;
  transition: all 0.2s ease;
}
.card:hover {
  box-shadow: var(--shadow-md);
}

.card.s7 { border-left: 5px solid var(--accent-blue); }
.card.s8 { border-left: 5px solid var(--accent-purple); }

.card h3 {
  font-family: 'Outfit', sans-serif;
  font-size: 19px;
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: 12px;
}

.grid-2 {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 18px;
}
@media (max-width: 768px) {
  .grid-2 { grid-template-columns: 1fr; }
}

.grid-3 {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
}
@media (max-width: 860px) {
  .grid-3 { grid-template-columns: 1fr; }
}

/* ─── FORMULA BOX ─── */
.formula-box {
  background: var(--accent-blue-light);
  border: 1px solid var(--accent-blue-border);
  border-left: 4px solid var(--accent-blue);
  border-radius: 10px;
  padding: 14px 18px;
  margin: 12px 0;
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
}
.s8-formula {
  background: var(--accent-purple-light);
  border-color: var(--accent-purple-border);
  border-left-color: var(--accent-purple);
}
.formula-label {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.6px;
  color: var(--text-secondary);
  text-transform: uppercase;
  margin-bottom: 6px;
}

/* ─── CALLOUTS ─── */
.callout {
  display: flex;
  gap: 12px;
  align-items: flex-start;
  padding: 14px 16px;
  border-radius: 10px;
  margin: 14px 0;
  font-size: 13.5px;
  line-height: 1.6;
}
.callout-icon { font-size: 18px; flex-shrink: 0; }
.callout-blue { background: var(--accent-blue-light); border: 1px solid var(--accent-blue-border); color: #1e3a8a; }
[data-theme="dark"] .callout-blue { color: #c4d9ff; }
.callout-purple { background: var(--accent-purple-light); border: 1px solid var(--accent-purple-border); color: #581c87; }
[data-theme="dark"] .callout-purple { color: #e1ccff; }
.callout-green { background: var(--accent-green-light); border: 1px solid var(--accent-green-border); color: #064e3b; }
[data-theme="dark"] .callout-green { color: #c0f7d5; }
.callout-orange { background: var(--accent-orange-light); border: 1px solid var(--accent-orange-border); color: #78350f; }
[data-theme="dark"] .callout-orange { color: #ffd6b8; }

/* ─── CHIPS ─── */
.key-chips {
  display: flex;
  gap: 6px;
  flex-wrap: wrap;
}
.chip {
  font-size: 11px;
  font-weight: 700;
  padding: 2px 8px;
  border-radius: 12px;
}
.chip-blue { background: var(--accent-blue-light); color: var(--accent-blue-text); border: 1px solid var(--accent-blue-border); }
.chip-purple { background: var(--accent-purple-light); color: var(--accent-purple-text); border: 1px solid var(--accent-purple-border); }
.chip-green { background: var(--accent-green-light); color: var(--accent-green-text); border: 1px solid var(--accent-green-border); }
.chip-orange { background: var(--accent-orange-light); color: var(--accent-orange-text); border: 1px solid var(--accent-orange-border); }
.chip-pink { background: var(--accent-pink-light); color: var(--accent-pink-text); border: 1px solid var(--accent-pink-border); }
.chip-cyan { background: var(--accent-cyan-light); color: #0369a1; border: 1px solid var(--accent-cyan-border); }

/* ─── SLIDE IMAGES ─── */
.slide-img-wrap {
  background: #ffffff;
  border: 1px solid var(--border);
  border-radius: 12px;
  overflow: hidden;
  box-shadow: var(--shadow-sm);
  transition: all 0.2s ease;
}
.slide-img-wrap:hover {
  box-shadow: var(--shadow-md);
  border-color: var(--border-strong);
}
.slide-img-wrap img {
  width: 100%;
  height: auto;
  display: block;
  object-fit: contain;
  background: #ffffff;
}
.slide-img-caption {
  padding: 8px 12px;
  background: var(--bg-subtle);
  font-size: 11.5px;
  color: var(--text-secondary);
  border-top: 1px solid var(--border);
  line-height: 1.5;
}

/* ─── RESPONSIVE TABLES ─── */
.table-responsive {
  width: 100%;
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
  margin: 14px 0;
  border-radius: 10px;
  border: 1px solid var(--border);
  background: var(--bg-card);
  box-shadow: var(--shadow-sm);
}
.comparison-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 13px;
  min-width: 540px;
}
.comparison-table th {
  background: var(--bg-secondary);
  color: var(--text-primary);
  font-weight: 700;
  text-align: left;
  padding: 10px 14px;
  border-bottom: 2px solid var(--border);
  font-family: 'Outfit', sans-serif;
  white-space: nowrap;
}
.comparison-table td {
  padding: 9px 14px;
  border-bottom: 1px solid var(--border);
  color: var(--text-secondary);
}
.comparison-table tr:hover td {
  background: var(--bg-subtle);
  color: var(--text-primary);
}

/* ─── BUTTONS ─── */
.quick-nav-btn {
  background: var(--bg-card);
  border: 1px solid var(--border-strong);
  color: var(--text-primary);
  padding: 7px 12px;
  border-radius: 8px;
  font-size: 12px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.15s ease;
  box-shadow: var(--shadow-sm);
}
.quick-nav-btn:hover {
  background: var(--accent-blue-light);
  border-color: var(--accent-blue);
  color: var(--accent-blue-text);
}

/* ─── 7x7 NUMERICAL WORKSHOP ─── */
.grid-7x7-container {
  display: flex;
  flex-direction: column;
  gap: 14px;
  align-items: center;
  margin: 14px 0;
}
.grid-7x7 {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  gap: 5px;
  background: var(--bg-secondary);
  padding: 12px;
  border-radius: 12px;
  border: 1px solid var(--border-strong);
  box-shadow: var(--shadow-sm);
  max-width: 460px;
  width: 100%;
}
.cell-7x7 {
  aspect-ratio: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 6px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 12.5px;
  font-weight: 700;
  color: var(--text-primary);
  transition: all 0.15s ease;
  user-select: none;
}
.cell-coord {
  font-size: 7.5px;
  color: var(--text-muted);
  font-weight: 500;
  margin-top: 1px;
}
.cell-7x7.in-window {
  border-color: var(--accent-blue);
  background: var(--accent-blue-light);
  transform: scale(1.03);
  z-index: 2;
  box-shadow: 0 0 8px rgba(37, 99, 235, 0.25);
}
.cell-7x7.cell-center {
  border-width: 2px;
}
.cell-7x7.cell-salt {
  background: var(--accent-pink-light) !important;
  border-color: var(--accent-pink) !important;
  color: var(--accent-pink-text) !important;
  box-shadow: 0 0 10px rgba(225, 29, 72, 0.35) !important;
}
.cell-7x7.cell-pepper {
  background: var(--accent-purple-light) !important;
  border-color: var(--accent-purple) !important;
  color: var(--accent-purple-text) !important;
  box-shadow: 0 0 10px rgba(124, 58, 237, 0.35) !important;
}
.solver-tabs {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
  justify-content: center;
  margin-bottom: 14px;
}
.solver-tab-btn {
  padding: 9px 16px;
  border-radius: 8px;
  border: 1px solid var(--border-strong);
  background: var(--bg-card);
  color: var(--text-primary);
  font-family: 'Outfit', sans-serif;
  font-weight: 700;
  font-size: 12.5px;
  cursor: pointer;
  transition: all 0.15s ease;
  display: flex;
  align-items: center;
  gap: 6px;
  box-shadow: var(--shadow-sm);
}
.solver-tab-btn:hover {
  border-color: var(--accent-blue);
  background: var(--bg-secondary);
}
.solver-tab-btn.active-salt {
  background: var(--accent-pink-light);
  border-color: var(--accent-pink);
  color: var(--accent-pink-text);
}
.solver-tab-btn.active-pepper {
  background: var(--accent-purple-light);
  border-color: var(--accent-purple);
  color: var(--accent-purple-text);
}
.calculation-result-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 12px;
  margin-top: 14px;
}
.calc-card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 12px 14px;
  box-shadow: var(--shadow-sm);
  transition: transform 0.15s ease, border-color 0.15s ease;
}
.calc-card-title {
  font-size: 12px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 5px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.calc-card-formula {
  font-size: 11.5px;
  color: var(--text-secondary);
  margin-bottom: 5px;
  font-family: 'JetBrains Mono', monospace;
}
.calc-card-val {
  font-size: 19px;
  font-weight: 800;
  font-family: 'Outfit', sans-serif;
  margin-bottom: 3px;
}
.calc-card-desc {
  font-size: 11.5px;
  color: var(--text-muted);
  line-height: 1.4;
}

/* ─── QUIZ STYLES ─── */
.question-card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 18px 20px;
  box-shadow: var(--shadow-sm);
  transition: border-color 0.15s ease;
}
.question-card.correct { border-color: var(--accent-green); background: var(--accent-green-light); }
.question-card.wrong { border-color: var(--accent-pink); background: var(--accent-pink-light); }

.q-num {
  font-size: 10.5px;
  font-weight: 700;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.8px;
  margin-bottom: 6px;
}
.q-text {
  font-size: 15px;
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: 12px;
  line-height: 1.45;
}
.q-options {
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.q-option {
  background: var(--bg-secondary);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 10px 14px;
  color: var(--text-primary);
  font-size: 13.5px;
  font-weight: 500;
  text-align: left;
  cursor: pointer;
  transition: all 0.15s ease;
}
.q-option:hover:not(:disabled) {
  border-color: var(--accent-blue);
  background: var(--accent-blue-light);
  color: var(--accent-blue-text);
}
.q-option.selected-correct {
  background: var(--accent-green-light) !important;
  border-color: var(--accent-green) !important;
  color: var(--accent-green-text) !important;
  font-weight: 700;
}
.q-option.selected-wrong {
  background: var(--accent-pink-light) !important;
  border-color: var(--accent-pink) !important;
  color: var(--accent-pink-text) !important;
}
.q-option.reveal-correct {
  border-color: var(--accent-green) !important;
  background: var(--accent-green-light) !important;
  color: var(--accent-green-text) !important;
  font-weight: 700;
}
.q-feedback {
  margin-top: 10px;
  padding: 10px 14px;
  border-radius: 8px;
  font-size: 12.5px;
  line-height: 1.5;
  display: none;
}
.q-feedback.show { display: block; }
.q-feedback.correct-fb { background: var(--accent-green-light); border: 1px solid var(--accent-green-border); color: var(--accent-green-text); }
.q-feedback.wrong-fb { background: var(--accent-pink-light); border: 1px solid var(--accent-pink-border); color: var(--accent-pink-text); }

.quiz-submit-btn {
  background: linear-gradient(135deg, #2563eb, #7c3aed);
  color: white;
  border: none;
  padding: 12px 24px;
  border-radius: 8px;
  font-family: 'Outfit', sans-serif;
  font-size: 14.5px;
  font-weight: 700;
  cursor: pointer;
  display: inline-block;
  transition: all 0.15s ease;
  box-shadow: 0 4px 14px rgba(37, 99, 235, 0.3);
}

/* ─── FIXED BOTTOM NAV BAR ─── */
.bottom-floating-bar {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  height: 54px;
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border-top: 1px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 16px;
  padding-bottom: env(safe-area-inset-bottom, 0px);
  z-index: 850;
  box-shadow: 0 -2px 10px rgba(0,0,0,0.03);
}
[data-theme="dark"] .bottom-floating-bar {
  background: rgba(17, 20, 36, 0.95);
}

.bottom-center {
  display: flex;
  align-items: center;
  gap: 12px;
}

.key-hint {
  font-size: 11.5px;
  color: var(--text-muted);
  display: flex;
  align-items: center;
  gap: 5px;
}
.key-badge {
  background: var(--bg-secondary);
  border: 1px solid var(--border-strong);
  padding: 2px 5px;
  border-radius: 4px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 10.5px;
  font-weight: 600;
  color: var(--text-secondary);
}

/* ─── SLIDE INDEX DRAWER MODAL ─── */
.index-drawer-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(15, 23, 42, 0.5);
  backdrop-filter: blur(6px);
  z-index: 1200;
  display: none;
  align-items: center;
  justify-content: center;
  padding: 16px;
}
.index-drawer-overlay.open {
  display: flex;
}
.index-drawer {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 16px;
  max-width: 820px;
  width: 100%;
  max-height: 85vh;
  display: flex;
  flex-direction: column;
  box-shadow: var(--shadow-lg);
  overflow: hidden;
  animation: modalPop 0.15s ease-out;
}
@keyframes modalPop {
  from { transform: scale(0.96); opacity: 0; }
  to { transform: scale(1); opacity: 1; }
}
.index-drawer-header {
  padding: 16px 20px;
  border-bottom: 1px solid var(--border);
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: var(--bg-secondary);
}
.index-drawer-header h3 {
  font-family: 'Outfit', sans-serif;
  font-size: 17px;
  font-weight: 700;
  margin: 0;
}
.close-drawer-btn {
  background: transparent;
  border: none;
  color: var(--text-muted);
  font-size: 24px;
  cursor: pointer;
  padding: 4px;
  line-height: 1;
}
.close-drawer-btn:hover { color: var(--text-primary); }
.index-drawer-body {
  padding: 16px 20px;
  overflow-y: auto;
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(230px, 1fr));
  gap: 10px;
}
.index-slide-item {
  background: var(--bg-secondary);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 10px 12px;
  cursor: pointer;
  transition: all 0.15s ease;
  display: flex;
  flex-direction: column;
  gap: 3px;
}
.index-slide-item:hover {
  border-color: var(--accent-blue);
  background: var(--accent-blue-light);
}
.index-slide-item.active {
  border-color: var(--accent-blue);
  background: var(--accent-blue-light);
  box-shadow: 0 0 0 2px var(--accent-blue-border);
}
.index-slide-num {
  font-size: 10.5px;
  font-weight: 700;
  color: var(--text-muted);
}
.index-slide-title {
  font-size: 12.5px;
  font-weight: 700;
  color: var(--text-primary);
  line-height: 1.35;
}

/* ─── COMPREHENSIVE MOBILE OPTIMIZATIONS ─── */
@media (max-width: 680px) {
  .top-control-bar {
    height: 52px;
    padding: 0 12px;
  }
  .brand-badge {
    font-size: 14px;
  }
  .category-pill {
    display: none; /* Hide category pill in top bar on small mobile to avoid crowd */
  }
  .top-bar-center {
    gap: 4px;
  }
  .slide-counter-badge {
    font-size: 12px;
    padding: 4px 10px;
  }
  .jump-form {
    display: none; /* Accessible in bottom bar and index modal */
  }
  .desktop-only-btn {
    display: none !important;
  }
  
  .presentation-container {
    margin-top: 52px;
    padding-bottom: 68px;
  }
  .presentation-slide {
    padding: 18px 12px 30px 12px;
  }
  .slide-h2 {
    font-size: 20px;
  }
  .slide-subtitle {
    font-size: 13px;
  }
  
  .card {
    padding: 16px 14px;
    border-radius: 12px;
    margin-bottom: 14px;
  }
  .card h3 {
    font-size: 17px;
  }
  
  .bottom-floating-bar {
    height: 54px;
    padding: 0 10px;
  }
  .bottom-floating-bar .nav-icon-btn {
    padding: 8px 16px;
    font-size: 13.5px;
    font-weight: 700;
    border-radius: 8px;
    min-height: 38px;
  }
  .key-hint {
    display: none; /* Hide keyboard text on mobile */
  }
  .mobile-bottom-counter {
    display: block !important;
    font-family: 'Outfit', sans-serif;
    font-size: 13px;
    font-weight: 700;
    color: var(--text-muted);
  }

  .grid-7x7 {
    padding: 8px;
    gap: 4px;
  }
  .cell-7x7 {
    font-size: 11px;
    border-radius: 4px;
  }
  .cell-coord {
    font-size: 6.5px;
  }
  .solver-tabs {
    flex-direction: column;
    width: 100%;
  }
  .solver-tab-btn {
    width: 100%;
    justify-content: center;
    padding: 8px 12px;
  }
  
  .index-drawer-body {
    grid-template-columns: 1fr;
    padding: 12px 14px;
  }
}

.mobile-bottom-counter {
  display: none;
}
</style>
</head>
<body>

<!-- Progress Bar -->
<div class="slide-progress-bar" id="progress-bar"></div>

<!-- Fixed Top Control Bar -->
<header class="top-control-bar">
  <div class="top-bar-left">
    <div class="brand-badge" onclick="goToSlide(1)">
      <span>🎓</span> DIP
    </div>
    <span class="category-pill s7-tag" id="top-category-pill">Slide 7</span>
  </div>

  <div class="top-bar-center">
    <div class="slide-counter-badge" id="top-counter-badge" onclick="toggleIndexDrawer()" title="Click to view all slides">Slide 1 / 38</div>
    <div class="jump-form">
      <label for="jump-slide-input">Go:</label>
      <input type="number" id="jump-slide-input" class="jump-input" min="1" max="38" value="1">
      <button class="jump-btn" onclick="handleJumpSubmit()">Go</button>
    </div>
  </div>

  <div class="top-bar-right">
    <button class="nav-icon-btn desktop-only-btn" id="btn-prev-top" onclick="prevSlide()" title="Previous Slide (Left Arrow)">◀ Prev</button>
    <button class="nav-icon-btn primary desktop-only-btn" id="btn-next-top" onclick="nextSlide()" title="Next Slide (Right Arrow / Space)">Next ▶</button>
    <button class="nav-icon-btn" onclick="toggleIndexDrawer()" title="View All Slides Index">📑 Index</button>
    <button class="nav-icon-btn desktop-only-btn" id="btn-mode-toggle" onclick="toggleViewMode()" title="Switch between Slide Deck and Scroll View">👁️ Slides</button>
    <button class="theme-toggle-btn" id="btn-theme-toggle" onclick="toggleTheme()" title="Toggle Light / Dark Theme">🌙</button>
  </div>
</header>

<!-- Main Presentation Slides Container -->
<main class="presentation-container" id="presentation-container">
<!-- SLIDES_INJECTION_POINT -->
</main>

<!-- Fixed Bottom Action Bar -->
<footer class="bottom-floating-bar">
  <button class="nav-icon-btn" id="btn-prev-bottom" onclick="prevSlide()">◀ Previous</button>
  
  <div class="bottom-center">
    <div class="key-hint">
      <span>Use</span>
      <span class="key-badge">←</span>
      <span class="key-badge">→</span>
      <span>or</span>
      <span class="key-badge">Space</span>
      <span>to flip slides &bull; Press</span>
      <span class="key-badge">G</span>
      <span>to jump</span>
    </div>
    <div class="mobile-bottom-counter" id="mobile-counter">1 / 38</div>
  </div>

  <button class="nav-icon-btn primary" id="btn-next-bottom" onclick="nextSlide()">Next ▶</button>
</footer>

<!-- Slide Index Modal / Drawer -->
<div class="index-drawer-overlay" id="index-drawer-overlay" onclick="closeIndexDrawer(event)">
  <div class="index-drawer" onclick="event.stopPropagation()">
    <div class="index-drawer-header">
      <h3>📑 Jump to Any Slide (1 – 38)</h3>
      <button class="close-drawer-btn" onclick="toggleIndexDrawer()">&times;</button>
    </div>
    <div class="index-drawer-body" id="index-drawer-body">
      <!-- Injected via JS -->
    </div>
  </div>
</div>

<script>
// ─── THEME CONTROLLER ───
let currentTheme = localStorage.getItem('dip_theme') || 'light';
document.documentElement.setAttribute('data-theme', currentTheme);

function updateThemeIcon() {
  const btn = document.getElementById('btn-theme-toggle');
  if (btn) btn.textContent = currentTheme === 'light' ? '🌙' : '☀️';
  const metaTheme = document.getElementById('theme-color-meta');
  if (metaTheme) metaTheme.setAttribute('content', currentTheme === 'light' ? '#ffffff' : '#0a0c16');
}
updateThemeIcon();

function toggleTheme() {
  currentTheme = currentTheme === 'light' ? 'dark' : 'light';
  document.documentElement.setAttribute('data-theme', currentTheme);
  localStorage.setItem('dip_theme', currentTheme);
  updateThemeIcon();
}

// ─── PRESENTATION CONTROLLER ───
const totalSlides = 38;
let currentSlide = 1;
let isScrollView = false;

const slidesData = SLIDES_DATA_JSON;

function initPresentation() {
  const drawerBody = document.getElementById('index-drawer-body');
  if (drawerBody) {
    drawerBody.innerHTML = '';
    slidesData.forEach(s => {
      const item = document.createElement('div');
      item.className = 'index-slide-item' + (s.id === currentSlide ? ' active' : '');
      item.id = 'index-item-' + s.id;
      item.onclick = () => {
        goToSlide(s.id);
        toggleIndexDrawer();
      };
      item.innerHTML = `
        <div class="index-slide-num">SLIDE ${s.id} &bull; ${s.category}</div>
        <div class="index-slide-title">${s.title}</div>
      `;
      drawerBody.appendChild(item);
    });
  }

  const hash = window.location.hash;
  if (hash && hash.startsWith('#slide-')) {
    const slideNum = parseInt(hash.replace('#slide-', ''), 10);
    if (!isNaN(slideNum) && slideNum >= 1 && slideNum <= totalSlides) {
      goToSlide(slideNum, false);
      return;
    }
  }

  goToSlide(1, false);
}

function goToSlide(n, updateHistory = true) {
  if (n < 1) n = 1;
  if (n > totalSlides) n = totalSlides;
  currentSlide = n;

  if (!isScrollView) {
    const allSlides = document.querySelectorAll('.presentation-slide');
    allSlides.forEach((el, idx) => {
      el.classList.toggle('active-slide', (idx + 1) === currentSlide);
    });
  }

  window.scrollTo({ top: 0, behavior: 'instant' });

  document.getElementById('top-counter-badge').textContent = `Slide ${currentSlide} / ${totalSlides}`;
  document.getElementById('mobile-counter').textContent = `${currentSlide} / ${totalSlides}`;
  document.getElementById('jump-slide-input').value = currentSlide;

  const currentData = slidesData[currentSlide - 1];
  const catPill = document.getElementById('top-category-pill');
  if (catPill && currentData) {
    catPill.textContent = currentData.category;
    catPill.className = 'category-pill ' + currentData.tag_class;
  }

  const progressPercent = (currentSlide / totalSlides) * 100;
  document.getElementById('progress-bar').style.width = progressPercent + '%';

  const prevTop = document.getElementById('btn-prev-top');
  const nextTop = document.getElementById('btn-next-top');
  if (prevTop) prevTop.disabled = (currentSlide === 1);
  if (nextTop) nextTop.disabled = (currentSlide === totalSlides);
  
  document.getElementById('btn-prev-bottom').disabled = (currentSlide === 1);
  document.getElementById('btn-next-bottom').disabled = (currentSlide === totalSlides);

  document.querySelectorAll('.index-slide-item').forEach(el => el.classList.remove('active'));
  const activeDrawerItem = document.getElementById('index-item-' + currentSlide);
  if (activeDrawerItem) activeDrawerItem.classList.add('active');

  if (updateHistory) {
    window.location.hash = 'slide-' + currentSlide;
  }

  if (currentSlide === 27) {
    setTimeout(renderGrid7x7, 50);
  }

  if (window.MathJax && window.MathJax.typesetPromise) {
    const activeEl = document.getElementById('slide-' + currentSlide);
    if (activeEl) MathJax.typesetPromise([activeEl]);
  }
}

function nextSlide() {
  if (currentSlide < totalSlides) goToSlide(currentSlide + 1);
}

function prevSlide() {
  if (currentSlide > 1) goToSlide(currentSlide - 1);
}

function handleJumpSubmit() {
  const input = document.getElementById('jump-slide-input');
  const val = parseInt(input.value, 10);
  if (!isNaN(val)) {
    goToSlide(val);
  }
}

document.getElementById('jump-slide-input').addEventListener('keydown', (e) => {
  if (e.key === 'Enter') {
    handleJumpSubmit();
    e.target.blur();
  }
});

function toggleViewMode() {
  isScrollView = !isScrollView;
  document.body.classList.toggle('mode-scroll', isScrollView);
  const btn = document.getElementById('btn-mode-toggle');
  if (btn) {
    btn.textContent = isScrollView ? '📄 Scroll View' : '👁️ Slides View';
    btn.classList.toggle('primary', isScrollView);
  }
  if (!isScrollView) {
    goToSlide(currentSlide);
  }
}

function toggleIndexDrawer() {
  const overlay = document.getElementById('index-drawer-overlay');
  overlay.classList.toggle('open');
}

function closeIndexDrawer(e) {
  if (e.target.id === 'index-drawer-overlay') {
    toggleIndexDrawer();
  }
}

// ─── KEYBOARD NAVIGATION ───
window.addEventListener('keydown', (e) => {
  if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;

  if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') {
    e.preventDefault();
    nextSlide();
  } else if (e.key === 'ArrowLeft' || e.key === 'Backspace' || e.key === 'PageUp') {
    e.preventDefault();
    prevSlide();
  } else if (e.key === 'Home') {
    e.preventDefault();
    goToSlide(1);
  } else if (e.key === 'End') {
    e.preventDefault();
    goToSlide(totalSlides);
  } else if (e.key.toLowerCase() === 'g' || e.key.toLowerCase() === 'j') {
    e.preventDefault();
    const input = document.getElementById('jump-slide-input');
    input.focus();
    input.select();
  } else if (e.key.toLowerCase() === 'm' || e.key.toLowerCase() === 'i') {
    e.preventDefault();
    toggleIndexDrawer();
  } else if (e.key === 'Escape') {
    const overlay = document.getElementById('index-drawer-overlay');
    if (overlay.classList.contains('open')) overlay.classList.remove('open');
  }
});

// ─── MOBILE TOUCH SWIPE GESTURES ───
let touchStartX = 0;
let touchStartY = 0;
let touchEndX = 0;
let touchEndY = 0;

document.addEventListener('touchstart', (e) => {
  touchStartX = e.changedTouches[0].screenX;
  touchStartY = e.changedTouches[0].screenY;
}, { passive: true });

document.addEventListener('touchend', (e) => {
  touchEndX = e.changedTouches[0].screenX;
  touchEndY = e.changedTouches[0].screenY;
  handleSwipe();
}, { passive: true });

function handleSwipe() {
  const diffX = touchEndX - touchStartX;
  const diffY = touchEndY - touchStartY;
  // Trigger if horizontal movement > 45px and predominantly horizontal (not vertical scroll)
  if (Math.abs(diffX) > 45 && Math.abs(diffX) > Math.abs(diffY) * 1.4) {
    if (diffX < 0) {
      nextSlide(); // Swiped left -> next slide
    } else {
      prevSlide(); // Swiped right -> prev slide
    }
  }
}

// ─── 7x7 NUMERICAL WORKSHOP LOGIC ───
const rawGrid7x7 = [
  [54, 52, 57, 55, 56, 52, 51],
  [50, 49, 51, 50, 52, 53, 58],
  [51, 204, 52, 52, 0, 57, 60],
  [48, 50, 51, 49, 53, 59, 63],
  [49, 51, 52, 55, 58, 64, 67],
  [50, 54, 57, 60, 63, 67, 70],
  [51, 55, 59, 62, 65, 69, 72]
];

let currentMode = 'salt';

function renderGrid7x7() {
  const container = document.getElementById('matrix-7x7');
  if (!container) return;
  container.innerHTML = '';

  const centerCol = currentMode === 'salt' ? 1 : 4;
  const centerRow = 2;

  for (let r = 0; r < 7; r++) {
    for (let c = 0; c < 7; c++) {
      const val = rawGrid7x7[r][c];
      const cell = document.createElement('div');
      cell.className = 'cell-7x7';

      const inWindow = Math.abs(r - centerRow) <= 1 && Math.abs(c - centerCol) <= 1;
      const isCenter = r === centerRow && c === centerCol;

      if (inWindow) cell.classList.add('in-window');
      if (isCenter) cell.classList.add('cell-center');
      if (r === 2 && c === 1) cell.classList.add('cell-salt');
      if (r === 2 && c === 4) cell.classList.add('cell-pepper');

      cell.innerHTML = `<span>${val}</span><span class="cell-coord">(${c},${r})</span>`;
      container.appendChild(cell);
    }
  }

  updateWorkshopDetails();
}

function setWorkshopMode(mode) {
  currentMode = mode;
  document.getElementById('btn-salt').className = 'solver-tab-btn' + (mode === 'salt' ? ' active-salt' : '');
  document.getElementById('btn-pepper').className = 'solver-tab-btn' + (mode === 'pepper' ? ' active-pepper' : '');
  renderGrid7x7();
}

function updateWorkshopDetails() {
  const centerCol = currentMode === 'salt' ? 1 : 4;
  const centerRow = 2;
  const targetVal = rawGrid7x7[centerRow][centerCol];
  const noiseType = currentMode === 'salt' ? 'Salt Noise (Outlier High)' : 'Pepper Noise (Outlier Low)';

  const windowVals = [];
  const matrixRows = [];
  for (let dr = -1; dr <= 1; dr++) {
    const row = [];
    for (let dc = -1; dc <= 1; dc++) {
      const v = rawGrid7x7[centerRow + dr][centerCol + dc];
      windowVals.push(v);
      row.push(v);
    }
    matrixRows.push(row);
  }

  const sortedVals = [...windowVals].sort((a,b) => a - b);
  const sumVal = windowVals.reduce((a,b) => a + b, 0);

  const detailsCard = document.getElementById('window-details-card');
  if (detailsCard) {
    detailsCard.innerHTML = `
      <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px;margin-bottom:12px;">
        <h4 style="margin:0;font-size:15.5px;font-weight:700;color:${currentMode==='salt'?'var(--accent-pink)':'var(--accent-purple)'};">
          Center Pixel (${centerCol}, ${centerRow}) = ${targetVal} [${noiseType}]
        </h4>
        <span class="category-pill ${currentMode==='salt'?'s7-tag':'s8-tag'}">Window: 3×3 (mn = 9)</span>
      </div>

      <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(180px, 1fr));gap:14px;">
        <div>
          <div style="font-size:11.5px;color:var(--text-muted);margin-bottom:5px;font-weight:700;">3×3 Spatial Window Matrix:</div>
          <div style="font-family:'JetBrains Mono',monospace;font-size:13px;background:var(--bg-secondary);padding:10px;border-radius:8px;border:1px solid var(--border);line-height:1.6;">
            [ ${matrixRows[0].map(v => v===targetVal?`<strong style="color:var(--accent-orange);">${v}</strong>`:v).join(', ')} ]<br>
            [ ${matrixRows[1].map(v => v===targetVal?`<strong style="color:var(--accent-orange);">${v}</strong>`:v).join(', ')} ]<br>
            [ ${matrixRows[2].map(v => v===targetVal?`<strong style="color:var(--accent-orange);">${v}</strong>`:v).join(', ')} ]
          </div>
        </div>
        <div>
          <div style="font-size:11.5px;color:var(--text-muted);margin-bottom:5px;font-weight:700;">Sorted Gray Levels:</div>
          <div style="font-family:'JetBrains Mono',monospace;font-size:12.5px;background:var(--bg-secondary);padding:10px;border-radius:8px;border:1px solid var(--border);line-height:1.6;word-break:break-all;">
            [ ${sortedVals.map((v, i) => i===4?`<strong style="color:var(--accent-green);border-bottom:2px solid var(--accent-green);">${v} (Med)</strong>`: (v===targetVal?`<strong style="color:var(--accent-pink);">${v}</strong>`:v)).join(', ')} ]
          </div>
          <div style="font-size:11px;color:var(--text-muted);margin-top:5px;font-weight:600;">
            Sum = ${sumVal} &bull; Min = ${sortedVals[0]} &bull; Max = ${sortedVals[8]} &bull; Med = ${sortedVals[4]}
          </div>
        </div>
      </div>
    `;
  }

  const resContainer = document.getElementById('calc-results-container');
  if (!resContainer) return;

  if (currentMode === 'salt') {
    resContainer.innerHTML = `
      <div class="calc-card">
        <div class="calc-card-title"><span style="color:var(--accent-blue);">1. Arithmetic Mean</span><span class="chip chip-orange">Poor</span></div>
        <div class="calc-card-formula">f̂ = (1/9) × 606</div>
        <div class="calc-card-val" style="color:var(--accent-orange);">67.33</div>
        <div class="calc-card-desc">The single 204 outlier corrupts the mean upwards from ~50 to 67.33. Image is blurred and remains brightened.</div>
      </div>

      <div class="calc-card">
        <div class="calc-card-title"><span style="color:var(--accent-cyan);">2. Geometric Mean</span><span class="chip chip-blue">Moderate</span></div>
        <div class="calc-card-formula">f̂ = [∏ g(s,t)]^(1/9)</div>
        <div class="calc-card-val" style="color:var(--accent-cyan);">58.70</div>
        <div class="calc-card-desc">Tolerates the high outlier slightly better than arithmetic mean, but still pulled upward.</div>
      </div>

      <div class="calc-card">
        <div class="calc-card-title"><span style="color:var(--accent-green);">3. Harmonic Mean</span><span class="chip chip-green">Good</span></div>
        <div class="calc-card-formula">f̂ = 9 / ∑(1/g)</div>
        <div class="calc-card-val" style="color:var(--accent-green);">54.81</div>
        <div class="calc-card-desc">1/204 is tiny, so salt contributes very little to the sum! Effectively suppresses salt noise.</div>
      </div>

      <div class="calc-card">
        <div class="calc-card-title"><span style="color:var(--accent-pink);">4. Contraharmonic (Q=-1.5)</span><span class="chip chip-green">Excellent</span></div>
        <div class="calc-card-formula">Q = -1.5 (Negative Q for Salt)</div>
        <div class="calc-card-val" style="color:var(--accent-green);">52.52</div>
        <div class="calc-card-desc">Negative Q heavily weights smaller pixel values, completely eliminating the 204 salt spike! (Warning: Q=+1.5 gives 127.99 disaster!)</div>
      </div>

      <div class="calc-card" style="border-color:var(--accent-green);box-shadow:0 0 12px rgba(5, 150, 105, 0.15);">
        <div class="calc-card-title"><span style="color:var(--accent-green);">5. Median Filter ⭐</span><span class="chip chip-green">Best Choice</span></div>
        <div class="calc-card-formula">f̂ = sorted[4]</div>
        <div class="calc-card-val" style="color:var(--accent-green);">51.00</div>
        <div class="calc-card-desc">204 is pushed to the far right of sorted array. 51 is the pure original background level. Flawless restoration!</div>
      </div>

      <div class="calc-card">
        <div class="calc-card-title"><span style="color:var(--accent-purple);">6. Midpoint Filter</span><span class="chip chip-orange">Poor</span></div>
        <div class="calc-card-formula">f̂ = ½(48 + 204)</div>
        <div class="calc-card-val" style="color:var(--accent-orange);">126.00</div>
        <div class="calc-card-desc">Max is 204, so the midpoint is severely ruined by the outlier (126 vs true value 50).</div>
      </div>

      <div class="calc-card">
        <div class="calc-card-title"><span style="color:var(--accent-blue);">7. Alpha-Trimmed (d=2)</span><span class="chip chip-green">Great</span></div>
        <div class="calc-card-formula">f̂ = sum(remaining 7) / 7</div>
        <div class="calc-card-val" style="color:var(--accent-green);">50.57</div>
        <div class="calc-card-desc">Trims min (48) and max (204). Remaining 7 pixels average to 50.57 — very close to true ground truth.</div>
      </div>

      <div class="calc-card">
        <div class="calc-card-title"><span style="color:var(--accent-cyan);">8. Alpha-Trimmed (d=4)</span><span class="chip chip-green">Great</span></div>
        <div class="calc-card-formula">f̂ = sum(remaining 5) / 5</div>
        <div class="calc-card-val" style="color:var(--accent-green);">50.60</div>
        <div class="calc-card-desc">Trims 2 lowest (48, 49) and 2 highest (52, 204). Outstanding noise robustness.</div>
      </div>
    `;
  } else {
    resContainer.innerHTML = `
      <div class="calc-card">
        <div class="calc-card-title"><span style="color:var(--accent-blue);">1. Arithmetic Mean</span><span class="chip chip-orange">Poor</span></div>
        <div class="calc-card-formula">f̂ = (1/9) × 425</div>
        <div class="calc-card-val" style="color:var(--accent-orange);">47.22</div>
        <div class="calc-card-desc">The 0 pepper outlier pulls down the average from ~53 to 47.22, creating a visible dark smudge.</div>
      </div>

      <div class="calc-card">
        <div class="calc-card-title"><span style="color:var(--accent-pink);">2. Geometric Mean</span><span class="chip chip-orange">Catastrophic (0.0)</span></div>
        <div class="calc-card-formula">f̂ = [0 × 50 × ...]^(1/9)</div>
        <div class="calc-card-val" style="color:var(--accent-pink);">0.00</div>
        <div class="calc-card-desc">A single 0 pixel sets the entire product to zero! The entire window turns completely black.</div>
      </div>

      <div class="calc-card">
        <div class="calc-card-title"><span style="color:var(--accent-pink);">3. Harmonic Mean</span><span class="chip chip-pink">FAILS (Div by 0)</span></div>
        <div class="calc-card-formula">1/0 → ∞ in denominator</div>
        <div class="calc-card-val" style="color:var(--accent-pink);">0.00 (Undefined)</div>
        <div class="calc-card-desc">Harmonic mean cannot handle pepper noise (zeros) because of division by zero.</div>
      </div>

      <div class="calc-card" style="border-color:var(--accent-green);box-shadow:0 0 12px rgba(5, 150, 105, 0.15);">
        <div class="calc-card-title"><span style="color:var(--accent-green);">4. Contraharmonic (Q=+1.5) ⭐</span><span class="chip chip-green">Best for Pepper</span></div>
        <div class="calc-card-formula">Q = +1.5 (Positive Q for Pepper)</div>
        <div class="calc-card-val" style="color:var(--accent-green);">53.41</div>
        <div class="calc-card-desc">0^(2.5) = 0 contributes nothing. Larger background values dominate, giving 53.41 (perfect restoration!). (Q < 0 causes div by zero).</div>
      </div>

      <div class="calc-card" style="border-color:var(--accent-green);box-shadow:0 0 12px rgba(5, 150, 105, 0.15);">
        <div class="calc-card-title"><span style="color:var(--accent-green);">5. Median Filter ⭐</span><span class="chip chip-green">Best Choice</span></div>
        <div class="calc-card-formula">f̂ = sorted[4]</div>
        <div class="calc-card-val" style="color:var(--accent-green);">52.00</div>
        <div class="calc-card-desc">0 is at index 0 of sorted array. Median is 52. Completely eliminates the pepper pixel with no blurring!</div>
      </div>

      <div class="calc-card">
        <div class="calc-card-title"><span style="color:var(--accent-purple);">6. Midpoint Filter</span><span class="chip chip-orange">Poor</span></div>
        <div class="calc-card-formula">f̂ = ½(0 + 59)</div>
        <div class="calc-card-val" style="color:var(--accent-orange);">29.50</div>
        <div class="calc-card-desc">Min is 0, so the midpoint is dragged down to 29.50 — a severe artificial dark blur.</div>
      </div>

      <div class="calc-card">
        <div class="calc-card-title"><span style="color:var(--accent-blue);">7. Alpha-Trimmed (d=2)</span><span class="chip chip-green">Great</span></div>
        <div class="calc-card-formula">f̂ = sum(remaining 7) / 7</div>
        <div class="calc-card-val" style="color:var(--accent-green);">52.29</div>
        <div class="calc-card-desc">Trims 0 and 59. Remaining 7 pixels average to 52.29. Outstanding result!</div>
      </div>

      <div class="calc-card">
        <div class="calc-card-title"><span style="color:var(--accent-cyan);">8. Alpha-Trimmed (d=4)</span><span class="chip chip-green">Great</span></div>
        <div class="calc-card-formula">f̂ = sum(remaining 5) / 5</div>
        <div class="calc-card-val" style="color:var(--accent-green);">52.00</div>
        <div class="calc-card-desc">Trims 0, 49 and 57, 59. Remaining [50, 52, 52, 53, 53] average to exactly 52.00.</div>
      </div>
    `;
  }
}

// ─── QUIZ LOGIC ───
const answers = {};
const feedbacks = {
  1: "✅ Correct! Multiplying by (-1)^(x+y) = e^(jπ(x+y)) shifts the DFT so the DC component (zero frequency) appears at the centre of the image/spectrum — essential for visualisation and filtering.",
  2: "✅ Correct! BLPF = 1/[1+(D/D₀)²ⁿ]. At D=D₀, H=0.5 (half power). Smooth transition, no ringing.",
  3: "✅ Correct! The Ideal LPF has a sharp 'brick wall' cutoff — this abrupt discontinuity in the frequency domain causes ringing (Gibbs phenomenon) oscillations in the spatial domain output.",
  4: "✅ Correct! H_hp = 1 - H_lp. This elegant relationship means high frequencies that the LPF blocks become the pass band of the HPF.",
  5: "✅ Correct! GHPF = 1 - GLPF = 1 - e^(-D²/2D₀²). At the centre (D=0), H=0 (DC completely blocked). Smoothly increases to 1.",
  6: "✅ Correct! g(x,y) = f(x,y) + η(x,y). The observed noisy image is the original plus an additive noise term η.",
  7: "✅ Correct! The median filter is specifically designed for impulse noise. It picks the actual median value from the neighbourhood — extreme noise pixels (0 or 255) are pushed to the ends of the sorted list and ignored.",
  8: "✅ Correct! Positive Q → favours larger (brighter) values → eliminates dark (pepper) pixels. Negative Q → favours smaller values → eliminates bright (salt) pixels.",
  9: "✅ Correct! Midpoint = ½(max + min). It averages the extremes of the neighbourhood, making it effective for symmetric noise distributions like Gaussian and Uniform.",
  10: "✅ Correct! Periodic noise creates spikes at specific frequencies in the Fourier spectrum. A band-reject filter selectively removes those frequency bands, eliminating the pattern.",
  11: "✅ Correct! When d = mn-1 (trim all but one value), the filter outputs the single middle-ranked value = the median!",
  12: "✅ Correct! For GLPF: H(D₀) = e^(-D₀²/2D₀²) = e^(-1/2) = e^(-0.5) ≈ 0.607. (Note: Butterworth cuts at H=0.5, but Gaussian cuts at H≈0.607)",
  13: "✅ Correct! FFT = O(N log N) — a massive improvement over O(N²) DFT, providing 100-600× speedup for practical image sizes.",
  14: "✅ Correct! Level A: A1 = z_med - z_min, A2 = z_med - z_max. If A1>0 AND A2<0, then z_min < z_med < z_max, meaning the median is NOT an extreme (not impulse) → safe to use. Otherwise expand window.",
  15: "✅ Correct! Restoration is more objective — it uses a mathematical model of the degradation (noise model, blur function) and tries to invert it. Enhancement is subjective — aimed at making images look better to humans without needing a specific model."
};

const wrongFeedbacks = {
  1: "❌ The purpose is to CENTRE the DFT spectrum — moving the DC component to the middle of the image for easier filtering.",
  2: "❌ The Butterworth LPF formula is H = 1/[1+(D/D₀)²ⁿ]. Option A is Gaussian LPF, B is Ideal LPF, D is Gaussian HPF.",
  3: "❌ It's the Ideal LPF! The abrupt frequency cutoff (brick wall) is the cause of ringing. Gaussian filters have NO ringing.",
  4: "❌ The correct relationship is H_hp = 1 - H_lp (complement). Think: what LPF blocks, HPF passes.",
  5: "❌ The GHPF is 1 - GLPF = 1 - e^(-D²/2D₀²). Option A is GLPF, B is Butterworth HPF, D is Laplacian.",
  6: "❌ The additive noise model is g = f + η (plus, not multiply or divide). The word 'additive' is a big hint!",
  7: "❌ Mean filters blur the image, reducing noise but also smearing edges. The median filter is special — it picks a real pixel value, so it removes impulse noise without blurring.",
  8: "❌ Positive Q removes pepper (dark) noise by favouring larger values. Negative Q removes salt (bright) noise.",
  9: "❌ The midpoint = ½(max + min). The median is the middle sorted value, and arithmetic mean is the average of all.",
  10: "❌ Periodic noise creates specific frequency spikes best attacked in the frequency domain with a band-reject filter, not spatial domain methods.",
  11: "❌ When d = mn-1, only one value remains — the middle-sorted one. That's the MEDIAN definition!",
  12: "❌ For Gaussian LPF: H(D₀) = e^(-0.5) ≈ 0.607. It's Butterworth that cuts at exactly 0.5 (half-power).",
  13: "❌ FFT achieves O(N log N) — the landmark improvement that made Fourier-based processing practical.",
  14: "❌ Level A checks if the MEDIAN z_med is reliable (not an impulse itself). Level B (if you pass Level A) checks whether z_xy itself is an impulse.",
  15: "❌ Restoration is more objective/model-based. Enhancement is subjective — no formal degradation model required."
};

function answer(q, btn, isCorrect) {
  const allBtns = btn.closest('.q-options').querySelectorAll('.q-option');
  allBtns.forEach(b => b.disabled = true);

  const fb = document.getElementById('fb-' + q);
  const card = document.getElementById('qc-' + q);

  if (isCorrect) {
    btn.classList.add('selected-correct');
    fb.textContent = feedbacks[q];
    fb.className = 'q-feedback show correct-fb';
    card.classList.add('correct');
    answers[q] = true;
  } else {
    btn.classList.add('selected-wrong');
    fb.textContent = wrongFeedbacks[q];
    fb.className = 'q-feedback show wrong-fb';
    card.classList.add('wrong');
    answers[q] = false;
    allBtns.forEach(b => {
      if (b.onclick.toString().includes('true')) {
        b.classList.add('reveal-correct');
      }
    });
  }

  if (window.MathJax) MathJax.typesetPromise([fb]);
}

function submitQuiz() {
  let score = 0;
  for (let i = 1; i <= 15; i++) {
    if (answers[i] === true) score++;
  }

  const numEl = document.getElementById('score-num');
  const labelEl = document.getElementById('score-label');

  numEl.textContent = score + '/15';
  
  let msg = '';
  if (score >= 13) msg = '🏆 Outstanding! Ready for a guaranteed 10/10 in the class test!';
  else if (score >= 10) msg = '👍 Strong grasp! Review the questions you missed on Slides 35-37.';
  else if (score >= 7) msg = '📚 Decent foundation! Go through Slides 4, 22, 27 and try again.';
  else msg = '💪 Review the slides from the start and test yourself again!';

  labelEl.innerHTML = `<strong>${msg}</strong><br><span style="color:var(--text-muted);font-size:13px;margin-top:6px;display:block;">Accuracy: ${Math.round(score/15*100)}%</span>`;

  numEl.style.color = score >= 13 ? 'var(--accent-green)' : score >= 10 ? 'var(--accent-blue)' : 'var(--accent-orange)';
}

window.addEventListener('DOMContentLoaded', initPresentation);
</script>

</body>
</html>
"""

# Construct the slide HTML blocks
slides_html = []
for s in slides_data:
    slide_block = f"""
  <div class="presentation-slide" id="slide-{s['id']}" data-slide="{s['id']}">
    <div class="slide-title-block">
      <div class="slide-meta-row">
        <span class="category-pill {s['tag_class']}">{s['category']}</span>
        <span class="slide-num-pill">SLIDE {s['id']} OF 38</span>
      </div>
      <h2 class="slide-h2">{s['title']}</h2>
      <div class="slide-subtitle">{s['subtitle']}</div>
    </div>
    {s['content']}
  </div>
"""
    slides_html.append(slide_block)

full_slides_markup = "\n".join(slides_html)

slides_json_str = json.dumps([{"id": s["id"], "category": s["category"], "tag_class": s["tag_class"], "title": s["title"]} for s in slides_data])

final_html = html_template.replace("<!-- SLIDES_INJECTION_POINT -->", full_slides_markup)
final_html = final_html.replace("SLIDES_DATA_JSON", slides_json_str)

# Write to both dip_mastery_guide.html and index.html
with open("dip_mastery_guide.html", "w", encoding="utf-8") as f:
    f.write(final_html)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(final_html)

print("Generated mobile-first dip_mastery_guide.html and index.html successfully! Length:", len(final_html))
