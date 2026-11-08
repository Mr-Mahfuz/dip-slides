"""Plain Bangla teaching text; formulas and exam terms match the English deck."""
import re
from study_data import lessons as english, quiz as english_quiz, table

def formula(expression, explanation=''):
    return f'<div class="formula"><div>{expression}</div><p>{explanation}</p></div>'

def example(title, steps, result):
    return '<section class="example"><div class="eyebrow">ধাপে ধাপে অঙ্ক</div><h3>'+title+'</h3><ol>'+''.join('<li>'+s+'</li>' for s in steps)+'</ol><div class="result">'+result+'</div></section>'

def recall(question, answer):
    return f'<section class="recall"><div class="eyebrow">একটু থামুন, নিজে বলুন</div><p>{question}</p><details><summary>উত্তর মিলিয়ে নিন</summary><div>{answer}</div></details></section>'

def note(text):
    return f'<aside class="note"><strong>CT-তে এই ভুলটি এড়ান</strong><p>{text}</p></aside>'

def component(lesson_id, start, end):
    body=english[lesson_id-1]['body']
    return body[body.index(start):body.index(end,body.index(start))+len(end)]

lessons=[]
def add(title, goal, body):
    base=english[len(lessons)]
    lessons.append({**base,'title':title,'goal':goal,'body':body})

add('এখান থেকেই শুরু করুন',
    'আগে কিছু জানা না থাকলেও সমস্যা নেই। পরের দুই ঘণ্টায় ধারণা বুঝুন, অঙ্ক করুন, তারপর নিজেকে যাচাই করুন।',
    '''<div class="intro-banner"><span class="eyebrow">আপনার দুই ঘণ্টার পড়ার পরিকল্পনা</span><p>দুটি লেকচার।<br>ধাপে ধাপে বুঝে পড়ুন।</p><div>শুরু হবে একদম গোড়া থেকে। উদাহরণের অঙ্কগুলো খাতায় করুন। শেষে উত্তর না দেখে নিজে পরীক্ষা দিন।</div></div>
    <h2>এই দুটি বিষয় আসলে কী?</h2><p>একটি ছবি হলো অনেকগুলো সংখ্যার ছক। <strong>লেকচার 7</strong>-এ শিখবেন, ছবির ধীরে ও দ্রুত বদলানো অংশ নিয়ন্ত্রণ করে ছবি কীভাবে মসৃণ বা ধারালো করা যায়। <strong>লেকচার 8</strong>-এ শিখবেন, ছবির অপ্রয়োজনীয় দাগ বা noise কীভাবে কমাতে হয়।</p>
    <div class="route"><div><b>01</b><strong>ভিত্তিটা বুঝুন</strong><span>0–18 মিনিট · পাঠ 1–4</span></div><div><b>02</b><strong>Frequency filter বুঝুন</strong><span>18–57 মিনিট · পাঠ 5–13</span></div><div><b>03</b><strong>Noise কমান, অঙ্ক করুন</strong><span>57–102 মিনিট · পাঠ 14–22</span></div><div><b>04</b><strong>মনে করুন, নিজে পরীক্ষা দিন</strong><span>102–120 মিনিট · পাঠ 23–24</span></div></div>
    <h2>কীভাবে পড়বেন?</h2><p>আগে মূল কথাটি পড়ুন। তারপর অঙ্কের প্রতিটি ধাপ খাতায় করুন। <strong>নিজে বলুন</strong> অংশের উত্তর আগে নিজে ভাবুন, তারপর খুলে মিলিয়ে নিন। নিজের ভাষায় বোঝাতে পারলে <strong>পড়া হয়েছে</strong> চাপুন। আটকে গেলে <strong>পরে আবার পড়ব</strong> দিয়ে এগিয়ে যান।</p><p class="muted">সময়গুলো শুধু গতি ধরে রাখার জন্য। কোনো একটি পাতায় একটু বেশি সময় লাগতেই পারে। সূত্র ও উদাহরণ ইন্টারনেট ছাড়াই কাজ করে। আপনার অগ্রগতি এই ব্রাউজারে সেভ থাকে।</p><button class="primary" data-go="2">পিক্সেল দিয়ে শুরু করি →</button>''')

add('ছবি মানে সংখ্যার একটি ছক',
    'পিক্সেল, উজ্জ্বলতা, অবস্থান এবং 3 × 3 window বুঝুন।',
    '''<p>সাদাকালো বা grayscale ছবির প্রতিটি ছোট ঘরকে <strong>পিক্সেল (pixel)</strong> বলে। প্রতিটি পিক্সেলে উজ্জ্বলতার একটি সংখ্যা থাকে। <strong>8-bit ছবিতে</strong> 0 হলো কালো, 255 হলো সাদা। মাঝের সংখ্যাগুলো ধূসর রং বোঝায়।</p><div class="pixel-demo"><div style="--v:0">0</div><div style="--v:64">64</div><div style="--v:128">128</div><div style="--v:192">192</div><div style="--v:255">255</div></div><p><span class="math">f(x,y)</span> মানে (x,y) অবস্থানের পিক্সেলের মান। এখানে x দিয়ে কলাম, y দিয়ে সারি বোঝানো হচ্ছে। গোনা শুরু হবে 0 থেকে।</p><h2>Filter কী করে?</h2><p>একটি spatial filter পিক্সেলের চারপাশের ছোট একটি অংশ নেয়। এই অংশকে <strong>window বা neighbourhood</strong> বলে। ওই মানগুলো দিয়ে হিসাব করে <strong>আলাদা output ছবির মাঝের অবস্থানে</strong> নতুন মান বসায়। তারপর window পরের পিক্সেলে যায়।</p>'''+
    example('3 × 3 window-এর মাঝের পিক্সেল বদলাই',[
    'Window: [10, 10, 10; 10, <strong>100</strong>, 10; 10, 10, 10]। মোট 9টি মান।',
    'Average filter সবগুলো যোগ করে: 8 × 10 + 100 = 180।',
    'এবার 9 দিয়ে ভাগ: 180/9 = 20। Output-এর মাঝের পিক্সেলে 20 বসবে।'],
    'মাঝের মান 100 → 20 হলো। উজ্জ্বল দাগটি কমল। তবে গড় করলে আসল সূক্ষ্ম অংশও ঝাপসা হতে পারে।')+
    note('3 × 3 filter একটি window থেকে একটি output পিক্সেলের মান দেয়। পুরো window-কে একটি ঘরে নামিয়ে আনে না। ছবির কিনারায় পুরো window না পেলে padding-এর নিয়ম লাগবে।')+
    recall('5 × 5 filter-এ কতটি মান নিয়ে হিসাব হয়? নতুন মানটি কোথায় বসে?', '25টি মান। হিসাবের ফল output ছবিতে window-এর মাঝের অবস্থানে বসে।'))

