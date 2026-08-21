(function(){'use strict';const searchInput=document.getElementById('search-input');const searchForm=document.getElementById('search-form');const resultsList=document.getElementById('results-list');const resultsTitle=document.getElementById('results-title');const resultsCount=document.getElementById('results-count');const typeFilters=document.querySelectorAll('.filter-tag');const loadMoreBtn=document.getElementById('load-more');const section=document.querySelector('.search-results-section');const basePath=section?(section.dataset.basePath||''):'';const noResultsTemplate=section?(section.dataset.noResults||'No results for “{query}”.'):'No results for “{query}”.';const resultsCountTemplate=section?(section.dataset.resultsCount||'{count} results'):'{count} results';const emptyMessage=section?(section.dataset.emptyMessage||'Enter keywords or select a type to start searching.'):'Enter keywords or select a type to start searching.';const loadingMessage=section?(section.dataset.loading||'Loading search index…'):'Loading search index…';const indexErrorMessage=section?(section.dataset.indexError||'Failed to load the search index.'):'Failed to load the search index.';const retryLabel=section?(section.dataset.retry||'Retry'):'Retry';let searchData={entries:[],index:{}};let activeType='all';let activeDomain='';const domainFilter=document.getElementById('domain-filter');let currentQuery='';let currentResults=[];let displayedCount=0;const PAGE_SIZE=20;const DEBOUNCE_MS=120;let debounceTimer=null;function tokenize(text){if(!text)return[];const tokens=[];const parts=text.toLowerCase().match(/[a-z0-9]+|[\u4e00-\u9fff\uac00-\ud7af]+/g)||[];for(const part of parts){if(/^[a-z0-9]+$/.test(part)){tokens.push(part);}else{const chars=Array.from(part);for(const ch of chars)tokens.push(ch);for(let i=0;i<chars.length-1;i++){tokens.push(chars[i]+chars[i+1]);}}}
return tokens;}
function uniqueTokens(text){const tokens=tokenize(text);const seen=new Set();const out=[];for(const t of tokens){if(!seen.has(t)){seen.add(t);out.push(t);}}
return out;}
async function loadIndex(){if(!resultsList)return;resultsList.innerHTML=`<div class="loading-state">${escapeHtml(loadingMessage)}</div>`;try{const res=await fetch(basePath+'/data/search-index.json');if(!res.ok)throw new Error('Failed to load search index');searchData=await res.json();if(!searchData.entries)searchData.entries=[];if(!searchData.index)searchData.index={};init();}catch(err){console.error(err);resultsList.innerHTML='';const box=document.createElement('div');box.className='empty-state search-index-error';const msg=document.createElement('span');msg.textContent=indexErrorMessage;const retry=document.createElement('button');retry.type='button';retry.className='btn btn-secondary search-index-retry';retry.textContent=retryLabel;retry.addEventListener('click',()=>loadIndex());box.appendChild(msg);box.appendChild(retry);resultsList.appendChild(box);}}
function findCandidates(qTokens){const counts=new Map();for(const t of qTokens){const hits=searchData.index[t];if(!hits)continue;for(const idx of hits){counts.set(idx,(counts.get(idx)||0)+1);}}
return counts;}
function scoreEntry(e,q,qTokens,candidateMatchCount){let score=0;let strongMatches=0;const name=(e.name||'').toLowerCase();const nameEn=(e.name_en||'').toLowerCase();const summary=(e.summary||'').toLowerCase();const tags=(e.tags||[]).map(t=>String(t).toLowerCase());const eid=(e.id||'').toLowerCase();const type=(e.type||'').toLowerCase();if(q){if(name===q){score+=600;strongMatches+=2;}
else if(name.startsWith(q)){score+=300;strongMatches++;}
else if(nameEn===q){score+=500;strongMatches+=2;}
else if(nameEn.startsWith(q)){score+=250;strongMatches++;}
else if(eid===q){score+=200;strongMatches++;}
else if(name.includes(q)){score+=120;strongMatches++;}
else if(nameEn.includes(q)){score+=100;strongMatches++;}
else if(tags.some(t=>t===q)){score+=90;strongMatches++;}
else if(eid.includes(q)){score+=60;}
else if(tags.some(t=>t.includes(q))){score+=50;}
else if(summary.includes(q)){score+=40;}}
for(const t of qTokens){if(t.length===0)continue;const isLatin=/^[a-z0-9]+$/.test(t);const WORD_RE=/[^a-z0-9\u4e00-\u9fff\uac00-\ud7af]+/;const inName=name.split(WORD_RE).includes(t)||name.includes(t);const inNameEn=nameEn.split(WORD_RE).includes(t)||nameEn.includes(t);const inId=eid.split(/[^a-z0-9_]+/).includes(t)||eid.includes(t);const inSummary=summary.includes(t);const inTags=tags.some(tg=>tg.includes(t));const inType=type.includes(t);const inDomain=e.domains&&e.domains.some(d=>d.toLowerCase().includes(t));if(isLatin){const whole=inName||inNameEn||inId||inType||inDomain||tags.some(tg=>tg.split(WORD_RE).includes(t))||summary.split(WORD_RE).includes(t);if(whole){if(inName){score+=20;strongMatches++;}
else if(inNameEn){score+=16;strongMatches++;}
else if(inId){score+=10;strongMatches++;}
else if(inType){score+=8;strongMatches++;}
else if(inDomain){score+=6;strongMatches++;}
else if(inTags){score+=5;strongMatches++;}
else if(inSummary){score+=4;}}else{score-=8;}}else{if(inName){score+=18;strongMatches++;}
else if(inNameEn){score+=14;strongMatches++;}
else if(inId){score+=8;strongMatches++;}
else if(inType){score+=6;strongMatches++;}
else if(inDomain){score+=4;strongMatches++;}
else if(inTags){score+=4;strongMatches++;}
else if(inSummary){score+=3;}}}
score+=candidateMatchCount*15;if(summary.length>20)score+=2;const primaryName=name||nameEn||eid;if(primaryName.length>80)score-=10;if(primaryName.length>140)score-=15;if(strongMatches===0&&!(q&&(summary.includes(q)||tags.some(t=>t.includes(q)))))return 0;return score;}
function search(query,typeFilter){const q=query.trim().toLowerCase();if(!q){let list=searchData.entries;if(typeFilter!=='all')list=list.filter(e=>e.type===typeFilter);if(activeDomain)list=list.filter(e=>(e.domains||[]).includes(activeDomain));return list.slice().sort((a,b)=>(a.name||a.id).localeCompare(b.name||b.id));}
const qTokens=uniqueTokens(q);const candidates=findCandidates(qTokens);const scores=[];for(let idx=0;idx<searchData.entries.length;idx++){const e=searchData.entries[idx];if(!e)continue;if(typeFilter!=='all'&&e.type!==typeFilter)continue;if(activeDomain&&!(e.domains||[]).includes(activeDomain))continue;const score=scoreEntry(e,q,qTokens,candidates.get(idx)||0);if(score>0)scores.push({entry:e,score});}
scores.sort((a,b)=>b.score-a.score);return scores.map(s=>s.entry);}
function formatCount(count){return resultsCountTemplate.replace('{count}',count);}
function updateLoadMore(){if(!loadMoreBtn)return;if(displayedCount<currentResults.length){loadMoreBtn.classList.remove('hidden');}else{loadMoreBtn.classList.add('hidden');}}
function highlight(text,q){if(!text||!q)return escapeHtml(text);const tokens=uniqueTokens(q).filter(t=>t.length>=2||!/^[a-z0-9]$/.test(t));if(tokens.length===0)return escapeHtml(text);tokens.sort((a,b)=>b.length-a.length);const pattern=tokens.map(escapeRegex).join('|');const re=new RegExp('('+pattern+')','gi');return escapeHtml(text).replace(re,'<mark>$1</mark>');}
function escapeRegex(s){return s.replace(/[.*+?^${}()|[\]\\]/g,'\\$&');}
function renderResults(results,query,append=false){if(!append){if(resultsList)resultsList.innerHTML='';displayedCount=0;currentResults=results;currentQuery=query;}
if(resultsCount)resultsCount.textContent=formatCount(results.length);if(results.length===0){if(resultsList){resultsList.innerHTML=`<div class="empty-state">${escapeHtml(noResultsTemplate.replace('{query}', query))}</div>`;}
updateLoadMore();return;}
const page=results.slice(displayedCount,displayedCount+PAGE_SIZE);displayedCount+=page.length;const q=query.trim().toLowerCase();for(const e of page){const item=document.createElement('a');item.className='result-item';item.href=basePath+'/'+e.url;const metaTags=(e.domain_labels||e.domains||[]).join(', ');const excerpt=(e.summary||'').slice(0,200);const hasMore=(e.summary||'').length>200;const nameHtml=highlight(e.name,q);const nameEnHtml=e.name_en&&e.name_en!==e.name?highlight(e.name_en,q):'';item.innerHTML=`
        <div class="result-meta">
          <span class="tag">${escapeHtml(e.type_label || e.type)}</span>
          <span>${escapeHtml(metaTags)}</span>
        </div>
        <h3>${nameHtml}${nameEnHtml ? ' <small>' + nameEnHtml + '</small>' : ''}</h3>
        <p>${highlight(excerpt, q)}${hasMore ? '…' : ''}</p>
      `;if(resultsList)resultsList.appendChild(item);}
updateLoadMore();}
function escapeHtml(text){const div=document.createElement('div');div.textContent=text;return div.innerHTML;}
const askRoot=document.getElementById('search-ask-root');let askModuleQuery=null;let askModuleKind=null;let askModuleInstance=null;function isQuestionLike(text){const t=text.trim();if(!t)return false;if(/[？?]\s*$/.test(t))return true;if(/^(什么|怎麼|怎么|怎样|怎樣|如何|为什么|為什麼|为何|為何|哪些|哪个|哪個|区别|區別|能不能|可不可以|可以|是不是|是)/.test(t))return true;return/^(what|how|why|which|compare|comparison|difference|differentiate|vs)\b/i.test(t);}
function queryHash(q){let h=0;const s=q.trim().toLowerCase();for(let i=0;i<s.length;i++)h=(h*31+s.charCodeAt(i))>>>0;return h.toString(36);}
function disposeAskModule(){if(askModuleInstance){askModuleInstance.unmount();askModuleInstance=null;}}
function mountAskInline(q,extra){if(!askRoot||!window.KGAsk)return;disposeAskModule();askRoot.innerHTML='';askModuleInstance=window.KGAsk.mount(askRoot,Object.assign({mode:'inline',historyScope:queryHash(q),onConfigSaved:()=>{if(askModuleQuery===q)renderAskTrigger(q);},},extra||{}))||null;askModuleQuery=q;askModuleKind='mounted';}
function renderAskHint(q){disposeAskModule();askRoot.innerHTML='';const hint=document.createElement('div');hint.className='search-ask-hint';const text=document.createElement('span');text.textContent=(askRoot.dataset.askSetupHint||'');const gear=document.createElement('button');gear.type='button';gear.className='search-ask-gear';gear.textContent='⚙';gear.title=askRoot.dataset.settings||'Settings';gear.setAttribute('aria-label',askRoot.dataset.settings||'Settings');gear.addEventListener('click',()=>{mountAskInline(q,{openSettings:true,prefill:q});});hint.appendChild(text);hint.appendChild(gear);askRoot.appendChild(hint);askModuleQuery=q;askModuleKind='hint';}
function renderAskTrigger(q){disposeAskModule();askRoot.innerHTML='';const btn=document.createElement('button');btn.type='button';btn.className='search-ask-trigger';btn.textContent=askRoot.dataset.askWithAi||'✨ Answer with AI';btn.addEventListener('click',()=>{mountAskInline(q,{initialQuestion:q});});askRoot.appendChild(btn);askModuleQuery=q;askModuleKind='trigger';}
function updateAskModule(query,allowAutoAsk){if(!askRoot)return;const q=query.trim();if(!q){disposeAskModule();askRoot.innerHTML='';askModuleQuery=null;askModuleKind=null;return;}
const hasKey=!!(localStorage.getItem('kg_ask_api_key')||'').trim();if(askModuleQuery===q){if(allowAutoAsk&&askModuleKind==='trigger'&&hasKey&&isQuestionLike(q)){mountAskInline(q,{initialQuestion:q});}
return;}
if(!hasKey){renderAskHint(q);}else if(isQuestionLike(q)&&allowAutoAsk){mountAskInline(q,{initialQuestion:q});}else{renderAskTrigger(q);}}
function performSearch(append=false,allowAutoAsk=false){const query=searchInput?searchInput.value:'';const results=search(query,activeType);renderResults(results,query,append);if(!append)updateAskModule(query,allowAutoAsk);}
function setUrlQuery(q){const url=new URL(window.location.href);if(q){url.searchParams.set('q',q);}else{url.searchParams.delete('q');}
window.history.replaceState({},'',url);}
function init(){const params=new URLSearchParams(window.location.search);const q=params.get('q')||'';const typeParam=params.get('type')||'';const domainParam=params.get('domain')||'';if(searchInput)searchInput.value=q;if(typeParam){activeType=typeParam;typeFilters.forEach(b=>b.classList.toggle('active',b.dataset.type===typeParam));}
if(domainParam){activeDomain=domainParam;if(domainFilter)domainFilter.value=domainParam;}
if(q||typeParam||domainParam){if(resultsTitle){let title=q?`“${q}”`:'';if(domainParam&&domainFilter&&domainFilter.selectedOptions.length){title=(title?title+' · ':'')+domainFilter.selectedOptions[0].textContent;}
resultsTitle.textContent=title;}
performSearch(false,true);}else{if(resultsTitle)resultsTitle.textContent='';if(resultsList)resultsList.innerHTML=`<div class="empty-state">${escapeHtml(emptyMessage)}</div>`;if(resultsCount)resultsCount.textContent=formatCount(0);updateLoadMore();}
if(searchInput){searchInput.addEventListener('input',()=>{clearTimeout(debounceTimer);debounceTimer=setTimeout(()=>{const q=searchInput.value;setUrlQuery(q);if(resultsTitle)resultsTitle.textContent=q?`“${q}”`:'';performSearch();},DEBOUNCE_MS);});}
if(searchForm){searchForm.addEventListener('submit',(e)=>{e.preventDefault();const q=searchInput?searchInput.value:'';setUrlQuery(q);if(resultsTitle)resultsTitle.textContent=q?`“${q}”`:'';performSearch(false,true);if(searchInput)searchInput.blur();});}
typeFilters.forEach(btn=>{btn.addEventListener('click',()=>{typeFilters.forEach(b=>b.classList.remove('active'));btn.classList.add('active');activeType=btn.dataset.type;performSearch();});});if(domainFilter){domainFilter.addEventListener('change',()=>{activeDomain=domainFilter.value;performSearch();});}
const loadMoreButton=loadMoreBtn?loadMoreBtn.querySelector('button'):null;if(loadMoreButton){loadMoreButton.addEventListener('click',()=>{renderResults(currentResults,currentQuery,true);});}}
window.KGSearch={setData(data){searchData=data;},search,scoreEntry,uniqueTokens,findCandidates,isQuestionLike,updateAskModule,};loadIndex();})();