import React, { useState, useEffect, useRef } from 'react';
import { modules } from './data/slides';
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
} from './components/InteractiveWidgets';
import { Play, Home, ChevronRight, Menu, X, ArrowLeft, ArrowRight, Maximize2, Monitor, BookOpen, Terminal, CheckCircle2 } from 'lucide-react';

function App() {
  const [currentModuleId, setCurrentModuleId] = useState('home');
  const [slideIdx, setSlideIdx] = useState(0);
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const [isFullscreen, setIsFullscreen] = useState(false);

  const activeModule = modules.find(m => m.id === currentModuleId);
  const slides = activeModule?.slides || [];
  const currentSlide = slides[slideIdx];

  // Reference for touch gestures
  const touchStartX = useRef(null);

  // Fullscreen toggle handler
  const toggleFullscreen = () => {
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen().then(() => {
        setIsFullscreen(true);
      }).catch(err => {
        console.error("Error enabling fullscreen:", err);
      });
    } else {
      document.exitFullscreen().then(() => {
        setIsFullscreen(false);
      });
    }
  };

  // Monitor fullscreen changes (e.g. if user exits using Escape key)
  useEffect(() => {
    const handleFullscreenChange = () => {
      setIsFullscreen(!!document.fullscreenElement);
    };
    document.addEventListener('fullscreenchange', handleFullscreenChange);
    return () => document.removeEventListener('fullscreenchange', handleFullscreenChange);
  }, []);

  // Keyboard navigation controller
  useEffect(() => {
    const handleKeyDown = (e) => {
      if (currentModuleId === 'home') return;
      
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
      } else if (e.key === 'Escape') {
        setSidebarOpen(false);
      }
    };

    document.addEventListener('keydown', handleKeyDown);
    return () => document.removeEventListener('keydown', handleKeyDown);
  }, [currentModuleId, slideIdx, slides]);

  // Touch navigation swiper
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

  const nextSlide = () => {
    if (slideIdx < slides.length - 1) {
      setSlideIdx(prev => prev + 1);
    }
  };

  const prevSlide = () => {
    if (slideIdx > 0) {
      setSlideIdx(prev => prev - 1);
    }
  };

  const handleModuleSelect = (moduleId) => {
    setCurrentModuleId(moduleId);
    setSlideIdx(0);
    setSidebarOpen(false);
  };

  // Helper function to return beautiful custom titles or badges for the sidebar
  const getSlideBadge = (slide) => {
    if (slide.type === 'title') return 'Intro';
    if (slide.type === 'quiz') return 'Quiz';
    if (slide.type === 'todo') return 'Practice';
    if (slide.type === 'blank') return 'Solve';
    if (slide.type === 'code') return 'C Code';
    if (['swapping', 'accumulator', 'ternary', 'recursion', 'pointers', 'loopTracer', 'arrayMath', 'stringTracer'].includes(slide.type)) return 'Trace';
    return 'Study';
  };

  return (
    <div className="app-root-container" style={{ display: 'flex', flexDirection: 'column', height: '100%', background: 'var(--black)' }}>
      {/* HEADER HUD BAR */}
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
          {currentModuleId !== 'home' && (
            <button 
              onClick={() => setCurrentModuleId('home')} 
              style={{
                background: 'transparent',
                border: '1px solid var(--border)',
                color: 'var(--mid)',
                borderRadius: '6px',
                padding: '0.5rem 0.8rem',
                cursor: 'pointer',
                display: 'flex',
                alignItems: 'center',
                gap: '0.4rem',
                transition: 'all 0.3s'
              }}
              className="widget-btn-secondary"
            >
              <Home size={16} /> Home
            </button>
          )}
          <span style={{ fontSize: '1.2rem', fontWeight: 'bold', letterSpacing: '0.02em', background: 'linear-gradient(90deg, #ffffff, var(--accent))', WebkitBackgroundClip: 'text', WebkitTextFillColor: 'transparent' }}>
            CRESCENT CSE
          </span>
        </div>

        {currentModuleId !== 'home' && (
          <div style={{ display: 'flex', alignItems: 'center', gap: '1rem' }}>
            <span style={{ fontSize: '1rem', fontWeight: '500', color: 'var(--low)', fontFamily: 'var(--mono)' }}>
              {activeModule.title}
            </span>
            <button 
              onClick={() => setSidebarOpen(!sidebarOpen)}
              style={{
                background: 'transparent',
                border: '1px solid var(--border)',
                borderRadius: '6px',
                padding: '0.5rem',
                color: 'var(--mid)',
                cursor: 'pointer'
              }}
              className="widget-btn-secondary"
            >
              {sidebarOpen ? <X size={18} /> : <Menu size={18} />}
            </button>
            <button 
              onClick={toggleFullscreen}
              style={{
                background: 'transparent',
                border: '1px solid var(--border)',
                borderRadius: '6px',
                padding: '0.5rem',
                color: 'var(--mid)',
                cursor: 'pointer'
              }}
              className="widget-btn-secondary"
            >
              <Maximize2 size={18} />
            </button>
          </div>
        )}
      </header>

      {/* DASHBOARD HOME SCREEN */}
      {currentModuleId === 'home' && (
        <div style={{ flex: '1', overflowY: 'auto', padding: '4rem 6vw' }}>
          <div style={{ maxWidth: '1200px', margin: '0 auto' }}>
            <div style={{ textAlign: 'center', marginBottom: '4rem' }}>
              <h1 style={{ fontFamily: 'var(--serif)', fontSize: 'clamp(3rem, 6vw, 5.5rem)', fontWeight: '900', lineHeight: '1.1', background: 'linear-gradient(135deg, #ffffff, #fcd34d, var(--accent))', WebkitBackgroundClip: 'text', WebkitTextFillColor: 'transparent', marginBottom: '1.5rem' }}>
                Programming for Problem Solving
              </h1>
              <p style={{ fontSize: '1.4rem', color: 'var(--mid)', fontWeight: '300', maxWidth: '65ch', margin: '0 auto', lineHeight: '1.6' }}>
                Interactive classroom learning deck & visualization tracing modules built specifically for Crescent CSE students.
              </p>
            </div>

            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(340px, 1fr))', gap: '2.5rem', marginInline: 'auto' }}>
              {modules.map((mod) => (
                <div 
                  key={mod.id}
                  style={{
                    background: 'var(--surface)',
                    border: '1px solid var(--border)',
                    borderRadius: '16px',
                    padding: '2.5rem',
                    display: 'flex',
                    flexDirection: 'column',
                    justifyContent: 'space-between',
                    boxShadow: '0 25px 50px rgba(0,0,0,0.5)',
                    transition: 'transform 0.3s, border-color 0.3s'
                  }}
                  className="dashboard-card"
                >
                  <div>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '0.8rem', marginBottom: '1.2rem' }}>
                      {mod.id === 'intro' && <BookOpen size={24} className="accent" style={{ color: 'var(--accent)' }} />}
                      {mod.id === 'control' && <Terminal size={24} className="accent" style={{ color: 'var(--blue)' }} />}
                      {mod.id === 'lab' && <CheckCircle2 size={24} className="accent" style={{ color: 'var(--green)' }} />}
                      <span style={{ fontSize: '0.85rem', fontFamily: 'var(--mono)', letterSpacing: '0.15em', textTransform: 'uppercase', color: 'var(--low)' }}>
                        {mod.slides.length} slides
                      </span>
                    </div>

                    <h3 style={{ fontFamily: 'var(--serif)', fontSize: '2.1rem', color: 'var(--hi)', fontWeight: '700', marginBottom: '1rem', lineHeight: '1.2' }}>
                      {mod.title}
                    </h3>
                    <p style={{ fontSize: '1.15rem', color: 'var(--mid)', fontWeight: '300', lineHeight: '1.6', marginBottom: '2rem' }}>
                      {mod.description}
                    </p>
                  </div>

                  <button 
                    onClick={() => handleModuleSelect(mod.id)}
                    style={{
                      width: '100%',
                      background: 'var(--surface2)',
                      border: '1px solid var(--border-hi)',
                      color: 'var(--hi)',
                      fontFamily: 'var(--sans)',
                      fontWeight: '600',
                      fontSize: '1.05rem',
                      padding: '1rem',
                      borderRadius: '8px',
                      cursor: 'pointer',
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'center',
                      gap: '0.6rem',
                      transition: 'all 0.3s'
                    }}
                    className="start-module-btn"
                  >
                    Start Presentation <ChevronRight size={18} />
                  </button>
                </div>
              ))}
            </div>
          </div>
        </div>
      )}

      {/* PRESENTATION VIEWPORT AND NAVIGATION SIDEBAR */}
      {currentModuleId !== 'home' && (
        <div style={{ flex: '1', display: 'flex', overflow: 'hidden', position: 'relative' }} onTouchStart={handleTouchStart} onTouchEnd={handleTouchEnd}>
          {/* SIDEBAR NAVIGATION */}
          <aside style={{
            position: 'absolute',
            top: 0, bottom: 0, right: 0,
            width: '350px',
            background: 'var(--surface)',
            borderLeft: '1px solid var(--border)',
            zIndex: 30,
            transform: sidebarOpen ? 'translateX(0)' : 'translateX(100%)',
            transition: 'transform 0.4s cubic-bezier(0.16, 1, 0.3, 1)',
            display: 'flex',
            flexDirection: 'column',
            overflow: 'hidden'
          }}>
            <div style={{ padding: '1.5rem', borderBottom: '1px solid var(--border)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <span className="bank-title">Slide Navigation Directory</span>
              <button onClick={() => setSidebarOpen(false)} style={{ background: 'transparent', border: 'none', color: 'var(--low)', cursor: 'pointer' }}>
                <X size={18} />
              </button>
            </div>
            <div style={{ flex: '1', overflowY: 'auto', padding: '1rem' }} className="sidebar-list">
              {slides.map((s, idx) => (
                <div 
                  key={idx}
                  onClick={() => {
                    setSlideIdx(idx);
                    setSidebarOpen(false);
                  }}
                  style={{
                    display: 'flex',
                    flexDirection: 'column',
                    gap: '0.4rem',
                    padding: '0.9rem 1.2rem',
                    borderRadius: '8px',
                    background: slideIdx === idx ? 'var(--surface2)' : 'transparent',
                    border: '1px solid',
                    borderColor: slideIdx === idx ? 'var(--border-hi)' : 'transparent',
                    cursor: 'pointer',
                    transition: 'all 0.2s',
                    marginBottom: '0.4rem'
                  }}
                  className="sidebar-item"
                >
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                    <span style={{ fontSize: '0.8rem', fontFamily: 'var(--mono)', color: slideIdx === idx ? 'var(--accent)' : 'var(--low)', fontWeight: '600' }}>
                      Slide {String(idx + 1).padStart(2, '0')}
                    </span>
                    <span style={{
                      fontSize: '0.65rem',
                      fontFamily: 'var(--mono)',
                      textTransform: 'uppercase',
                      padding: '0.15rem 0.4rem',
                      borderRadius: '4px',
                      background: slideIdx === idx ? 'var(--accent-soft)' : 'var(--surface3)',
                      color: slideIdx === idx ? 'var(--accent)' : 'var(--mid)'
                    }}>
                      {getSlideBadge(s)}
                    </span>
                  </div>
                  <span style={{ fontSize: '1.05rem', color: slideIdx === idx ? 'var(--hi)' : 'var(--mid)', fontWeight: slideIdx === idx ? '600' : '400', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>
                    {s.title || s.question || s.eyebrow || 'Intro Slide'}
                  </span>
                </div>
              ))}
            </div>
          </aside>

          {/* MAIN PRESENTATION CANVAS */}
          <main style={{ flex: '1', display: 'flex', flexDirection: 'column', overflow: 'hidden' }}>
            <div className="slide-viewport">
              {/* RENDER TITLE SLIDE */}
              {currentSlide.type === 'title' && (
                <div style={{ animation: 'fadeIn 0.6s' }}>
                  <div className="eyebrow">{currentSlide.eyebrow}</div>
                  <h2 className="title" style={{ fontSize: 'clamp(3.5rem, 8vw, 6.2rem)' }}>{currentSlide.title}</h2>
                  {currentSlide.subtitle && (
                    <div style={{ fontSize: 'clamp(1.8rem, 3.5vw, 3rem)', color: 'var(--accent)', fontFamily: 'var(--sans)', marginTop: '0.5rem', fontWeight: '700' }}>
                      {currentSlide.subtitle}
                    </div>
                  )}
                  {currentSlide.lede && <p className="lede" style={{ marginTop: '2rem' }}>{currentSlide.lede}</p>}
                </div>
              )}

              {/* RENDER AGENDA SLIDE */}
              {currentSlide.type === 'agenda' && (
                <div style={{ animation: 'fadeIn 0.6s' }}>
                  <div className="eyebrow">{currentSlide.eyebrow}</div>
                  <h2 className="title">{currentSlide.title}</h2>
                  <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: '2rem', marginTop: '2.5rem' }}>
                    {currentSlide.facts.map((f, idx) => (
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

              {/* RENDER BULLET SLIDE */}
              {currentSlide.type === 'bullets' && (
                <div style={{ animation: 'fadeIn 0.6s' }}>
                  <div className="eyebrow">{currentSlide.eyebrow}</div>
                  <h2 className="title">{currentSlide.title}</h2>
                  {currentSlide.lede && <p className="lede">{currentSlide.lede}</p>}
                  <ul className="simple-list" style={{ marginTop: '2rem' }}>
                    {currentSlide.bullets.map((b, idx) => (
                      <li key={idx}>
                        <strong>{b.bold}</strong> {b.text}
                      </li>
                    ))}
                  </ul>
                </div>
              )}

              {/* RENDER TIMELINE SLIDE */}
              {currentSlide.type === 'timeline' && (
                <div style={{ animation: 'fadeIn 0.6s' }}>
                  <div className="eyebrow">{currentSlide.eyebrow}</div>
                  <h2 className="title">{currentSlide.title}</h2>
                  <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem', marginTop: '3rem', borderLeft: '2px solid var(--border-hi)', paddingLeft: '2rem', position: 'relative' }}>
                    {currentSlide.timeline.map((item, idx) => (
                      <div key={idx} style={{ position: 'relative' }}>
                        <div style={{
                          position: 'absolute',
                          left: 'calc(-2rem - 6px)',
                          top: '0.4rem',
                          width: '10px',
                          height: '10px',
                          borderRadius: '50%',
                          background: 'var(--accent)',
                          boxShadow: '0 0 10px var(--accent)'
                        }}></div>
                        <span style={{ fontFamily: 'var(--mono)', color: 'var(--accent)', fontWeight: 'bold', fontSize: '1.25rem' }}>{item.yr}</span>
                        <h4 style={{ fontSize: '1.3rem', color: 'var(--hi)', margin: '0.2rem 0' }}>{item.title}</h4>
                        <p style={{ color: 'var(--mid)', fontSize: '1.05rem' }}>{item.desc}</p>
                      </div>
                    ))}
                  </div>
                </div>
              )}

              {/* RENDER CINEMATIC HERO SLIDE */}
              {currentSlide.type === 'hero' && (
                <div className="split" style={{ animation: 'fadeIn 0.6s' }}>
                  <div style={{ flex: '1.1' }}>
                    <div className="eyebrow">{currentSlide.eyebrow}</div>
                    <h2 className="title" style={{ marginBottom: '1.5rem' }}>{currentSlide.title}</h2>
                    <p className="body-copy" style={{ fontSize: '1.35rem', lineHeight: '1.6', marginBottom: '2rem' }}>{currentSlide.lede}</p>
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
                      {currentSlide.highlight}
                    </div>
                  </div>
                  <div style={{
                    flex: '0.9',
                    height: '350px',
                    borderRadius: '12px',
                    border: '1px solid var(--border)',
                    background: `linear-gradient(to bottom, rgba(0,0,0,0.4), rgba(0,0,0,0.8)), url('https://images.unsplash.com/photo-1517694712202-14dd9538aa97?q=80&w=600&auto=format&fit=crop')`,
                    backgroundSize: 'cover',
                    backgroundPosition: 'center',
                    boxShadow: '0 20px 45px rgba(0,0,0,0.5)',
                    opacity: '0.8'
                  }}></div>
                </div>
              )}

              {/* RENDER TABLE SLIDE */}
              {currentSlide.type === 'table' && (
                <div style={{ animation: 'fadeIn 0.6s' }}>
                  <div className="eyebrow">{currentSlide.eyebrow}</div>
                  <h2 className="title" style={{ marginBottom: '2rem' }}>{currentSlide.title}</h2>
                  <div style={{ overflowX: 'auto', border: '1px solid var(--border)', borderRadius: '12px', background: 'var(--surface)' }}>
                    <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left', fontFamily: 'var(--sans)' }}>
                      <thead>
                        <tr style={{ borderBottom: '2px solid var(--border-hi)', background: 'var(--surface2)' }}>
                          {currentSlide.headers.map((h, i) => (
                            <th key={i} style={{ padding: '1.2rem 1.8rem', fontSize: '1.1rem', fontWeight: 'bold', color: 'var(--accent)' }}>{h}</th>
                          ))}
                        </tr>
                      </thead>
                      <tbody>
                        {currentSlide.rows.map((row, i) => (
                          <tr key={i} style={{ borderBottom: '1px solid var(--border)', transition: 'background 0.3s' }} className="table-row-hover">
                            {row.map((cell, j) => (
                              <td key={j} style={{ padding: '1.2rem 1.8rem', fontSize: '1.1rem', color: j === 0 ? 'var(--hi)' : 'var(--mid)' }}>{cell}</td>
                            ))}
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>
                </div>
              )}

              {/* RENDER STRUCTURE ANATOMY SLIDE */}
              {currentSlide.type === 'structure' && (
                <div style={{ animation: 'fadeIn 0.6s' }}>
                  <div className="eyebrow">{currentSlide.eyebrow}</div>
                  <h2 className="title" style={{ marginBottom: '1.5rem' }}>{currentSlide.title}</h2>
                  <div className="split" style={{ alignItems: 'stretch' }}>
                    <pre className="code" style={{ flex: '1.3', fontSize: '1.1rem', padding: '2rem' }}>
                      {currentSlide.code}
                    </pre>
                    <div style={{ flex: '0.8', display: 'flex', flexDirection: 'column', gap: '0.8rem', justifyContent: 'center' }}>
                      <span className="bank-title" style={{ marginBottom: '0.4rem' }}>Anatomy Sections</span>
                      {currentSlide.sections.map((sect, idx) => (
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
                          <span style={{ color: 'var(--mid)' }}>{sect}</span>
                        </div>
                      ))}
                    </div>
                  </div>
                </div>
              )}

              {/* RENDER CODE VIEW SLIDE */}
              {currentSlide.type === 'code' && (
                <div style={{ animation: 'fadeIn 0.6s' }}>
                  <div className="eyebrow">{currentSlide.eyebrow}</div>
                  <h2 className="title">{currentSlide.title}</h2>
                  {currentSlide.lede && <p className="lede" style={{ marginBottom: '1.5rem' }}>{currentSlide.lede}</p>}
                  <pre className="code" style={{ marginTop: '1rem', maxHeight: '55vh' }}>
                    {currentSlide.code}
                  </pre>
                </div>
              )}

              {/* RENDER TERMINAL SCANF VIEW SLIDE */}
              {currentSlide.type === 'terminal' && (
                <div style={{ animation: 'fadeIn 0.6s' }}>
                  <div className="eyebrow">{currentSlide.eyebrow}</div>
                  <h2 className="title">{currentSlide.title}</h2>
                  <div className="split" style={{ alignItems: 'stretch' }}>
                    <pre className="code" style={{ flex: '1.2', fontSize: '1.1rem' }}>
                      {currentSlide.code}
                    </pre>
                    <div style={{ flex: '0.8', display: 'flex', flexDirection: 'column', justifyContent: 'center', background: '#070809', border: '1px solid var(--border)', borderRadius: '12px', padding: '2rem' }}>
                      <span className="bank-title" style={{ marginBottom: '1rem' }}>Output Terminal Console</span>
                      <div className="console-line">Enter score: <span className="accent" style={{ animation: 'pulse 1.2s infinite' }}>85█</span></div>
                      <div className="console-line text-accent" style={{ marginTop: '0.8rem', borderLeftColor: 'var(--accent)' }}>✔ scanf mapped address &amp;score directly in RAM memory (address: 0x7ffd5a).</div>
                    </div>
                  </div>
                </div>
              )}

              {/* RENDER INTERACTIVE SIMULATORS */}
              {currentSlide.type === 'swapping' && (
                <div style={{ animation: 'fadeIn 0.6s' }}>
                  <div className="eyebrow">{currentSlide.eyebrow}</div>
                  <h2 className="title">{currentSlide.title}</h2>
                  {currentSlide.lede && <p className="lede">{currentSlide.lede}</p>}
                  <SwappingCups />
                </div>
              )}

              {currentSlide.type === 'accumulator' && (
                <div style={{ animation: 'fadeIn 0.6s' }}>
                  <div className="eyebrow">{currentSlide.eyebrow}</div>
                  <h2 className="title">{currentSlide.title}</h2>
                  <div className="split">
                    <pre className="code" style={{ flex: '1.1', fontSize: '1.05rem' }}>
                      {currentSlide.code}
                    </pre>
                    <div style={{ flex: '0.9' }}>
                      <SumAccumulator />
                    </div>
                  </div>
                </div>
              )}

              {currentSlide.type === 'ternary' && (
                <div style={{ animation: 'fadeIn 0.6s' }}>
                  <div className="eyebrow">{currentSlide.eyebrow}</div>
                  <h2 className="title">{currentSlide.title}</h2>
                  {currentSlide.lede && <p className="lede" style={{ marginBottom: '1.5rem' }}>{currentSlide.lede}</p>}
                  <TernaryGate />
                </div>
              )}

              {currentSlide.type === 'loopTracer' && (
                <div style={{ animation: 'fadeIn 0.6s' }}>
                  <div className="eyebrow">{currentSlide.eyebrow}</div>
                  <h2 className="title">{currentSlide.title}</h2>
                  <LoopTracer />
                </div>
              )}

              {currentSlide.type === 'arrayMath' && (
                <div style={{ animation: 'fadeIn 0.6s' }}>
                  <div className="eyebrow">{currentSlide.eyebrow}</div>
                  <h2 className="title">{currentSlide.title}</h2>
                  {currentSlide.lede && <p className="lede" style={{ marginBottom: '1.5rem' }}>{currentSlide.lede}</p>}
                  <ArrayMath />
                </div>
              )}

              {currentSlide.type === 'stringTracer' && (
                <div style={{ animation: 'fadeIn 0.6s' }}>
                  <div className="eyebrow">{currentSlide.eyebrow}</div>
                  <h2 className="title">{currentSlide.title}</h2>
                  {currentSlide.lede && <p className="lede" style={{ marginBottom: '1.5rem' }}>{currentSlide.lede}</p>}
                  <StringGarland />
                </div>
              )}

              {currentSlide.type === 'recursion' && (
                <div style={{ animation: 'fadeIn 0.6s' }}>
                  <div className="eyebrow">{currentSlide.eyebrow}</div>
                  <h2 className="title">{currentSlide.title}</h2>
                  {currentSlide.lede && <p className="lede" style={{ marginBottom: '1rem' }}>{currentSlide.lede}</p>}
                  <RecursionStack />
                </div>
              )}

              {currentSlide.type === 'pointers' && (
                <div style={{ animation: 'fadeIn 0.6s' }}>
                  <div className="eyebrow">{currentSlide.eyebrow}</div>
                  <h2 className="title">{currentSlide.title}</h2>
                  <div className="split">
                    <pre className="code" style={{ flex: '1.1', fontSize: '1.05rem' }}>
                      {currentSlide.code}
                    </pre>
                    <div style={{ flex: '0.9' }}>
                      <PointerVisualizer />
                    </div>
                  </div>
                </div>
              )}

              {/* RENDER COMPILATIONS AND TODO CHEATS */}
              {currentSlide.type === 'quiz' && (
                <div style={{ animation: 'fadeIn 0.6s' }}>
                  <div className="eyebrow">{currentSlide.eyebrow}</div>
                  <QuizCard question={currentSlide.question} options={currentSlide.options} />
                </div>
              )}

              {currentSlide.type === 'blank' && (
                <div style={{ animation: 'fadeIn 0.6s' }}>
                  <div className="eyebrow">{currentSlide.eyebrow}</div>
                  <h2 className="title" style={{ marginBottom: '1rem' }}>{currentSlide.title}</h2>
                  <p className="lede" style={{ marginBottom: '2rem' }}>{currentSlide.lede}</p>
                  <CodeBlank code={currentSlide.code} blankVal={currentSlide.blankVal} />
                </div>
              )}

              {currentSlide.type === 'todo' && (
                <div style={{ animation: 'fadeIn 0.6s' }}>
                  <div className="eyebrow">{currentSlide.eyebrow}</div>
                  <TodoCard title={currentSlide.title} desc={currentSlide.desc} hint={currentSlide.hint} />
                </div>
              )}
            </div>

            {/* BOTTOM PERSISTENT NAVIGATION BAR */}
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
                  style={{
                    background: 'transparent',
                    border: '1px solid var(--border)',
                    color: slideIdx === 0 ? 'var(--low)' : 'var(--mid)',
                    borderRadius: '6px',
                    padding: '0.5rem 1rem',
                    cursor: slideIdx === 0 ? 'not-allowed' : 'pointer',
                    display: 'flex',
                    alignItems: 'center',
                    gap: '0.4rem'
                  }}
                  className="widget-btn-secondary"
                >
                  <ArrowLeft size={16} /> Prev
                </button>
                <button 
                  onClick={nextSlide} 
                  disabled={slideIdx === slides.length - 1}
                  style={{
                    background: 'transparent',
                    border: '1px solid var(--border)',
                    color: slideIdx === slides.length - 1 ? 'var(--low)' : 'var(--mid)',
                    borderRadius: '6px',
                    padding: '0.5rem 1rem',
                    cursor: slideIdx === slides.length - 1 ? 'not-allowed' : 'pointer',
                    display: 'flex',
                    alignItems: 'center',
                    gap: '0.4rem'
                  }}
                  className="widget-btn-secondary"
                >
                  Next <ArrowRight size={16} />
                </button>
              </div>

              {/* PROGRESS BAR BAR WIDGET */}
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
                <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.75rem', fontFamily: 'var(--mono)', color: 'var(--low)' }}>
                  <span>Chapter {String(slideIdx + 1).padStart(2, '0')} of {String(slides.length).padStart(2, '0')}</span>
                  <span>Keyboard navigation enabled (← / → / Space)</span>
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
      )}
    </div>
  );
}

export default App;
