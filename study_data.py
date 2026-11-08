"""Beginner-first lessons. Times add up to a two-hour study session."""

def formula(expression, note=""):
    return f'<div class="formula"><div>{expression}</div><p>{note}</p></div>'

def example(title, steps, result):
    return '<section class="example"><div class="eyebrow">WORKED EXAMPLE</div><h3>'+title+'</h3><ol>'+''.join('<li>'+s+'</li>' for s in steps)+'</ol><div class="result">'+result+'</div></section>'

def recall(question, answer):
    return f'<section class="recall"><div class="eyebrow">PAUSE & RECALL</div><p>{question}</p><details><summary>Check your answer</summary><div>{answer}</div></details></section>'

def note(text):
    return f'<aside class="note"><strong>CT pitfall</strong><p>{text}</p></aside>'

def table(head, rows):
    return '<div class="table-wrap"><table><thead><tr>'+''.join('<th scope="col">'+h+'</th>' for h in head)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+c+'</td>' for c in r)+'</tr>' for r in rows)+'</tbody></table></div>'

lessons=[]
def add(title, group, minutes, goal, body, pages=None):
    lessons.append(dict(id=len(lessons)+1,title=title,group=group,minutes=minutes,goal=goal,body=body,pages=pages))

add('Start here. You can learn this.', 'Start', 2,
    'Use the next two hours to understand the ideas, practise the calculations, and test what you remember.',
    '''<div class="intro-banner"><span class="eyebrow">YOUR TWO-HOUR STUDY PLAN</span><p>Two lectures.<br>One clear path.</p><div>Start with the basics. Work each example on paper. Then close the answers and try the final test.</div></div>
    <h2>What are these topics about?</h2><p>An image is a grid of numbers. <strong>Lecture 7</strong> changes the image by controlling its slow and fast patterns. <strong>Lecture 8</strong> removes unwanted noise from those numbers.</p>
    <div class="route"><div><b>01</b><strong>Build your foundation</strong><span>0–18 min · Lessons 1–4</span></div><div><b>02</b><strong>Understand frequency filters</strong><span>18–57 min · Lessons 5–13</span></div><div><b>03</b><strong>Remove noise & solve math</strong><span>57–102 min · Lessons 14–22</span></div><div><b>04</b><strong>Recall, then test yourself</strong><span>102–120 min · Lessons 23–24</span></div></div>
    <h2>How to use this deck</h2><p>Read the main idea, follow the numbered calculation, then answer <strong>Pause & recall</strong> before revealing it. Mark a lesson studied only after you can explain it. Use <strong>Review later</strong> when you get stuck; keep moving.</p><p class="muted">The times are a pacing guide, not a deadline per page. All examples and formulas work offline. Your progress stays in this browser.</p><button class="primary" data-go="2">Begin with pixels <span aria-hidden="true">→</span></button>''')

add('An image is a grid of numbers', 'Foundations', 5,
    'Understand pixels, intensity, coordinates, and a 3 × 3 neighbourhood.',
    '''<p>A grayscale image stores one brightness number per pixel. In an <strong>8-bit image</strong>, 0 means black, 255 means white, and values between them are shades of gray.</p><div class="pixel-demo"><div style="--v:0">0</div><div style="--v:64">64</div><div style="--v:128">128</div><div style="--v:192">192</div><div style="--v:255">255</div></div><p>We write an image as <span class="math">f(x,y)</span>: the number at position (x,y). Here x means column and y means row, counted from zero.</p><h2>What does a filter do?</h2><p>A spatial filter takes a small window around a pixel, calculates a new value, and writes that value at the window’s centre in a <strong>separate output image</strong>. Then it moves to the next pixel.</p>'''+example('Replace the centre of a 3 × 3 window',[
    'The window contains [10, 10, 10; 10, <strong>100</strong>, 10; 10, 10, 10]. There are 9 values.',
    'An averaging filter adds all of them: 8 × 10 + 100 = 180.',
    'Divide by 9: 180 / 9 = 20. Write 20 at the centre of the output.'],
    'Centre pixel: 100 → 20. One bright spike is reduced, but averaging can also blur real detail.')+
    note('A 3 × 3 filter does not replace the whole window with one value. It produces one output pixel per window. At image borders, state a padding rule if a question asks for the full output.')+
    recall('How many values are used by a 5 × 5 filter? Which output pixel is calculated?', '25 values. Their calculation gives the output value at the centre of that window.'))

add('Frequency means how fast brightness changes', 'Foundations', 5,
    'Connect slow patterns to low frequencies and edges to high frequencies.',
    '''<p><strong>Spatial domain</strong> means looking at pixel values and positions. <strong>Frequency domain</strong> means looking at the patterns that make up those pixels.</p>
    <div class="compare"><section><h3>Low frequency</h3><div class="swatch slow"></div><p>Brightness changes slowly across space. Think: a smooth sky, background shading, or broad shapes.</p></section><section><h3>High frequency</h3><div class="swatch fast"></div><p>Brightness changes quickly. Think: edges, fine text, tiny details, or some kinds of noise.</p></section></div>
    <p>Fourier’s idea: build a complicated signal by adding simple waves of different frequencies, strengths, and positions.</p>'''+example('Read two short pixel rows',[
    '[50, 51, 52, 53, 54] changes by only 1 at a time → mostly slow variation.',
    '[0, 255, 0, 255, 0] changes sharply at every step → strong high-frequency variation.',
    'A constant row [50, 50, 50, 50] has only a zero-frequency component, called <strong>DC</strong>.'],
    'Low-pass keeps slow changes → smoothing. High-pass keeps fast changes → edges.')+
    note('High frequency does not mean “bright.” A bright constant image is DC. Also, useful edges and unwanted noise can both contain high frequencies.')+
    recall('If you remove high frequencies from printed text, what happens?', 'The sharp character boundaries become softer. Small details can disappear: this is low-pass smoothing.'),[7,4])