add('Frequency: উজ্জ্বলতা কত দ্রুত বদলায়',
    'ধীরে বদলানো অংশকে low frequency, আর দ্রুত বদলানো অংশকে high frequency হিসেবে চিনুন।',
    '''<p><strong>Spatial domain</strong>-এ আমরা দেখি কোন অবস্থানে পিক্সেলের মান কত। <strong>Frequency domain</strong>-এ দেখি উজ্জ্বলতা কী ধরনের ঢেউ বা pattern মেনে বদলাচ্ছে।</p><div class="compare"><section><h3>Low frequency</h3><div class="swatch slow"></div><p>এক জায়গা থেকে অন্য জায়গায় উজ্জ্বলতা ধীরে বদলায়। যেমন মসৃণ আকাশ, বড় আকারের ছায়া বা ছবির পটভূমি।</p></section><section><h3>High frequency</h3><div class="swatch fast"></div><p>অল্প দূরত্বেই উজ্জ্বলতা দ্রুত বদলায়। যেমন বস্তুর ধার (edge), ছোট লেখা, সূক্ষ্ম নকশা বা কিছু noise।</p></section></div><p>Fourier-এর ধারণা: আলাদা frequency, শক্তি ও অবস্থানের সহজ কিছু ঢেউ যোগ করে জটিল pattern তৈরি করা যায়।</p>'''+
    example('দুটি পিক্সেল-সারি দেখি',[
    '[50,51,52,53,54] প্রতিবার মাত্র 1 করে বদলাচ্ছে → পরিবর্তন ধীর।',
    '[0,255,0,255,0] প্রতি ধাপেই অনেক বদলাচ্ছে → high-frequency অংশ শক্তিশালী।',
    '[50,50,50,50] একদম বদলাচ্ছে না। এতে শুধু zero-frequency অংশ আছে, যাকে <strong>DC</strong> বলে।'],
    'Low-pass ধীর পরিবর্তন রাখে → ছবি মসৃণ হয়। High-pass দ্রুত পরিবর্তন রাখে → ধার ফুটে ওঠে।')+
    note('High frequency মানে বেশি উজ্জ্বল নয়। পুরো ছবি সমান সাদা হলেও সেটি DC। আবার আসল edge এবং অপ্রয়োজনীয় noise—দুটিতেই high frequency থাকতে পারে।')+
    recall('লেখার ছবি থেকে high frequency বাদ দিলে কী হবে?', 'অক্ষরের ধার নরম বা ঝাপসা হবে। ছোট অংশ হারিয়ে যেতে পারে। এটাই low-pass smoothing-এর প্রভাব।'))

add('Fourier transform: ছোট অঙ্ক দিয়ে বুঝি',
    'F(u,v) কী বোঝায় জানুন এবং মাত্র দুটি মান দিয়ে DFT করুন।',
    '''<p><strong>Discrete Fourier Transform (DFT)</strong> একটি তালিকা বা ছবিকে frequency coefficient-এ প্রকাশ করে। প্রতিটি coefficient বলে দেয়, নির্দিষ্ট ঢেউটি কতটা আছে। মানটি complex-ও হতে পারে; এখানে <span class="math">j² = −1</span>।</p>'''+
    formula('F(k) = ∑<sub>x=0</sub><sup>N−1</sup> f(x)e<sup>−j2πkx/N</sup>', 'N = মোট sample, x = sample-এর অবস্থান, k = frequency index। ∑ মানে x-এর সব মানের জন্য হিসাবগুলো যোগ করতে হবে।')+
    example('দুটি পিক্সেল: f = [10,20]',[
    'k = 0 হলে exponential সবগুলো 1। তাই F(0) = 10+20 = <strong>30</strong>। এটি DC sum।',
    'k = 1 হলে e⁰ = 1 এবং e<sup>−jπ</sup> = −1। তাই F(1) = 10−20 = <strong>−10</strong>।',
    'উল্টো করে ফেরত আনি: f(0) = (30−10)/2 = 10; f(1) = (30+10)/2 = 20।'],
    'Transform ছবিকে প্রকাশ করার ধরন বদলায়। Inverse transform দিয়ে আগের মান ফিরে পাওয়া যায়।')+
    '<h2>এবার দুই মাত্রার ছবি</h2>'+
    formula('F(u,v) = ∑<sub>x=0</sub><sup>M−1</sup> ∑<sub>y=0</sub><sup>N−1</sup> f(x,y)e<sup>−j2π(ux/M + vy/N)</sup>', 'এই সূত্রে M,N হলো সংশ্লিষ্ট দুই অক্ষ বরাবর ছবির মাপ। u,v হলো ওই দুই অক্ষের frequency index।')+
    formula('f(x,y) = (1/MN) ∑<sub>u=0</sub><sup>M−1</sup> ∑<sub>v=0</sub><sup>N−1</sup> F(u,v)e<sup>+j2π(ux/M + vy/N)</sup>', 'Inverse DFT-তে exponent-এর চিহ্ন + হয় এবং মোট MN দিয়ে ভাগ করতে হয়।')+
    '<p><strong>Magnitude</strong> |F| ঢেউটির শক্তি বোঝায়। <strong>Phase</strong> ঢেউগুলোর পারস্পরিক অবস্থান বোঝায়; ছবির গঠনে এটি গুরুত্বপূর্ণ। Spectrum দেখাতে প্রায়ই log(1+|F|) ব্যবহার করা হয়, যাতে ছোট মানও দেখা যায়।</p>'+
    recall('2 × 2 ছবি [1,2;3,4]-এর F(0,0) কত?', '1+2+3+4 = 10। এখানে forward DFT-তে ভাগ করা হয়নি, তাই DC হলো যোগফল। গড় উজ্জ্বলতা 10/4 = 2.5।'))

add('Frequency filtering করার ধাপগুলো',
    'কেন frequency domain-এ গুণ করলেই filter হয়, তা বুঝুন।',
    '''<p><span class="math">H(u,v)</span> হলো filter-এর ওজন বা gain-এর ছক। প্রতিটি Fourier coefficient-কে তার জায়গার H দিয়ে গুণ করা হয়। H = 1 হলে রাখি, H = 0 হলে বাদ দিই, H = 0.5 হলে amplitude অর্ধেক করি।</p><div class="pipeline"><span>ছবি f</span><b>→</b><span>DFT: F</span><b>→</b><span>G = HF</span><b>→</b><span>Inverse DFT: g</span></div>'''+
    formula('g = f ∗ h &nbsp; ↔ &nbsp; G = F · H', 'এটাই convolution theorem। ∗ হলো spatial convolution। · হলো একই অবস্থানের frequency মানগুলোর গুণ। h হলো spatial filter, H তার transform।')+
    '''<h2>Theory প্রশ্নে ধাপগুলো এভাবে লিখুন</h2><ol class="steps"><li><strong>প্রস্তুতি:</strong> দরকার হলে padding দিন, যাতে circular wraparound-এর প্রভাব কমে। একটি প্রচলিত মাপ হলো P = 2M, Q = 2N।</li><li><strong>কেন্দ্রে আনা:</strong> padded ছবিকে (−1)<sup>x+y</sup> দিয়ে গুণ করুন।</li><li><strong>Transform:</strong> 2D DFT নিয়ে F বের করুন।</li><li><strong>Filter:</strong> G(u,v) = H(u,v)F(u,v) করুন। H ও F-এর কেন্দ্র মিলতে হবে।</li><li><strong>Inverse:</strong> inverse DFT নিন। খুব ছোট imaginary error থাকলে real অংশ ব্যবহার করুন।</li><li><strong>কেন্দ্রে আনার প্রভাব সরান:</strong> আবার (−1)<sup>x+y</sup> দিয়ে গুণ করুন। তারপর আসল মাপ পর্যন্ত crop করুন।</li></ol>'''+
    example('একটি coefficient-এ হিসাব', ['ধরি F(u,v) = 80 এবং H(u,v) = 0.25।', 'G(u,v) = 80 × 0.25 = 20। অন্য coefficient-গুলোর হিসাবও আলাদাভাবে হবে।'], 'এই frequency-র amplitude আগের এক-চতুর্থাংশ হলো।')+
    note('ঠিক অর্ধেক grid shift-এর জন্য (−1)^(x+y) পদ্ধতিতে transform-এর মাপ জোড় হতে হয়। fftshift দিয়েও spectrum সাজানো যায়। দুটো centring পদ্ধতি একসঙ্গে ব্যবহার করবেন না; inverse-এ উল্টো ধাপটি ঠিকমতো করুন।')+
    recall('Frequency domain-এ filtering সুবিধাজনক কেন?', 'Spatial convolution frequency domain-এ সরাসরি একই অবস্থানের মানগুলোর গুণে পরিণত হয়। কোন frequency রাখবেন, সেটিও বেছে নেওয়া সহজ হয়।'))

