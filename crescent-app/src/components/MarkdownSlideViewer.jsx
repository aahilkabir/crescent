import React, { useState, useEffect, useRef } from 'react';
import { 
  SwappingCups, 
  SumAccumulator, 
  TernaryGate, 
  LoopTracer, 
  ArrayMath, 
  RecursionStack, 
  PointerVisualizer, 
  QuizCard, 
  CodeBlank, 
  TodoCard,
  StringGarland
} from './InteractiveWidgets';
import { ChevronLeft, ChevronRight, Maximize2, X, RefreshCw, ArrowLeft, ArrowRight, Play, RotateCcw } from 'lucide-react';

export default function MarkdownSlideViewer({ filePath, title, onBack }) {
  const [slides, setSlides] = useState([]);
  const [slideIdx, setSlideIdx] = useState(0);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [isFullscreen, setIsFullscreen] = useState(false);

  const touchStartX = useRef(null);

  // Parse custom YAML-like metadata and Markdown content
  const parseSlides = (rawText) => {
    // Split slides by triple-dashes
    const rawSlides = rawText.split(/^---$/m);
    const parsed = [];

    rawSlides.forEach(slideStr => {
      const trimmed = slideStr.trim();
      if (!trimmed) return;

      const lines = trimmed.split('\n');
      const meta = {};
      const bodyLines = [];
      let parsingCodeKey = null;

      lines.forEach(line => {
        const trimmedLine = line.trim();

        // If currently parsing a multiline code block
        if (parsingCodeKey) {
          // Check if line indicates a new meta property
          const metaMatch = trimmedLine.match(/^([a-zA-Z0-9_-]+)\s*:\s*(.*)$/);
          if (metaMatch && !line.startsWith(' ') && !line.startsWith('\t')) {
            parsingCodeKey = null;
          } else {
            meta[parsingCodeKey] += line + '\n';
            return;
          }
        }

        const metaMatch = trimmedLine.match(/^([a-zA-Z0-9_-]+)\s*:\s*(.*)$/);
        
        // Match frontmatter keys at top of the slide
        if (metaMatch && bodyLines.length === 0) {
          const key = metaMatch[1];
          let val = metaMatch[2].trim();

          if (val === '|') {
            meta[key] = '';
            parsingCodeKey = key;
          } else {
            // Strip quotes
            if ((val.startsWith('"') && val.endsWith('"')) || (val.startsWith("'") && val.endsWith("'"))) {
              val = val.substring(1, val.length - 1);
            }
            meta[key] = val;
          }
        } else {
          bodyLines.push(line);
        }
      });

      // Simple Markdown list parser inside body
      const bodyText = bodyLines.join('\n').trim();
      parsed.push({
        meta,
        body: bodyText
      });
    });

    return parsed;
  };

  // Fetch slide markdown from public folder
  useEffect(() => {
    setLoading(true);
    setError('');
    fetch(filePath)
      .then(res => {
        if (!res.ok) throw new Error(`Failed to load slide file: ${res.statusText}`);
        return res.text();
      })
      .then(text => {
        const parsed = parseSlides(text);
        setSlides(parsed);
        setSlideIdx(0);
        setLoading(false);
      })
      .catch(err => {
        console.error(err);
        setError(err.message);
        setLoading(false);
      });
  }, [filePath]);

  // Keyboard navigation controller
  useEffect(() => {
    if (slides.length === 0) return;
    
    const handleKeyDown = (e) => {
      if (['ArrowRight', 'ArrowDown', 'PageDown', ' '].includes(e.key)) {
        e.preventDefault();
        nextSlide();
      } else if (['ArrowLeft', 'ArrowUp', 'PageUp'].includes(e.key)) {
        e.preventDefault();
        prevSlide();
      } else if (e.key === 'Home') {
        e.preventDefault();
        setSlideIdx(0);
      } else if (e.key === 'End') {
        e.preventDefault();
        setSlideIdx(slides.length - 1);
      } else if (e.key.toLowerCase() === 'f') {
        toggleFullscreen();
      }
    };

    document.addEventListener('keydown', handleKeyDown);
    return () => document.removeEventListener('keydown', handleKeyDown);
  }, [slides, slideIdx]);

  const nextSlide = () => {
    if (slideIdx < slides.length - 1) setSlideIdx(prev => prev + 1);
  };

  const prevSlide = () => {
    if (slideIdx > 0) setSlideIdx(prev => prev - 1);
  };

  // Fullscreen toggler
  const toggleFullscreen = () => {
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen().then(() => {
        setIsFullscreen(true);
      }).catch(err => {
        console.error(err);
      });
    } else {
      document.exitFullscreen().then(() => {
        setIsFullscreen(false);
      });
    }
  };

  // Touch gesture handlers
  const handleTouchStart = (e) => {
    touchStartX.current = e.touches[0].clientX;
  };

  const handleTouchEnd = (e) => {
    if (touchStartX.current === null) return;
    const dx = e.changedTouches[0].clientX - touchStartX.current;
    if (Math.abs(dx) > 50) {
      if (dx < 0) nextSlide();
      else prevSlide();
    }
    touchStartX.current = null;
  };

  // Helper to convert simple Markdown text into HTML tags
  const renderMarkdown = (text) => {
    if (!text) return '';
    let parsed = text;
    
    // Bold: **text**
    parsed = parsed.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
    
    // Code blocks: `code`
    parsed = parsed.replace(/`(.*?)`/g, '<code class="mono" style="color:var(--accent); background:rgba(255,255,255,0.05); padding:0.1rem 0.3rem; border-radius:4px;">$1</code>');
    
    // High-impact quotes: > text
    parsed = parsed.replace(/^>\s*(.*)$/gm, '<div style="padding: 1rem 1.5rem; background: var(--accent-soft); border-left: 4px solid var(--accent); border-radius: 0 8px 8px 0; margin-top: 1rem; color: var(--hi);">$1</div>');

    // Bullet lists: - text
    const lines = parsed.split('\n');
    let insideList = false;
    const listParsed = [];

    lines.forEach(line => {
      const trimmed = line.trim();
      if (trimmed.startsWith('-')) {
        if (!insideList) {
          listParsed.push('<ul class="simple-list">');
          insideList = true;
        }
        listParsed.push(`<li>${trimmed.substring(1).trim()}</li>`);
      } else {
        if (insideList) {
          listParsed.push('</ul>');
          insideList = false;
        }
        listParsed.push(line);
      }
    });
    if (insideList) listParsed.push('</ul>');
    
    return listParsed.join('\n');
  };

  // Parse YAML-like bullet properties
  const parseYamlBullets = (bulletsText) => {
    if (!bulletsText) return [];
    const lines = bulletsText.split('\n');
    const items = [];
    let currentItem = null;

    lines.forEach(line => {
      const trimmed = line.trim();
      if (trimmed.startsWith('-')) {
        if (currentItem) items.push(currentItem);
        currentItem = { bold: '', text: '' };
        const boldMatch = trimmed.match(/^-\s*bold\s*:\s*(.*)$/i);
        if (boldMatch) {
          currentItem.bold = boldMatch[1];
        }
      } else if (trimmed.startsWith('text:')) {
        if (currentItem) currentItem.text = trimmed.substring(5).trim();
      } else if (currentItem && trimmed.startsWith('bold:')) {
        currentItem.bold = trimmed.substring(5).trim();
      }
    });
    if (currentItem) items.push(currentItem);
    return items;
  };

  // Parse YAML-like facts grid properties
  const parseYamlFacts = (factsText) => {
    if (!factsText) return [];
    const lines = factsText.split('\n');
    const items = [];
    let currentItem = null;

    lines.forEach(line => {
      const trimmed = line.trim();
      if (trimmed.startsWith('-')) {
        if (currentItem) items.push(currentItem);
        currentItem = { num: '', title: '', desc: '' };
        const numMatch = trimmed.match(/^-\s*num\s*:\s*(.*)$/i);
        if (numMatch) currentItem.num = numMatch[1];
      } else if (trimmed.startsWith('title:')) {
        if (currentItem) currentItem.title = trimmed.substring(6).trim();
      } else if (trimmed.startsWith('desc:')) {
        if (currentItem) currentItem.desc = trimmed.substring(5).trim();
      } else if (currentItem && trimmed.startsWith('num:')) {
        currentItem.num = trimmed.substring(4).trim();
      }
    });
    if (currentItem) items.push(currentItem);
    return items;
  };

  // Parse YAML-like quiz options properties
  const parseYamlOptions = (optionsText) => {
    if (!optionsText) return [];
    const lines = optionsText.split('\n');
    const items = [];
    let currentItem = null;

    lines.forEach(line => {
      const trimmed = line.trim();
      if (trimmed.startsWith('-')) {
        if (currentItem) items.push(currentItem);
        currentItem = { text: '', correct: false, feedback: '' };
        const textMatch = trimmed.match(/^-\s*text\s*:\s*(.*)$/i);
        if (textMatch) currentItem.text = textMatch[1];
      } else if (trimmed.startsWith('correct:')) {
        if (currentItem) currentItem.correct = trimmed.substring(8).trim() === 'true';
      } else if (trimmed.startsWith('feedback:')) {
        if (currentItem) currentItem.feedback = trimmed.substring(9).trim();
      } else if (currentItem && trimmed.startsWith('text:')) {
        currentItem.text = trimmed.substring(5).trim();
      }
    });
    if (currentItem) items.push(currentItem);
    return items;
  };

  if (loading) {
    return (
      <div style={{ flex: '1', display: 'flex', alignItems: 'center', justifyContent: 'center', background: 'var(--black)', color: 'var(--mid)' }}>
        <RefreshCw size={24} style={{ animation: 'spin 1s infinite linear', marginRight: '0.8rem' }} /> Loading presentation slides...
      </div>
    );
  }

  if (error) {
    return (
      <div style={{ flex: '1', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', background: 'var(--black)', color: 'var(--rose)', padding: '2rem' }}>
        <h3>Error Loading Slides</h3>
        <p style={{ marginTop: '0.5rem' }}>{error}</p>
        <button onClick={onBack} className="widget-btn-secondary" style={{ marginTop: '1.5rem' }}>Go Back</button>
      </div>
    );
  }

  const currentSlide = slides[slideIdx] || { meta: {}, body: '' };
  const { meta, body } = currentSlide;
  const layout = meta.layout || 'study';

  return (
    <div className="app-root-container" style={{ display: 'flex', flexDirection: 'column', height: '100%', background: 'var(--black)' }}>
      {/* HEADER NAV HUD */}
      <header style={{
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
        padding: '1.2rem 3vw',
        borderBottom: '1px solid var(--border)',
        background: 'var(--surface)',
        zIndex: 40
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '0.8rem' }}>
          <button onClick={onBack} className="widget-btn-secondary" style={{ display: 'flex', alignItems: 'center', gap: '0.4rem' }}>
            <ChevronLeft size={16} /> Back to Courses
          </button>
          <span style={{ fontSize: '1.1rem', fontWeight: 'bold', color: 'var(--hi)' }}>{title}</span>
        </div>
        
        <div style={{ display: 'flex', alignItems: 'center', gap: '1rem' }}>
          <span style={{ fontSize: '0.9rem', fontFamily: 'var(--mono)', color: 'var(--low)' }}>
            Slide {slideIdx + 1} / {slides.length}
          </span>
          <button onClick={toggleFullscreen} className="widget-btn-secondary" style={{ padding: '0.4rem' }}>
            <Maximize2 size={16} />
          </button>
        </div>
      </header>

      {/* SLIDE PORTAL VIEWPORT */}
      <div 
        style={{ flex: '1', display: 'flex', overflow: 'hidden', position: 'relative' }} 
        onTouchStart={handleTouchStart} 
        onTouchEnd={handleTouchEnd}
      >
        <main style={{ flex: '1', display: 'flex', flexDirection: 'column', overflow: 'hidden' }}>
          <div className="slide-viewport">
            
            {/* RENDER TITLE LAYOUT */}
            {layout === 'title' && (
              <div style={{ animation: 'fadeIn 0.5s' }}>
                <div className="eyebrow">{meta.eyebrow}</div>
                <h2 className="title" style={{ fontSize: 'clamp(3.5rem, 8vw, 6.2rem)' }}>{meta.title}</h2>
                {meta.subtitle && (
                  <div style={{ fontSize: 'clamp(1.8rem, 3.5vw, 3rem)', color: 'var(--accent)', fontFamily: 'var(--sans)', marginTop: '0.5rem', fontWeight: '700' }}>
                    {meta.subtitle}
                  </div>
                )}
                {meta.lede && <p className="lede" style={{ marginTop: '2rem' }}>{meta.lede}</p>}
              </div>
            )}

            {/* RENDER AGENDA LAYOUT */}
            {layout === 'agenda' && (
              <div style={{ animation: 'fadeIn 0.5s' }}>
                <div className="eyebrow">{meta.eyebrow}</div>
                <h2 className="title">{meta.title}</h2>
                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: '2rem', marginTop: '2.5rem' }}>
                  {parseYamlFacts(meta.facts).map((f, idx) => (
                    <div key={idx} style={{ background: 'var(--surface)', padding: '1.5rem', borderRadius: '10px', border: '1px solid var(--border)' }}>
                      <div style={{ fontSize: '1.6rem', fontFamily: 'var(--mono)', color: 'var(--accent)', fontWeight: 'bold', marginBottom: '0.4rem' }}>
                        {f.num}
                      </div>
                      <h4 style={{ fontSize: '1.25rem', color: 'var(--hi)', fontWeight: '600', marginBottom: '0.4rem' }}>{f.title}</h4>
                      <p style={{ fontSize: '1rem', color: 'var(--low)', lineHeight: '1.5' }}>{f.desc}</p>
                    </div>
                  ))}
                </div>
              </div>
            )}

            {/* RENDER BULLET STUDY LAYOUT */}
            {layout === 'bullets' && (
              <div style={{ animation: 'fadeIn 0.5s' }}>
                <div className="eyebrow">{meta.eyebrow}</div>
                <h2 className="title">{meta.title}</h2>
                <ul className="simple-list" style={{ marginTop: '2.5rem' }}>
                  {parseYamlBullets(meta.bullets).map((b, idx) => (
                    <li key={idx}>
                      <strong>{b.bold}</strong> {b.text}
                    </li>
                  ))}
                </ul>
              </div>
            )}

            {/* RENDER DYNAMIC 2-COLUMN HERO LAYOUT */}
            {layout === 'hero' && (
              <div className="split" style={{ animation: 'fadeIn 0.5s', alignItems: 'center', gap: '4vw' }}>
                <div style={{ flex: '1.1' }}>
                  <div className="eyebrow">{meta.eyebrow}</div>
                  <h2 className="title" style={{ marginBottom: '1.5rem' }}>{meta.title}</h2>
                  <p className="body-copy" style={{ fontSize: '1.35rem', lineHeight: '1.6', marginBottom: '2rem' }}>{meta.lede}</p>
                  <div style={{
                    padding: '1.8rem',
                    background: 'var(--accent-soft)',
                    borderLeft: '4px solid var(--accent)',
                    borderRadius: '0 8px 8px 0',
                    fontSize: '1.25rem',
                    color: 'var(--hi)',
                    lineHeight: '1.6',
                    fontWeight: '300'
                  }}>
                    {meta.highlight}
                  </div>
                </div>
                <div style={{
                  flex: '0.9',
                  height: '380px',
                  borderRadius: '12px',
                  border: '1px solid var(--border-hi)',
                  backgroundSize: 'cover',
                  backgroundPosition: 'center',
                  boxShadow: '0 20px 45px rgba(0,0,0,0.55)',
                  backgroundImage: `url('/${meta.image ? meta.image.replace('../../assets/', '') : 'samayal_chef.jpg'}')`
                }}></div>
              </div>
            )}

            {/* RENDER STUDY LAYOUT */}
            {layout === 'study' && (
              <div style={{ animation: 'fadeIn 0.5s' }}>
                <div className="eyebrow">{meta.eyebrow}</div>
                <h2 className="title" style={{ marginBottom: '1.5rem' }}>{meta.title}</h2>
                <div dangerouslySetInnerHTML={{ __html: renderMarkdown(body) }} />
              </div>
            )}

            {/* RENDER TABLE LAYOUT */}
            {layout === 'table' && (
              <div style={{ animation: 'fadeIn 0.5s' }}>
                <div className="eyebrow">{meta.eyebrow}</div>
                <h2 className="title" style={{ marginBottom: '2rem' }}>{meta.title}</h2>
                <div style={{ overflowX: 'auto', border: '1px solid var(--border)', borderRadius: '12px', background: 'var(--surface)' }}>
                  <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left', fontFamily: 'var(--sans)' }}>
                    <thead>
                      <tr style={{ borderBottom: '2px solid var(--border-hi)', background: 'var(--surface2)' }}>
                        {meta.headers && meta.headers.split(',').map((h, i) => (
                          <th key={i} style={{ padding: '1.2rem 1.8rem', fontSize: '1.1rem', fontWeight: 'bold', color: 'var(--accent)' }}>{h.trim()}</th>
                        ))}
                      </tr>
                    </thead>
                    <tbody>
                      {/* Simple parse for rows data structure */}
                      {meta.rows && meta.rows.split('\n').filter(r => r.trim()).map((row, i) => {
                        const cells = row.replace(/[\[\]]/g, '').split(',');
                        return (
                          <tr key={i} style={{ borderBottom: '1px solid var(--border)', transition: 'background 0.3s' }} className="table-row-hover">
                            {cells.map((cell, j) => (
                              <td key={j} style={{ padding: '1.2rem 1.8rem', fontSize: '1.1rem', color: j === 0 ? 'var(--hi)' : 'var(--mid)' }}>{cell.trim()}</td>
                            ))}
                          </tr>
                        );
                      })}
                    </tbody>
                  </table>
                </div>
              </div>
            )}

            {/* RENDER STRUCTURE ANATOMY LAYOUT */}
            {layout === 'structure' && (
              <div style={{ animation: 'fadeIn 0.5s' }}>
                <div className="eyebrow">{meta.eyebrow}</div>
                <h2 className="title" style={{ marginBottom: '1.5rem' }}>{meta.title}</h2>
                <div className="split" style={{ alignItems: 'stretch', gap: '3vw' }}>
                  <pre className="code" style={{ flex: '1.3', fontSize: '1.1rem', padding: '2rem', whiteSpace: 'pre-wrap' }}>
                    {meta.code}
                  </pre>
                  <div style={{ flex: '0.8', display: 'flex', flexDirection: 'column', gap: '0.8rem', justifyContent: 'center' }}>
                    <span className="bank-title" style={{ marginBottom: '0.4rem' }}>Anatomy Sections</span>
                    {meta.sections && meta.sections.split('\n').filter(s => s.trim()).map((sect, idx) => (
                      <div key={idx} style={{
                        padding: '0.9rem 1.2rem',
                        background: 'var(--surface)',
                        border: '1px solid var(--border)',
                        borderRadius: '8px',
                        fontSize: '1.05rem',
                        display: 'flex',
                        alignItems: 'center',
                        gap: '0.8rem'
                      }}>
                        <span style={{ fontFamily: 'var(--mono)', color: 'var(--accent)', fontWeight: 'bold' }}>0{idx + 1}</span>
                        <span style={{ color: 'var(--mid)' }}>{sect.replace(/^-\s*/, '')}</span>
                      </div>
                    ))}
                  </div>
                </div>
              </div>
            )}

            {/* RENDER CODE VIEW LAYOUT */}
            {layout === 'code' && (
              <div style={{ animation: 'fadeIn 0.5s' }}>
                <div className="eyebrow">{meta.eyebrow}</div>
                <h2 className="title">{meta.title}</h2>
                {meta.lede && <p className="lede" style={{ marginBottom: '1.5rem' }}>{meta.lede}</p>}
                <pre className="code" style={{ marginTop: '1rem', maxHeight: '55vh', fontSize: '1.15rem' }}>
                  {meta.code}
                </pre>
              </div>
            )}

            {/* RENDER QUIZ LAYOUT */}
            {layout === 'quiz' && (
              <div style={{ animation: 'fadeIn 0.5s' }}>
                <div className="eyebrow">{meta.eyebrow}</div>
                <QuizCard slideId={meta.question} question={meta.question} options={parseYamlOptions(meta.options)} />
              </div>
            )}

            {/* RENDER CODE BLANK LAYOUT */}
            {layout === 'blank' && (
              <div style={{ animation: 'fadeIn 0.5s' }}>
                <div className="eyebrow">{meta.eyebrow}</div>
                <h2 className="title" style={{ marginBottom: '1rem' }}>{meta.title}</h2>
                <p className="lede" style={{ marginBottom: '2rem' }}>{meta.lede}</p>
                <CodeBlank slideId={meta.title} code={meta.code} blankVal={meta.blankVal} />
              </div>
            )}

            {/* RENDER PRACTICE TODO LAYOUT */}
            {layout === 'todo' && (
              <div style={{ animation: 'fadeIn 0.5s' }}>
                <div className="eyebrow">{meta.eyebrow}</div>
                <TodoCard title={meta.title} desc={meta.desc} hint={meta.hint} />
              </div>
            )}

            {/* RENDER STATEFUL CONCEPTS SIMULATORS */}
            {layout === 'trace' && (
              <div style={{ animation: 'fadeIn 0.5s' }}>
                <div className="eyebrow">{meta.eyebrow}</div>
                <h2 className="title">{meta.title}</h2>
                {meta.lede && <p className="lede" style={{ marginBottom: '1.5rem' }}>{meta.lede}</p>}
                
                {meta.type === 'swapping' && <SwappingCups />}
                {meta.type === 'accumulator' && <SumAccumulator />}
                {meta.type === 'ternary' && <TernaryGate />}
                {meta.type === 'loopTracer' && <LoopTracer />}
                {meta.type === 'arrayMath' && <ArrayMath />}
                {meta.type === 'stringTracer' && <StringGarland />}
                {meta.type === 'recursion' && <RecursionStack />}
                {meta.type === 'pointers' && <PointerVisualizer />}
              </div>
            )}

          </div>

          {/* BOTTOM PERSISTENT NAV FOOTER */}
          <footer style={{
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'center',
            padding: '1.5rem 3vw',
            borderTop: '1px solid var(--border)',
            background: 'var(--surface)',
            zIndex: 20
          }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
              <button 
                onClick={prevSlide} 
                disabled={slideIdx === 0}
                className="widget-btn-secondary"
                style={{ display: 'flex', alignItems: 'center', gap: '0.4rem', color: slideIdx === 0 ? 'var(--low)' : 'var(--mid)' }}
              >
                <ChevronLeft size={16} /> Prev
              </button>
              <button 
                onClick={nextSlide} 
                disabled={slideIdx === slides.length - 1}
                className="widget-btn-secondary"
                style={{ display: 'flex', alignItems: 'center', gap: '0.4rem', color: slideIdx === slides.length - 1 ? 'var(--low)' : 'var(--mid)' }}
              >
                Next <ChevronRight size={16} />
              </button>
            </div>

            <div style={{ flex: '1', margin: '0 3rem', display: 'flex', flexDirection: 'column', gap: '0.5rem' }}>
              <div style={{ height: '4px', background: 'var(--surface3)', borderRadius: '2px', overflow: 'hidden' }}>
                <div style={{
                  width: `${((slideIdx + 1) / slides.length) * 100}%`,
                  height: '100%',
                  background: 'var(--accent)',
                  boxShadow: '0 0 8px var(--accent)',
                  transition: 'width 0.3s ease'
                }}></div>
              </div>
            </div>

            <div style={{ display: 'flex', alignItems: 'center', gap: '0.8rem' }}>
              <span style={{ fontSize: '1.25rem', fontFamily: 'var(--mono)', fontWeight: 'bold', color: 'var(--accent)' }}>
                {String(slideIdx + 1).padStart(2, '0')}
              </span>
              <span style={{ color: 'var(--low)' }}>/</span>
              <span style={{ color: 'var(--low)', fontSize: '0.9rem', fontFamily: 'var(--mono)' }}>
                {String(slides.length).padStart(2, '0')}
              </span>
            </div>
          </footer>
        </main>
      </div>
    </div>
  );
}