add('The Fourier transform, without the fear', 'Foundations', 6,
    'Know what F(u,v) means and calculate one tiny DFT by hand.',
    '''<p>The <strong>Discrete Fourier Transform (DFT)</strong> converts a finite list or image into frequency coefficients. A coefficient tells us how strongly a particular wave is present. It can be complex: <span class="math">j² = −1</span>.</p>'''+
    formula('F(k) = ∑<sub>x=0</sub><sup>N−1</sup> f(x)e<sup>−j2πkx/N</sup>', '1D DFT: N = number of samples, x = sample position, k = frequency index. ∑ means “add over all x.”')+
    example('Two pixels: f = [10, 20]',[
    'For k = 0: every exponential is 1. F(0) = 10 + 20 = <strong>30</strong> (the DC sum).',
    'For k = 1: e⁰ = 1 and e<sup>−jπ</sup> = −1. F(1) = 10 − 20 = <strong>−10</strong>.',
    'Inverse: f(0) = (30 − 10)/2 = 10; f(1) = (30 + 10)/2 = 20.'],
    'A transform changes the representation. The inverse recovers the original samples.')+
    '<h2>Now extend it to an image</h2>'+
    formula('F(u,v) = ∑<sub>x=0</sub><sup>M−1</sup> ∑<sub>y=0</sub><sup>N−1</sup> f(x,y)e<sup>−j2π(ux/M + vy/N)</sup>', 'M,N = image dimensions in this summation convention. u,v index frequencies along the corresponding axes.')+
    formula('f(x,y) = (1/MN) ∑<sub>u=0</sub><sup>M−1</sup> ∑<sub>v=0</sub><sup>N−1</sup> F(u,v)e<sup>+j2π(ux/M + vy/N)</sup>', 'Inverse DFT: the sign changes to + and we divide by MN.')+
    '<p><strong>Magnitude</strong> |F| gives strength; <strong>phase</strong> gives relative alignment and carries important structure. A displayed spectrum often uses log(1 + |F|) so weak details become visible.</p>'+
    recall('What is F(0,0) for a 2 × 2 image [1,2;3,4]?', '1 + 2 + 3 + 4 = 10. With this unnormalised forward DFT, DC is the sum; average intensity is 10/4 = 2.5.'),[7,7])

add('The frequency-filtering recipe', 'Lecture 7', 5,
    'Explain the processing steps and why multiplication replaces convolution.',
    '''<p>A frequency filter is a grid of weights <span class="math">H(u,v)</span>. Multiply each Fourier coefficient by its matching weight: 1 keeps it, 0 removes it, and 0.5 halves its amplitude.</p><div class="pipeline"><span>Image f</span><b>→</b><span>DFT: F</span><b>→</b><span>G = HF</span><b>→</b><span>Inverse DFT: g</span></div>'''+
    formula('g = f ∗ h &nbsp; ↔ &nbsp; G = F · H', 'Convolution theorem: ∗ is spatial convolution; · is pointwise frequency multiplication. h is the spatial filter, H its transform.')+
    '''<h2>Write these steps in a theory answer</h2><ol class="steps"><li><strong>Prepare:</strong> pad the image if needed to reduce circular wraparound. A common choice is P = 2M, Q = 2N.</li><li><strong>Centre:</strong> multiply the padded image by (−1)<sup>x+y</sup>.</li><li><strong>Transform:</strong> compute the 2D DFT F.</li><li><strong>Filter:</strong> form G(u,v) = H(u,v)F(u,v), with H centred the same way.</li><li><strong>Invert:</strong> take the inverse DFT; use its real part (tiny imaginary errors can occur).</li><li><strong>Undo centring:</strong> multiply by (−1)<sup>x+y</sup> again and crop to the original size.</li></ol>'''+
    example('One coefficient, one multiplication', ['Suppose F(u,v) = 80 and H(u,v) = 0.25.', 'Then G(u,v) = 80 × 0.25 = 20. Other coefficients are processed separately.'], 'That frequency’s amplitude is reduced to one quarter.')+
    note('The checkerboard centring method assumes even transform dimensions for an exact half-grid shift. fftshift is another way to rearrange the spectrum; keep the inverse shift consistent. Do not apply two centring methods together.')+
    recall('Why can filtering be convenient in the frequency domain?', 'Convolution in space becomes pointwise multiplication in frequency. You can directly select which frequency components to keep.'),[7,15])

add('Find the distance from DC', 'Lecture 7', 3,
    'Calculate D(u,v), the input used by circular frequency filters.',
    '''<p>After centring, the middle of the spectrum is DC. Frequencies farther away represent faster spatial changes. A circular filter uses distance from that centre.</p>'''+
    formula('D(u,v) = √[(u − P/2)² + (v − Q/2)²]', 'P,Q are the transform dimensions. D₀ is a chosen cutoff distance, not the DC value.')+
    example('A centred 8 × 8 spectrum; point (1,0)', ['The centre is (4,4). The offsets are 1 − 4 = −3 and 0 − 4 = −4.', 'Square, add, then take the square root: D = √[(−3)² + (−4)²] = √25 = 5.'], 'At (1,0), D = 5. Compare that distance with D₀ to get the filter weight.')+
    recall('In an 8 × 8 centred spectrum, what is D(4,4)? What does it represent?', 'D = 0. This is the DC location.'),[7,21])