add('DC থেকে দূরত্ব D বের করি',
    'গোলাকার frequency filter-এর জন্য D(u,v) হিসাব করুন।',
    '<p>Spectrum কেন্দ্রে আনার পর মাঝখানে থাকে DC। কেন্দ্র থেকে দূরে গেলে তুলনামূলক দ্রুত পরিবর্তনের frequency পাওয়া যায়। Circular filter এই দূরত্ব ব্যবহার করে।</p>'+
    formula('D(u,v) = √[(u − P/2)² + (v − Q/2)²]', 'P,Q = transform-এর মাপ। D₀ = আমরা যে cutoff দূরত্ব বেছে নিই। D₀ এবং DC এক জিনিস নয়।')+
    example('8 × 8 centred spectrum-এ (1,0) বিন্দু', ['কেন্দ্র (4,4)। পার্থক্য: 1−4 = −3 এবং 0−4 = −4।', 'বর্গ করে যোগ করুন, তারপর বর্গমূল নিন: D = √[(−3)²+(−4)²] = √25 = 5।'], 'এখানে D = 5। এবার D₀-এর সঙ্গে তুলনা করে H বের করা যাবে।')+
    recall('8 × 8 centred spectrum-এ D(4,4) কত? এটি কোন অংশ?', 'D = 0। এই অবস্থানেই DC থাকে।'))

add('Ideal low-pass: ভেতরের অংশ রাখি',
    'Ideal LPF দিয়ে gain বের করুন; blur ও ringing-এর কারণ বুঝুন।',
    '<p><strong>Low-pass filter (LPF)</strong> ধীরে বদলানো অংশ রাখে, দ্রুত বদলানো অংশ কমায়। Ideal LPF-এ cutoff-এর ভেতরে সব রাখা হয়, বাইরে সব বাদ যায়।</p>'+
    formula('H<sub>ILP</sub>(D) = 1 যদি D ≤ D₀; &nbsp; 0 যদি D > D₀', 'D = DC থেকে দূরত্ব; D₀ = cutoff radius। H দিয়ে coefficient-কে গুণ করতে হবে; H নিজে পিক্সেলের উজ্জ্বলতা নয়।')+
    example('D₀ = 10 হলে', ['D = 4: H = 1 → F = 80 হলে G = 80।', 'D = 10: এখানে ≤ নিয়ম ধরা হয়েছে, তাই H = 1।', 'D = 15: H = 0 → F = 80 হলে G = 0।'], 'D₀ ছোট করলে বেশি frequency বাদ পড়ে → blur বাড়ে।')+
    '<h2>ধারের পাশে ঢেউয়ের মতো দাগ কেন হয়?</h2><p>Frequency-তে হঠাৎ cutoff দিলে spatial response-এ ওঠানামা তৈরি হয়। তাই sharp edge-এর পাশে হালকা-গাঢ় বলয়ের মতো দাগ দেখা যেতে পারে। একে <strong>ringing</strong> বলে। Cutoff ধীরে বদলালে এই সমস্যা কমে।</p>'+
    recall('D₀ বাড়ালে ideal LPF-এ blur বেশি হবে, না কম?', 'সাধারণত কম হবে। বড় বৃত্তের ভেতর বেশি high-frequency detail থাকে। তবে ideal cutoff-এর কারণে ringing হতে পারে।'))

add('Butterworth: cutoff ধীরে বদলায়',
    'D, D₀ এবং order n বসিয়ে Butterworth-এর gain বের করুন।',
    formula('H<sub>BLP</sub>(D) = 1 / [1 + (D/D₀)<sup>2n</sup>]', 'n হলো ধনাত্মক পূর্ণসংখ্যা order। n বাড়লে cutoff খাড়া হয়, ideal filter-এর মতো হতে থাকে।')+
    example('D₀ = 10, n = 2', ['D = 0: H = 1/(1+0) = <strong>1</strong>।', 'D = 10: D/D₀ = 1। তাই H = 1/(1+1⁴) = <strong>0.5</strong>।', 'D = 20: D/D₀ = 2। তাই H = 1/(1+2⁴) = 1/17 ≈ <strong>0.0588</strong>।'], 'D = D₀ হলে Butterworth gain সবসময় 0.5; order বদলালেও এটি একই থাকে।')+
    '<p>কম order-এর Butterworth ideal filter-এর তুলনায় মসৃণভাবে বদলায়। Order বেশি হলে cutoff তীক্ষ্ণ হয় এবং ringing বাড়তে পারে।</p>'+
    note('H = 0.5 মানে amplitude অর্ধেক। Power amplitude-এর বর্গের সমানুপাতিক, তাই power-এর অংশ 0.25। একে half-power লিখবেন না।')+
    recall('n = 1 এবং D = 2D₀ হলে H কত?', '1/(1+2²) = 1/5 = 0.2। আগে D/D₀ অনুপাত বের করুন, তারপর 2n ঘাত দিন।'))

add('Gaussian: খুব মসৃণ একটি filter',
    'Gaussian gain হিসাব করুন এবং তিনটি LPF-এর পার্থক্য মনে রাখুন।',
    formula('H<sub>GLP</sub>(D) = e<sup>−D²/(2D₀²)</sup>', 'e ≈ 2.718। D₀ বাড়লে response বেশি দূর পর্যন্ত ছড়ায়। এখানে হঠাৎ বন্ধ হওয়ার বদলে gain ধীরে কমে।')+
    example('D₀ = 10 হলে', ['D = 0: exponent = 0 → H = e⁰ = <strong>1</strong>।', 'D = 10: exponent = −100/200 = −0.5 → H ≈ <strong>0.6065</strong>।', 'D = 20: exponent = −400/200 = −2 → H ≈ <strong>0.1353</strong>।'], 'আদর্শ Gaussian spatial response-এ ওঠানামা করা lobe থাকে না। তাই cutoff-এর কারণে ringing হয় না।')+
    table(['LPF','কীভাবে বদলায়','D₀-এ gain','মনে রাখুন'],[['Ideal','হঠাৎ cutoff','1 (≤ ধরলে)','Ringing হতে পারে'],['Butterworth','Order দিয়ে নিয়ন্ত্রিত','0.5','n বেশি → cutoff খাড়া'],['Gaussian','খুব মসৃণভাবে','≈ 0.607','Cutoff-এর কারণে ringing নেই']])+
    note('একই D₀ মানে তিন filter-এর gain একই নয়। Butterworth-এর 0.5 Gaussian-এর অঙ্কে বসাবেন না।')+
    recall('একটি নির্দিষ্ট D-তে D₀ কমালে Gaussian gain কী হবে?', 'Exponent আরও ঋণাত্মক হবে, তাই H কমবে। ওই frequency আরও কমবে, ছবি বেশি মসৃণ হবে।'))

