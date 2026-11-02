# -*- coding: utf-8 -*-
import sys

# Define all 38 slides metadata and content
slides_data = [
    {
        "id": 1,
        "category": "WELCOME & ROADMAP",
        "tag_class": "s7-tag",
        "title": "🎓 DIP Class Test Mastery: Complete Slide Deck",
        "subtitle": "Slide 7: Frequency Domain Filtering & Slide 8: Image Restoration & Noise Removal",
        "content": r"""
        <div class="card s7">
          <div style="display:flex;align-items:center;gap:16px;flex-wrap:wrap;margin-bottom:20px;">
            <div style="font-size:42px;">🎯</div>
            <div>
              <h3 style="margin:0;font-size:24px;color:var(--text-primary);">Guaranteed 10/10 Class Test Study System</h3>
              <p style="margin:4px 0 0;color:var(--text-secondary);font-size:14px;">Presentation Slide Mode &bull; Use &larr; &rarr; or Spacebar to flip slides &bull; Enter slide number above to jump</p>
            </div>
          </div>

          <div class="grid-3" style="margin:20px 0;">
            <div class="calc-card" style="border-color:var(--accent-blue);">
              <div class="calc-card-title"><span style="color:var(--accent-blue);">Slide 7 Coverage</span><span class="chip chip-blue">66 Slides</span></div>
              <p style="color:var(--text-secondary);font-size:13px;line-height:1.6;">
                &bull; 2D Fourier Transform & Centering<br>
                &bull; Smoothing LPFs: Ideal, Butterworth, Gaussian<br>
                &bull; Sharpening HPFs: Ideal, Butterworth, Gaussian<br>
                &bull; Laplacian & High-Frequency Emphasis<br>
                &bull; FFT Algorithm & Template Matching
              </p>
            </div>
            <div class="calc-card" style="border-color:var(--accent-purple);">
              <div class="calc-card-title"><span style="color:var(--accent-purple);">Slide 8 Coverage</span><span class="chip chip-purple">46 Slides</span></div>
              <p style="color:var(--text-secondary);font-size:13px;line-height:1.6;">
                &bull; Image Restoration vs Enhancement<br>
                &bull; 6 Noise Probability Density Functions<br>
                &bull; Mean Filters: Arithmetic, Geometric, Harmonic, Contraharmonic<br>
                &bull; Order Statistics: Median, Max, Min, Midpoint, Alpha-Trimmed<br>
                &bull; Periodic Noise & Band-Reject Filters<br>
                &bull; Adaptive Median Filter (2-Level AMF)
              </p>
            </div>
            <div class="calc-card" style="border-color:var(--accent-green);">
              <div class="calc-card-title"><span style="color:var(--accent-green);">Exam Weapons</span><span class="chip chip-green">10/10 Score</span></div>
              <p style="color:var(--text-secondary);font-size:13px;line-height:1.6;">
                &bull; <strong>Slide 27</strong>: Solved 7&times;7 Blackboard Slide Math Problem<br>
                &bull; <strong>Slide 32-34</strong>: Formula Cheat Sheets & Memory Hooks<br>
                &bull; <strong>Slide 35-38</strong>: 15-Question Interactive Mock Exam<br>
                &bull; 32 Original Slide Graphics Embedded
              </p>
            </div>
          </div>

          <div class="callout callout-blue">
            <span class="callout-icon">🚀</span>
            <div>
              <strong>Quick Module Navigation (Click to Jump Directly):</strong>
              <div style="display:flex;gap:10px;flex-wrap:wrap;margin-top:10px;">
                <button class="quick-nav-btn" onclick="goToSlide(2)">Slide 2: Prerequisites</button>
                <button class="quick-nav-btn" onclick="goToSlide(4)">Slide 4: Slide 7 Intro</button>
                <button class="quick-nav-btn" onclick="goToSlide(7)">Slide 7: Low-Pass Filters</button>
                <button class="quick-nav-btn" onclick="goToSlide(11)">Slide 11: High-Pass Filters</button>
                <button class="quick-nav-btn" onclick="goToSlide(18)">Slide 18: Slide 8 Intro</button>
                <button class="quick-nav-btn" onclick="goToSlide(21)">Slide 21: Mean Filters</button>
                <button class="quick-nav-btn" onclick="goToSlide(24)">Slide 24: Order Statistics</button>
                <button class="quick-nav-btn" onclick="goToSlide(27)" style="border-color:var(--accent-pink);color:#ff94c9;">Slide 27: 🧮 7×7 Blackboard Math</button>
                <button class="quick-nav-btn" onclick="goToSlide(30)">Slide 30: Adaptive Median</button>
                <button class="quick-nav-btn" onclick="goToSlide(32)">Slide 32: Cheat Sheet</button>
                <button class="quick-nav-btn" onclick="goToSlide(35)" style="border-color:var(--accent-green);color:var(--accent-green);">Slide 35: 🎯 15-Q Quiz</button>
              </div>
            </div>
          </div>
        </div>
        """
    },
    {
        "id": 2,
        "category": "PREREQUISITES",
        "tag_class": "s7-tag",
        "title": "📸 Prerequisites: Digital Images & Frequency Concept",
        "subtitle": "What is an image mathematically, and what does 'frequency' mean in an image?",
        "content": r"""
        <div class="grid-2">
          <div class="card">
            <h3>📸 What is a Digital Image?</h3>
            <p>Mathematically, a 2D image is represented as a 2D intensity function:</p>
            <div class="formula-box">
              <div class="formula-label">Image Function</div>
              $$f(x, y)$$
            </div>
            <ul style="color:var(--text-secondary);font-size:13px;line-height:1.7;margin-top:10px;">
              <li>$(x,y)$ are discrete spatial (pixel) coordinates.</li>
              <li>$f(x,y)$ is the <strong>intensity (gray level)</strong> at that pixel.</li>
              <li>For standard 8-bit images: $f(x,y) \in [0, 255]$ ($0 =$ pure black, $255 =$ pure white).</li>
              <li>Dimensions: $M$ rows (height) &times; $N$ columns (width).</li>
            </ul>
          </div>

          <div class="card">
            <h3>🌊 What is Frequency in Images?</h3>
            <p>In audio, frequency is pitch (cycles per second). In images, <strong>spatial frequency is the rate of brightness change over distance (pixels)</strong>:</p>
            <div class="grid-2" style="margin-top:12px;">
              <div style="background:var(--bg-secondary);padding:12px;border-radius:8px;border:1px solid var(--border);">
                <div style="color:var(--accent-cyan);font-weight:700;margin-bottom:6px;">Low Spatial Frequencies:</div>
                <p style="font-size:12px;color:var(--text-secondary);margin:0;">Slow, gradual brightness changes. Uniform areas (flat sky, skin tone, walls, background). Carries general contrast & lighting.</p>
              </div>
              <div style="background:var(--bg-secondary);padding:12px;border-radius:8px;border:1px solid var(--border);">
                <div style="color:var(--accent-pink);font-weight:700;margin-bottom:6px;">High Spatial Frequencies:</div>
                <p style="font-size:12px;color:var(--text-secondary);margin:0;">Rapid, abrupt brightness changes over few pixels. Sharp edges, fine textures, hair, corners & <strong>noise</strong>!</p>
              </div>
            </div>
            <div class="callout callout-blue" style="margin-top:14px;">
              <span class="callout-icon">💡</span>
              <p><strong>Core Rule:</strong> Filtering out high frequencies = Blurring / Smoothing. Filtering out low frequencies = Edge Sharpening!</p>
            </div>
          </div>
        </div>
        """
    },
    {
        "id": 3,
        "category": "PREREQUISITES",
        "tag_class": "s7-tag",
        "title": "⚙️ Prerequisites: Convolution Theorem & Enhancement vs Restoration",
        "subtitle": "The mathematical foundation that links spatial domain and frequency domain",
        "content": r"""
        <div class="grid-2">
          <div class="card">
            <h3>🔑 The Convolution Theorem</h3>
            <p>Spatial filtering slides a mask (kernel) $h(x,y)$ across the image, computing weighted sums at every pixel (convolution):</p>
            <div class="formula-box">
              <div class="formula-label">The Convolution Theorem (Exam Favorite!)</div>
              $$f(x,y) \star h(x,y) \;\Longleftrightarrow\; F(u,v) \cdot H(u,v)$$
            </div>
            <p style="color:var(--text-secondary);font-size:13px;margin-top:10px;">
              <strong>Profound Meaning:</strong> Convolution in the spatial domain is equivalent to simple pointwise <strong>multiplication</strong> in the frequency domain!
            </p>
            <div class="callout callout-green" style="margin-top:12px;">
              <span class="callout-icon">⚡</span>
              <p>For large kernel masks, computing pointwise multiplication in frequency domain via FFT is orders of magnitude faster than spatial convolution!</p>
            </div>
          </div>

          <div class="card">
            <h3>🔧 Enhancement vs. Restoration</h3>
            <p>Professors love asking this fundamental distinction on exams:</p>
            <table class="comparison-table" style="margin-top:10px;">
              <thead>
                <tr><th>Aspect</th><th>Image Enhancement (Slide 7)</th><th>Image Restoration (Slide 8)</th></tr>
              </thead>
              <tbody>
                <tr><td>Nature</td><td><strong>Subjective</strong> (heuristic)</td><td><strong>Objective</strong> (mathematical)</td></tr>
                <tr><td>Goal</td><td>Make image look better to human eye</td><td>Recover original scene $f(x,y)$</td></tr>
                <tr><td>Model</td><td>No degradation model needed</td><td>Requires degradation/noise model</td></tr>
                <tr><td>Technique</td><td>Contrast stretch, unsharp mask</td><td>Inverse filter, Wiener, AMF</td></tr>
              </tbody>
            </table>
          </div>
        </div>
        """
    },
    {
        "id": 4,
        "category": "SLIDE 7: FREQUENCY FILTERING",
        "tag_class": "s7-tag",
        "title": "🔄 Slide 7: The 6-Step Frequency Domain Filtering Protocol",
        "subtitle": "The standard protocol for filtering images in the frequency domain",
        "content": r"""
        <div class="card s7">
          <div class="grid-2">
            <div>
              <h3>🔄 The 6-Step Protocol (Memorize for Exam!)</h3>
              <ol style="color:var(--text-primary);font-size:14px;line-height:1.8;padding-left:20px;">
                <li><strong>Pre-process (Centering):</strong> Multiply input image $f(x,y)$ by $(-1)^{x+y}$ to shift the DC component to $(M/2, N/2)$.</li>
                <li><strong>Compute DFT:</strong> Calculate 2D DFT $F(u,v)$ of the centered image.</li>
                <li><strong>Filter Multiplication:</strong> Multiply $F(u,v)$ by filter transfer function $H(u,v)$:
                  $$G(u,v) = H(u,v) \cdot F(u,v)$$</li>
                <li><strong>Compute IDFT:</strong> Calculate inverse 2D DFT of $G(u,v)$.</li>
                <li><strong>Extract Real Part:</strong> $g_r(x,y) = \text{Re}\{\text{IDFT}\}$.</li>
                <li><strong>Post-process (De-centering):</strong> Multiply by $(-1)^{x+y}$ to restore original spatial coordinates.</li>
              </ol>
            </div>
            <div>
              <div class="slide-img-wrap">
                <img src="slides_images/slide7_page_07.png" alt="6-step frequency filtering diagram">
                <div class="slide-img-caption"><strong>Slide 7 Page 7</strong>: The official 6-step frequency domain filtering block diagram.</div>
              </div>
            </div>
          </div>
          <div class="callout callout-blue" style="margin-top:16px;">
            <span class="callout-icon">💡</span>
            <p><strong>Why $(-1)^{x+y}$?</strong> By the Fourier shift theorem, multiplying by $(-1)^{x+y} = e^{j\pi(x+y)}$ shifts the Fourier transform by $(M/2, N/2)$, placing the zero-frequency DC component at the visual center of the spectrum!</p>
          </div>
        </div>
        """
    },
    {
        "id": 5,
        "category": "SLIDE 7: FREQUENCY FILTERING",
        "tag_class": "s7-tag",
        "title": "📐 The Discrete Fourier Transform (1D & 2D DFT)",
        "subtitle": "Equations for transforming discrete images into their spatial frequency spectrum",
        "content": r"""
        <div class="grid-2">
          <div class="card s7">
            <h3>1D DFT (Foundation)</h3>
            <p style="color:var(--text-secondary);font-size:13px;">For a discrete 1D sequence $f(x)$ of length $N$ ($x, u = 0, 1, \dots, N-1$):</p>
            <div class="formula-box">
              <div class="formula-label">1D Forward DFT</div>
              $$F(u) = \frac{1}{N} \sum_{x=0}^{N-1} f(x) e^{-j 2\pi u x / N}$$
            </div>
            <div class="formula-box" style="margin-top:12px;">
              <div class="formula-label">1D Inverse DFT (IDFT)</div>
              $$f(x) = \sum_{u=0}^{N-1} F(u) e^{j 2\pi u x / N}$$
            </div>
            <p style="color:var(--text-secondary);font-size:12px;margin-top:8px;">Euler's formula: $e^{j\theta} = \cos\theta + j\sin\theta$. Fourier transform decomposes the signal into sums of orthogonal sines and cosines.</p>
          </div>

          <div class="card s7">
            <h3>2D DFT (For Digital Images)</h3>
            <p style="color:var(--text-secondary);font-size:13px;">For an $M \times N$ digital image $f(x,y)$ ($u=0\dots M-1$, $v=0\dots N-1$):</p>
            <div class="formula-box">
              <div class="formula-label">2D Forward DFT</div>
              $$F(u,v) = \frac{1}{MN} \sum_{x=0}^{M-1} \sum_{y=0}^{N-1} f(x,y) e^{-j 2\pi \left(\frac{ux}{M} + \frac{vy}{N}\right)}$$
            </div>
            <div class="formula-box" style="margin-top:12px;">
              <div class="formula-label">2D Inverse DFT (IDFT)</div>
              $$f(x,y) = \sum_{u=0}^{M-1} \sum_{v=0}^{N-1} F(u,v) e^{j 2\pi \left(\frac{ux}{M} + \frac{vy}{N}\right)}$$
            </div>
            <p style="color:var(--text-secondary);font-size:12px;margin-top:8px;">Separability: 2D DFT can be computed by applying 1D DFT to each row, then 1D DFT to each resulting column!</p>
          </div>
        </div>
        """
    },
    {
        "id": 6,
        "category": "SLIDE 7: FREQUENCY FILTERING",
        "tag_class": "s7-tag",
        "title": "📊 The Fourier Spectrum, Centering & Distance D(u,v)",
        "subtitle": "How to visualize Fourier components and compute frequency distance",
        "content": r"""
        <div class="grid-2">
          <div class="card s7">
            <h3>📊 Understanding the Fourier Spectrum</h3>
            <p style="color:var(--text-secondary);font-size:13px;">Since $F(u,v)$ is complex ($F = R + jI$), we visualize the magnitude (spectrum):</p>
            <div class="formula-box">
              <div class="formula-label">Fourier Spectrum & Power Spectrum</div>
              $$|F(u,v)| = \sqrt{R^2(u,v) + I^2(u,v)}, \quad P(u,v) = |F(u,v)|^2$$
            </div>
            <div class="formula-box" style="margin-top:10px;">
              <div class="formula-label">The DC Component (Zero Frequency)</div>
              $$F(0,0) = \frac{1}{MN} \sum_{x=0}^{M-1} \sum_{y=0}^{N-1} f(x,y) = \bar{f} \quad (\text{Average image brightness!})$$
            </div>
            <div class="formula-box" style="margin-top:10px;">
              <div class="formula-label">Distance from Center D(u,v)</div>
              $$D(u,v) = \sqrt{\left(u - \frac{M}{2}\right)^2 + \left(v - \frac{N}{2}\right)^2}$$
            </div>
          </div>
          <div>
            <div class="slide-img-wrap">
              <img src="slides_images/slide7_page_15.png" alt="Centered Fourier Spectrum">
              <div class="slide-img-caption"><strong>Slide 7 Page 15</strong>: The centered Fourier spectrum $|F(u,v)|$. The bright central point is the DC component $F(0,0)$. Frequencies increase outward radially as $D(u,v)$ increases.</div>
            </div>
          </div>
        </div>
        """
    },
    {
        "id": 7,
        "category": "SLIDE 7: FREQUENCY FILTERING",
        "tag_class": "s7-tag",
        "title": "🌊 Low-Pass Filters: Ideal LPF (ILPF) & Ringing Effect",
        "subtitle": "Brick-wall frequency cutoff and why it produces Gibbs phenomenon ringing",
        "content": r"""
        <div class="card s7">
          <div class="grid-2">
            <div>
              <h3>Ideal Low-Pass Filter (ILPF)</h3>
              <p style="color:var(--text-secondary);font-size:13px;">Completely passes all frequencies inside circle of radius $D_0$, and completely blocks all frequencies outside:</p>
              <div class="formula-box">
                <div class="formula-label">ILPF Transfer Function</div>
                $$H(u,v) = \begin{cases} 1 & \text{if } D(u,v) \le D_0 \\ 0 & \text{if } D(u,v) > D_0 \end{cases}$$
              </div>
              <div class="key-chips" style="margin:12px 0;">
                <span class="chip chip-orange">Cutoff: D₀</span>
                <span class="chip chip-pink">Severe Ringing Artefacts</span>
                <span class="chip chip-blue">Sharp Transition</span>
              </div>
              <div class="callout callout-orange">
                <span class="callout-icon">⚠️</span>
                <p><strong>Gibbs Phenomenon (Ringing):</strong> The sharp rectangular cutoff in frequency corresponds to a 2D sinc ($J_1(r)/r$) function in spatial domain. Its concentric ripple lobes create visible ringing halos around edges!</p>
              </div>
            </div>
            <div>
              <div class="slide-img-wrap">
                <img src="slides_images/slide7_page_26.png" alt="ILPF ringing on image">
                <div class="slide-img-caption"><strong>Slide 7 Page 26</strong>: ILPF applied at various $D_0$. Notice the severe concentric ringing rings caused by the abrupt brick-wall cutoff!</div>
              </div>
            </div>
          </div>
        </div>
        """
    },
    {
        "id": 8,
        "category": "SLIDE 7: FREQUENCY FILTERING",
        "tag_class": "s7-tag",
        "title": "🌊 Butterworth Low-Pass Filter (BLPF)",
        "subtitle": "Smooth roll-off filter with adjustable order n to eliminate ringing",
        "content": r"""
        <div class="card s7">
          <div class="grid-2">
            <div>
              <h3>Butterworth Low-Pass Filter (BLPF)</h3>
              <p style="color:var(--text-secondary);font-size:13px;">Provides a smooth transition between passed and filtered frequencies without sharp discontinuities:</p>
              <div class="formula-box">
                <div class="formula-label">BLPF of Order n with Cutoff D₀ (Exam Essential!)</div>
                $$H(u,v) = \frac{1}{1 + \left[\frac{D(u,v)}{D_0}\right]^{2n}}$$
              </div>
              <div class="key-chips" style="margin:12px 0;">
                <span class="chip chip-blue">At D = D₀: H = 0.5 (-3 dB)</span>
                <span class="chip chip-green">n = 1: Zero Ringing</span>
                <span class="chip chip-orange">Higher n: Approximates ILPF</span>
              </div>
              <p style="color:var(--text-secondary);font-size:13px;line-height:1.6;">
                <strong>Order $n$ behavior:</strong><br>
                &bull; At $n=1$: completely smooth roll-off, zero ringing.<br>
                &bull; At $n=2$: very mild, negligible ringing.<br>
                &bull; As $n \to \infty$: BLPF converges to the Ideal LPF (ringing becomes severe).
              </p>
            </div>
            <div>
              <div class="slide-img-wrap">
                <img src="slides_images/slide7_page_30.png" alt="BLPF comparison across orders">
                <div class="slide-img-caption"><strong>Slide 7 Page 30</strong>: BLPF comparison across orders $n=1, 2, 5, 20$. Notice order 1 and 2 produce clean blurring with no visible ringing rings!</div>
              </div>
            </div>
          </div>
        </div>
        """
    },
    {
        "id": 9,
        "category": "SLIDE 7: FREQUENCY FILTERING",
        "tag_class": "s7-tag",
        "title": "🌊 Gaussian Low-Pass Filter (GLPF)",
        "subtitle": "The king of smooth blurring: mathematically guaranteed zero ringing",
        "content": r"""
        <div class="card s7">
          <div class="grid-2">
            <div>
              <h3>Gaussian Low-Pass Filter (GLPF)</h3>
              <p style="color:var(--text-secondary);font-size:13px;">Uses a 2D Gaussian bell curve as its transfer function:</p>
              <div class="formula-box">
                <div class="formula-label">GLPF Transfer Function</div>
                $$H(u,v) = e^{-\frac{D^2(u,v)}{2 D_0^2}}$$
              </div>
              <div class="key-chips" style="margin:12px 0;">
                <span class="chip chip-green">⭐ 100% Ringing-Free</span>
                <span class="chip chip-cyan">At D = D₀: H = e^(-0.5) ≈ 0.607</span>
              </div>
              <div class="callout callout-green">
                <span class="callout-icon">🏆</span>
                <p><strong>Why Gaussian NEVER Rings:</strong> The inverse Fourier transform of a Gaussian is another Gaussian! Since a spatial Gaussian is purely positive with zero oscillating side-lobes, it is impossible for ringing ripples to appear.</p>
              </div>
            </div>
            <div>
              <div class="slide-img-wrap">
                <img src="slides_images/slide7_page_35.png" alt="GLPF 3D bell curve">
                <div class="slide-img-caption"><strong>Slide 7 Page 35</strong>: 3D perspective and cross-section of the Gaussian Low-Pass Filter. Smooth decay to zero at high frequencies.</div>
              </div>
            </div>
          </div>
        </div>
        """
    },
    {
        "id": 10,
        "category": "SLIDE 7: FREQUENCY FILTERING",
        "tag_class": "s7-tag",
        "title": "📊 Low-Pass Filters Comparison & Real Applications",
        "subtitle": "Side-by-side comparison table and practical applications from the lecture slides",
        "content": r"""
        <div class="card s7">
          <div class="table-responsive"><table class="comparison-table">
            <thead>
              <tr><th>Filter</th><th>Formula $H(u,v)$</th><th>Value at $D=D_0$</th><th>Ringing Artefacts</th><th>Transition Sharpness</th></tr>
            </thead>
            <tbody>
              <tr><td><strong>Ideal (ILPF)</strong></td><td>$1$ if $D \le D_0$, else $0$</td><td>Discontinuity ($1 \to 0$)</td><td>Severe (Gibbs ripples)</td><td>Infinite (step function)</td></tr>
              <tr><td><strong>Butterworth (BLPF)</strong></td><td>$\dfrac{1}{1 + [D/D_0]^{2n}}$</td><td>$0.5$ (Half power)</td><td>None at $n=1,2$; rises with $n$</td><td>Adjustable via order $n$</td></tr>
              <tr><td><strong>Gaussian (GLPF)</strong></td><td>$e^{-D^2 / (2D_0^2)}$</td><td>$e^{-0.5} \approx 0.607$</td><td><strong>None (Zero ringing)</strong></td><td>Smooth exponential bell</td></tr>
            </tbody>
          </table></div>

          <div class="grid-2" style="margin-top:20px;">
            <div>
              <h4 style="color:var(--accent-blue);margin:0 0 8px;">🎯 3 Key LPF Applications (from slides):</h4>
              <ul style="color:var(--text-secondary);font-size:13px;line-height:1.7;">
                <li><strong>Cosmetic image processing</strong>: Smooths skin blemishes, wrinkles, and shadows while preserving major facial facial landmarks.</li>
                <li><strong>Machine-printed character recognition</strong>: Blurs jagged edges and repairs broken character strokes so OCR models can classify correctly.</li>
                <li><strong>False contour removal</strong>: Smooths quantization steps in heavily compressed images.</li>
              </ul>
            </div>
            <div>
              <div class="slide-img-wrap">
                <img src="slides_images/slide7_page_39.png" alt="GLPF cosmetic processing and character recognition">
                <div class="slide-img-caption"><strong>Slide 7 Page 39</strong>: GLPF applied for cosmetic blemish reduction and broken character text restoration.</div>
              </div>
            </div>
          </div>
        </div>
        """
    },
    {
        "id": 11,
        "category": "SLIDE 7: FREQUENCY FILTERING",
        "tag_class": "s7-tag",
        "title": "🔪 High-Pass Filters: Core Principle & Ideal HPF",
        "subtitle": "How high-pass filters sharpen edges and the fundamental complement relationship",
        "content": r"""
        <div class="card s7">
          <div class="grid-2">
            <div>
              <h3>🔑 The Fundamental Complement Rule</h3>
              <p style="color:var(--text-secondary);font-size:13px;">A high-pass filter passes the frequencies blocked by a low-pass filter:</p>
              <div class="formula-box">
                <div class="formula-label">HPF / LPF Relationship (Class Test Classic!)</div>
                $$H_{hp}(u,v) = 1 - H_{lp}(u,v)$$
              </div>
              <div class="formula-box" style="margin-top:12px;">
                <div class="formula-label">Ideal High-Pass Filter (IHPF)</div>
                $$H(u,v) = \begin{cases} 0 & \text{if } D(u,v) \le D_0 \\ 1 & \text{if } D(u,v) > D_0 \end{cases}$$
              </div>
              <div class="callout callout-purple" style="margin-top:12px;">
                <span class="callout-icon">💡</span>
                <p><strong>DC Suppression:</strong> Notice at origin $D(0,0)=0 \implies H_{hp}(0,0)=0$. This completely zeroes out the DC component (average brightness), turning the background dark/grey and preserving only edge spikes!</p>
              </div>
            </div>
            <div>
              <div class="slide-img-wrap">
                <img src="slides_images/slide7_page_41.png" alt="HPF complement principle and cross sections">
                <div class="slide-img-caption"><strong>Slide 7 Page 41</strong>: $H_{hp} = 1 - H_{lp}$ relationship and filter profile cross sections.</div>
              </div>
            </div>
          </div>
        </div>
        """
    },
    {
        "id": 12,
        "category": "SLIDE 7: FREQUENCY FILTERING",
        "tag_class": "s7-tag",
        "title": "🔪 Butterworth & Gaussian High-Pass Filters",
        "subtitle": "Equations and 3D frequency characteristics of BHPF and GHPF",
        "content": r"""
        <div class="grid-2">
          <div class="card s7">
            <h3>Butterworth HPF (BHPF)</h3>
            <div class="formula-box">
              <div class="formula-label">BHPF Transfer Function</div>
              $$H(u,v) = \frac{1}{1 + \left[\frac{D_0}{D(u,v)}\right]^{2n}}$$
            </div>
            <p style="color:var(--text-secondary);font-size:13px;margin-top:8px;">
              Notice $D_0 / D(u,v)$ is inverted! At $D = D_0$, $H = 0.5$. Order $n$ controls transition steepness.
            </p>
            <div class="slide-img-wrap" style="margin-top:12px;">
              <img src="slides_images/slide7_page_43.png" alt="BHPF 3D perspective">
              <div class="slide-img-caption"><strong>Slide 7 Page 43</strong>: 3D perspective of the Butterworth High-Pass Filter.</div>
            </div>
          </div>

          <div class="card s7">
            <h3>Gaussian HPF (GHPF)</h3>
            <div class="formula-box">
              <div class="formula-label">GHPF Transfer Function</div>
              $$H(u,v) = 1 - e^{-\frac{D^2(u,v)}{2 D_0^2}}$$
            </div>
            <p style="color:var(--text-secondary);font-size:13px;margin-top:8px;">
              At $D = 0$, $H = 1 - 1 = 0$. At $D = D_0$, $H = 1 - e^{-0.5} \approx 0.393$. Produces smooth, clean edge profiles with zero ringing.
            </p>
            <div class="slide-img-wrap" style="margin-top:12px;">
              <img src="slides_images/slide7_page_45.png" alt="GHPF 3D perspective">
              <div class="slide-img-caption"><strong>Slide 7 Page 45</strong>: 3D perspective of the Gaussian High-Pass Filter.</div>
            </div>
          </div>
        </div>
        """
    },
    {
        "id": 13,
        "category": "SLIDE 7: FREQUENCY FILTERING",
        "tag_class": "s7-tag",
        "title": "📊 High-Pass Filters Visual Comparison (D₀ = 15)",
        "subtitle": "Comparing Ideal vs Butterworth vs Gaussian High-Pass outputs on test image",
        "content": r"""
        <div class="card s7">
          <div class="grid-2">
            <div>
              <h3>Visual Analysis: IHPF vs BHPF vs GHPF</h3>
              <ul style="color:var(--text-secondary);font-size:13px;line-height:1.8;">
                <li><strong>Ideal HPF (top row)</strong>: Shows severe ringing ripples around all edges and boundaries, creating false phantom contours.</li>
                <li><strong>Butterworth HPF (middle row)</strong>: Mild transition. Notice edges are sharper than Gaussian, with slight, controlled ringing at higher orders.</li>
                <li><strong>Gaussian HPF (bottom row)</strong>: Produces the smoothest edges without a trace of ringing ripples. Excellent for edge detection and natural sharpening.</li>
                <li><strong>Cutoff frequency effect</strong>: As $D_0$ increases (e.g. 15 to 30 to 80), more low frequencies are blocked $\implies$ only the thinnest, highest-frequency edge contours survive.</li>
              </ul>
            </div>
            <div>
              <div class="slide-img-wrap">
                <img src="slides_images/slide7_page_50.png" alt="HPF visual comparison at D0=15">
                <div class="slide-img-caption"><strong>Slide 7 Page 50</strong>: Visual results for Ideal, Butterworth, and Gaussian High-Pass Filters.</div>
              </div>
            </div>
          </div>
        </div>
        """
    },
    {
        "id": 14,
        "category": "SLIDE 7: FREQUENCY FILTERING",
        "tag_class": "s7-tag",
        "title": "∇² Laplacian in the Frequency Domain",
        "subtitle": "Deriving second derivatives in Fourier space and Laplacian image enhancement",
        "content": r"""
        <div class="card s7">
          <div class="grid-2">
            <div>
              <h3>Mathematical Derivation</h3>
              <p style="color:var(--text-secondary);font-size:13px;">Spatial Laplacian is the sum of second partial derivatives:</p>
              $$\nabla^2 f(x,y) = \frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2}$$
              <p style="color:var(--text-secondary);font-size:13px;">By Fourier derivative theorem, differentiation by $x$ is multiplication by $ju$:</p>
              $$\mathcal{F}\left\{\frac{\partial^2 f}{\partial x^2}\right\} = (ju)^2 F(u,v) = -u^2 F(u,v)$$
              <div class="formula-box">
                <div class="formula-label">Centered Frequency Domain Laplacian</div>
                $$H(u,v) = -\left[\left(u - \frac{M}{2}\right)^2 + \left(v - \frac{N}{2}\right)^2\right] = -D^2(u,v)$$
              </div>
            </div>
            <div>
              <h3>Laplacian Image Enhancement</h3>
              <p style="color:var(--text-secondary);font-size:13px;">To sharpen an image, we subtract its Laplacian from itself:</p>
              $$g(x,y) = f(x,y) - \nabla^2 f(x,y)$$
              <p style="color:var(--text-secondary);font-size:13px;">In frequency domain, substituting $H(u,v) = -D^2(u,v)$:</p>
              <div class="formula-box" style="border-color:var(--accent-green);">
                <div class="formula-label">Laplacian Enhancement Transfer Function</div>
                $$H_{enh}(u,v) = 1 - (-D^2(u,v)) = 1 + D^2(u,v)$$
              </div>
              <div class="callout callout-green" style="margin-top:12px;">
                <span class="callout-icon">💡</span>
                <p>The minus signs cancel! The filter passes the original image with gain 1 and adds the boosted high frequencies ($D^2$) directly.</p>
              </div>
            </div>
          </div>
        </div>
        """
    },
    {
        "id": 15,
        "category": "SLIDE 7: FREQUENCY FILTERING",
        "tag_class": "s7-tag",
        "title": "🫁 High-Frequency Emphasis & Chest X-Ray Case Study",
        "subtitle": "Boosting edges while preserving overall illumination and contrast",
        "content": r"""
        <div class="card s7">
          <div class="grid-2">
            <div>
              <h3>High-Frequency Emphasis Filtering</h3>
              <p style="color:var(--text-secondary);font-size:13px;">Standard HPF zeroes the DC term, losing tonality. High-Frequency Emphasis fixes this:</p>
              <div class="formula-box">
                <div class="formula-label">High-Frequency Emphasis Transfer Function</div>
                $$H_{hfe}(u,v) = a + b \cdot H_{hp}(u,v) \quad (a \ge 0, b > a)$$
              </div>
              <ul style="color:var(--text-secondary);font-size:13px;line-height:1.7;margin-top:10px;">
                <li>$a$ is the low-frequency offset (typically $a = 0.5$): keeps overall image lighting!</li>
                <li>$b$ is the high-frequency multiplier (typically $b = 1.5 - 2.0$): dramatically sharpens edges!</li>
                <li>When $H_{hp} \to 0$ (low freq): $H \to a$.</li>
                <li>When $H_{hp} \to 1$ (high freq): $H \to a + b$.</li>
              </ul>
            </div>
            <div>
              <div class="slide-img-wrap">
                <img src="slides_images/slide7_page_54.png" alt="High-frequency emphasis filter shape">
                <div class="slide-img-caption"><strong>Slide 7 Page 54</strong>: High-frequency emphasis cross-section showing base offset $a$ and peak gain $a+b$.</div>
              </div>
            </div>
          </div>

          <div class="grid-2" style="margin-top:16px;">
            <div class="slide-img-wrap">
              <img src="slides_images/slide7_page_59.png" alt="Chest X-Ray enhancement steps">
              <div class="slide-img-caption"><strong>Slide 7 Page 59</strong>: (a) Original chest X-ray; (b) Highpass filtered; (c) High-frequency emphasis; (d) High-frequency emphasis + Histogram Equalization.</div>
            </div>
            <div class="slide-img-wrap">
              <img src="slides_images/slide7_page_60.png" alt="Close-up comparison of chest X-ray enhancement">
              <div class="slide-img-caption"><strong>Slide 7 Page 60</strong>: Full-resolution final result. Tiny bone fractures and delicate lung tissues become clearly visible to radiologists!</div>
            </div>
          </div>
        </div>
        """
    },
    {
        "id": 16,
        "category": "SLIDE 7: FREQUENCY FILTERING",
        "tag_class": "s7-tag",
        "title": "🎯 Lecture Highlight: Template Matching via 2D Correlation",
        "subtitle": "Character recognition and object detection in frequency domain (Slide 7, Pages 64–65)",
        "content": r"""
        <div class="card s7">
          <p style="color:var(--text-secondary);font-size:14px;">
            In Slide 7 Pages 64–65, the professor highlights how frequency domain filtering can perform instantaneous <strong>template matching (character recognition)</strong> using 2D correlation:
          </p>
          <div class="grid-2" style="margin:16px 0;">
            <div class="slide-img-wrap">
              <img src="slides_images/slide7_page_64.png" alt="UTK original image and letter T template">
              <div class="slide-img-caption"><strong>Slide 7 Page 64</strong>: Input image with letters <code>"UTK"</code> and the target template letter <code>"T"</code>.</div>
            </div>
            <div class="slide-img-wrap">
              <img src="slides_images/slide7_page_65.png" alt="Correlation output showing bright peak at letter T">
              <div class="slide-img-caption"><strong>Slide 7 Page 65</strong>: 2D Fourier Correlation output — a massive bright energy spike marks the exact center of <code>"T"</code>!</div>
            </div>
          </div>

          <div class="formula-box">
            <div class="formula-label">Frequency Domain Correlation Theorem</div>
            $$f(x,y) \circ h(x,y) \;\Longleftrightarrow\; F(u,v) \cdot H^*(u,v)$$
            <p style="color:var(--text-secondary);font-size:13px;margin-top:8px;">
              Where $H^*(u,v)$ is the <em>complex conjugate</em> of the template's Fourier transform. Instead of computationally heavy 2D sliding spatial template matching, you multiply $F(u,v) \cdot H^*(u,v)$ in the frequency domain and compute the IDFT. The highest peak corresponds to the exact match!
            </p>
          </div>
        </div>
        """
    },
    {
        "id": 17,
        "category": "SLIDE 7: FREQUENCY FILTERING",
        "tag_class": "s7-tag",
        "title": "⚡ Fast Fourier Transform (FFT) & Summary",
        "subtitle": "The landmark algorithm that made frequency domain filtering practical",
        "content": r"""
        <div class="card s7">
          <div class="grid-2">
            <div>
              <h3>⚡ The Fast Fourier Transform (FFT)</h3>
              <p style="color:var(--text-secondary);font-size:13px;">Direct computation of 2D DFT requires $M^2 N^2$ complex operations. For $N \times N$, that is $\mathcal{O}(N^2)$ per dimension.</p>
              <div class="formula-box">
                <div class="formula-label">FFT Computational Complexity</div>
                $$\mathcal{O}(N \log_2 N)$$
              </div>
              <div class="key-chips" style="margin:12px 0;">
                <span class="chip chip-green">100× to 600× Speedup</span>
                <span class="chip chip-blue">Cooley-Tukey Algorithm</span>
              </div>
              <p style="color:var(--text-secondary);font-size:13px;">This landmark complexity reduction is the sole reason frequency domain techniques are used in real-time medical imaging, JPEG compression, and computer vision.</p>
            </div>
            <div>
              <h3>⚖️ Frequency Domain vs Spatial Domain</h3>
              <div class="table-responsive"><table class="comparison-table">
                <thead>
                  <tr><th>Aspect</th><th>Spatial Domain</th><th>Frequency Domain</th></tr>
                </thead>
                <tbody>
                  <tr><td>Operation</td><td>Convolution with small kernel</td><td>Pointwise multiplication $F \cdot H$</td></tr>
                  <tr><td>Intuition</td><td>Direct, pixel manipulation</td><td>Frequency perspective</td></tr>
                  <tr><td>Speed (Small mask)</td><td>Fast for $3\times 3, 5\times 5$</td><td>FFT overhead not worth it</td></tr>
                  <tr><td>Speed (Large mask)</td><td>Very slow</td><td>Extremely fast via FFT</td></tr>
                  <tr><td>Periodic Noise</td><td>Difficult to eliminate</td><td>Trivial via Band-Reject/Notch</td></tr>
                </tbody>
              </table></div>
            </div>
          </div>
        </div>
        """
    },
    {
        "id": 18,
        "category": "SLIDE 8: IMAGE RESTORATION",
        "tag_class": "s8-tag",
        "title": "🔬 Slide 8: Image Restoration & Degradation Model",
        "subtitle": "Understanding objective restoration and the mathematical degradation model",
        "content": r"""
        <div class="card s8">
          <div class="grid-2">
            <div>
              <h3>🔬 What is Image Restoration?</h3>
              <p style="color:var(--text-secondary);font-size:13px;">
                Unlike enhancement (which is subjective), <strong>restoration is an objective process</strong>: it attempts to reconstruct an image that has been degraded by using a mathematical model of the degradation phenomenon.
              </p>
              <div class="formula-box s8-formula">
                <div class="formula-label">Degradation Model (Spatial Domain)</div>
                $$g(x,y) = f(x,y) \star h(x,y) + \eta(x,y)$$
              </div>
              <div class="formula-box s8-formula" style="margin-top:10px;">
                <div class="formula-label">Degradation Model (Frequency Domain)</div>
                $$G(u,v) = F(u,v) H(u,v) + N(u,v)$$
              </div>
              <p style="color:var(--text-secondary);font-size:13px;margin-top:8px;">
                Where $f$ is original image, $h$ is degradation function (blur, motion), $\eta$ is additive noise, and $g$ is the observed degraded image.
              </p>
            </div>
            <div>
              <div class="slide-img-wrap">
                <img src="slides_images/slide8_page_04.png" alt="Degradation / restoration block diagram">
                <div class="slide-img-caption"><strong>Slide 8 Page 4</strong>: The degradation/restoration process. We model degradation $H$ and noise $\eta$, then apply restoration filter to obtain estimate $\hat{f}(x,y)$.</div>
              </div>
            </div>
          </div>
        </div>
        """
    },
    {
        "id": 19,
        "category": "SLIDE 8: IMAGE RESTORATION",
        "tag_class": "s8-tag",
        "title": "📐 Noise Sources & The 6 Noise PDFs",
        "subtitle": "How noise enters images and the 6 probability density functions from Slide 8",
        "content": r"""
        <div class="card s8">
          <div class="grid-2">
            <div>
              <h3>📡 Sources of Noise in Images</h3>
              <ul style="color:var(--text-secondary);font-size:13px;line-height:1.7;">
                <li><strong>Image Acquisition (Digitization)</strong>: Sensor circuit noise, electronic amplifier noise, thermal noise (higher temperature $\implies$ higher noise).</li>
                <li><strong>Transmission</strong>: Packet loss, radio interference, atmospheric conditions.</li>
                <li><strong>Light Levels</strong>: Low illumination requires high sensor gain, amplifying noise.</li>
              </ul>
              <div class="formula-box s8-formula" style="margin-top:12px;">
                <div class="formula-label">The Additive Noise Model (Slide 8 Focus)</div>
                $$g(x,y) = f(x,y) + \eta(x,y)$$
                <p style="color:var(--text-secondary);font-size:12px;margin-top:4px;">When blur $h(x,y)$ is identity, observed image is simply true image plus additive noise $\eta$.</p>
              </div>
            </div>
            <div>
              <div class="slide-img-wrap">
                <img src="slides_images/slide8_page_07.png" alt="All 6 noise PDF curves">
                <div class="slide-img-caption"><strong>Slide 8 Page 7</strong>: The 6 Noise Probability Density Functions: Gaussian, Rayleigh, Erlang (Gamma), Exponential, Uniform, and Impulse (Salt & Pepper).</div>
              </div>
            </div>
          </div>
        </div>
        """
    },
    {
        "id": 20,
        "category": "SLIDE 8: IMAGE RESTORATION",
        "tag_class": "s8-tag",
        "title": "🖼️ Visual Noise Examples & Noise-to-Filter Matrix",
        "subtitle": "How each noise looks visually and the master lookup table for exams",
        "content": r"""
        <div class="card s8">
          <div class="grid-2">
            <div>
              <div class="slide-img-wrap">
                <img src="slides_images/slide8_page_09.png" alt="Visual noise corrupted images">
                <div class="slide-img-caption"><strong>Slide 8 Page 9</strong>: Visual appearance of images corrupted by Gaussian, Rayleigh, Erlang, Exponential, Uniform, and Salt & Pepper noise.</div>
              </div>
            </div>
            <div>
              <h4 style="color:var(--accent-purple);margin:0 0 10px;">🔑 Master Noise-to-Filter Table (Memorize!):</h4>
              <div class="table-responsive"><table class="comparison-table">
                <thead>
                  <tr><th>Noise Type</th><th>Best Spatial Filter</th><th>Why it Works</th></tr>
                </thead>
                <tbody>
                  <tr><td><strong>Gaussian</strong></td><td>Arithmetic Mean / Geometric Mean</td><td>Averages out zero-mean random fluctuations</td></tr>
                  <tr><td><strong>Salt &amp; Pepper</strong></td><td><strong>Median Filter ⭐</strong></td><td>Outliers (0, 255) are discarded by sorting</td></tr>
                  <tr><td><strong>Pepper Only (Dark)</strong></td><td>Contraharmonic ($Q > 0$) / Max Filter</td><td>Weights brighter pixels, knocks out 0</td></tr>
                  <tr><td><strong>Salt Only (Bright)</strong></td><td>Contraharmonic ($Q < 0$) / Min / Harmonic</td><td>Weights darker pixels, knocks out 255</td></tr>
                  <tr><td><strong>Uniform</strong></td><td>Midpoint Filter</td><td>Averages symmetric minimum and maximum</td></tr>
                  <tr><td><strong>Mixed (Gaussian + Salt & Pepper)</strong></td><td>Alpha-Trimmed Mean Filter</td><td>Trims impulse outliers, averages Gaussian residue</td></tr>
                  <tr><td><strong>Periodic</strong></td><td>Band-Reject / Notch Filter</td><td>Frequency spikes removed in Fourier domain</td></tr>
                </tbody>
              </table></div>
            </div>
          </div>
        </div>
        """
    },
    {
        "id": 21,
        "category": "SLIDE 8: IMAGE RESTORATION",
        "tag_class": "s8-tag",
        "title": "📊 Spatial Mean Filters: Arithmetic & Geometric",
        "subtitle": "The standard averaging filters and detail preservation trade-offs",
        "content": r"""
        <div class="card s8">
          <div class="grid-2">
            <div>
              <div class="slide-label s8">Arithmetic Mean Filter</div>
              <div class="formula-box s8-formula">
                <div class="formula-label">Arithmetic Mean (Simple Average)</div>
                $$\hat{f}(x,y) = \frac{1}{mn} \sum_{(s,t) \in S_{xy}} g(s,t)$$
              </div>
              <p style="color:var(--text-secondary);font-size:13px;line-height:1.6;margin-top:10px;">
                &bull; Computes average pixel value in $m \times n$ window $S_{xy}$.<br>
                &bull; Effective for Gaussian noise.<br>
                &bull; <strong>Downside:</strong> Blurs edges and softens fine image details.
              </p>
            </div>

            <div>
              <div class="slide-label s8">Geometric Mean Filter</div>
              <div class="formula-box s8-formula">
                <div class="formula-label">Geometric Mean</div>
                $$\hat{f}(x,y) = \left[\prod_{(s,t) \in S_{xy}} g(s,t)\right]^{\frac{1}{mn}}$$
              </div>
              <p style="color:var(--text-secondary);font-size:13px;line-height:1.6;margin-top:10px;">
                &bull; Multiplies all pixels, then takes the $mn$-th root.<br>
                &bull; Achieves similar smoothing to arithmetic mean, but <strong>tends to preserve more image detail</strong>.<br>
                &bull; <strong>Danger:</strong> A single 0 pixel in window sets entire result to 0!
              </p>
            </div>
          </div>

          <div class="slide-img-wrap" style="margin-top:16px;">
            <img src="slides_images/slide8_page_20.png" alt="Arithmetic vs Geometric mean on Gaussian noise">
            <div class="slide-img-caption"><strong>Slide 8 Page 20</strong>: Original &rarr; Gaussian noisy &rarr; Arithmetic mean 3&times;3 &rarr; Geometric mean 3&times;3. Geometric preserves slightly sharper details.</div>
          </div>
        </div>
        """
    },
    {
        "id": 22,
        "category": "SLIDE 8: IMAGE RESTORATION",
        "tag_class": "s8-tag",
        "title": "📊 Harmonic & Contraharmonic Mean Filters",
        "subtitle": "Formulas, Q rules, and why harmonic fails for pepper noise",
        "content": r"""
        <div class="card s8">
          <div class="grid-2">
            <div>
              <div class="slide-label s8">Harmonic Mean Filter</div>
              <div class="formula-box s8-formula">
                <div class="formula-label">Harmonic Mean</div>
                $$\hat{f}(x,y) = \frac{mn}{\sum_{(s,t) \in S_{xy}} \frac{1}{g(s,t)}}$$
              </div>
              <div class="key-chips" style="margin:10px 0;">
                <span class="chip chip-green">Good for Salt Noise</span>
                <span class="chip chip-pink">❌ FAILS on Pepper Noise (0)</span>
              </div>
              <p style="color:var(--text-secondary);font-size:13px;">If any pixel is 0 (pepper noise), $1/0 \to \infty$ in denominator, so the output becomes 0!</p>
            </div>

            <div>
              <div class="slide-label s8">Contraharmonic Mean Filter</div>
              <div class="formula-box s8-formula">
                <div class="formula-label">Contraharmonic Mean of Order Q</div>
                $$\hat{f}(x,y) = \frac{\sum_{(s,t) \in S_{xy}} g(s,t)^{Q+1}}{\sum_{(s,t) \in S_{xy}} g(s,t)^Q}$$
              </div>
              <div class="key-chips" style="margin:10px 0;">
                <span class="chip chip-blue">Q > 0 &rarr; Removes PEPPER</span>
                <span class="chip chip-purple">Q < 0 &rarr; Removes SALT</span>
                <span class="chip chip-green">Q = 0 &rarr; Arithmetic Mean</span>
                <span class="chip chip-cyan">Q = -1 &rarr; Harmonic Mean</span>
              </div>
            </div>
          </div>
        </div>
        """
    },
    {
        "id": 23,
        "category": "SLIDE 8: IMAGE RESTORATION",
        "tag_class": "s8-tag",
        "title": "🐉 Contraharmonic in Action & 'Here Be Dragons'",
        "subtitle": "Visual proof of pepper removal and the catastrophe of selecting the wrong Q",
        "content": r"""
        <div class="card s8">
          <div class="grid-2">
            <div>
              <div class="slide-img-wrap">
                <img src="slides_images/slide8_page_21.png" alt="Contraharmonic filter Q=1.5 removing pepper noise">
                <div class="slide-img-caption"><strong>Slide 8 Page 21</strong>: Image corrupted by Pepper Noise restored with 3&times;3 Contraharmonic Filter ($Q = +1.5$). Dark pepper spots disappear completely!</div>
              </div>
            </div>
            <div>
              <div class="slide-img-wrap">
                <img src="slides_images/slide8_page_23.png" alt="Contraharmonic Filter: Here Be Dragons">
                <div class="slide-img-caption"><strong>Slide 8 Page 23</strong>: <em>"Here Be Dragons"</em> &mdash; Applying $Q > 0$ to salt noise or $Q < 0$ to pepper noise completely destroys the image!</div>
              </div>
            </div>
          </div>

          <div class="callout callout-orange" style="margin-top:16px;">
            <span class="callout-icon">🐉</span>
            <p><strong>Exam Trap Warning:</strong> If an image has SALT noise and you mistakenly use $Q > 0$, the filter will make the salt noise worse (pure white blowout). Always remember: <strong>P for Pepper &rarr; Positive Q!</strong></p>
          </div>
        </div>
        """
    },
    {
        "id": 24,
        "category": "SLIDE 8: IMAGE RESTORATION",
        "tag_class": "s8-tag",
        "title": "📈 Order Statistics Filters: The Median Filter",
        "subtitle": "How sorting destroys salt-and-pepper impulse noise without blurring edges",
        "content": r"""
        <div class="card s8">
          <div class="grid-2">
            <div>
              <h3>📈 The Legendary Median Filter ⭐</h3>
              <p style="color:var(--text-secondary);font-size:13px;">Sorts all pixel values in neighbourhood $S_{xy}$ in ascending order and takes the middle value:</p>
              <div class="formula-box s8-formula">
                <div class="formula-label">Median Filter Definition</div>
                $$\hat{f}(x,y) = \underset{(s,t) \in S_{xy}}{\text{median}} \{g(s,t)\}$$
              </div>
              <div class="key-chips" style="margin:12px 0;">
                <span class="chip chip-green">⭐ Best for Salt & Pepper</span>
                <span class="chip chip-blue">Zero Edge Blurring</span>
                <span class="chip chip-purple">Preserves Sharpness</span>
              </div>
              <p style="color:var(--text-secondary);font-size:13px;line-height:1.7;">
                <strong>Why it works so well:</strong> Impulse noise pixels are outliers ($0$ or $255$). Sorting automatically pushes them to the extreme left or right of the list. The median selects a real, valid neighborhood pixel, completely discarding the noise!
              </p>
            </div>
            <div>
              <div class="slide-img-wrap">
                <img src="slides_images/slide8_page_33.png" alt="Median filter on salt & pepper noise">
                <div class="slide-img-caption"><strong>Slide 8 Page 33</strong>: Salt &amp; Pepper &rarr; 1 pass 3&times;3 median &rarr; 2 passes &rarr; 3 passes. Near-perfect restoration after 1-2 passes!</div>
              </div>
            </div>
          </div>
        </div>
        """
    },
    {
        "id": 25,
        "category": "SLIDE 8: IMAGE RESTORATION",
        "tag_class": "s8-tag",
        "title": "📈 Order Statistics: Max, Min & Midpoint Filters",
        "subtitle": "Formulas and applications for extreme-value order statistics",
        "content": r"""
        <div class="card s8">
          <div class="grid-2">
            <div>
              <div class="slide-label s8">Max & Min Filters</div>
              <div class="formula-box s8-formula">
                <div class="formula-label">Max Filter (Removes Pepper Noise)</div>
                $$\hat{f}(x,y) = \max_{(s,t) \in S_{xy}} \{g(s,t)\}$$
              </div>
              <div class="formula-box s8-formula" style="margin-top:10px;">
                <div class="formula-label">Min Filter (Removes Salt Noise)</div>
                $$\hat{f}(x,y) = \min_{(s,t) \in S_{xy}} \{g(s,t)\}$$
              </div>
              <div class="slide-img-wrap" style="margin-top:10px;">
                <img src="slides_images/slide8_page_35.png" alt="Max and min filter on impulse noise">
                <div class="slide-img-caption"><strong>Slide 8 Page 35</strong>: Max filter removes dark pepper noise; Min filter removes bright salt noise.</div>
              </div>
            </div>

            <div>
              <div class="slide-label s8">Midpoint Filter</div>
              <div class="formula-box s8-formula">
                <div class="formula-label">Midpoint Filter</div>
                $$\hat{f}(x,y) = \frac{1}{2} \left[\max_{(s,t) \in S_{xy}} \{g(s,t)\} + \min_{(s,t) \in S_{xy}} \{g(s,t)\}\right]$$
              </div>
              <p style="color:var(--text-secondary);font-size:13px;margin-top:8px;">
                Combines order statistics with averaging. Works best for randomly distributed noise with symmetric distributions like <strong>Uniform</strong> and <strong>Gaussian</strong> noise.
              </p>
              <div class="slide-img-wrap" style="margin-top:10px;">
                <img src="slides_images/slide8_page_36.png" alt="Midpoint filter on uniform noise">
                <div class="slide-img-caption"><strong>Slide 8 Page 36</strong>: Midpoint filter applied to uniform noise.</div>
              </div>
            </div>
          </div>
        </div>
        """
    },
    {
        "id": 26,
        "category": "SLIDE 8: IMAGE RESTORATION",
        "tag_class": "s8-tag",
        "title": "📈 Alpha-Trimmed Mean Filter & Summary",
        "subtitle": "Trimming both extremes to eliminate mixed Gaussian and impulse noise",
        "content": r"""
        <div class="card s8">
          <div class="grid-2">
            <div>
              <h3>Alpha-Trimmed Mean Filter</h3>
              <p style="color:var(--text-secondary);font-size:13px;">Sort all pixels, trim $d/2$ lowest and $d/2$ highest, and average remaining $mn - d$ pixels:</p>
              <div class="formula-box s8-formula">
                <div class="formula-label">Alpha-Trimmed Mean Filter (Exam Favorite!)</div>
                $$\hat{f}(x,y) = \frac{1}{mn - d} \sum_{(s,t) \in S_{xy}} g_r(s,t)$$
              </div>
              <div class="key-chips" style="margin:12px 0;">
                <span class="chip chip-blue">d = 0 &rarr; Arithmetic Mean</span>
                <span class="chip chip-green">d = mn - 1 &rarr; Median Filter</span>
                <span class="chip chip-orange">Best for Mixed Noise</span>
              </div>
              <p style="color:var(--text-secondary);font-size:13px;line-height:1.7;">
                <strong>Why it is powerful:</strong> If an image has BOTH Gaussian noise AND Salt & Pepper noise, standard mean blurs salt/pepper, and median blurs Gaussian. Alpha-trimmed eliminates the impulse outliers via trimming, then averages the rest to smooth Gaussian noise!
              </p>
            </div>
            <div>
              <div class="slide-img-wrap">
                <img src="slides_images/slide8_page_38.png" alt="Filter comparison on mixed noise">
                <div class="slide-img-caption"><strong>Slide 8 Page 38</strong>: Image corrupted by both Gaussian and Salt &amp; Pepper noise. Arithmetic mean, geometric mean, and median all struggle, but Alpha-Trimmed Mean produces a clean, sharp restoration!</div>
              </div>
            </div>
          </div>
        </div>
        """
    },
    {
        "id": 27,
        "category": "🧮 NUMERICAL WORKSHOP",
        "tag_class": "s8-tag",
        "title": "🧮 Exam Math Workshop: The 7×7 Grid Solved Step-by-Step",
        "subtitle": "Slide 8 Page 12 Blackboard Problem: Full calculation for every filter",
        "content": r"""
        <div class="card s8">
          <div class="callout callout-purple">
            <span class="callout-icon">📝</span>
            <p><strong>The Ultimate 10/10 Exam Question!</strong> Throughout Slide 8 (Pages 12, 15, 17, 19, 26, 32), the professor repeatedly poses this blackboard problem: a 7&times;7 image matrix with two clear impulse noise corruptions: a <strong>Salt noise pixel (204)</strong> at coordinate $(1,2)$ and a <strong>Pepper noise pixel (0)</strong> at $(4,2)$. Below is the complete interactive step-by-step mathematical walkthrough for every filter!</p>
          </div>

          <div class="solver-tabs" style="margin-top:16px;">
            <button class="solver-tab-btn active-salt" id="btn-salt" onclick="setWorkshopMode('salt')">
              <span>🔴</span> Inspect Salt Noise: Pixel (1, 2) = 204
            </button>
            <button class="solver-tab-btn" id="btn-pepper" onclick="setWorkshopMode('pepper')">
              <span>🟣</span> Inspect Pepper Noise: Pixel (4, 2) = 0
            </button>
          </div>

          <!-- Interactive 7x7 Grid Representation -->
          <div class="grid-7x7-container">
            <div style="font-size:13px;color:var(--text-secondary);display:flex;gap:20px;">
              <span><span style="color:var(--accent-pink);">■</span> Salt Pixel = 204</span>
              <span><span style="color:var(--accent-purple);">■</span> Pepper Pixel = 0</span>
              <span><span style="color:var(--accent-cyan);">□</span> Active 3&times;3 Window ($S_{xy}$)</span>
            </div>
            <div class="grid-7x7" id="matrix-7x7">
              <!-- Rendered via JS -->
            </div>
          </div>

          <!-- Active Window Details -->
          <div id="window-details-card" style="background:var(--bg-card);border:1px solid var(--border);border-radius:12px;padding:20px;margin-top:20px;">
            <!-- Populated via JS -->
          </div>

          <!-- Complete Calculated Results Grid -->
          <div class="calculation-result-grid" id="calc-results-container">
            <!-- Populated via JS -->
          </div>
        </div>
        """
    },
    {
        "id": 28,
        "category": "SLIDE 8: IMAGE RESTORATION",
        "tag_class": "s8-tag",
        "title": "〰️ Periodic Noise & Frequency Domain Band-Reject Filters",
        "subtitle": "How periodic electrical interference creates frequency spikes and how to filter them",
        "content": r"""
        <div class="card s8">
          <div class="grid-2">
            <div>
              <h3>〰️ What is Periodic Noise?</h3>
              <p style="color:var(--text-secondary);font-size:13px;">
                Arises from electrical or electromechanical interference (e.g., power line 50/60 Hz hum, electric motors, unshielded wires, radio transmitters).
              </p>
              <ul style="color:var(--text-secondary);font-size:13px;line-height:1.7;">
                <li>Produces a regular geometric grid/stripe pattern over the image.</li>
                <li><strong>Spatial domain filters struggle</strong> to remove periodic noise without destroying real image content.</li>
                <li><strong>Fourier domain reveals periodic noise instantly</strong> as concentrated conjugate pairs of bright impulse spikes!</li>
              </ul>
              <div class="formula-box s8-formula" style="margin-top:12px;">
                <div class="formula-label">Band-Reject & Band-Pass Relation</div>
                $$H_{bp}(u,v) = 1 - H_{br}(u,v)$$
              </div>
            </div>
            <div>
              <div class="slide-img-wrap">
                <img src="slides_images/slide8_page_39.png" alt="Periodic noise and spectrum spikes">
                <div class="slide-img-caption"><strong>Slide 8 Page 39</strong>: (Left) Image with sinusoidal periodic noise; (Center) Fourier spectrum showing 4 bright conjugate noise spikes; (Right) Butterworth Band-Reject filter removing the spikes!</div>
              </div>
            </div>
          </div>
        </div>
        """
    },
    {
        "id": 29,
        "category": "SLIDE 8: IMAGE RESTORATION",
        "tag_class": "s8-tag",
        "title": "🤖 Adaptive Filters: Why Adaptive & AMF Motivation",
        "subtitle": "Overcoming fixed filter limitations when noise density is high",
        "content": r"""
        <div class="card s8">
          <div class="grid-2">
            <div>
              <h3>🤖 What Makes a Filter 'Adaptive'?</h3>
              <p style="color:var(--text-secondary);font-size:13px;">
                Standard filters apply the exact same formula to every pixel in the image regardless of local characteristics.
              </p>
              <div class="callout callout-purple">
                <span class="callout-icon">💡</span>
                <p><strong>Adaptive filters</strong> dynamically change their mathematical behavior (and window size!) based on statistical properties inside the local filter region.</p>
              </div>
              <h4 style="color:var(--accent-purple);margin:14px 0 6px;">Why Standard Median Fails in Dense Noise:</h4>
              <p style="color:var(--text-secondary);font-size:13px;line-height:1.6;">
                When impulse noise spatial density is high ($> 20\% - 30\%$), it becomes very likely that the median of a $3\times 3$ window is itself a noise pixel! Applying larger fixed windows (like $7\times 7$) removes the noise but smears away fine details and thins lines.
              </p>
            </div>
            <div>
              <h4 style="color:var(--accent-blue);margin:0 0 10px;">The 3 Core Purposes of AMF (Slide 8 Page 45):</h4>
              <div style="background:var(--bg-secondary);padding:14px;border-radius:10px;border:1px solid var(--border);margin-bottom:12px;">
                <div style="color:var(--accent-pink);font-weight:700;">1. Remove Impulse Noise</div>
                <div style="font-size:12px;color:var(--text-secondary);margin-top:4px;">Handles dense salt &amp; pepper noise even up to 50%!</div>
              </div>
              <div style="background:var(--bg-secondary);padding:14px;border-radius:10px;border:1px solid var(--border);margin-bottom:12px;">
                <div style="color:var(--accent-cyan);font-weight:700;">2. Provide Smoothing for Other Noise</div>
                <div style="font-size:12px;color:var(--text-secondary);margin-top:4px;">Reduces mild Gaussian and non-impulse random noise.</div>
              </div>
              <div style="background:var(--bg-secondary);padding:14px;border-radius:10px;border:1px solid var(--border);">
                <div style="color:var(--accent-green);font-weight:700;">3. Reduce Distortion (Preserve Detail)</div>
                <div style="font-size:12px;color:var(--text-secondary);margin-top:4px;">Prevents thinning or thickening of object boundaries and lines!</div>
              </div>
            </div>
          </div>
        </div>
        """
    },
    {
        "id": 30,
        "category": "SLIDE 8: IMAGE RESTORATION",
        "tag_class": "s8-tag",
        "title": "🔄 Adaptive Median Filter: The 2-Level Algorithm",
        "subtitle": "Step-by-step logic for Level A (window size) and Level B (pixel replacement)",
        "content": r"""
        <div class="card s8">
          <div style="display:flex;gap:16px;flex-wrap:wrap;background:var(--bg-secondary);padding:12px 16px;border-radius:8px;border:1px solid var(--border);font-family:'JetBrains Mono',monospace;font-size:13px;margin-bottom:16px;">
            <span>$z_{min}$ = min in $S_{xy}$</span>
            <span>$z_{max}$ = max in $S_{xy}$</span>
            <span>$z_{med}$ = median in $S_{xy}$</span>
            <span>$z_{xy}$ = center pixel value</span>
            <span>$S_{max}$ = max window size</span>
          </div>

          <div class="grid-2">
            <div style="background:var(--bg-secondary);padding:16px;border-radius:10px;border:1px solid var(--accent-blue);">
              <h4 style="color:var(--accent-blue);margin:0 0 10px;">Level A: Is the Median an Impulse?</h4>
              <div style="font-family:'JetBrains Mono',monospace;font-size:13px;line-height:1.7;">
                $A1 = z_{med} - z_{min}$<br>
                $A2 = z_{med} - z_{max}$<br>
                <strong>If</strong> $A1 > 0$ <strong>and</strong> $A2 < 0$:<br>
                &nbsp;&nbsp;&rarr; <em>(Median is NOT an impulse!)</em> &rarr; <strong>Go to Level B</strong><br>
                <strong>Else</strong>:<br>
                &nbsp;&nbsp;Increase window size<br>
                &nbsp;&nbsp;<strong>If</strong> window size $\le S_{max}$:<br>
                &nbsp;&nbsp;&nbsp;&nbsp;Repeat Level A<br>
                &nbsp;&nbsp;<strong>Else</strong>:<br>
                &nbsp;&nbsp;&nbsp;&nbsp;Output $z_{med}$
              </div>
            </div>

            <div style="background:var(--bg-secondary);padding:16px;border-radius:10px;border:1px solid var(--accent-green);">
              <h4 style="color:var(--accent-green);margin:0 0 10px;">Level B: Is the Center Pixel an Impulse?</h4>
              <div style="font-family:'JetBrains Mono',monospace;font-size:13px;line-height:1.7;">
                $B1 = z_{xy} - z_{min}$<br>
                $B2 = z_{xy} - z_{max}$<br>
                <strong>If</strong> $B1 > 0$ <strong>and</strong> $B2 < 0$:<br>
                &nbsp;&nbsp;&rarr; <em>(Center pixel is clean, NOT an impulse!)</em><br>
                &nbsp;&nbsp;&rarr; <strong>Output $z_{xy}$</strong> <em>(Keep original detail!)</em><br>
                <strong>Else</strong>:<br>
                &nbsp;&nbsp;&rarr; <em>(Center pixel IS an impulse noise!)</em><br>
                &nbsp;&nbsp;&rarr; <strong>Output $z_{med}$</strong> <em>(Replace with clean median!)</em>
              </div>
            </div>
          </div>
        </div>
        """
    },
    {
        "id": 31,
        "category": "SLIDE 8: IMAGE RESTORATION",
        "tag_class": "s8-tag",
        "title": "📋 Adaptive Median Filter in Action & Summary",
        "subtitle": "50% noise test results and the complete Slide 8 summary table",
        "content": r"""
        <div class="card s8">
          <div class="grid-2">
            <div>
              <div class="slide-img-wrap">
                <img src="slides_images/slide8_page_46.png" alt="Adaptive Median Filter on 50% noise">
                <div class="slide-img-caption"><strong>Slide 8 Page 46</strong>: (Left) Image corrupted by 50% salt & pepper noise ($P_a = P_b = 0.25$); (Center) 7&times;7 Standard Median Filter (blurred, smeared traces); (Right) Adaptive Median Filter ($S_{max}=7$) &mdash; crisp, clean circuit board with fine lines intact!</div>
              </div>
            </div>
            <div>
              <div class="slide-img-wrap">
                <img src="slides_images/slide8_page_40.png" alt="Slide 8 summary slide">
                <div class="slide-img-caption"><strong>Slide 8 Page 40</strong>: Core takeaway: Spatial domain techniques are particularly useful for removing <strong>random noise</strong>; Frequency domain techniques are particularly useful for removing <strong>periodic noise</strong>.</div>
              </div>
            </div>
          </div>
        </div>
        """
    },
    {
        "id": 32,
        "category": "MASTER CHEAT SHEET",
        "tag_class": "s7-tag",
        "title": "🔵 Master Cheat Sheet: Slide 7 Formulas at a Glance",
        "subtitle": "Quick-reference table of every frequency domain formula for exam day",
        "content": r"""
        <div class="card s7">
          <div class="table-responsive"><table class="comparison-table">
            <thead>
              <tr><th>Concept</th><th>Formula / Transfer Function</th><th>Key Notes for Exam</th></tr>
            </thead>
            <tbody>
              <tr><td><strong>1D DFT</strong></td><td>$F(u) = \frac{1}{N} \sum_{x=0}^{N-1} f(x) e^{-j 2\pi ux / N}$</td><td>$u = 0, \dots, N-1$</td></tr>
              <tr><td><strong>2D DFT</strong></td><td>$F(u,v) = \frac{1}{MN} \sum_x \sum_y f(x,y) e^{-j 2\pi (ux/M + vy/N)}$</td><td>Separable into row 1D DFT then column 1D DFT</td></tr>
              <tr><td><strong>Centering</strong></td><td>Multiply $f(x,y)$ by $(-1)^{x+y}$</td><td>Shifts DC to $(M/2, N/2)$</td></tr>
              <tr><td><strong>DC Component</strong></td><td>$F(0,0) = \frac{1}{MN} \sum \sum f(x,y)$</td><td>Equal to average image brightness</td></tr>
              <tr><td><strong>Distance</strong></td><td>$D(u,v) = \sqrt{(u - M/2)^2 + (v - N/2)^2}$</td><td>Radius from centered origin</td></tr>
              <tr><td><strong>Ideal LPF</strong></td><td>$H = 1$ if $D \le D_0$, else $0$</td><td>Severe ringing (Gibbs phenomenon)</td></tr>
              <tr><td><strong>Butterworth LPF</strong></td><td>$H = \dfrac{1}{1 + [D/D_0]^{2n}}$</td><td>At $D_0$: $H = 0.5$; $n=1$ has no ringing</td></tr>
              <tr><td><strong>Gaussian LPF</strong></td><td>$H = e^{-D^2 / (2D_0^2)}$</td><td>At $D_0$: $H \approx 0.607$; <strong>100% ringing-free</strong></td></tr>
              <tr><td><strong>HPF from LPF</strong></td><td>$H_{hp}(u,v) = 1 - H_{lp}(u,v)$</td><td>Zeroes DC: $H(0,0) = 0$</td></tr>
              <tr><td><strong>Butterworth HPF</strong></td><td>$H = \dfrac{1}{1 + [D_0/D]^{2n}}$</td><td>Inverted ratio $D_0/D$</td></tr>
              <tr><td><strong>Gaussian HPF</strong></td><td>$H = 1 - e^{-D^2 / (2D_0^2)}$</td><td>Smooth, ringing-free edges</td></tr>
              <tr><td><strong>Laplacian</strong></td><td>$H(u,v) = -D^2(u,v)$</td><td>Enhancement: $H_{enh} = 1 + D^2(u,v)$</td></tr>
              <tr><td><strong>High-Boost</strong></td><td>$H_{hfe} = a + b \cdot H_{hp}(u,v)$</td><td>$a \approx 0.5$ preserves DC, $b \approx 2$ sharpens</td></tr>
              <tr><td><strong>FFT Complexity</strong></td><td>$\mathcal{O}(N \log_2 N)$</td><td>$100\times - 600\times$ faster than $\mathcal{O}(N^2)$</td></tr>
            </tbody>
          </table></div>
        </div>
        """
    },
    {
        "id": 33,
        "category": "MASTER CHEAT SHEET",
        "tag_class": "s8-tag",
        "title": "🟣 Master Cheat Sheet: Slide 8 Formulas at a Glance",
        "subtitle": "Quick-reference table of every image restoration and noise filter formula",
        "content": r"""
        <div class="card s8">
          <div class="table-responsive"><table class="comparison-table">
            <thead>
              <tr><th>Filter</th><th>Mathematical Formula</th><th>Best Used For / Exam Gotchas</th></tr>
            </thead>
            <tbody>
              <tr><td><strong>Arithmetic Mean</strong></td><td>$\hat{f} = \frac{1}{mn}\sum g(s,t)$</td><td>Gaussian noise; blurs edges</td></tr>
              <tr><td><strong>Geometric Mean</strong></td><td>$\hat{f} = [\prod g(s,t)]^{1/mn}$</td><td>Gaussian noise; preserves slightly more detail than arithmetic; <strong>fails if any pixel is 0</strong></td></tr>
              <tr><td><strong>Harmonic Mean</strong></td><td>$\hat{f} = \frac{mn}{\sum \frac{1}{g(s,t)}}$</td><td>Salt noise; <strong>FAILS on pepper noise</strong> ($1/0 \to \infty$)</td></tr>
              <tr><td><strong>Contraharmonic</strong></td><td>$\hat{f} = \frac{\sum g^{Q+1}}{\sum g^Q}$</td><td><strong>$Q>0$ for Pepper</strong>; <strong>$Q<0$ for Salt</strong>; $Q=0 \to$ Arithmetic; $Q=-1 \to$ Harmonic</td></tr>
              <tr><td><strong>Median Filter</strong></td><td>$\hat{f} = \text{median}\{g(s,t)\}$</td><td><strong>Salt & Pepper noise</strong>; zero blurring; preserves edges</td></tr>
              <tr><td><strong>Max Filter</strong></td><td>$\hat{f} = \max\{g(s,t)\}$</td><td>Eliminates Pepper (dark) noise</td></tr>
              <tr><td><strong>Min Filter</strong></td><td>$\hat{f} = \min\{g(s,t)\}$</td><td>Eliminates Salt (bright) noise</td></tr>
              <tr><td><strong>Midpoint Filter</strong></td><td>$\hat{f} = \frac{1}{2}[\max + \min]$</td><td>Uniform & Gaussian noise</td></tr>
              <tr><td><strong>Alpha-Trimmed</strong></td><td>$\hat{f} = \frac{1}{mn-d}\sum g_r(s,t)$</td><td>Mixed noise (Salt & Pepper + Gaussian); $d=0 \to$ Mean; $d=mn-1 \to$ Median</td></tr>
              <tr><td><strong>Adaptive Median</strong></td><td>Level A (window size) + Level B (pixel replace)</td><td>Dense impulse noise ($>20\%-50\%$); preserves thin lines</td></tr>
              <tr><td><strong>Band-Reject</strong></td><td>$H_{br}(u,v)$ in Fourier domain</td><td><strong>Periodic noise</strong> (removes conjugate frequency spikes)</td></tr>
            </tbody>
          </table></div>
        </div>
        """
    },
    {
        "id": 34,
        "category": "EXAM STRATEGY",
        "tag_class": "s7-tag",
        "title": "🧠 10/10 Exam Memory Tricks & Golden Rules",
        "subtitle": "10 quick mnemonics that prevent mistakes and guarantee full marks",
        "content": r"""
        <div class="card s7">
          <div class="grid-2">
            <div>
              <h4 style="color:var(--accent-blue);margin:0 0 10px;">Slide 7 Golden Rules:</h4>
              <ul style="color:var(--text-primary);font-size:13px;line-height:1.8;">
                <li>🧱 <strong>Brick wall = Ringing:</strong> Any filter with an abrupt step discontinuity in the frequency domain (like ILPF or high-order BLPF) WILL cause ringing ripples in the spatial domain.</li>
                <li>🔔 <strong>Gaussian is Invariant:</strong> The Fourier transform of a Gaussian is another Gaussian &rarr; <strong>GLPF and GHPF have ZERO ringing</strong>!</li>
                <li>🎯 <strong>Cutoff Points:</strong> Butterworth cuts at $H = 0.5$ (half-power); Gaussian cuts at $H = e^{-0.5} \approx 0.607$.</li>
                <li>🌓 <strong>Complement Rule:</strong> $H_{hp} = 1 - H_{lp}$. Because $H(0,0)=0$, pure HPFs erase the DC component and leave a dark gray background.</li>
                <li>⚡ <strong>Laplacian Plus Sign:</strong> $g = f - \nabla^2 f \Longleftrightarrow H = 1 - (-D^2) = 1 + D^2$.</li>
              </ul>
            </div>
            <div>
              <h4 style="color:var(--accent-purple);margin:0 0 10px;">Slide 8 Golden Rules:</h4>
              <ul style="color:var(--text-primary);font-size:13px;line-height:1.8;">
                <li>🌶️ <strong>P for Pepper &rarr; Positive Q:</strong> Contraharmonic with $Q > 0$ destroys Pepper noise. Negative $Q$ destroys Salt noise.</li>
                <li>💀 <strong>Harmonic Pepper Crash:</strong> Never use Harmonic mean or Geometric mean on pepper noise &mdash; zeroes in the window cause division by zero or a complete black-out!</li>
                <li>🛡️ <strong>Median is an Existing Pixel:</strong> Median does not compute new intermediate values; it picks an actual neighbor, keeping boundaries crisp.</li>
                <li>🎛️ <strong>AMF Hierarchy:</strong> Level A tests if the <em>median</em> is noise. Level B tests if the <em>center pixel</em> is noise.</li>
                <li>🌐 <strong>Domain Strategy:</strong> Spatial domain for random noise; Frequency domain (Band-Reject/Notch) for periodic noise.</li>
              </ul>
            </div>
          </div>
        </div>
        """
    },
    {
        "id": 35,
        "category": "CLASS TEST QUIZ",
        "tag_class": "s7-tag",
        "title": "🎯 Mock Class Test: Questions 1 – 5",
        "subtitle": "Test your knowledge on frequency domain fundamentals and filtering",
        "content": r"""
        <div class="card s7">
          <!-- Q1 -->
          <div class="question-card" id="qc-1" style="margin-bottom:20px;">
            <div class="q-num">Question 1 of 15</div>
            <div class="q-text">In frequency domain filtering, what does the step "multiply f(x,y) by (-1)^(x+y)" achieve?</div>
            <div class="q-options">
              <button class="q-option" onclick="answer(1, this, false)">A) It removes noise from the image</button>
              <button class="q-option" onclick="answer(1, this, true)">B) It shifts the Fourier transform so the DC component appears at the centre of the spectrum</button>
              <button class="q-option" onclick="answer(1, this, false)">C) It applies the Gaussian filter</button>
              <button class="q-option" onclick="answer(1, this, false)">D) It converts the image to grayscale</button>
            </div>
            <div class="q-feedback" id="fb-1"></div>
          </div>

          <!-- Q2 -->
          <div class="question-card" id="qc-2" style="margin-bottom:20px;">
            <div class="q-num">Question 2 of 15</div>
            <div class="q-text">What is the formula for a Butterworth Low-Pass Filter of order n with cutoff D₀?</div>
            <div class="q-options">
              <button class="q-option" onclick="answer(2, this, false)">A) $H = e^{-D^2/2D_0^2}$</button>
              <button class="q-option" onclick="answer(2, this, false)">B) $H = 1$ if $D \le D_0$, else $0$</button>
              <button class="q-option" onclick="answer(2, this, true)">C) $H(u,v) = \dfrac{1}{1 + [D(u,v)/D_0]^{2n}}$</button>
              <button class="q-option" onclick="answer(2, this, false)">D) $H(u,v) = 1 - e^{-D^2/2D_0^2}$</button>
            </div>
            <div class="q-feedback" id="fb-2"></div>
          </div>

          <!-- Q3 -->
          <div class="question-card" id="qc-3" style="margin-bottom:20px;">
            <div class="q-num">Question 3 of 15</div>
            <div class="q-text">Which low-pass filter causes severe ringing (Gibbs phenomenon) artefacts?</div>
            <div class="q-options">
              <button class="q-option" onclick="answer(3, this, false)">A) Gaussian LPF</button>
              <button class="q-option" onclick="answer(3, this, false)">B) Butterworth LPF (n=1)</button>
              <button class="q-option" onclick="answer(3, this, true)">C) Ideal LPF</button>
              <button class="q-option" onclick="answer(3, this, false)">D) Alpha-trimmed LPF</button>
            </div>
            <div class="q-feedback" id="fb-3"></div>
          </div>

          <!-- Q4 -->
          <div class="question-card" id="qc-4" style="margin-bottom:20px;">
            <div class="q-num">Question 4 of 15</div>
            <div class="q-text">Given that H_lp(u,v) is a low-pass filter, what is the equivalent high-pass filter H_hp(u,v)?</div>
            <div class="q-options">
              <button class="q-option" onclick="answer(4, this, false)">A) $H_{hp} = 1 / H_{lp}$</button>
              <button class="q-option" onclick="answer(4, this, true)">B) $H_{hp} = 1 - H_{lp}$</button>
              <button class="q-option" onclick="answer(4, this, false)">C) $H_{hp} = -H_{lp}$</button>
              <button class="q-option" onclick="answer(4, this, false)">D) $H_{hp} = \sqrt{1 - H_{lp}}$</button>
            </div>
            <div class="q-feedback" id="fb-4"></div>
          </div>

          <!-- Q5 -->
          <div class="question-card" id="qc-5">
            <div class="q-num">Question 5 of 15</div>
            <div class="q-text">The Gaussian high-pass filter formula is:</div>
            <div class="q-options">
              <button class="q-option" onclick="answer(5, this, false)">A) $H = e^{-D^2/2D_0^2}$</button>
              <button class="q-option" onclick="answer(5, this, true)">B) $H(u,v) = 1 - e^{-D^2(u,v)/2D_0^2}$</button>
              <button class="q-option" onclick="answer(5, this, false)">C) $H = 1 / (1 + [D_0/D]^{2n})$</button>
              <button class="q-option" onclick="answer(5, this, false)">D) $H = -D^2$</button>
            </div>
            <div class="q-feedback" id="fb-5"></div>
          </div>
        </div>
        """
    },
    {
        "id": 36,
        "category": "CLASS TEST QUIZ",
        "tag_class": "s8-tag",
        "title": "🎯 Mock Class Test: Questions 6 – 10",
        "subtitle": "Test your knowledge on noise models and spatial restoration filters",
        "content": r"""
        <div class="card s8">
          <!-- Q6 -->
          <div class="question-card" id="qc-6" style="margin-bottom:20px;">
            <div class="q-num">Question 6 of 15</div>
            <div class="q-text">The additive noise model in image restoration is expressed as:</div>
            <div class="q-options">
              <button class="q-option" onclick="answer(6, this, false)">A) $g(x,y) = f(x,y) \cdot \eta(x,y)$</button>
              <button class="q-option" onclick="answer(6, this, true)">B) $g(x,y) = f(x,y) + \eta(x,y)$</button>
              <button class="q-option" onclick="answer(6, this, false)">C) $g(x,y) = f(x,y) / \eta(x,y)$</button>
              <button class="q-option" onclick="answer(6, this, false)">D) $g(x,y) = f(x,y) - \eta(x,y)$</button>
            </div>
            <div class="q-feedback" id="fb-6"></div>
          </div>

          <!-- Q7 -->
          <div class="question-card" id="qc-7" style="margin-bottom:20px;">
            <div class="q-num">Question 7 of 15</div>
            <div class="q-text">Which spatial filter is BEST for removing salt-and-pepper noise while preserving edges?</div>
            <div class="q-options">
              <button class="q-option" onclick="answer(7, this, false)">A) Arithmetic Mean Filter</button>
              <button class="q-option" onclick="answer(7, this, false)">B) Geometric Mean Filter</button>
              <button class="q-option" onclick="answer(7, this, true)">C) Median Filter</button>
              <button class="q-option" onclick="answer(7, this, false)">D) Harmonic Mean Filter</button>
            </div>
            <div class="q-feedback" id="fb-7"></div>
          </div>

          <!-- Q8 -->
          <div class="question-card" id="qc-8" style="margin-bottom:20px;">
            <div class="q-num">Question 8 of 15</div>
            <div class="q-text">In the contraharmonic mean filter, what value of Q should you use to eliminate PEPPER (dark) noise?</div>
            <div class="q-options">
              <button class="q-option" onclick="answer(8, this, true)">A) Positive Q (Q &gt; 0)</button>
              <button class="q-option" onclick="answer(8, this, false)">B) Negative Q (Q &lt; 0)</button>
              <button class="q-option" onclick="answer(8, this, false)">C) Exactly Q = 0</button>
              <button class="q-option" onclick="answer(8, this, false)">D) Exactly Q = -1</button>
            </div>
            <div class="q-feedback" id="fb-8"></div>
          </div>

          <!-- Q9 -->
          <div class="question-card" id="qc-9" style="margin-bottom:20px;">
            <div class="q-num">Question 9 of 15</div>
            <div class="q-text">The midpoint filter is computed as:</div>
            <div class="q-options">
              <button class="q-option" onclick="answer(9, this, false)">A) Average of all values in window</button>
              <button class="q-option" onclick="answer(9, this, true)">B) Half the sum of the maximum and minimum values: ½[max + min]</button>
              <button class="q-option" onclick="answer(9, this, false)">C) The middle value in a sorted list</button>
              <button class="q-option" onclick="answer(9, this, false)">D) Product of max and min</button>
            </div>
            <div class="q-feedback" id="fb-9"></div>
          </div>

          <!-- Q10 -->
          <div class="question-card" id="qc-10">
            <div class="q-num">Question 10 of 15</div>
            <div class="q-text">Periodic noise in images is MOST effectively removed by:</div>
            <div class="q-options">
              <button class="q-option" onclick="answer(10, this, false)">A) Spatial median filter</button>
              <button class="q-option" onclick="answer(10, this, false)">B) Arithmetic mean filter</button>
              <button class="q-option" onclick="answer(10, this, true)">C) Frequency domain band-reject or notch filter</button>
              <button class="q-option" onclick="answer(10, this, false)">D) Laplacian sharpening</button>
            </div>
            <div class="q-feedback" id="fb-10"></div>
          </div>
        </div>
        """
    },
    {
        "id": 37,
        "category": "CLASS TEST QUIZ",
        "tag_class": "s8-tag",
        "title": "🎯 Mock Class Test: Questions 11 – 15",
        "subtitle": "Test your mastery on advanced filters, algorithm steps and restoration theory",
        "content": r"""
        <div class="card s8">
          <!-- Q11 -->
          <div class="question-card" id="qc-11" style="margin-bottom:20px;">
            <div class="q-num">Question 11 of 15</div>
            <div class="q-text">In the Alpha-Trimmed Mean filter, when d = mn - 1 (maximum trimming), the filter becomes equivalent to:</div>
            <div class="q-options">
              <button class="q-option" onclick="answer(11, this, false)">A) Arithmetic Mean Filter</button>
              <button class="q-option" onclick="answer(11, this, true)">B) Median Filter</button>
              <button class="q-option" onclick="answer(11, this, false)">C) Midpoint Filter</button>
              <button class="q-option" onclick="answer(11, this, false)">D) Harmonic Mean Filter</button>
            </div>
            <div class="q-feedback" id="fb-11"></div>
          </div>

          <!-- Q12 -->
          <div class="question-card" id="qc-12" style="margin-bottom:20px;">
            <div class="q-num">Question 12 of 15</div>
            <div class="q-text">What happens at the cutoff frequency D₀ for a Gaussian LPF (what is the value of H)?</div>
            <div class="q-options">
              <button class="q-option" onclick="answer(12, this, false)">A) $H(D_0) = 0$</button>
              <button class="q-option" onclick="answer(12, this, false)">B) $H(D_0) = 0.5$</button>
              <button class="q-option" onclick="answer(12, this, true)">C) $H(D_0) = e^{-0.5} \approx 0.607$</button>
              <button class="q-option" onclick="answer(12, this, false)">D) $H(D_0) = 1.0$</button>
            </div>
            <div class="q-feedback" id="fb-12"></div>
          </div>

          <!-- Q13 -->
          <div class="question-card" id="qc-13" style="margin-bottom:20px;">
            <div class="q-num">Question 13 of 15</div>
            <div class="q-text">The Fast Fourier Transform (FFT) reduces DFT computation complexity from O(N²) to:</div>
            <div class="q-options">
              <button class="q-option" onclick="answer(13, this, false)">A) $\mathcal{O}(N)$</button>
              <button class="q-option" onclick="answer(13, this, true)">B) $\mathcal{O}(N \log_2 N)$</button>
              <button class="q-option" onclick="answer(13, this, false)">C) $\mathcal{O}(\sqrt{N})$</button>
              <button class="q-option" onclick="answer(13, this, false)">D) $\mathcal{O}(N^{1.5})$</button>
            </div>
            <div class="q-feedback" id="fb-13"></div>
          </div>

          <!-- Q14 -->
          <div class="question-card" id="qc-14" style="margin-bottom:20px;">
            <div class="q-num">Question 14 of 15</div>
            <div class="q-text">In the Adaptive Median Filter (AMF) algorithm, what does Level A check?</div>
            <div class="q-options">
              <button class="q-option" onclick="answer(14, this, false)">A) If the center pixel z_xy is an impulse</button>
              <button class="q-option" onclick="answer(14, this, true)">B) If the median value z_med itself is an impulse (z_min &lt; z_med &lt; z_max)</button>
              <button class="q-option" onclick="answer(14, this, false)">C) If the noise is Gaussian</button>
              <button class="q-option" onclick="answer(14, this, false)">D) If the image is color or grayscale</button>
            </div>
            <div class="q-feedback" id="fb-14"></div>
          </div>

          <!-- Q15 -->
          <div class="question-card" id="qc-15">
            <div class="q-num">Question 15 of 15</div>
            <div class="q-text">Which statement about image restoration vs. image enhancement is CORRECT?</div>
            <div class="q-options">
              <button class="q-option" onclick="answer(15, this, true)">A) Restoration is objective and model-based; enhancement is subjective and heuristic</button>
              <button class="q-option" onclick="answer(15, this, false)">B) Restoration is subjective; enhancement is objective</button>
              <button class="q-option" onclick="answer(15, this, false)">C) Both require an explicit mathematical noise model</button>
              <button class="q-option" onclick="answer(15, this, false)">D) Enhancement can only be done in the frequency domain</button>
            </div>
            <div class="q-feedback" id="fb-15"></div>
          </div>
        </div>
        """
    },
    {
        "id": 38,
        "category": "QUIZ EVALUATION",
        "tag_class": "s8-tag",
        "title": "🏆 Mock Exam Score, Evaluation & Final Checklist",
        "subtitle": "Check your readiness score and review the 10/10 exam checklist",
        "content": r"""
        <div class="card s8" style="text-align:center;padding:30px 20px;">
          <div style="font-size:54px;margin-bottom:12px;">🎓</div>
          <h3 style="font-size:26px;color:var(--text-primary);margin:0 0 10px;">Your Class Test Readiness</h3>
          
          <div id="score-display" class="show" style="margin:20px auto;max-width:480px;background:var(--bg-secondary);padding:24px;border-radius:12px;border:1px solid var(--border);">
            <div class="score-number" id="score-num" style="font-size:48px;font-weight:800;color:var(--accent-green);">0/15</div>
            <div class="score-label" id="score-label" style="margin-top:10px;font-size:16px;">Complete questions on Slides 35–37 to evaluate your score!</div>
          </div>

          <div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap;margin:24px 0;">
            <button class="quiz-submit-btn" style="margin:0;" onclick="submitQuiz()">📊 Calculate Live Score</button>
            <button class="quick-nav-btn" style="padding:12px 24px;font-size:15px;" onclick="goToSlide(35)">↩ Go to Questions 1–5</button>
            <button class="quick-nav-btn" style="padding:12px 24px;font-size:15px;" onclick="goToSlide(1)">🏠 Return to Slide 1</button>
          </div>

          <div class="callout callout-green" style="text-align:left;max-width:700px;margin:24px auto 0;">
            <span class="callout-icon">✅</span>
            <div>
              <strong style="color:var(--accent-green);font-size:16px;">Final 10/10 Exam Readiness Checklist:</strong>
              <ul style="margin-top:8px;font-size:13px;line-height:1.7;color:var(--text-primary);">
                <li>&check; Know the 6-Step Frequency Filtering Protocol by heart (Slide 4).</li>
                <li>&check; Know the ILPF, BLPF, and GLPF formulas and ringing behaviors (Slides 7–9).</li>
                <li>&check; Know the High-Pass complement rule $H_{hp} = 1 - H_{lp}$ and High-Boost $a + b \cdot H_{hp}$ (Slides 11–15).</li>
                <li>&check; Know why Harmonic Mean fails on Pepper noise ($1/0 \to \infty$) (Slide 22).</li>
                <li>&check; Know Contraharmonic $Q$ signs: $Q > 0$ for Pepper, $Q < 0$ for Salt (Slide 22–23).</li>
                <li>&check; Understand the 7&times;7 blackboard calculations for both 204 and 0 (Slide 27).</li>
                <li>&check; Memorize the 2-level logic of Adaptive Median Filter (AMF) (Slide 30).</li>
              </ul>
            </div>
          </div>
        </div>
        """
    }
]

print(f"Total slides defined: {len(slides_data)}")