add('Ideal low-pass: keep the inner circle', 'Lecture 7', 5,
    'Use an ideal LPF and explain smoothing and ringing.',
    '''<p>A <strong>low-pass filter (LPF)</strong> keeps low frequencies and suppresses high frequencies. The ideal version acts like a hard gate: inside the cutoff circle is kept; outside is removed.</p>'''+
    formula('H<sub>ILP</sub>(D) = 1 if D ≤ D₀; &nbsp; 0 if D > D₀', 'D = distance from DC; D₀ = cutoff radius. The gain H is a multiplier, not an intensity.')+
    example('D₀ = 10; filter three coefficients', ['At D = 4: H = 1 → F = 80 becomes G = 80.', 'At D = 10: H = 1 under the stated ≤ convention.', 'At D = 15: H = 0 → F = 80 becomes G = 0.'], 'A smaller D₀ removes more frequencies → stronger blur.')+
    '<h2>Why do halos appear?</h2><p>The abrupt frequency cutoff corresponds to an oscillating spatial response. Around a sharp edge, it can create alternating bright and dark ripples: <strong>ringing</strong>. A gentler frequency transition reduces this problem.</p>'+
    recall('If D₀ increases, will an ideal LPF usually blur more or less?', 'Less: a larger pass region retains more high-frequency detail. The ideal cutoff can still cause ringing.'),[7,20])

add('Butterworth: a softer cutoff', 'Lecture 7', 5,
    'Substitute D, D₀, and order n into the Butterworth formula.',
    formula('H<sub>BLP</sub>(D) = 1 / [1 + (D/D₀)<sup>2n</sup>]', 'n is a positive integer order. Larger n gives a steeper transition, more like an ideal filter.')+
    example('D₀ = 10 and n = 2', ['At D = 0: H = 1/(1+0) = <strong>1</strong>.', 'At D = 10: D/D₀ = 1, so H = 1/(1+1⁴) = <strong>0.5</strong>.', 'At D = 20: D/D₀ = 2, so H = 1/(1+2⁴) = 1/17 ≈ <strong>0.0588</strong>.'], 'At D = D₀, Butterworth gain is always 0.5, independent of order.')+
    '<p>A low-order Butterworth filter is smoother than an ideal filter. Increasing the order sharpens the cutoff and can increase ringing.</p>'+
    note('H = 0.5 means half <em>amplitude</em>. Power is proportional to amplitude squared, so the power fraction is 0.25. Do not call H = 0.5 “half-power.”')+
    recall('For n = 1, D = 2D₀, what is H?', '1/(1 + 2²) = 1/5 = 0.2. Write the ratio before raising it to 2n.'),[7,28])

add('Gaussian: the smoothest transition', 'Lecture 7', 5,
    'Calculate Gaussian gain and compare the three low-pass families.',
    formula('H<sub>GLP</sub>(D) = e<sup>−D²/(2D₀²)</sup>', 'e ≈ 2.718. D₀ controls the spread. The response changes smoothly rather than switching off.')+
    example('D₀ = 10', ['At D = 0: exponent = 0 → H = e⁰ = <strong>1</strong>.', 'At D = 10: exponent = −100/200 = −0.5 → H ≈ <strong>0.6065</strong>.', 'At D = 20: exponent = −400/200 = −2 → H ≈ <strong>0.1353</strong>.'], 'An ideal Gaussian response has no oscillating spatial lobes, so it avoids cutoff-induced ringing.')+
    table(['LPF','Transition','At D₀','Remember'],[['Ideal','Abrupt','1 (≤ convention)','Hard cutoff; ringing'],['Butterworth','Order-controlled','0.5','Higher n → steeper'],['Gaussian','Very smooth','≈ 0.607','No cutoff-induced ringing']])+
    note('At the same D₀, these filters do not have identical gains. Do not substitute the Butterworth cutoff value into the Gaussian formula.')+
    recall('What happens to Gaussian gain at a fixed D if you decrease D₀?', 'The negative exponent has larger magnitude, so H decreases. More frequencies are attenuated; the image becomes smoother.'),[7,32])

add('See what a filter actually keeps', 'Lecture 7', 4,
    'Move the cutoff and connect the response curve to an actual filtered signal.',
    '''<p>This small signal contains a slow wave (frequency 2) and a fast wave (frequency 12). The curves below are computed from those components and the selected filter gains.</p>
    <section class="lab"><div class="lab-controls"><label>Filter family<select id="family"><option value="ideal">Ideal</option><option value="butter">Butterworth (n = 2)</option><option value="gaussian" selected>Gaussian</option></select></label><label>Pass type<select id="pass"><option value="low">Low-pass</option><option value="high">High-pass</option></select></label><label class="range-label">Cutoff D₀: <output id="cutoff-value">6</output><input id="cutoff" type="range" min="1" max="20" value="6"></label></div><figure><svg id="response-plot" viewBox="0 0 660 220" role="img" aria-label="Filter gain versus distance from DC"></svg><figcaption>Filter response · horizontal: distance D · vertical: gain H</figcaption></figure><figure><svg id="signal-plot" viewBox="0 0 660 180" role="img" aria-label="Input and filtered signal"></svg><figcaption><span class="legend original">Original</span><span class="legend filtered">Filtered</span> · horizontal: sample position · vertical: brightness</figcaption></figure><p id="gain-readout" class="result" aria-live="polite"></p></section>
    <div class="image-lab"><figure><canvas id="frequency-original" width="128" height="128" role="img" aria-label="Synthetic image with slow vertical bands and fine horizontal stripes"></canvas><figcaption>Original image</figcaption></figure><figure><canvas id="frequency-mask" width="128" height="128" role="img" aria-label="Centred two-dimensional filter gain mask"></canvas><figcaption>Filter mask H · white = keep</figcaption></figure><figure><canvas id="frequency-output" width="128" height="128" role="img" aria-label="Image after the chosen frequency filter"></canvas><figcaption>Filtered image</figcaption></figure></div><p class="small muted">The synthetic image adds a slow frequency-2 wave across columns and a fast frequency-12 wave across rows. The filter scales both components by their exact gains. High-pass output is displayed with 128 added for visibility.</p>
    <h2>Try this sequence</h2><ol><li>Use Gaussian low-pass at D₀ = 3. The fine horizontal stripes fade.</li><li>Raise D₀ to 20. More of the fast stripes survive.</li><li>Switch to high-pass. The broad, slow bands fade instead.</li></ol>'''+
    note('Read the mask as gain: white = 1 (keep), black = 0 (remove). The mask is centred, but the spatial image is not a map of frequencies. These sinusoidal examples demonstrate attenuation; sharp-edge ringing needs an edge-containing input.')+
    recall('At a frequency where low-pass gain is 0.2, what is complementary high-pass gain?', '1 − 0.2 = 0.8.'))