add('Filter কী রাখছে, চোখে দেখে বুঝুন',
    'Cutoff বদলে graph এবং ছবির পরিবর্তন একসঙ্গে দেখুন।',
    '<p>এখানে একটি ধীর ঢেউ (frequency 2) এবং একটি দ্রুত ঢেউ (frequency 12) যোগ করা হয়েছে। বেছে নেওয়া filter-এর gain দিয়ে প্রতিটি অংশ গুণ করে ফল দেখানো হচ্ছে।</p>'+
    component(10,'<section class="lab">','</section>')+
    component(10,'<div class="image-lab">','</div>')+
    '<p class="small muted">ছবিতে কলাম বরাবর ধীর frequency-2 ঢেউ এবং সারি বরাবর দ্রুত frequency-12 ঢেউ আছে। High-pass ফল দেখা সহজ করতে ছবিতে 128 যোগ করে দেখানো হয়েছে।</p><h2>এভাবে চেষ্টা করুন</h2><ol><li>Gaussian low-pass-এ D₀ = 3 দিন। সরু আড়াআড়ি দাগ অনেকটা মিলিয়ে যাবে।</li><li>D₀ = 20 করুন। দ্রুত বদলানো দাগের বেশি অংশ থাকবে।</li><li>High-pass দিন। এবার চওড়া, ধীর অংশগুলো কমবে।</li></ol>'+
    note('Mask-এ সাদা মানে gain 1: রাখবে। কালো মানে gain 0: বাদ দেবে। Mask-এর অবস্থান frequency বোঝায়; আসল ছবির অবস্থান বোঝায় না। এখানে মসৃণ ঢেউ দিয়ে attenuation দেখানো হয়েছে। Ringing দেখতে sharp edge-সহ input দরকার।')+
    recall('কোনো frequency-তে low-pass gain 0.2 হলে complementary high-pass gain কত?', '1−0.2 = 0.8।'))

add('High-pass: দ্রুত বদলানো অংশ রাখি',
    'LPF থেকে HPF বের করুন এবং DC বাদ যাওয়ার প্রভাব বুঝুন।',
    '<p><strong>High-pass filter (HPF)</strong> ধীরে বদলানো অংশ কমায়, দ্রুত বদলানো অংশ রাখে। ফলে ধার দেখা যায়। তবে noise-ও বেশি ফুটে উঠতে পারে।</p>'+
    formula('H<sub>HP</sub> = 1 − H<sub>LP</sub>', 'এই LPF-গুলোর DC gain 1। তাই complementary HPF-এর DC gain 0।')+
    table(['ধরন','High-pass gain'],[['Ideal','D ≤ D₀ হলে 0; D > D₀ হলে 1'],['Butterworth','D > 0 হলে 1/[1+(D₀/D)²ⁿ]; D = 0-তে gain 0 ধরি'],['Gaussian','1 − e<sup>−D²/(2D₀²)</sup>']])+
    example('D = D₀-তে Gaussian HPF', ['GLPF gain = e<sup>−0.5</sup> ≈ 0.6065।', 'GHPF gain = 1−0.6065 = <strong>0.3935</strong>।', 'D = 0-তে H = 1−1 = 0। তাই ছবির গড় উজ্জ্বলতার অংশ বাদ যায়।'], 'শুধু edge-এর ছবি এবং আসল ছবির উন্নত সংস্করণ এক জিনিস নয়।')+
    recall('Ideal HPF-এ D₀ বাড়ালে কী হবে?', 'আরও বেশি low ও middle frequency বাদ যাবে। শুধু তুলনামূলক সূক্ষ্ম, দ্রুত পরিবর্তনের অংশ থাকবে।'))

add('Sharpening: আসল ছবির সঙ্গে detail যোগ',
    'High-frequency emphasis ও Laplacian sharpening আলাদা করে বুঝুন।',
    '<p>পটভূমিও রাখতে চাই, আবার detail-ও বাড়াতে চাই। তাই আসল ছবির সঙ্গে high-pass ফলের একটি অংশ যোগ করি।</p>'+
    formula('H<sub>emphasis</sub> = a + bH<sub>HP</sub>', 'a > 0 হলে low-frequency পটভূমির কিছু অংশ থাকে। b > 0 detail বাড়ায়। প্রচলিতভাবে a = 1 নেওয়া হয়।')+
    example('a = 1, b = 2', ['DC-তে H<sub>HP</sub> = 0 → emphasis gain = 1।', 'High frequency-তে H<sub>HP</sub> ≈ 1 হলে gain ≈ 1+2 = 3।', 'পটভূমি থাকে, আর ওই high-frequency অংশ তিন গুণ হয়।'], 'Emphasis-এ brightness baseline থাকে। শুধু HPF দিলে DC বাদ যায়।')+
    '<h2>Laplacian হলো second derivative</h2><p>Continuous spatial coordinate ব্যবহার করলে ∇²-এর frequency multiplier −4π²(u²+v²)। কেন্দ্র ধরে এটি প্রায়ই −4π²D² লেখা হয়। Frequency-এর scale কী ধরা হয়েছে, তা খেয়াল করুন।</p>'+
    formula('g = f − c∇²f &nbsp; ⇒ &nbsp; G = [1 + 4π²cD²] F', 'c > 0। এখানে negative-centre Laplacian kernel ধরা হয়েছে, যেমন [0,1,0;1,−4,1;0,1,0]।')+
    note('Discrete Laplacian-এর সঠিক response এবং continuous D² সূত্র আলাদা। কোনো বইয়ে 4π² ধ্রুবকের মধ্যে রাখা হয়, আবার kernel-এর চিহ্নও উল্টো হতে পারে। প্রশ্নে দেওয়া kernel অনুযায়ী যোগ বা বিয়োগ করুন।')+
    recall('f = 100, ∇²f = −20, c = 1 হলে g কত?', 'g = 100−(−20) = 120। ঋণাত্মক response বিয়োগ করায় মান বাড়ল।'))

add('FFT ও template matching',
    'FFT কেন দ্রুত এবং correlation দিয়ে কী খোঁজা হয়, তা জানুন।',
    '<h2>FFT হলো DFT করার দ্রুত পদ্ধতি</h2><p>Transform বদলায় না, হিসাবের algorithm বদলায়। দৈর্ঘ্য L-এর 1D signal-এর direct DFT-তে O(L²) কাজ লাগে। FFT-তে সাধারণত O(L log L) কাজ লাগে।</p>'+
    example('L = 1024 হলে তুলনা', ['L² = 1,048,576।', 'L log₂L = 1024×10 = 10,240।', 'অনুপাত প্রায় 102.4। এটি কাজের পরিমাণ বাড়ার তুলনা; বাস্তবে ঠিক এত গুণ দ্রুত হবেই, এমন দাবি নয়।'], 'M × N ছবির separable FFT-তে সাধারণত O(MN(log M + log N)) কাজ লাগে।')+
    '<h2>Correlation: এই pattern-টি কোথায় মেলে?</h2><p>ছোট template-কে ছবির বিভিন্ন জায়গায় রেখে মিলের score হিসাব করা হয়। Score-এর বড় peak একটি সম্ভাব্য মিলের অবস্থান দেখায়।</p>'+
    formula('r = IDFT{ F · W* }', 'F = ছবির transform; W = zero-padded template-এর transform। এখানে * মানে complex conjugate। যথেষ্ট padding না থাকলে circular shift অনুযায়ী correlation হবে।')+
    '<p>যেমন [0,1,1,0] সারিতে [1,1] template-টি index 1 থেকে মেলে। সেখানে dot-product score = 1×1+1×1 = 2। অন্য shift-এ score কম। Brightness বা contrast বদলালে normalised correlation কাজে লাগে।</p>'+
    recall('FFT কি DFT থেকে আলাদা ধরনের ফল দেয়?', 'না। FFT হলো DFT হিসাব করার কার্যকর ও দ্রুত algorithm।'))

