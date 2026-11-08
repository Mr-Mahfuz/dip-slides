'use strict';
const $ = id => document.getElementById(id);
const STORE = 'dip-study-room-v2';
let state = {done:[],review:[],current:1,theme:'paper',size:19,answers:{},timerEnd:null,timerRemaining:7200000};
let storageOK=true;
try { Object.assign(state,JSON.parse(localStorage.getItem(STORE)||'{}')); } catch { storageOK=false; }
state.done = Array.isArray(state.done) ? state.done.filter(n=>Number.isInteger(n)&&n>=1&&n<=24) : [];
state.review = Array.isArray(state.review) ? state.review.filter(n=>Number.isInteger(n)&&n>=1&&n<=24) : [];
state.answers = state.answers && typeof state.answers==='object' ? state.answers : {};
let reviewOnly=false, activeId=1, toastTimeout;
function save(){try{localStorage.setItem(STORE,JSON.stringify(state));}catch{storageOK=false;}}
function toast(message){$('toast').textContent=message;$('toast').classList.add('show');clearTimeout(toastTimeout);toastTimeout=setTimeout(()=>$('toast').classList.remove('show'),2400);}
function applyReading(){
  if(!['paper','light','dark'].includes(state.theme))state.theme='paper';
  if(![17,19,21].includes(state.size))state.size=19;
  document.documentElement.dataset.theme=state.theme;
  document.documentElement.style.setProperty('--size',state.size+'px');
  document.querySelector('meta[name=theme-color]').content=state.theme==='dark'?'#1c2422':state.theme==='paper'?'#f6f4ed':'#f5f7f7';
  document.querySelectorAll('[data-theme-choice]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.themeChoice===state.theme)));
  document.querySelectorAll('[data-size]').forEach(b=>b.setAttribute('aria-pressed',String(Number(b.dataset.size)===state.size)));
}
function renderNav(){
  const query=$('search').value.trim().toLowerCase();let last='',html='',count=0;
  for(const l of LESSONS){
    if(reviewOnly&&!state.review.includes(l.id))continue;
    const searchable=(l.title+' '+l.goal+' '+l.body.replace(/<[^>]*>/g,' ')).toLowerCase();
    if(query&&!searchable.includes(query))continue;
    if(last!==l.group){last=l.group;html+='<div class="nav-group">'+last+'</div>';}
    const done=state.done.includes(l.id);
    html+='<button class="lesson-link'+(done?' done':'')+'" data-go="'+l.id+'" '+(activeId===l.id?'aria-current="page"':'')+'><span class="num">'+(done?'✓':String(l.id).padStart(2,'0'))+'</span><span>'+l.title+'</span>'+(state.review.includes(l.id)?'<span class="flag" aria-label="Saved for review">☆</span>':'')+'</button>';count++;
  }
  $('lesson-nav').innerHTML=html;$('no-results').hidden=count>0;
  $('no-results').textContent=reviewOnly&&!state.review.length?'No lessons saved yet. Use “Review later” in a lesson.':'No matching lessons. Try another term.';
  $('progress-label').textContent=state.done.length+' of 24 studied';
  $('progress-percent').textContent=Math.round(state.done.length/24*100)+'%';$('progress').value=state.done.length;
  $('review-count').textContent=state.review.length;
  $('all-lessons').setAttribute('aria-pressed',String(!reviewOnly));$('review-filter').setAttribute('aria-pressed',String(reviewOnly));
}
function closeMenu(){ $('sidebar').classList.remove('open');$('shade').hidden=true;$('menu').setAttribute('aria-expanded','false');if(matchMedia('(max-width:850px)').matches)$('sidebar').inert=true; }
function navigate(id,focus=true){
  id=Number(id);if(!Number.isInteger(id)||id<1||id>LESSONS.length)id=1;
  activeId=id;const l=LESSONS[id-1];state.current=id;save();
  $('lesson-title').textContent=l.title;$('lesson-goal').textContent=l.goal;$('lesson-body').innerHTML=l.body;
  $('lesson-meta').textContent=(id===1?'YOUR STARTING POINT':l.group.toUpperCase())+' · '+l.minutes+' MIN';
  $('chapter-label').textContent=l.group==='Start'?'GETTING STARTED':l.group.toUpperCase();$('position').textContent='LESSON '+String(id).padStart(2,'0')+' / 24';
  const start=LESSONS.slice(0,id-1).reduce((s,x)=>s+x.minutes,0);$('time-range').textContent=start+'–'+(start+l.minutes)+' min';
  $('source-link').innerHTML=l.pages?'Compare with your source: <button id="lesson-source">Lecture '+l.pages[0]+' · page '+l.pages[1]+' ↗</button>':'Sources: your Lecture 7 and Lecture 8 PDFs · <button id="lesson-source">Browse original slides ↗</button>';
  $('lesson-source').onclick=()=>openReferences(...(l.pages||[7,1]));
  $('previous').disabled=id===1;$('next').disabled=id===24;$('next-title').textContent=id<24?LESSONS[id].title:'You have reached the end';
  updateLessonButtons();renderNav();closeMenu();
  if(id===10)initFrequencyLab();if(id===18)renderNoiseDemo();if(id===20)initWindowLab();if(id===24)renderQuiz();
  document.title=l.title+' · DIP Study Room';
  if(location.hash!=='#lesson-'+id)history.pushState(null,'','#lesson-'+id);
  window.scrollTo({top:0,behavior:'instant'});if(focus)$('lesson-title').focus({preventScroll:true});
}
function updateLessonButtons(){const done=state.done.includes(activeId),review=state.review.includes(activeId);$('complete').setAttribute('aria-pressed',String(done));$('complete').textContent=done?'✓ Studied':'Mark as studied';$('review').setAttribute('aria-pressed',String(review));$('review').textContent=review?'★ Saved for review':'☆ Review later';}
function toggleList(key){const arr=state[key],i=arr.indexOf(activeId);if(i<0)arr.push(activeId);else arr.splice(i,1);save();updateLessonButtons();renderNav();}
document.addEventListener('click',e=>{const go=e.target.closest('[data-go]');if(go)navigate(go.dataset.go);});
$('previous').onclick=()=>navigate(activeId-1);$('next').onclick=()=>navigate(activeId+1);
$('complete').onclick=()=>{toggleList('done');toast(state.done.includes(activeId)?'Lesson marked as studied. Try recalling it once more.':'Lesson marked as not yet studied.');};
$('review').onclick=()=>toggleList('review');$('search').oninput=renderNav;
$('all-lessons').onclick=()=>{reviewOnly=false;renderNav();};$('review-filter').onclick=()=>{reviewOnly=true;renderNav();};
$('menu').onclick=()=>{const open=!$('sidebar').classList.contains('open');$('sidebar').classList.toggle('open',open);$('shade').hidden=!open;$('menu').setAttribute('aria-expanded',String(open));$('sidebar').inert=!open;if(open)$('search').focus();};
$('menu-close').onclick=()=>{closeMenu();$('menu').focus();};$('shade').onclick=closeMenu;
document.addEventListener('keydown',e=>{
  if(e.key==='Escape'){closeMenu();return;}
  if(e.ctrlKey||e.altKey||e.metaKey||document.querySelector('dialog[open]'))return;
  if(e.target.closest('input,textarea,select,button,summary,a,[contenteditable=true]'))return;
  if(e.key==='ArrowRight'&&activeId<24){e.preventDefault();navigate(activeId+1);}
  if(e.key==='ArrowLeft'&&activeId>1){e.preventDefault();navigate(activeId-1);}
  if(e.key==='/'){e.preventDefault();if(matchMedia('(max-width:850px)').matches&&!$('sidebar').classList.contains('open'))$('menu').click();$('search').focus();}
});
window.addEventListener('hashchange',()=>navigateFromHash());
function navigateFromHash(){const match=location.hash.match(/^#(?:lesson|slide)-(\d+)$/);navigate(match?Number(match[1]):state.current,false);}
let dialogReturnFocus=null;
function showDialog(id){dialogReturnFocus=document.activeElement;$(id).showModal();}
document.querySelectorAll('[data-close]').forEach(b=>b.onclick=()=>$(b.dataset.close).close());
document.querySelectorAll('dialog').forEach(d=>{d.addEventListener('close',()=>{if(dialogReturnFocus?.isConnected)dialogReturnFocus.focus();$('settings-open').setAttribute('aria-expanded','false');});d.addEventListener('click',e=>{if(e.target===d){const r=d.getBoundingClientRect();if(e.clientX<r.left||e.clientX>r.right||e.clientY<r.top||e.clientY>r.bottom)d.close();}});});
$('settings-open').onclick=()=>{applyReading();$('settings-open').setAttribute('aria-expanded','true');showDialog('settings');};
document.querySelectorAll('[data-theme-choice]').forEach(b=>b.onclick=()=>{state.theme=b.dataset.themeChoice;applyReading();save();if(activeId===10)updateFrequency();});
document.querySelectorAll('[data-size]').forEach(b=>b.onclick=()=>{state.size=Number(b.dataset.size);applyReading();save();});
function openReferences(lecture=7,page=1){$('reference-lecture').value=String(lecture);populatePages(page);if(!$('references').open)showDialog('references');}
function populatePages(page=1){const count=$('reference-lecture').value==='7'?66:46;$('reference-page').innerHTML=Array.from({length:count},(_,i)=>'<option value="'+(i+1)+'">'+(i+1)+'</option>').join('');$('reference-page').value=String(Math.max(1,Math.min(count,page)));updateReference();}
function updateReference(){const lec=$('reference-lecture').value,p=Number($('reference-page').value),max=lec==='7'?66:46;$('reference-image').src='slides_images/slide'+lec+'_page_'+String(p).padStart(2,'0')+'.png';$('reference-image').alt='Original Lecture '+lec+', page '+p;$('reference-caption').textContent='Lecture '+lec+' · page '+p+' of '+max;$('pdf-link').href='dip%20slide%20'+lec+'.pdf#page='+p;$('reference-prev').disabled=p===1;$('reference-next').disabled=p===max;}
$('reference-open').onclick=()=>openReferences();$('reference-lecture').onchange=()=>populatePages();$('reference-page').onchange=updateReference;
$('reference-prev').onclick=()=>{$('reference-page').value=String(Number($('reference-page').value)-1);updateReference();};$('reference-next').onclick=()=>{$('reference-page').value=String(Number($('reference-page').value)+1);updateReference();};
function lowGain(d,d0,family){if(family==='ideal')return d<=d0?1:0;if(family==='butter')return 1/(1+(d/d0)**4);return Math.exp(-d*d/(2*d0*d0));}
function gain(d,d0,family,pass){const low=lowGain(d,d0,family);return pass==='high'?1-low:low;}
function initFrequencyLab(){['family','pass','cutoff'].forEach(id=>$(id).oninput=updateFrequency);updateFrequency();}
function pathFrom(points){return points.map((p,i)=>(i?'L':'M')+p.map(v=>v.toFixed(2)).join(',')).join(' ');}
function updateFrequency(){
  if(!$('cutoff'))return;const d0=Number($('cutoff').value),family=$('family').value,pass=$('pass').value;$('cutoff-value').value=d0;
  const points=Array.from({length:601},(_,i)=>{const d=i/30;return[44+d*29,180-150*gain(d,d0,family,pass)];});
  let axes='<path d="M44 25V180H630" fill="none" stroke="var(--border)"/>';
  for(const d of [0,5,10,15,20])axes+='<text x="'+(44+d*29)+'" y="202" text-anchor="middle">'+d+'</text>';
  axes+='<text x="25" y="184">0</text><text x="25" y="34">1</text><text x="636" y="184">D</text><text x="25" y="17">H</text>';
  $('response-plot').innerHTML=axes+'<path d="'+pathFrom(points)+'" fill="none" stroke="var(--accent)" stroke-width="3"/><path d="M'+(44+d0*29)+' 25V180" stroke="var(--plot)" stroke-dasharray="4 4"/><text x="'+Math.min(590,44+d0*29+7)+'" y="20">D₀ = '+d0+'</text>';
  const g2=gain(2,d0,family,pass),g12=gain(12,d0,family,pass);
  const input=[],output=[];for(let i=0;i<=300;i++){const t=2*Math.PI*i/300;input.push([44+i*1.93,90-35*Math.sin(2*t)-20*Math.sin(12*t)]);output.push([44+i*1.93,90-35*g2*Math.sin(2*t)-20*g12*Math.sin(12*t)]);}
  $('signal-plot').innerHTML='<path d="M44 20V155H630 M44 90H630" fill="none" stroke="var(--border)"/><text x="14" y="94">128</text><text x="44" y="175">0</text><text x="590" y="175">end</text><path d="'+pathFrom(input)+'" fill="none" stroke="var(--muted)" opacity=".5" stroke-width="1.5"/><path d="'+pathFrom(output)+'" fill="none" stroke="var(--accent)" stroke-width="2.5"/>';
  $('gain-readout').textContent='Slow wave gain: '+g2.toFixed(3)+' · Fast wave gain: '+g12.toFixed(3)+'. '+(pass==='low'?'Low-pass retains slow variation and reduces the fast wiggle.':'High-pass reduces the slow wave and retains faster detail.');
  renderGray('frequency-original',(x,y)=>128+45*Math.sin(2*Math.PI*2*x/128)+25*Math.sin(2*Math.PI*12*y/128));
  renderGray('frequency-mask',(x,y)=>255*gain(Math.hypot(x-64,y-64),d0,family,pass));
  renderGray('frequency-output',(x,y)=>128+45*g2*Math.sin(2*Math.PI*2*x/128)+25*g12*Math.sin(2*Math.PI*12*y/128));
}
function renderGray(id,pixel){const canvas=$(id);if(!canvas)return;const ctx=canvas.getContext('2d'),data=ctx.createImageData(canvas.width,canvas.height);for(let y=0;y<canvas.height;y++)for(let x=0;x<canvas.width;x++){const i=(y*canvas.width+x)*4,z=Math.max(0,Math.min(255,Math.round(pixel(x,y))));data.data[i]=data.data[i+1]=data.data[i+2]=z;data.data[i+3]=255;}ctx.putImageData(data,0,0);}
function renderNoiseDemo(){const n=96;let seed=42;const random=()=>{seed=(Math.imul(1664525,seed)+1013904223)>>>0;return seed/4294967296;};const clean=Array.from({length:n},(_,y)=>Array.from({length:n},(_,x)=>x===73&&y>12&&y<83?210:x>21&&x<65&&y>21&&y<74?195:65));const noisy=clean.map(row=>row.map(v=>{const r=random();return r<.04?0:r<.08?255:v;}));renderGray('noise-clean',(x,y)=>clean[y][x]);renderGray('noise-corrupt',(x,y)=>noisy[y][x]);renderGray('noise-median',(x,y)=>{const values=[];for(let j=-1;j<=1;j++)for(let i=-1;i<=1;i++)values.push(noisy[Math.max(0,Math.min(n-1,y+j))][Math.max(0,Math.min(n-1,x+i))]);return values.sort((a,b)=>a-b)[4];});}
const GRID=[[54,52,57,55,56,52,51],[50,49,51,50,52,53,58],[51,204,52,52,0,57,60],[48,50,51,49,53,59,63],[49,51,52,55,58,64,67],[50,54,57,60,63,67,70],[51,55,59,62,65,69,72]];
let windowMode='salt';
function windowValues(mode){const col=mode==='salt'?1:4;return GRID.slice(1,4).flatMap(row=>row.slice(col-1,col+2));}
function calculateFilters(values){const sorted=[...values].sort((a,b)=>a-b),sum=values.reduce((s,z)=>s+z,0),k=values.length,zero=values.includes(0),q=windowMode==='salt'?-1.5:1.5;
  const trim=d=>sorted.slice(d/2,k-d/2).reduce((s,z)=>s+z,0)/(k-d);
  return{sorted,sum,arithmetic:sum/k,geometric:zero?0:Math.exp(values.reduce((s,z)=>s+Math.log(z),0)/k),harmonic:zero?null:k/values.reduce((s,z)=>s+1/z,0),contra:values.reduce((s,z)=>s+z**(q+1),0)/values.reduce((s,z)=>s+z**q,0),q,median:sorted[(k-1)/2],min:sorted[0],max:sorted[k-1],midpoint:(sorted[0]+sorted[k-1])/2,trim2:trim(2),trim4:trim(4)};
}
function initWindowLab(){$('salt').onclick=()=>{windowMode='salt';updateWindow();};$('pepper').onclick=()=>{windowMode='pepper';updateWindow();};updateWindow();}
function updateWindow(){
  const col=windowMode==='salt'?1:4,values=windowValues(windowMode),r=calculateFilters(values),fmt=n=>n===null?'Undefined':n.toFixed(3);
  $('salt').setAttribute('aria-pressed',String(windowMode==='salt'));$('pepper').setAttribute('aria-pressed',String(windowMode==='pepper'));
  $('matrix').innerHTML=GRID.flatMap((row,y)=>row.map((v,x)=>'<div class="cell'+(y>=1&&y<=3&&x>=col-1&&x<=col+1?' in-window':'')+(y===2&&x===col?' centre':'')+'" aria-label="Column '+x+', row '+y+', value '+v+(y===2&&x===col?', selected centre':'')+'">'+v+'</div>')).join('');
  $('window-math').innerHTML='<h3>Centre ('+col+', 2) = '+GRID[2][col]+'</h3><p><strong>Window, row by row</strong></p><p class="sorted-list">'+[values.slice(0,3),values.slice(3,6),values.slice(6)].map(row=>'[ '+row.join(', ')+' ]').join('<br>')+'</p><p><strong>Sorted</strong></p><p class="sorted-list">[ '+r.sorted.join(', ')+' ]</p><p>Sum = '+r.sum+' · K = 9</p>';
  const rows=[['Arithmetic',r.sum+' / 9',fmt(r.arithmetic)],['Geometric','('+values.join(' × ')+')<sup>1/9</sup>',fmt(r.geometric)],['Harmonic','9 / ('+values.map(z=>'1/'+z).join(' + ')+')',fmt(r.harmonic)],['Contraharmonic, Q = '+r.q,'∑z<sup>'+ (r.q+1)+'</sup> / ∑z<sup>'+r.q+'</sup>',fmt(r.contra)],['Median','5th sorted value',fmt(r.median)],['Min / Max','First / last sorted value',r.min+' / '+r.max],['Midpoint','('+r.min+' + '+r.max+') / 2',fmt(r.midpoint)],['Alpha-trimmed, d = 2','('+r.sorted.slice(1,-1).join(' + ')+') / 7',fmt(r.trim2)],['Alpha-trimmed, d = 4','('+r.sorted.slice(2,-2).join(' + ')+') / 5',fmt(r.trim4)]];
  $('filter-results').innerHTML='<div class="table-wrap"><table><thead><tr><th>Filter</th><th>Substitution</th><th>Output</th></tr></thead><tbody>'+rows.map(row=>'<tr>'+row.map(v=>'<td>'+v+'</td>').join('')+'</tr>').join('')+'</tbody></table></div><p class="small muted">'+(windowMode==='pepper'?'The harmonic formula is undefined here because it includes 1/0. Positive Q ignores zero contributions when other positive values remain.':'The salt-like outlier 204 pushes the arithmetic mean upward. Negative Q reduces its influence; it does not guarantee the true original intensity.')+'</p><details><summary>Show the contraharmonic sums</summary><p class="small">Numerator = '+values.reduce((s,z)=>s+z**(r.q+1),0).toFixed(6)+'; denominator = '+values.reduce((s,z)=>s+z**r.q,0).toFixed(6)+'. Divide them to get '+fmt(r.contra)+'. Keep full precision until the final answer.</p></details>';
}
function renderQuiz(){
  $('quiz').innerHTML=QUESTIONS.map((q,i)=>{const a=state.answers[i],answered=Number.isInteger(a)&&a>=0&&a<q.options.length;return '<section class="quiz-card"><div class="eyebrow">QUESTION '+String(i+1).padStart(2,'0')+' / 12</div><h2 id="question-'+i+'">'+q.q+'</h2><div class="quiz-options" role="group" aria-labelledby="question-'+i+'">'+q.options.map((o,j)=>'<button data-question="'+i+'" data-option="'+j+'" '+(answered?'disabled':'')+' class="'+(answered&&j===q.correct?'correct':answered&&j===a?'wrong':'')+'">'+String.fromCharCode(65+j)+'. '+o+(answered&&j===q.correct?' · Correct answer':answered&&j===a?' · Your answer':'')+'</button>').join('')+'</div><div id="feedback-'+i+'" class="quiz-feedback" '+(!answered?'hidden':'')+' role="status">'+(answered?quizFeedback(q,a):'')+'</div></section>';}).join('');
  document.querySelectorAll('[data-question]').forEach(b=>b.onclick=()=>answerQuestion(Number(b.dataset.question),Number(b.dataset.option)));
  $('reset-quiz').onclick=()=>{state.answers={};save();renderQuiz();toast('Fresh attempt started. All 12 questions are ready.');};updateQuizScore();
}
function quizFeedback(q,a){return '<p><strong>'+(a===q.correct?'Correct.':'Review this one.')+'</strong> '+q.why+'</p><button data-go="'+q.lesson+'">Revisit lesson '+q.lesson+' →</button>';}
function answerQuestion(i,option){if(Number.isInteger(state.answers[i]))return;state.answers[i]=option;save();const card=$('feedback-'+i).closest('.quiz-card');card.querySelectorAll('[data-option]').forEach(b=>{b.disabled=true;const j=Number(b.dataset.option);if(j===QUESTIONS[i].correct){b.classList.add('correct');b.textContent+=' · Correct answer';}else if(j===option){b.classList.add('wrong');b.textContent+=' · Your answer';}});$('feedback-'+i).hidden=false;$('feedback-'+i).innerHTML=quizFeedback(QUESTIONS[i],option);updateQuizScore();}
function updateQuizScore(){const entries=QUESTIONS.map((q,i)=>({q,i,a:state.answers[i]})).filter(x=>Number.isInteger(x.a)&&x.a>=0&&x.a<x.q.options.length),correct=entries.filter(x=>x.a===x.q.correct).length;$('quiz-score').textContent=entries.length+' / 12 answered · '+correct+' correct';if(entries.length===12){const missed=[...new Set(entries.filter(x=>x.a!==x.q.correct).map(x=>x.q.lesson))];$('study-advice').textContent=missed.length?'First-attempt score: '+correct+'/12. Revisit lessons '+missed.join(', ')+', then explain each missed answer on paper before trying again.':'First-attempt score: 12/12. Now write one filter calculation and the adaptive-median steps without looking. This checks recall beyond recognition.';}else $('study-advice').textContent='Complete the test to see which lessons to revisit.';}
function timerTick(){const remaining=state.timerEnd?Math.max(0,state.timerEnd-Date.now()):state.timerRemaining,sec=Math.ceil(remaining/1000);$('timer-display').value=String(Math.floor(sec/60)).padStart(2,'0')+':'+String(sec%60).padStart(2,'0');$('timer-toggle').textContent=state.timerEnd?'Pause study timer':remaining===7200000?'Start 120-min timer':remaining===0?'Start another 120 min':'Resume study timer';$('timer-reset').hidden=remaining===7200000&&!state.timerEnd;if(state.timerEnd&&remaining===0){state.timerEnd=null;state.timerRemaining=0;save();toast('Two hours completed. Review your missed questions and take a short break.');}}
$('timer-toggle').onclick=()=>{if(state.timerEnd){state.timerRemaining=Math.max(0,state.timerEnd-Date.now());state.timerEnd=null;}else{if(state.timerRemaining<=0)state.timerRemaining=7200000;state.timerEnd=Date.now()+state.timerRemaining;}save();timerTick();};
$('timer-reset').onclick=()=>{state.timerEnd=null;state.timerRemaining=7200000;save();timerTick();};
const compactMedia=matchMedia('(max-width:1200px)'),mobileMedia=matchMedia('(max-width:850px)');
const sessionCard=document.querySelector('.session-card');
function arrangeSession(){if(compactMedia.matches)$('mobile-session').append(sessionCard);else document.querySelector('.study-aside').prepend(sessionCard);$('sidebar').inert=mobileMedia.matches&&!$('sidebar').classList.contains('open');}
compactMedia.addEventListener('change',arrangeSession);mobileMedia.addEventListener('change',arrangeSession);
applyReading();arrangeSession();navigateFromHash();timerTick();setInterval(timerTick,1000);
if(!storageOK){document.querySelector('.sidebar-footer').textContent='Progress is available for this session; browser storage is unavailable.';}