add('High-pass filters find rapid changes', 'Lecture 7', 4,
    'Obtain each HPF from its LPF complement and recognise lost brightness.',
    '''<p>A <strong>high-pass filter (HPF)</strong> suppresses slow variation and keeps fast variation. Its output emphasises edges, but can also amplify visible noise.</p>'''+
    formula('H<sub>HP</sub> = 1 − H<sub>LP</sub>', 'At DC, the LPFs here have H = 1, so their complementary HPFs have H = 0.')+
    table(['Family','High-pass gain'],[['Ideal','0 for D ≤ D₀; 1 for D > D₀'],['Butterworth','1 / [1 + (D₀/D)²ⁿ] for D > 0; define H(0) = 0'],['Gaussian','1 − e<sup>−D²/(2D₀²)</sup>']])+
    example('Gaussian HPF at D = D₀', ['The matching GLPF gives e⁻⁰·⁵ ≈ 0.6065.', 'GHPF gives 1 − 0.6065 = <strong>0.3935</strong>.', 'At D = 0, H = 1 − 1 = 0: average brightness is removed.'], 'An edge image alone is not the original image with improved brightness.')+
    recall('For an ideal HPF, what happens when D₀ gets larger?', 'More low and middle frequencies are blocked. Fewer frequencies pass; only finer rapid changes remain.'),[7,40])

add('Sharpening: put detail back into the image', 'Lecture 7', 4,
    'Distinguish high-frequency emphasis from Laplacian sharpening.',
    '''<p>To keep the background while strengthening detail, combine the original with a high-pass result.</p>'''+
    formula('H<sub>emphasis</sub> = a + bH<sub>HP</sub>', 'a > 0 retains some low-frequency background; b > 0 adds detail. A common choice is a = 1, b > 0.')+
    example('Use a = 1 and b = 2', ['At DC, H<sub>HP</sub> = 0 → emphasis gain = 1.', 'At a high frequency with H<sub>HP</sub> ≈ 1 → emphasis gain ≈ 3.', 'Background is retained while that high-frequency component is tripled.'], 'Emphasis preserves a brightness baseline; a pure HPF removes DC.')+
    '<h2>The Laplacian is a second derivative</h2><p>For continuous spatial coordinates, the frequency multiplier of ∇² is −4π²(u²+v²). In centred coordinates this is often written −4π²D², with frequency scaling specified.</p>'+
    formula('g = f − c∇²f &nbsp; ⇒ &nbsp; G = [1 + 4π²cD²] F', 'c > 0. This sign assumes the Laplacian kernel has a negative centre, e.g. [0,1,0; 1,−4,1; 0,1,0].')+
    note('The exact discrete Laplacian response differs from the continuous D² formula. Some lectures absorb 4π² into a constant or reverse the kernel sign; keep the subtraction/addition consistent with the stated convention.')+
    recall('A negative-centre Laplacian gives ∇²f = −20 at a pixel with f = 100. If c = 1, what is g?', 'g = 100 − (−20) = 120. Subtracting a negative detail response raises that pixel.'),[7,54])

add('FFT & template matching', 'Lecture 7', 4,
    'Explain why FFT is useful and what correlation locates.',
    '''<h2>FFT is a fast way to calculate the DFT</h2><p>The transform is the same; the algorithm is faster. For a 1D length-L signal, a direct DFT uses O(L²) work, while an FFT typically uses O(L log L).</p>'''+
    example('Compare growth for L = 1024', ['L² = 1,048,576.', 'L log₂L = 1024 × 10 = 10,240.', 'Their ratio is about 102.4. These are operation-growth estimates, not a guaranteed measured speedup.'], 'For an M × N image, a separable FFT typically takes O(MN(log M + log N)).')+
    '''<h2>Correlation asks: where does this pattern fit?</h2><p>Slide a small template over an image and measure how well they match at each shift. A strong correlation peak indicates a candidate location.</p>'''+
    formula('r = IDFT{ F · W* }', 'F is the image transform; W is the zero-padded template transform; * here means complex conjugate, not convolution. This convention computes correlation by circular shifts unless adequately padded.')+
    '<p>Example: an image row [0,1,1,0] contains template [1,1] beginning at index 1. An unnormalised dot-product match there is 1×1 + 1×1 = 2. Other shifts score less. Normalised correlation helps when brightness or contrast vary.</p>'+
    recall('Does FFT produce a different frequency representation from DFT?', 'No. FFT is an efficient algorithm for computing the DFT.'),[7,61])