add('Restoration: ছবির ক্ষতির কারণ আগে বুঝি',
    'আসল ছবি, blur, noise এবং দেখা ছবির মধ্যে সম্পর্ক বুঝুন।',
    '<p><strong>Enhancement</strong>-এ ছবিকে দেখতে বা কাজে ব্যবহার করতে ভালো করা হয়। <strong>Restoration</strong>-এ ছবি কীভাবে নষ্ট হয়েছে তার model ব্যবহার করে আসল ছবির মান অনুমান করা হয়।</p>'+
    formula('g(x,y) = h(x,y) ∗ f(x,y) + η(x,y)', 'f = আসল ছবি; h = blur বা degradation response; η (eta) = noise; g = আমরা যে নষ্ট ছবিটি দেখছি। ∗ মানে convolution।')+
    formula('G = HF + N', 'বড় হাতের অক্ষরগুলো সংশ্লিষ্ট Fourier transform। N হলো noise η-এর transform।')+
    example('শুধু noise আছে, blur নেই', ['তখন model: g = f+η।', 'আসল পিক্সেল f = 100; যোগ হওয়া noise η = −7।', 'দেখা পিক্সেল g = 100−7 = 93।'], 'আমরা g থেকে f অনুমান করতে চাই। বাস্তবে প্রতিটি পিক্সেলে ঠিক কত noise যোগ হয়েছে, তা জানা থাকে না।')+
    note('H খুব ছোট হলে G/H করলে noise অনেক বেড়ে যেতে পারে। H = 0 হলে ভাগ সংজ্ঞায়িত নয়। Model জানলেই পুরোপুরি আসল ছবি পাওয়া যাবে, এমন নয়।')+
    recall('Contrast সুন্দর করা, নাকি জানা blur ব্যবহার করে sharp ছবি অনুমান করা—কোনটি restoration?', 'জানা blur model ব্যবহার করে sharp ছবি অনুমান করা restoration। শুধু দেখতে ভালো করতে contrast বদলানো enhancement।'))

add('আগে noise চিনুন, তারপর filter বাছুন',
    'লেকচারের ছয়টি noise model এবং PDF-এর অর্থ বুঝুন।',
    '<p><strong>Noise</strong> হলো ছবির অপ্রয়োজনীয় পরিবর্তন বা দাগ। কোন noise মান কতটা সম্ভাব্য, সেটি বোঝায় probability density function বা <strong>PDF</strong>। Continuous PDF-এ কোনো interval-এর নিচের ক্ষেত্রফল হলো probability; একটি বিন্দুর height নিজে probability নয়।</p>'+
    table(['Model','আকার বা অর্থ','মনে রাখুন'],[['Gaussian','ঘণ্টার মতো; μ-এর দুই পাশে সমান','Mean μ; variance σ²'],['Uniform','a থেকে b পর্যন্ত সমান height','Mean (a+b)/2; variance (b−a)²/12'],['Rayleigh','a থেকে শুরু; ডানদিকে লেজ','একদিকে সীমাবদ্ধ, shifted distribution'],['Erlang (Gamma)','ডানদিকে লেজ; shape k পূর্ণসংখ্যা','k = 1 হলে exponential'],['Exponential','0-তে সবচেয়ে বেশি, তারপর কমে','মান ঋণাত্মক নয়; rate λ'],['Impulse','হঠাৎ কিছু কালো বা সাদা দাগ','Pepper: 0; salt: উজ্জ্বল, সাধারণত 255']])+
    example('Uniform noise: −3 থেকে 3', ['Mean = (−3+3)/2 = 0।', 'Variance = [3−(−3)]²/12 = 36/12 = 3।', 'PDF height = 1/6। [0,3]-এর probability = প্রস্থ 3 × height 1/6 = 1/2।'], 'Mean শূন্য মানে noise নেই, তা নয়। ধনাত্মক ও ঋণাত্মক error গড়ে কেটে যেতে পারে।')+
    '''<details><summary>ছয়টি PDF-এর সূত্র ও parameter</summary><div class="detail-body"><p><b>Gaussian:</b> p(z) = [1/(σ√(2π))]e<sup>−(z−μ)²/(2σ²)</sup>। সব বাস্তব z-এর জন্য; σ > 0।</p><p><b>Uniform:</b> a ≤ z ≤ b হলে p(z) = 1/(b−a); অন্যত্র 0। b > a।</p><p><b>Rayleigh:</b> z ≥ a হলে p(z) = [2(z−a)/b]e<sup>−(z−a)²/b</sup>; অন্যত্র 0। b > 0। Mean a+√(πb)/2; variance b(4−π)/4।</p><p><b>Erlang:</b> z ≥ 0 হলে p(z) = λ<sup>k</sup>z<sup>k−1</sup>e<sup>−λz</sup>/(k−1)!; অন্যত্র 0। λ > 0, k ≥ 1 পূর্ণসংখ্যা। Mean k/λ; variance k/λ²।</p><p><b>Exponential:</b> z ≥ 0 হলে p(z) = λe<sup>−λz</sup>; অন্যত্র 0। Mean 1/λ; variance 1/λ²।</p><p><b>Impulse:</b> a ও b-তে discrete probability mass P<sub>a</sub> ও P<sub>b</sub>। Corruption-এর probability P<sub>a</sub>+P<sub>b</sub>। Replacement model-এ বাকি পিক্সেল আগের মতো থাকে। এগুলো continuous density নয়, probability mass।</p></div></details><p>ছোট ছোট random পরিবর্তন → smoothing কাজে আসতে পারে। বিচ্ছিন্ন কালো-সাদা দাগ → median দিয়ে শুরু করা যায়। বারবার একই pattern-এর দাগ → frequency domain-এ দেখুন।</p>'''+
    recall('কয়েকটি পিক্সেল হঠাৎ 0 বা 255 হয়ে গেছে। কী noise?', 'Impulse বা salt-and-pepper noise। গড় extreme মানের দিকে টেনে যেতে পারে। Median বা adaptive median বিবেচনা করুন।'))

add('Mean filter: গড় করার চারটি ধরন',
    'Arithmetic, geometric ও harmonic mean হিসাব করুন এবং সীমাবদ্ধতা জানুন।',
    '<p>Window-এ K = mnটি মান আছে: z₁,…,z<sub>K</sub>। হিসাবের ফল শুধু মাঝের output পিক্সেলে বসবে।</p>'+
    table(['Filter','সূত্র','কী খেয়াল করবেন'],[['Arithmetic','∑z / K','Random পরিবর্তন মসৃণ করে; বড় outlier গড় টেনে নেয়'],['Geometric','(∏z)<sup>1/K</sup>','∏ মানে সবগুলো গুণ। একটি 0 থাকলেই গুণফল 0'],['Harmonic','K / ∑(1/z)','বড় salt মানের প্রভাব কমায়; input ধনাত্মক হতে হবে'],['Contraharmonic','∑z<sup>Q+1</sup> / ∑z<sup>Q</sup>','Salt বা pepper অনুযায়ী Q বাছুন; পরের পাঠে আছে']])+
    example('ছোট window [2,4,8]', ['Arithmetic: (2+4+8)/3 = 14/3 ≈ <strong>4.667</strong>।', 'Geometric: (2×4×8)<sup>1/3</sup> = 64<sup>1/3</sup> = <strong>4</strong>।', 'Harmonic: 3/(1/2+1/4+1/8) = 3/0.875 ≈ <strong>3.429</strong>।'], 'একই window থেকেও আলাদা mean আলাদা ফল দেয়।')+
    note('কোনো মান 0 হলে harmonic সূত্রে 1/0 আসে। তাই সরাসরি লেখা সূত্রটি undefined। Limit বা implementation-এর বিশেষ নিয়মে 0 ধরা হতে পারে, কিন্তু অঙ্কে চুপচাপ 1/0 হিসাব করবেন না।')+
    recall('একটি pepper পিক্সেলের মান 0 হলে geometric mean কত?', 'গুণফল 0, তাই geometric mean-ও 0। Pepper zero সরানোর জন্য এটি ভালো পছন্দ নয়।'))