add('Restoration starts with a damage model', 'Lecture 8', 3,
    'Separate original image, blur, noise, and the observed image.',
    '''<p><strong>Enhancement</strong> aims to make an image more useful or visually pleasing. <strong>Restoration</strong> estimates the original using a model of how it was degraded.</p>'''+
    formula('g(x,y) = h(x,y) ∗ f(x,y) + η(x,y)', 'f = original; h = blur/degradation response; η (eta) = noise; g = observed image. ∗ means convolution.')+
    formula('G = HF + N', 'Capital letters are the corresponding Fourier transforms. N is the transform of the noise η.')+
    example('Noise only: no blur', ['The model simplifies to g = f + η.', 'Original pixel f = 100, additive noise η = −7.', 'Observed pixel g = 100 − 7 = 93.'], 'The goal is to estimate f from g. In practice, the exact noise at each pixel is unknown.')+
    note('Dividing G by H can amplify noise badly when H is small, and is undefined where H = 0. A known model does not promise perfect recovery.')+
    recall('Which is model-based: making contrast look better, or estimating a sharp image using a known blur?', 'Estimating using a known blur is restoration. Contrast adjustment for appearance is enhancement.'),[8,3])

add('Recognise the noise before choosing a filter', 'Lecture 8', 5,
    'Know the six lecture noise models and what a PDF tells you.',
    '''<p><strong>Noise</strong> is unwanted variation. A probability density function (PDF) describes which noise values are more likely. For a continuous PDF, <em>area over an interval</em> gives probability; the height at a point is not itself a probability.</p>'''+
    table(['Model','Shape / meaning','Useful fact'],[['Gaussian','Bell-shaped; symmetric about μ','Mean μ, variance σ²'],['Uniform','Flat between a and b','Mean (a+b)/2; variance (b−a)²/12'],['Rayleigh','Right-skewed; starts at a','One-sided shifted distribution'],['Erlang (Gamma)','Right-skewed; integer shape k','Exponential is k = 1'],['Exponential','Largest at zero, decays to the right','Nonnegative; rate λ'],['Impulse','Occasional dark/bright replacements','Pepper: 0; salt: bright (often 255)']])+
    example('Uniform noise between −3 and 3', ['Mean = (−3+3)/2 = 0.', 'Variance = [3−(−3)]²/12 = 36/12 = 3.', 'PDF height = 1/[3−(−3)] = 1/6. Probability of [0,3] = width 3 × height 1/6 = 1/2.'], 'Zero mean does not mean zero noise: positive and negative errors can cancel in average.')+
    '''<details><summary>All six PDF formulas and parameters</summary><div class="detail-body">
    <p><b>Gaussian:</b> p(z) = [1/(σ√(2π))]e<sup>−(z−μ)²/(2σ²)</sup>, all real z; σ > 0.</p>
    <p><b>Uniform:</b> p(z) = 1/(b−a) for a ≤ z ≤ b; 0 elsewhere; b > a.</p>
    <p><b>Rayleigh:</b> p(z) = [2(z−a)/b]e<sup>−(z−a)²/b</sup> for z ≥ a; 0 elsewhere; b > 0. Mean a + √(πb)/2; variance b(4−π)/4.</p>
    <p><b>Erlang:</b> p(z) = λ<sup>k</sup>z<sup>k−1</sup>e<sup>−λz</sup>/(k−1)! for z ≥ 0; 0 elsewhere; λ > 0, integer k ≥ 1. Mean k/λ; variance k/λ².</p>
    <p><b>Exponential:</b> p(z) = λe<sup>−λz</sup> for z ≥ 0; 0 elsewhere. Mean 1/λ; variance 1/λ².</p>
    <p><b>Impulse:</b> discrete masses P<sub>a</sub> at a and P<sub>b</sub> at b; corruption probability P<sub>a</sub>+P<sub>b</sub>. In a replacement model the remaining pixels stay unchanged. Unlike the continuous models above, these are probability masses.</p></div></details>
    <p>Random fine fluctuations → smoothing may help. Isolated bright/dark outliers → median is a useful starting choice. Repeated stripes → look in the frequency domain.</p>'''+
    recall('A few pixels suddenly become 0 or 255. Which noise model fits best?', 'Impulse (salt-and-pepper) noise. A mean can be pulled toward these extremes; try a median or adaptive median.'),[8,7])

add('Mean filters: four different averages', 'Lecture 8', 5,
    'Compute arithmetic, geometric, and harmonic means; recognise their limits.',
    '''<p>Let the window contain K = mn values z₁,…,z<sub>K</sub>. The output replaces only its centre pixel.</p>'''+
    table(['Filter','Formula','Behaviour'],[['Arithmetic','∑z / K','Smooths random variation; outliers pull it strongly'],['Geometric','(∏z)<sup>1/K</sup>','∏ means multiply all values; one zero makes the product zero'],['Harmonic','K / ∑(1/z)','Downweights large salt outliers; requires positive values'],['Contraharmonic','∑z<sup>Q+1</sup> / ∑z<sup>Q</sup>','Choose Q for salt or pepper; next lesson']])+
    example('Use the small window [2, 4, 8]', ['Arithmetic: (2+4+8)/3 = 14/3 ≈ <strong>4.667</strong>.', 'Geometric: (2×4×8)<sup>1/3</sup> = 64<sup>1/3</sup> = <strong>4</strong>.', 'Harmonic: 3/(1/2+1/4+1/8) = 3/0.875 ≈ <strong>3.429</strong>.'], 'Different means return different values even on the same window.')+
    note('If a value is 0, the reciprocal formula for the harmonic mean contains division by zero. It is undefined as written; a limit or an implementation convention may give 0. State this rather than silently calculating 1/0.')+
    recall('What happens to the geometric mean if the window contains one pepper pixel of value 0?', 'The product becomes 0, so the geometric mean is 0. It is not a good choice for removing pepper zeros.'),[8,11])