add('Contraharmonic: Q-এর চিহ্নটি জরুরি',
    'সঠিক Q বাছুন এবং লব-হর আলাদা করে হিসাব করুন।',
    formula('f̂ = ∑ z<sup>Q+1</sup> / ∑ z<sup>Q</sup>', 'f̂ মানে আসল intensity-এর অনুমান। লবে এক ঘাত, হরে আরেক ঘাত—দুটির যোগফল আলাদা করে বের করুন।')+
    '<div class="compare"><section><h3>Q ধনাত্মক → pepper</h3><p>Q > 0 হলে 0-এর অবদান 0 হয়। আশপাশের উজ্জ্বল মান তুলনামূলক বেশি ওজন পায়।</p></section><section><h3>Q ঋণাত্মক → salt</h3><p>বড় salt মান তুলনামূলক কম ওজন পায়। তবে 0-এর ঋণাত্মক ঘাত সংজ্ঞায়িত নয়।</p></section></div>'+
    example('Pepper window [0,10,10], Q = 1', ['লব: 0²+10²+10² = 200।', 'হর: 0¹+10¹+10¹ = 20।', 'ফল = 200/20 = <strong>10</strong>। Arithmetic mean হলে 20/3 ≈ 6.667 হতো।'], 'এই উদাহরণে ধনাত্মক Q pepper zero-এর প্রভাব সরিয়ে দিল।')+
    example('Salt window [10,10,100], Q = −1', ['সব input ধনাত্মক, তাই লব ∑z⁰ = 3।', 'হর = 1/10+1/10+1/100 = 0.21।', 'ফল = 3/0.21 ≈ <strong>14.286</strong>। Arithmetic mean হতো 40।'], 'সব input ধনাত্মক হলে Q = −1-এ harmonic mean পাওয়া যায়।')+
    note('একটি স্থির Q দিয়ে মিশ্র salt-and-pepper noise নির্ভরযোগ্যভাবে সরানো যায় না। Q < 0 হলে zero সমস্যা করে। সব মান 0 হলে Q > 0-তেও 0/0 হয়। এই filter-এ z⁰ = 1 ধরার প্রচলিত নিয়ম ব্যবহার করলে Q = 0-তে arithmetic mean পাওয়া যায়।')+
    recall('গাঢ় pepper noise-এর জন্য Q = +1.5 নেবেন, না −1.5?', '+1.5। ধনাত্মক Q pepper zero-এর প্রভাব কমায়, যদি হর শূন্য না হয়।'))

add('আগে সাজাই: median, min, max, midpoint',
    'কোনটি মাঝের মান, আর কোনটি দুই প্রান্তের গড়—পার্থক্য বুঝুন।',
    '<p>Order-statistic filter আগে window-এর মানগুলো ছোট থেকে বড় করে সাজায়। <strong>Median হলো সাজানো তালিকার মাঝের মান</strong>। এটি সর্বনিম্ন ও সর্বোচ্চের গড় নয়।</p>'+
    component(18,'<div class="image-lab">','</div>')+
    '<p class="small muted">প্রতিটি পিক্সেলে 3 × 3 median হিসাব করা হয়েছে। অনেক বিচ্ছিন্ন দাগ সরে গেছে। তবে সরু রেখাটিও হারিয়ে যেতে পারে। Noise কমাতে গিয়ে detail হারানোর এই দিকটি মনে রাখুন।</p>'+
    example('Window [10,11,10,255,9,10,12,11,10]', ['সাজালে: [9,10,10,10,<strong>10</strong>,11,11,12,255]।', '9টি মান, তাই 5ম মানটি median → <strong>10</strong>।', 'Min = <strong>9</strong>, max = <strong>255</strong>।', 'Midpoint = (9+255)/2 = <strong>132</strong>।'], 'এখানে median বিচ্ছিন্ন salt দাগটি সরায়। Midpoint বড় outlier-এর কারণে অনেক বেড়ে যায়।')+
    table(['Filter','কখন শুরুতে ভাবতে পারেন','সীমাবদ্ধতা'],[['Median','মিশ্র salt ও pepper','গড়ের চেয়ে edge ভালো রাখতে পারে; সরু detail মুছে যেতে পারে'],['Max','Pepper বা কালো দাগ','উজ্জ্বল অংশ ছড়ায়; salt থেকে যায়'],['Min','Salt বা উজ্জ্বল দাগ','গাঢ় অংশ ছড়ায়; pepper থেকে যায়'],['Midpoint','কিছু Gaussian/uniform noise-এর ক্ষেত্রে','দুই প্রান্তের গড়; impulse outlier-এ ফল খারাপ হয়']])+
    recall('3 × 3 window-এর সাজানো 9টি মানের কত নম্বরটি median?', '1 থেকে গুনলে 5ম মান। 0 থেকে index ধরলে index 4। বিজোড় সংখ্যক মান থাকলে মাঝের একটি মানই নিতে হবে।'))

add('Alpha-trimmed mean: সাজাই, বাদ দিই, গড় করি',
    'd মানে মোট কতটি বাদ যাবে, তা বুঝে সঠিক সংখ্যা দিয়ে ভাগ করুন।',
    formula('f̂ = (বাকি রাখা মানগুলোর যোগফল) / (K − d)', 'd জোড় সংখ্যা। ছোট দিক থেকে d/2টি, বড় দিক থেকে d/2টি বাদ দিন। 0 ≤ d < K; K = mn হলো শুরুতে থাকা মানের সংখ্যা।')+
    example('সাজানো তালিকা [0,10,10,11,11,12,12,13,255]; d = 2', ['সবচেয়ে ছোট <strong>একটি</strong> 0 এবং সবচেয়ে বড় <strong>একটি</strong> 255 বাদ দিন।', 'বাকি [10,10,11,11,12,12,13]। যোগফল 79।', 'বাকি মানের সংখ্যা = 9−2 = 7। ফল = 79/7 ≈ <strong>11.286</strong>।'], 'আগে extreme outlier বাদ, তারপর বাকিগুলোর গড়।')+
    '<p>d = 0 হলে arithmetic mean। K বিজোড় এবং d = K−1 হলে শুধু মাঝের একটি মান থাকে: সেটিই median। মাঝামাঝি পরিমাণ trim করলে random ও impulse noise মিশে থাকা ক্ষেত্রে কাজে আসতে পারে।</p>'+
    recall('3 × 3 window-এ d = 4 হলে প্রতি প্রান্ত থেকে কতটি বাদ দেবেন? কত দিয়ে ভাগ করবেন?', 'ছোট দিক থেকে 2টি, বড় দিক থেকে 2টি। বাকি 5টির যোগফলকে 5 দিয়ে ভাগ করবেন, 9 দিয়ে নয়।'))

add('লেকচারের 7 × 7 অঙ্কটি নিজে করুন',
    'সঠিক 3 × 3 window নিন, তারপর মাঝের পিক্সেলের নতুন মান হিসাব করুন।',
    '<p>এটি লেকচার 8-এর সংখ্যার ছক। Salt-এর মতো উজ্জ্বল outlier 204 অথবা pepper 0 বাছুন। ঘেরা <strong>9টি ঘর হলো input</strong>। গাঢ় রঙের ঘরটি হলো নতুন মান বসানোর অবস্থান।</p>'+
    component(20,'<section class="lab">','</section>')+
    '<h2>CT-তে অঙ্কের উত্তরে যা দেখাবেন</h2><ol><li>বেছে নেওয়া window এবং তার 9টি মান।</li><li>Filter-এর সূত্র। দরকার হলে ছোট থেকে বড় সাজানো তালিকা।</li><li>সংখ্যা বসানো লব ও হর।</li><li>শেষে ফল বের করে round করুন। Output ছবিতে মাঝের অবস্থানে ফলটি বসবে।</li></ol>'+
    note('হিসাবের ফল আসল মানের একটি অনুমান। নষ্ট পিক্সেলের আসল মান এখানে জানা নেই। প্রশ্নে আলাদা করে না বললে আগের filtered output দিয়ে পরের window-এর হিসাব করবেন না।')+
    recall('সব 49টি পিক্সেলের গড় না করে 3 × 3 window নিই কেন?', 'প্রশ্নে filter-এর window 3 × 3। পুরো ছবির মাপ 7 × 7, সেটি filter-এর মাপ নয়।'))

add('Periodic noise: নির্দিষ্ট band বাদ দিই',
    'বারবার আসা দাগ চিনুন এবং ideal band-reject-এর gain বের করুন।',
    '<p>একই ধরনের ডোরা বা ঢেউ বারবার দেখা গেলে সেটি <strong>periodic noise</strong> হতে পারে। Fourier spectrum-এ এর আলাদা peak দেখা যায়। Band-reject filter একটি বৃত্তাকার frequency band বাদ দেয়; তার নিচে ও ওপরে থাকা frequency রাখে।</p>'+
    formula('H<sub>IBR</sub>(D) = 0 যদি D₀ − W/2 ≤ D ≤ D₀ + W/2; &nbsp; অন্যত্র 1', 'D₀ = বাদ দেওয়া band-এর মাঝের radius; W = band-এর প্রস্থ। Complementary band-pass: HBP = 1−HBR।')+
    example('D₀ = 30, W = 10', ['নিচের সীমানা 30−5 = 25। ওপরের সীমানা 30+5 = 35।', 'D = 28 হলে [25,35]-এর ভেতর → H = 0 → বাদ যাবে।', 'D = 10 বা 40 হলে বাইরে → H = 1 → থাকবে।'], 'সব high frequency না কেটে, সমস্যার band-টি লক্ষ্য করে বাদ দিন।')+
    '<details><summary>মসৃণ band-reject-এর আরও দুটি সূত্র</summary><div class="detail-body"><p><b>Butterworth:</b> H = 1/[1+(DW/(D²−D₀²))<sup>2n</sup>]। D = D₀-তে limit অনুযায়ী H = 0 ধরুন।</p><p><b>Gaussian:</b> H = 1−exp{−[(D²−D₀²)/(DW)]²}। D₀ > 0 হলে D = 0-তে limit অনুযায়ী gain 1; D = D₀-তে gain 0।</p><p><b>Notch reject</b> পুরো বৃত্ত বাদ না দিয়ে আলাদা conjugate peak pair লক্ষ্য করে। এতে উপকারী frequency বেশি রাখা যেতে পারে। লেকচারে band-reject-এ জোর দেওয়া হয়েছে।</p></div></details>'+
    recall('Band-reject-এর gain 0.2 হলে complementary band-pass-এর gain কত?', '1−0.2 = 0.8।'))

add('Adaptive median: যাচাই করে সিদ্ধান্ত নিই',
    'Level A, Level B এবং কখন window বাড়বে, তা ধাপে ধাপে বুঝুন।',
    '<p>Fixed median filter প্রতিটি centre-কে median দিয়ে বদলায়। <strong>Adaptive median</strong> ভালো centre আগের মতো রাখতে পারে। বর্তমান median বিশ্বাসযোগ্য না হলে window-ও বড় করতে পারে।</p><p>এখানে z<sub>min</sub> = সবচেয়ে ছোট, z<sub>max</sub> = সবচেয়ে বড়, z<sub>med</sub> = median, z<sub>xy</sub> = মাঝের মান। 3 × 3 দিয়ে শুরু করুন; সর্বোচ্চ মাপ S<sub>max</sub> ঠিক করে নিন।</p><div class="decision"><section><span class="eyebrow">LEVEL A · MEDIAN বিশ্বাসযোগ্য?</span><h3>z<sub>min</sub> &lt; z<sub>med</sub> &lt; z<sub>max</sub></h3><p><strong>হ্যাঁ →</strong> Level B-তে যান।<br><strong>না →</strong> window-এর মাপ 2 বাড়ান। S<sub>max</sub>-এর মধ্যে হলে আবার A যাচাই করুন। আর বাড়ানো না গেলে বর্তমান median output দিন।</p></section><section><span class="eyebrow">LEVEL B · মাঝের মানটি বিশ্বাসযোগ্য?</span><h3>z<sub>min</sub> &lt; z<sub>xy</sub> &lt; z<sub>max</sub></h3><p><strong>হ্যাঁ →</strong> আসল centre রেখে দিন।<br><strong>না →</strong> centre-কে z<sub>med</sub> দিয়ে বদলান।</p></section></div>'+
    example('min = 0, median = 51, max = 255, centre = 255', ['A: 0 < 51 < 255 সত্য → median ঠিক আছে → B-তে যান।', 'B: 0 < 255 < 255 মিথ্যা। কারণ 255 নিজে 255-এর চেয়ে ছোট নয়।', 'Centre বদলে median <strong>51</strong> দিন। Centre 50 হলে সেটি আগের মতো রাখতেন।'], 'Level A median যাচাই করে। Level B centre যাচাই করে।')+
    '<details><summary>লেকচারের A₁/A₂ আকারে লিখি</summary><div class="detail-body"><p>A₁ = z<sub>med</sub>−z<sub>min</sub>; A₂ = z<sub>med</sub>−z<sub>max</sub>। A₁ > 0 এবং A₂ < 0 হলে A পাস।</p><p>B₁ = z<sub>xy</sub>−z<sub>min</sub>; B₂ = z<sub>xy</sub>−z<sub>max</sub>। B₁ > 0 এবং B₂ < 0 হলে B পাস।</p></div></details>'+
    recall('3 × 3 window-এ min = 0, median = 0, max = 255। এখন কি Level B-তে যাবেন?', 'না। 0 < 0 মিথ্যা, তাই A ফেল। অনুমতি থাকলে 5 × 5 করুন। সর্বোচ্চ মাপে পৌঁছে গেলে শেষ যাচাই করা window-এর median output দিন।'))