add('Contraharmonic: the sign of Q matters', 'Lecture 8', 5,
    'Choose the correct Q sign and work through the numerator and denominator.',
    formula('f̂ = ∑ z<sup>Q+1</sup> / ∑ z<sup>Q</sup>', 'f̂ means estimated original intensity. Sum powers in the numerator and denominator separately.')+
    '<div class="compare"><section><h3>Positive Q → pepper</h3><p>Zero-valued pepper pixels contribute zero when Q > 0. Brighter neighbours carry more weight.</p></section><section><h3>Negative Q → salt</h3><p>Large salt pixels receive lower relative weight. Zero values cause negative-power problems.</p></section></div>'+
    example('Pepper window [0, 10, 10], Q = 1', ['Numerator: 0² + 10² + 10² = 200.', 'Denominator: 0¹ + 10¹ + 10¹ = 20.', 'Output = 200/20 = <strong>10</strong>. Arithmetic mean would be 20/3 ≈ 6.667.'], 'Positive Q suppresses the pepper zero in this example.')+
    example('Salt window [10, 10, 100], Q = −1', ['For positive inputs, numerator is ∑z⁰ = 3.', 'Denominator is 1/10+1/10+1/100 = 0.21.', 'Output = 3/0.21 ≈ <strong>14.286</strong>, versus arithmetic mean 40.'], 'Q = −1 gives the harmonic mean when every input is positive.')+
    note('One fixed Q cannot reliably handle mixed salt-and-pepper noise. Q < 0 is undefined at zeros; an all-zero window also gives 0/0 for Q > 0. Q = 0 reduces to the arithmetic mean, using the usual z⁰ = 1 convention for this filter.')+
    recall('Your noise is dark pepper. Should Q be +1.5 or −1.5?', '+1.5. Positive Q suppresses pepper zeros, provided the denominator is nonzero.'),[8,18])

add('Sort first: median, min, max, midpoint', 'Lecture 8', 5,
    'Calculate order-statistic filters without confusing their definitions.',
    '''<p>Order-statistic filters use the <strong>sorted values</strong> in a window. The median is the middle-ranked value; it is not the average of the smallest and largest.</p><div class="image-lab"><figure><canvas id="noise-clean" width="96" height="96" role="img" aria-label="Clean synthetic image with a bright square and thin line"></canvas><figcaption>Clean example</figcaption></figure><figure><canvas id="noise-corrupt" width="96" height="96" role="img" aria-label="Same image with salt-and-pepper impulses"></canvas><figcaption>Salt & pepper added</figcaption></figure><figure><canvas id="noise-median" width="96" height="96" role="img" aria-label="Result of a three by three median filter"></canvas><figcaption>3 × 3 median result</figcaption></figure></div><p class="small muted">A real median calculation at every pixel: many isolated dots disappear, but the thin line can also disappear. This is the detail/noise tradeoff.</p>'''+
    example('Window [10, 11, 10, 255, 9, 10, 12, 11, 10]', ['Sort: [9, 10, 10, 10, <strong>10</strong>, 11, 11, 12, 255].', 'There are 9 values; median is the 5th → <strong>10</strong>.', 'Minimum = <strong>9</strong>; maximum = <strong>255</strong>.', 'Midpoint = (min+max)/2 = (9+255)/2 = <strong>132</strong>.'], 'Median rejects this isolated salt outlier; midpoint is strongly affected by it.')+
    table(['Filter','Good starting use','Tradeoff'],[['Median','Mixed salt and pepper','Often preserves edges better than averaging, but can remove thin details'],['Max','Pepper (dark) impulses','Expands bright regions; salt survives'],['Min','Salt (bright) impulses','Expands dark regions; pepper survives'],['Midpoint','Some Gaussian/uniform noise settings','Averages extremes; poor with impulse outliers']])+
    recall('A sorted 3 × 3 window has 9 values. Which position is its median?', 'The 5th value (1-based indexing), or index 4 with zero-based indexing. No averaging is needed for an odd window.'),[8,25])

add('Alpha-trimmed mean: sort, trim, average', 'Lecture 8', 4,
    'Interpret d as the total number removed, then use the correct divisor.',
    formula('f̂ = (sum of retained sorted values) / (K − d)', 'd is even: remove d/2 lowest and d/2 highest. Use 0 ≤ d < K. K = mn is the original window size.')+
    example('Sorted window [0, 10, 10, 11, 11, 12, 12, 13, 255]; d = 2', ['Remove <strong>one</strong> lowest (0) and <strong>one</strong> highest (255).', 'Keep [10,10,11,11,12,12,13]. Sum = 79.', 'K − d = 9 − 2 = 7. Output = 79/7 ≈ <strong>11.286</strong>.'], 'Trim outliers, then average what remains.')+
    '<p>At d = 0, this is the arithmetic mean. For odd K, d = K−1 leaves one central value: the median. Intermediate trimming can help with mixed random and impulse noise.</p>'+
    recall('For a 3 × 3 window and d = 4, how many values are removed from each end? What is the divisor?', 'Remove 2 from each end; 5 remain. Divide their sum by 5, not by 9.'),[8,31])

add('Your lecture’s 7 × 7 numerical problem', 'Lecture 8', 8,
    'Extract the right 3 × 3 window and calculate its replacement value.',
    '''<p>This is the numerical grid from Lecture 8. Select the salt-like outlier (204) or pepper outlier (0). The outlined cells are the <strong>nine inputs</strong>; the filled cell is the output position.</p><section class="lab"><div class="segmented" role="group" aria-label="Select noisy pixel"><button id="salt" aria-pressed="true">Salt · 204</button><button id="pepper" aria-pressed="false">Pepper · 0</button></div><div class="matrix-layout"><div><div id="matrix" class="matrix" aria-label="Lecture seven by seven image grid"></div><p class="muted small">Coordinates: (column x, row y), starting at 0.</p></div><div id="window-math" aria-live="polite"></div></div><div id="filter-results"></div></section>
    <h2>For a numerical CT answer, always show</h2><ol><li>The selected neighbourhood, with all nine values.</li><li>The filter formula; for order filters, write the sorted list.</li><li>The substituted numerator and denominator.</li><li>The final value, rounded only at the end. Write it at the centre in the output image.</li></ol>'''+
    note('These are calculated estimates, not proof of exact recovery. The clean original value at each corrupted location is unknown. Do not reuse earlier filtered outputs as inputs unless the question specifically requests that procedure.')+
    recall('Why do we take a 3 × 3 neighbourhood instead of averaging all 49 pixels?', 'The stated filter uses a local 3 × 3 window. The 7 × 7 matrix is the image, not the filter size.'),[8,26])