add('চার মিনিটে সূত্রগুলো ঝালাই করুন',
    'আগে না দেখে মনে করার চেষ্টা করুন, তারপর মিলিয়ে নিন।',
    '<p>ডান পাশ ঢেকে প্রতিটি নিয়ম নিজের ভাষায় বলুন। কোনো symbol বুঝতে না পারলে সেই পাঠে ফিরুন। সূত্র দেখা এবং নিজে অঙ্ক করতে পারা—দুটিই দরকার।</p>'+
    table(['বিষয়','নিয়ম / উত্তর'],[['Frequency filtering','G = HF; spatial convolution ↔ frequency-তে গুণ'],['কেন্দ্র থেকে দূরত্ব','D = √[(u−P/2)²+(v−Q/2)²]'],['Ideal LPF','D ≤ D₀-তে 1; বাইরে 0'],['Butterworth LPF','1/[1+(D/D₀)²ⁿ]; H(D₀) = 0.5'],['Gaussian LPF','e<sup>−D²/(2D₀²)</sup>; H(D₀) ≈ 0.607'],['Complementary HPF','1−LPF; H(0) = 0'],['Emphasis','a+bHHP; a পটভূমি রাখে'],['Restoration','g = h∗f+η; শুধু noise হলে g = f+η'],['Arithmetic / geometric','∑z/K; (∏z)<sup>1/K</sup>'],['Harmonic / contraharmonic','K/∑(1/z); ∑z<sup>Q+1</sup>/∑z<sup>Q</sup>'],['Q-এর চিহ্ন','Pepper-এ ধনাত্মক; salt-এ ঋণাত্মক'],['Median / midpoint','সাজানো মাঝের মান; (min+max)/2'],['Alpha-trimmed','প্রতি প্রান্তে d/2টি বাদ; বাকি যোগফলকে K−d দিয়ে ভাগ'],['Ideal band reject','D₀−W/2 ≤ D ≤ D₀+W/2 band বাদ'],['Adaptive median','A median দেখে; B centre দেখে; < ও >, সমান নয়']])+
    '<h2>কারণ বুঝিয়ে filter বাছুন</h2><p><strong>ছোট random পরিবর্তন:</strong> mean বা smooth LPF কাজে আসতে পারে; detail কমতে পারে। <strong>Impulse দাগ:</strong> median; স্থানভেদে অবস্থা বদলালে adaptive median। <strong>বারবার ডোরা:</strong> band-reject বা নির্দিষ্ট notch।</p>'+
    note('এই জোড়াগুলো গুলিয়ে ফেলবেন না: amplitude/power; median/midpoint; ছবির মাপ/window-এর মাপ; Level A/Level B। উত্তরে পদ্ধতির সুবিধা ও সীমাবদ্ধতা দুটোই বলুন।')+
    recall('না দেখে বলুন: D₀-তে কোন LPF-এর gain 0.5, কোনটির প্রায় 0.607?', 'Butterworth → 0.5। Gaussian → e<sup>−0.5</sup> ≈ 0.607।'))

add('CT-এর আগে নিজে পরীক্ষা দিন',
    'নোট না দেখে 10 মিনিট উত্তর দিন। পরের 4 মিনিট ভুলগুলো বুঝে ঠিক করুন।',
    '<p>অঙ্ক খাতায় করুন। উত্তর দিলে ব্যাখ্যা পাবেন এবং কোন পাঠ আবার পড়বেন, তা জানতে পারবেন। Score-এ আপনার <strong>প্রথম উত্তর</strong> গণনা হবে। সব প্রশ্নের উত্তর দেওয়ার পর ফল বিচার করুন।</p><div class="quiz-toolbar"><div id="quiz-score" role="status" aria-live="polite">0 / 12টি উত্তর দেওয়া হয়েছে</div><button id="reset-quiz">আবার নতুন করে পরীক্ষা দিন</button></div><div id="quiz"></div><section class="example"><div class="eyebrow">শেষ করার আগে</div><h3>শুধু সংখ্যা নয়, হিসাবের ধাপও লিখুন</h3><p>অঙ্কে: সূত্র → মান বসানো → হিসাব → ফল। Theory-তে: পদ্ধতিটি কী → কীভাবে কাজ করে → একটি ব্যবহার → একটি সীমাবদ্ধতা।</p><p id="study-advice">পরীক্ষা শেষ করলে কোন পাঠ আবার পড়া দরকার, তা দেখাবে।</p></section>')

quiz_text=[
('2 × 2 ছবির প্রতিটি পিক্সেলের মান 5। Unnormalised F(0,0) কত?',None,'DC হলো সব পিক্সেলের যোগফল: 4×5 = 20। গড় intensity হলো 5।'),
('জোড় মাপের ছবিতে DFT-এর আগে (−1)^(x+y) দিয়ে গুণ করা হয় কেন?', ['Noise সরাতে','Edge ধারালো করতে','DC-কে মাঝখানে আনতে','পিক্সেল ধনাত্মক করতে'],'এই checkerboard modulation spectrum-কে দুই অক্ষেই অর্ধেক মাপ shift করে। Inverse-এর পরে এর প্রভাব সরাতে হবে।'),
('Butterworth LPF: n = 1 এবং D = 2D₀। H কত?',None,'H = 1/[1+2²] = 1/5 = 0.2।'),
('Gaussian HPF-এ D = D₀ হলে আনুমানিক gain কত?',None,'GHPF = 1−e^(−0.5) = 1−0.6065 ≈ 0.3935।'),
('হঠাৎ cutoff-এর কারণে কোন filter-এ ringing বেশি দেখা যায়?', ['Gaussian LPF','Ideal LPF','কোনো filter-এই ringing হয় না','সব মসৃণ response-এ সমান'],'Frequency-তে হঠাৎ সীমানা কাটলে spatial response-এ ওঠানামা হয়। তাই edge-এর পাশে বলয়ের মতো দাগ হয়।'),
('[0,10,10] window-এ Q = 1 হলে contraharmonic ফল কত?',None,'লব = 0²+10²+10² = 200। হর = 0+10+10 = 20। ফল = 10।'),
('মিশ্র salt-and-pepper দাগ কমাতে কোনটি উপযুক্ত?', ['Geometric mean','Midpoint','Zero থাকা অবস্থায় ঋণাত্মক Q','Median'],'Median সাজানো তালিকার মাঝের মান নেয়, তাই বিচ্ছিন্ন extreme মানের প্রভাব কমে। তবে সরু detail হারাতে পারে; দাগ খুব ঘন হলেও সমস্যা হতে পারে।'),
('[0,10,10,11,11,12,12,13,255]-এ d = 4 দিয়ে alpha-trim করলে ফল কত?',None,'[0,10] এবং [13,255] বাদ দিন। বাকি [10,11,11,12,12]-এর যোগফল 56। 5 দিয়ে ভাগ করলে 11.2।'),
('Ideal band reject: D₀ = 30, W = 10। D = 35-এ কী হবে?', ['Gain 1','Gain 0','Gain 0.5','বলা যায় না'],'বাদ দেওয়া interval [25,35]। দেওয়া নিয়মে সীমানাও এর মধ্যে, তাই gain 0।'),
('Adaptive median: min=0, median=50, max=255, centre=49। Output কত?',None,'A পাস: 0<50<255। B-ও পাস: 0<49<255। তাই আসল centre 49 রেখে দিন।'),
('3 × 3 window-এ min=0, median=0, max=255। 5 × 5 নেওয়া যাবে। পরের ধাপ কী?', ['সঙ্গে সঙ্গে centre রেখে দিই','Level B-তে যাই','255 output দিই','5 × 5 করে আবার A যাচাই করি'],'Median ও min সমান বলে Level A ফেল। বড় window নেওয়ার অনুমতি থাকলে মাপ বাড়াতে হবে।'),
('Convolution theorem-এর মূল কথা কোনটি?', ['Spatial convolution ↔ frequency-তে গুণ','FFT আর DFT আলাদা transform','Restoration সব noise সরিয়েই দেয়','High frequency মানে উজ্জ্বল পিক্সেল'],'g=f∗h-এর সঙ্গে G=FH মেলে। Linear convolution-এর জন্য প্রয়োজনমতো padding লাগবে। উজ্জ্বলতা আর স্থান বরাবর বদলের গতি আলাদা বিষয়।'),
]
quiz=[{**base,'q':q,'options':options if options is not None else base['options'],'why':why} for base,(q,options,why) in zip(english_quiz,quiz_text)]

assert len(lessons)==len(english)==24
assert len(quiz)==len(english_quiz)==12
for en,bn in zip(english,lessons):
    assert re.findall(r'id="([^"]+)"',en['body'])==re.findall(r'id="([^"]+)"',bn['body']), f'Interactive IDs differ in lesson {en["id"]}'