add('Periodic noise: remove a frequency band', 'Lecture 8', 4,
    'Recognise repeated interference and calculate an ideal band-reject response.',
    '''<p>Repeated stripes or a repeating wave are <strong>periodic noise</strong>. They can produce distinct peaks in a Fourier spectrum. A band-reject filter blocks a ring of frequencies while keeping lower and higher ones.</p>'''+
    formula('H<sub>IBR</sub>(D) = 0 if D₀ − W/2 ≤ D ≤ D₀ + W/2; &nbsp; 1 otherwise', 'D₀ = centre radius of the rejected band; W = band width. Band-pass is its complement: HBP = 1 − HBR.')+
    example('D₀ = 30 and W = 10', ['Lower boundary = 30 − 5 = 25. Upper boundary = 30 + 5 = 35.', 'At D = 28: inside [25,35] → H = 0 → reject.', 'At D = 10 or 40: outside → H = 1 → keep.'], 'Reject the offending band, rather than removing every high frequency.')+
    '''<details><summary>Smooth band-reject variants</summary><div class="detail-body"><p><b>Butterworth:</b> H = 1 / [1 + (DW/(D²−D₀²))<sup>2n</sup>]. Define its limiting value H(D₀) = 0.</p><p><b>Gaussian:</b> H = 1 − exp{−[(D²−D₀²)/(DW)]²}. At D = 0 use limiting gain 1 (for D₀ > 0); at D = D₀ gain is 0.</p><p>A <b>notch reject</b> targets individual conjugate peak pairs and can preserve more useful frequencies than rejecting an entire ring. The lecture emphasises band rejection.</p></div></details>'''+
    recall('A band-reject filter has H = 0.2 at one frequency. What is the complementary band-pass gain?', '1 − 0.2 = 0.8.'),[8,36])

add('Adaptive median: check, then decide', 'Lecture 8', 6,
    'Follow Level A and Level B, including the window-expansion case.',
    '''<p>A fixed median replaces every centre with a median. An <strong>adaptive median</strong> can keep a reliable centre unchanged and grow its window if the current median seems corrupted.</p><p>For the current window: z<sub>min</sub> = smallest, z<sub>max</sub> = largest, z<sub>med</sub> = median, z<sub>xy</sub> = centre. Start with 3 × 3 and choose a maximum size S<sub>max</sub>.</p><div class="decision"><section><span class="eyebrow">LEVEL A · TRUST THE MEDIAN?</span><h3>z<sub>min</sub> &lt; z<sub>med</sub> &lt; z<sub>max</sub></h3><p><strong>Yes →</strong> go to B.<br><strong>No →</strong> increase window size by 2; repeat A if within S<sub>max</sub>. If no larger window is allowed, output the current median.</p></section><section><span class="eyebrow">LEVEL B · TRUST THE CENTRE?</span><h3>z<sub>min</sub> &lt; z<sub>xy</sub> &lt; z<sub>max</sub></h3><p><strong>Yes →</strong> output the original centre.<br><strong>No →</strong> replace the centre with z<sub>med</sub>.</p></section></div>'''+
    example('min = 0, median = 51, max = 255, centre = 255', ['A: 0 < 51 < 255 → median passes → go to B.', 'B: 0 < 255 < 255 is false because 255 is not strictly less than 255.', 'Replace the centre with the median <strong>51</strong>. If the centre had been 50, keep 50.'], 'Level A checks the median. Level B checks the centre.')+
    '<details><summary>Write it in the lecture’s A₁/A₂ notation</summary><div class="detail-body"><p>A₁ = z<sub>med</sub> − z<sub>min</sub>; A₂ = z<sub>med</sub> − z<sub>max</sub>. Pass A if A₁ > 0 and A₂ < 0.</p><p>B₁ = z<sub>xy</sub> − z<sub>min</sub>; B₂ = z<sub>xy</sub> − z<sub>max</sub>. Pass B if B₁ > 0 and B₂ < 0.</p></div></details>'+
    recall('A 3 × 3 window has min = 0, median = 0, max = 255. Do you go to Level B?', 'No. The strict test 0 < 0 fails. Grow to 5 × 5 if allowed. If already at the maximum size, output the median of the last evaluated window.'),[8,44])

add('Your four-minute recall sheet', 'Revision', 4,
    'Try to reconstruct these formulas before checking them.',
    '''<p>Cover the right-hand side and say each rule aloud. If you cannot explain a symbol, return to that lesson. This is review, not a substitute for doing the examples.</p>'''+
    table(['Prompt','Rule / answer'],[['Frequency filtering','G = HF; spatial convolution ↔ frequency multiplication'],['Centred distance','D = √[(u−P/2)²+(v−Q/2)²]'],['Ideal LPF','1 inside D ≤ D₀; 0 outside'],['Butterworth LPF','1/[1+(D/D₀)²ⁿ]; H(D₀) = 0.5'],['Gaussian LPF','e<sup>−D²/(2D₀²)</sup>; H(D₀) ≈ 0.607'],['Complementary HPF','1 − LPF; H(0) = 0'],['Emphasis','a + bHHP; a retains background'],['Restoration','g = h∗f + η; noise-only g = f + η'],['Arithmetic / geometric','∑z/K; (∏z)<sup>1/K</sup>'],['Harmonic / contraharmonic','K/∑(1/z); ∑z<sup>Q+1</sup>/∑z<sup>Q</sup>'],['Contraharmonic Q sign','Positive for pepper; negative for salt'],['Median / midpoint','Middle sorted value; (min+max)/2'],['Alpha-trimmed','Remove d/2 each end; divide retained sum by K−d'],['Ideal band reject','Reject D₀−W/2 ≤ D ≤ D₀+W/2'],['Adaptive median','A trusts median; B trusts centre; strict inequalities']])+
    '<h2>Choose a method with a reason</h2><p><strong>Fine random variation:</strong> a mean or smooth LPF, with a detail/blur tradeoff. <strong>Impulse outliers:</strong> median; adaptive median when local conditions vary. <strong>Periodic stripes:</strong> frequency band rejection or targeted notches.</p>'+
    note('Keep these pairs separate: amplitude vs power; median vs midpoint; image size vs window size; Level A vs Level B. State a filter’s benefit and its detail/noise tradeoff.')+
    recall('Without looking: which two LPFs give 0.5 and 0.607 at D₀?', 'Butterworth → 0.5. Gaussian → e⁻⁰·⁵ ≈ 0.607.'))

add('Test yourself before the CT', 'Revision', 14,
    'Spend 10 minutes answering without notes, then 4 minutes correcting your mistakes.',
    '''<p>Use paper for calculations. Each question gives feedback and a lesson to revisit. Your score counts your <strong>first attempt</strong>; answer every question before judging your result.</p><div class="quiz-toolbar"><div id="quiz-score" role="status" aria-live="polite">0 / 12 answered</div><button id="reset-quiz">Start a fresh attempt</button></div><div id="quiz"></div><section class="example"><div class="eyebrow">BEFORE YOU FINISH</div><h3>A clear written answer earns more than a guessed number</h3><p>For math: write the formula → substitute values → calculate → label the result. For theory: define the method → explain how it works → give a use and a limitation.</p><p id="study-advice">Complete the test to see which lessons to revisit.</p></section>''')

quiz = [
    dict(q='A constant 2 × 2 image has all pixels equal to 5. What is its unnormalised F(0,0)?', options=['5','20','0','10'], correct=1, why='DC is the sum of all pixel values: 4 × 5 = 20. The average intensity is 5.', lesson=4),
    dict(q='Why multiply an even-sized image by (−1)^(x+y) before the DFT?', options=['To remove noise','To sharpen edges','To move DC to the centre','To make pixels positive'],correct=2,why='The checkerboard modulation shifts the spectrum by half its size along both axes. Undo it after the inverse.',lesson=5),
    dict(q='Butterworth LPF: n = 1 and D = 2D₀. Find H.',options=['0.2','0.5','0.607','0.8'],correct=0,why='H = 1/[1 + (2)²] = 1/5 = 0.2.',lesson=8),
    dict(q='Gaussian HPF: D = D₀. Find the approximate gain.',options=['0.607','0.5','1','0.393'],correct=3,why='GHPF = 1 − e⁻⁰·⁵ = 1 − 0.6065 ≈ 0.3935.',lesson=11),
    dict(q='Which frequency filter is most associated with ringing from an abrupt cutoff?',options=['Gaussian LPF','Ideal LPF','No filter ever rings','All smooth responses equally'],correct=1,why='A sharp frequency boundary gives an oscillatory spatial response, causing halos near edges.',lesson=7),
    dict(q='Use Q = 1 on the window [0, 10, 10]. What is the contraharmonic result?',options=['0','6.667','10','20'],correct=2,why='Numerator = 0²+10²+10² = 200. Denominator = 0+10+10 = 20. Output = 10.',lesson=17),
    dict(q='Which choice is suitable for mixed salt-and-pepper impulses?',options=['Geometric mean','Midpoint','Negative Q with zeros','Median'],correct=3,why='Median uses a middle-ranked value and resists isolated extremes. It can still lose thin details or fail with dense corruption.',lesson=18),
    dict(q='Sort [0,10,10,11,11,12,12,13,255]. Alpha-trim with d = 4: what is the output?',options=['11.2','11.286','9','12'],correct=0,why='Remove [0,10] and [13,255]. Keep [10,11,11,12,12]; sum 56; divide by 5 → 11.2.',lesson=19),
    dict(q='Ideal band reject: D₀ = 30, W = 10. What happens at D = 35?',options=['Gain is 1','Gain is 0','Gain is 0.5','Cannot determine'],correct=1,why='The rejected interval is [25,35], including its boundaries under the stated convention.',lesson=21),
    dict(q='Adaptive median: min=0, median=50, max=255, centre=49. What is the output?',options=['0','50','49','255'],correct=2,why='A passes: 0<50<255. B also passes: 0<49<255. Keep the original centre 49.',lesson=22),
    dict(q='For a 3 × 3 window, min=0, median=0, max=255. A 5 × 5 window is allowed. What is next?',options=['Keep the centre immediately','Go to Level B','Output 255','Expand to 5 × 5 and repeat A'],correct=3,why='Level A fails because median equals min. Grow the window if the maximum size permits.',lesson=22),
    dict(q='Which statement explains the convolution theorem?',options=['Spatial convolution equals frequency multiplication','FFT is a different transform from DFT','Restoration always removes all noise','High frequency means bright pixels'],correct=0,why='g=f∗h corresponds to G=FH, with appropriate padding for linear convolution. Brightness and rate of spatial change are different ideas.',lesson=5),
]

assert len(lessons) == 24
assert sum(x['minutes'] for x in lessons) == 120
