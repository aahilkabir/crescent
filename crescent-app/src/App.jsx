import React, { useState, useEffect, useRef } from 'react';
import { modules } from './data/slides';
import { subjects } from './data/subjects';
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
import { Play, Home, ChevronRight, Menu, X, ArrowLeft, ArrowRight, Maximize2, Monitor, BookOpen, Terminal, CheckCircle2, Code, Lightbulb, Cpu, Briefcase, ExternalLink, RefreshCw, Users, HelpCircle, GraduationCap, ChevronLeft } from 'lucide-react';

function App() {
  const [currentSubjectId, setCurrentSubjectId] = useState(null);
  const [currentModuleId, setCurrentModuleId] = useState(null);
  const [slideIdx, setSlideIdx] = useState(0);
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const [isFullscreen, setIsFullscreen] = useState(false);

  // Attendance Check-in State
  const [rollNumber, setRollNumber] = useState('');
  const [studentName, setStudentName] = useState('');
  const [isCheckedIn, setIsCheckedIn] = useState(false);
  const [checkInError, setCheckInError] = useState('');
  const [checkInLoading, setCheckInLoading] = useState(false);

  // Admin Dashboard State
  const [isAdminView, setIsAdminView] = useState(false);
  const [adminData, setAdminData] = useState({ students: [], stats: [], rawResponses: [] });
  const [adminLoading, setAdminLoading] = useState(false);
  const [adminSearch, setAdminSearch] = useState('');

  const activeModule = modules.find(m => m.id === currentModuleId);
  const slides = activeModule?.slides || [];
  const currentSlide = slides[slideIdx];

  const activeSubject = subjects.find(s => s.id === currentSubjectId);
  const touchStartX = useRef(null);

  // Initialize and check local storage check-in credentials
  useEffect(() => {
    // Check if path or hash is admin
    const checkRoute = () => {
      const isHashAdmin = window.location.hash === '#admin';
      const isPathAdmin = window.location.pathname === '/admin';
      setIsAdminView(isHashAdmin || isPathAdmin);
    };

    checkRoute();
    window.addEventListener('hashchange', checkRoute);
    
    const savedRoll = localStorage.getItem('crescent_roll_number');
    const savedName = localStorage.getItem('crescent_name');
    const presenterFlag = localStorage.getItem('crescent_presenter_view');
    
    if ((savedRoll && savedName) || presenterFlag === 'true') {
      setIsCheckedIn(true);
    }

    return () => window.removeEventListener('hashchange', checkRoute);
  }, []);

  // Fetch admin stats when admin panel is visible
  useEffect(() => {
    if (isAdminView) {
      fetchAdminData();
    }
  }, [isAdminView]);

  const fetchAdminData = async () => {
    setAdminLoading(true);
    try {
      const res = await fetch('/api/submissions');
      if (res.ok) {
        const data = await res.json();
        setAdminData(data);
      }
    } catch (err) {
      console.error("Failed to fetch admin stats:", err);
    } finally {
      setAdminLoading(false);
    }
  };

  const handleCheckInSubmit = async (e) => {
    e.preventDefault();
    if (!rollNumber.trim() || !studentName.trim()) {
      setCheckInError('Please enter both your Roll Number and Name.');
      return;
    }

    setCheckInLoading(true);
    setCheckInError('');

    try {
      const res = await fetch('/api/checkin', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          rollNumber: rollNumber.trim(),
          name: studentName.trim()
        })
      });

      if (res.ok) {
        localStorage.setItem('crescent_roll_number', rollNumber.trim().toUpperCase());
        localStorage.setItem('crescent_name', studentName.trim());
        localStorage.removeItem('crescent_presenter_view');
        setIsCheckedIn(true);
      } else {
        const errData = await res.json();
        setCheckInError(errData.error || 'Check-in failed. Please try again.');
      }
    } catch (err) {
      setCheckInError('Network error. Check your connection.');
    } finally {
      setCheckInLoading(false);
    }
  };

  const skipCheckInAsPresenter = () => {
    localStorage.setItem('crescent_presenter_view', 'true');
    localStorage.removeItem('crescent_roll_number');
    localStorage.removeItem('crescent_name');
    setIsCheckedIn(true);
  };

  const logout = () => {
    localStorage.removeItem('crescent_roll_number');
    localStorage.removeItem('crescent_name');
    localStorage.removeItem('crescent_presenter_view');
    setIsCheckedIn(false);
    setRollNumber('');
    setStudentName('');
  };

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

  const handleSubjectSelect = (subjectId) => {
    setCurrentSubjectId(subjectId);
    setCurrentModuleId(null);
  };

  const getSlideBadge = (slide) => {
    if (slide.type === 'title') return 'Intro';
    if (slide.type === 'quiz') return 'Quiz';
    if (slide.type === 'todo') return 'Practice';
    if (slide.type === 'blank') return 'Solve';
    if (slide.type === 'code') return 'C Code';
    if (['swapping', 'accumulator', 'ternary', 'recursion', 'pointers', 'loopTracer', 'arrayMath', 'stringTracer'].includes(slide.type)) return 'Trace';
    return 'Study';
  };

  const getSubjectIcon = (iconName) => {
    switch (iconName) {
      case 'code': return <Code size={32} style={{ color: 'var(--accent)' }} />;
      case 'lightbulb': return <Lightbulb size={32} style={{ color: 'var(--rose)' }} />;
      case 'cpu': return <Cpu size={32} style={{ color: 'var(--blue)' }} />;
      case 'briefcase': return <Briefcase size={32} style={{ color: 'var(--green)' }} />;
      default: return <BookOpen size={32} />;
    }
  };

  // Render Admin Console Dashboard
  if (isAdminView) {
    const filteredStudents = adminData.students.filter(s => 
      s.name.toLowerCase().includes(adminSearch.toLowerCase()) || 
      s.roll_number.toLowerCase().includes(adminSearch.toLowerCase())
    );

    // Group stats by slide_id
    const groupedStats = {};
    adminData.stats.forEach(item => {
      if (!groupedStats[item.slide_id]) {
        groupedStats[item.slide_id] = { correct: 0, incorrect: 0, responses: [] };
      }
      if (item.is_correct) {
        groupedStats[item.slide_id].correct += parseInt(item.count);
      } else {
        groupedStats[item.slide_id].incorrect += parseInt(item.count);
      }
      groupedStats[item.slide_id].responses.push(item);
    });

    return (
      <div style={{ display: 'flex', flexDirection: 'column', height: '100%', background: 'var(--black)' }}>
        <header style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '1.2rem 3vw', borderBottom: '1px solid var(--border)', background: 'var(--surface)' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.8rem' }}>
            <button 
              onClick={() => {
                window.location.hash = '';
                setIsAdminView(false);
              }}
              className="widget-btn-secondary"
            >
              <ChevronLeft size={16} /> Exit Admin Dashboard
            </button>
            <span style={{ fontSize: '1.2rem', fontWeight: 'bold', color: 'var(--accent)' }}>CLASSROOM ANALYTICS</span>
          </div>
          <button onClick={fetchAdminData} className="widget-btn-secondary" disabled={adminLoading}>
            <RefreshCw size={16} style={{ animation: adminLoading ? 'spin 1s infinite linear' : 'none' }} /> {adminLoading ? 'Refreshing...' : 'Refresh Data'}
          </button>
        </header>

        <div style={{ flex: '1', overflowY: 'auto', padding: '3rem 5vw' }}>
          <div style={{ maxWidth: '1200px', margin: '0 auto', display: 'flex', flexDirection: 'column', gap: '2.5rem' }}>
            
            {/* KPI STATS ROW */}
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: '1.5rem' }}>
              <div style={{ background: 'var(--surface)', border: '1px solid var(--border)', borderRadius: '12px', padding: '2rem', display: 'flex', alignItems: 'center', gap: '1.5rem' }}>
                <Users size={40} style={{ color: 'var(--accent)' }} />
                <div>
                  <h4 style={{ color: 'var(--low)', fontSize: '0.85rem', textTransform: 'uppercase', letterSpacing: '0.1em' }}>Students Checked-in</h4>
                  <div style={{ fontSize: '2.5rem', fontWeight: 'bold', color: 'var(--hi)' }}>{adminData.students.length}</div>
                </div>
              </div>
              <div style={{ background: 'var(--surface)', border: '1px solid var(--border)', borderRadius: '12px', padding: '2rem', display: 'flex', alignItems: 'center', gap: '1.5rem' }}>
                <CheckCircle2 size={40} style={{ color: 'var(--green)' }} />
                <div>
                  <h4 style={{ color: 'var(--low)', fontSize: '0.85rem', textTransform: 'uppercase', letterSpacing: '0.1em' }}>Total Responses</h4>
                  <div style={{ fontSize: '2.5rem', fontWeight: 'bold', color: 'var(--hi)' }}>{adminData.rawResponses.length}</div>
                </div>
              </div>
              <div style={{ background: 'var(--surface)', border: '1px solid var(--border)', borderRadius: '12px', padding: '2rem', display: 'flex', alignItems: 'center', gap: '1.5rem' }}>
                <HelpCircle size={40} style={{ color: 'var(--blue)' }} />
                <div>
                  <h4 style={{ color: 'var(--low)', fontSize: '0.85rem', textTransform: 'uppercase', letterSpacing: '0.1em' }}>Active Quiz Elements</h4>
                  <div style={{ fontSize: '2.5rem', fontWeight: 'bold', color: 'var(--hi)' }}>{Object.keys(groupedStats).length}</div>
                </div>
              </div>
            </div>

            <div className="split" style={{ alignItems: 'stretch', gap: '2rem' }}>
              {/* ATTENDANCE SECTION */}
              <div style={{ flex: '1', background: 'var(--surface)', border: '1px solid var(--border)', borderRadius: '16px', padding: '2rem', display: 'flex', flexDirection: 'column' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1.5rem' }}>
                  <h3 style={{ fontFamily: 'var(--serif)', fontSize: '1.8rem' }}>Checked-in Roll Directory</h3>
                  <input 
                    type="text" 
                    placeholder="Search roll or name..." 
                    value={adminSearch}
                    onChange={(e) => setAdminSearch(e.target.value)}
                    style={{
                      background: 'var(--surface2)',
                      border: '1px solid var(--border)',
                      borderRadius: '6px',
                      color: 'var(--hi)',
                      padding: '0.5rem 1rem',
                      fontSize: '0.95rem',
                      width: '200px'
                    }}
                  />
                </div>
                <div style={{ flex: '1', overflowY: 'auto', maxHeight: '400px' }}>
                  {filteredStudents.length === 0 ? (
                    <div style={{ padding: '2rem', textAlign: 'center', color: 'var(--low)' }}>No checked-in students found.</div>
                  ) : (
                    <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left' }}>
                      <thead>
                        <tr style={{ borderBottom: '1px solid var(--border-hi)', color: 'var(--accent)' }}>
                          <th style={{ padding: '0.8rem' }}>Roll Number</th>
                          <th style={{ padding: '0.8rem' }}>Student Name</th>
                          <th style={{ padding: '0.8rem' }}>Registered At</th>
                        </tr>
                      </thead>
                      <tbody>
                        {filteredStudents.map((st, i) => (
                          <tr key={i} style={{ borderBottom: '1px solid var(--border)' }}>
                            <td style={{ padding: '0.8rem', fontWeight: 'bold' }}>{st.roll_number}</td>
                            <td style={{ padding: '0.8rem' }}>{st.name}</td>
                            <td style={{ padding: '0.8rem', color: 'var(--low)' }}>{new Date(st.checked_in_at).toLocaleTimeString()}</td>
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  )}
                </div>
              </div>

              {/* QUIZ METRICS SECTION */}
              <div style={{ flex: '1.2', background: 'var(--surface)', border: '1px solid var(--border)', borderRadius: '16px', padding: '2rem', display: 'flex', flexDirection: 'column' }}>
                <h3 style={{ fontFamily: 'var(--serif)', fontSize: '1.8rem', marginBottom: '1.5rem' }}>Slide Quiz Analytics</h3>
                <div style={{ flex: '1', overflowY: 'auto', maxHeight: '400px', display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
                  {Object.keys(groupedStats).length === 0 ? (
                    <div style={{ padding: '2rem', textAlign: 'center', color: 'var(--low)' }}>No submissions submitted yet.</div>
                  ) : (
                    Object.entries(groupedStats).map(([slideId, data], idx) => {
                      const total = data.correct + data.incorrect;
                      const correctPct = total > 0 ? (data.correct / total) * 100 : 0;
                      return (
                        <div key={idx} style={{ paddingBottom: '1.2rem', borderBottom: '1px solid var(--border)' }}>
                          <h4 style={{ fontSize: '1.15rem', color: 'var(--hi)', marginBottom: '0.6rem' }}>{slideId}</h4>
                          <div style={{ display: 'flex', alignItems: 'center', gap: '1rem' }}>
                            <div style={{ flex: '1', height: '10px', background: 'var(--surface3)', borderRadius: '5px', overflow: 'hidden', display: 'flex' }}>
                              <div style={{ width: `${correctPct}%`, height: '100%', background: 'var(--green)' }}></div>
                              <div style={{ width: `${100 - correctPct}%`, height: '100%', background: 'var(--rose)' }}></div>
                            </div>
                            <span style={{ fontSize: '0.95rem', fontWeight: 'bold', fontFamily: 'var(--mono)', width: '80px', textAlign: 'right' }}>
                              {data.correct} / {total} Correct
                            </span>
                          </div>
                          <div style={{ display: 'flex', gap: '0.8rem', marginTop: '0.4rem', fontSize: '0.85rem', color: 'var(--low)' }}>
                            {data.responses.map((resp, rIdx) => (
                              <span key={rIdx}>
                                {resp.answer}: <strong style={{ color: 'var(--hi)' }}>{resp.count}</strong>
                              </span>
                            ))}
                          </div>
                        </div>
                      );
                    })
                  )}
                </div>
              </div>
            </div>

          </div>
        </div>
      </div>
    );
  }

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
          {currentSubjectId !== null && (
            <button 
              onClick={() => {
                if (currentModuleId !== null) {
                  setCurrentModuleId(null);
                } else {
                  setCurrentSubjectId(null);
                }
              }} 
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
              <Home size={16} /> {currentModuleId !== null ? 'Back to Subject' : 'Back to Subjects'}
            </button>
          )}
          <span style={{ fontSize: '1.2rem', fontWeight: 'bold', letterSpacing: '0.02em', background: 'linear-gradient(90deg, #ffffff, var(--accent))', WebkitBackgroundClip: 'text', WebkitTextFillColor: 'transparent' }}>
            CRESCENT ACADEMY
          </span>
        </div>

        <div style={{ display: 'flex', alignItems: 'center', gap: '1rem' }}>
          {isCheckedIn && (
            <button 
              onClick={logout} 
              style={{
                background: 'transparent',
                border: '1px solid var(--border)',
                color: 'var(--low)',
                borderRadius: '6px',
                padding: '0.4rem 0.8rem',
                fontSize: '0.85rem',
                cursor: 'pointer'
              }}
              className="widget-btn-secondary"
            >
              Logout / Reset check-in
            </button>
          )}
          {currentModuleId !== null && (
            <>
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
            </>
          )}
        </div>
      </header>

      {/* STUDENT REGISTRATION CHECK-IN OVERLAY MODAL */}
      {!isCheckedIn && (
        <div style={{
          position: 'fixed', inset: 0,
          background: 'rgba(0,0,0,0.85)',
          backdropFilter: 'blur(8px)',
          display: 'flex', alignItems: 'center', justifyContent: 'center',
          zIndex: 100, padding: '1rem'
        }}>
          <form 
            onSubmit={handleCheckInSubmit}
            style={{
              background: 'var(--surface)',
              border: '1px solid var(--accent-soft)',
              borderRadius: '16px',
              padding: '3rem',
              maxWidth: '480px',
              width: '100%',
              boxShadow: '0 25px 60px rgba(0,0,0,0.8)',
              display: 'flex', flexDirection: 'column', gap: '1.5rem'
            }}
          >
            <div style={{ textAlign: 'center', marginBottom: '1rem' }}>
              <GraduationCap size={48} style={{ color: 'var(--accent)', marginInline: 'auto', marginBottom: '1rem' }} />
              <h2 style={{ fontFamily: 'var(--serif)', fontSize: '2.2rem', fontWeight: 'bold' }}>Classroom Check-in</h2>
              <p style={{ color: 'var(--low)', fontSize: '1rem', marginTop: '0.4rem' }}>Register your credentials to log slide observations and quizzes.</p>
            </div>

            {checkInError && (
              <div style={{ background: 'rgba(244,63,94,0.1)', borderLeft: '3px solid var(--rose)', color: 'var(--rose)', padding: '0.8rem 1.2rem', borderRadius: '4px', fontSize: '0.95rem' }}>
                {checkInError}
              </div>
            )}

            <div style={{ display: 'flex', flexDirection: 'column', gap: '0.5rem' }}>
              <label style={{ fontFamily: 'var(--mono)', fontSize: '0.8rem', color: 'var(--low)', textTransform: 'uppercase', letterSpacing: '0.05em' }}>Roll Number</label>
              <input 
                type="text" 
                placeholder="e.g. 23CSE01 or RR21003" 
                value={rollNumber}
                onChange={(e) => setRollNumber(e.target.value)}
                style={{
                  background: 'var(--surface2)',
                  border: '1px solid var(--border)',
                  borderRadius: '6px',
                  color: 'var(--hi)',
                  padding: '0.8rem 1.2rem',
                  fontSize: '1.05rem',
                  outline: 'none'
                }}
              />
            </div>

            <div style={{ display: 'flex', flexDirection: 'column', gap: '0.5rem' }}>
              <label style={{ fontFamily: 'var(--mono)', fontSize: '0.8rem', color: 'var(--low)', textTransform: 'uppercase', letterSpacing: '0.05em' }}>Student Name</label>
              <input 
                type="text" 
                placeholder="e.g. Arun Kumar" 
                value={studentName}
                onChange={(e) => setStudentName(e.target.value)}
                style={{
                  background: 'var(--surface2)',
                  border: '1px solid var(--border)',
                  borderRadius: '6px',
                  color: 'var(--hi)',
                  padding: '0.8rem 1.2rem',
                  fontSize: '1.05rem',
                  outline: 'none'
                }}
              />
            </div>

            <button 
              type="submit" 
              disabled={checkInLoading}
              style={{
                background: 'var(--accent)',
                color: 'var(--black)',
                fontWeight: '700',
                fontSize: '1.05rem',
                padding: '1rem',
                border: 'none',
                borderRadius: '6px',
                cursor: 'pointer',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                gap: '0.5rem',
                transition: 'all 0.3s'
              }}
            >
              {checkInLoading ? 'Checking in...' : 'Register & Enter Portal'}
            </button>

            <button 
              type="button" 
              onClick={skipCheckInAsPresenter}
              style={{
                background: 'transparent',
                border: '1px solid var(--border)',
                color: 'var(--low)',
                fontSize: '0.95rem',
                padding: '0.8rem',
                borderRadius: '6px',
                cursor: 'pointer',
                transition: 'all 0.3s'
              }}
              className="widget-btn-secondary"
            >
              Skip Check-in / Presenter View
            </button>
          </form>
        </div>
      )}

      {/* PORTAL MAIN HOME SCREEN (SUBJECT SELECTION) */}
      {currentSubjectId === null && (
        <div style={{ flex: '1', overflowY: 'auto', padding: '4rem 6vw' }}>
          <div style={{ maxWidth: '1200px', margin: '0 auto' }}>
            <div style={{ textAlign: 'center', marginBottom: '4.5rem' }}>
              <h1 style={{ fontFamily: 'var(--serif)', fontSize: 'clamp(3rem, 5.8vw, 5.2rem)', fontWeight: '900', lineHeight: '1.1', background: 'linear-gradient(135deg, #ffffff, #fcd34d, var(--accent))', WebkitBackgroundClip: 'text', WebkitTextFillColor: 'transparent', marginBottom: '1.5rem' }}>
                Crescent Student Learning Portal
              </h1>
              <p style={{ fontSize: '1.35rem', color: 'var(--mid)', fontWeight: '300', maxWidth: '65ch', margin: '0 auto', lineHeight: '1.6' }}>
                Select a subject path to view interactive slide presentations, quizzes, lab guides, and engineering blueprints.
              </p>
            </div>

            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(270px, 1fr))', gap: '2rem' }}>
              {subjects.map((sub) => (
                <div 
                  key={sub.id}
                  style={{
                    background: 'var(--surface)',
                    border: '1px solid var(--border)',
                    borderRadius: '16px',
                    padding: '2rem',
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
                      {getSubjectIcon(sub.icon)}
                      <span style={{ fontSize: '0.8rem', fontFamily: 'var(--mono)', letterSpacing: '0.12em', color: 'var(--low)', fontWeight: '600' }}>
                        {sub.code}
                      </span>
                    </div>

                    <h3 style={{ fontFamily: 'var(--serif)', fontSize: '1.8rem', color: 'var(--hi)', fontWeight: '700', marginBottom: '1rem', lineHeight: '1.2' }}>
                      {sub.title}
                    </h3>
                    <p style={{ fontSize: '1.1rem', color: 'var(--mid)', fontWeight: '300', lineHeight: '1.6', marginBottom: '2rem' }}>
                      {sub.desc}
                    </p>
                  </div>

                  <button 
                    onClick={() => handleSubjectSelect(sub.id)}
                    style={{
                      width: '100%',
                      background: 'var(--surface2)',
                      border: '1px solid var(--border-hi)',
                      color: 'var(--hi)',
                      fontFamily: 'var(--sans)',
                      fontWeight: '600',
                      fontSize: '1rem',
                      padding: '0.9rem',
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
                    Open Course <ChevronRight size={18} />
                  </button>
                </div>
              ))}
            </div>
          </div>
        </div>
      )}

      {/* SUBJECT MODULES PAGE */}
      {currentSubjectId !== null && currentModuleId === null && (
        <div style={{ flex: '1', overflowY: 'auto', padding: '4rem 6vw' }}>
          <div style={{ maxWidth: '1000px', margin: '0 auto' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '1rem', marginBottom: '1.5rem' }}>
              {getSubjectIcon(activeSubject.icon)}
              <h2 style={{ fontFamily: 'var(--serif)', fontSize: '3rem', color: 'var(--hi)', fontWeight: '700' }}>
                {activeSubject.title}
              </h2>
            </div>
            <p style={{ fontSize: '1.25rem', color: 'var(--mid)', fontWeight: '300', lineHeight: '1.6', marginBottom: '3.5rem', maxWidth: '75ch' }}>
              {activeSubject.desc}
            </p>

            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: '2rem' }}>
              {activeSubject.modules.map((mod, idx) => (
                <div 
                  key={idx}
                  style={{
                    background: 'var(--surface)',
                    border: '1px solid var(--border)',
                    borderRadius: '12px',
                    padding: '2rem',
                    display: 'flex',
                    flexDirection: 'column',
                    justifyContent: 'space-between',
                    minHeight: '220px',
                    boxShadow: '0 15px 35px rgba(0,0,0,0.4)'
                  }}
                  className="dashboard-card"
                >
                  <div>
                    <h4 style={{ fontFamily: 'var(--sans)', fontSize: '1.35rem', color: 'var(--hi)', fontWeight: '600', marginBottom: '0.8rem' }}>
                      {mod.title}
                    </h4>
                    <p style={{ fontSize: '1rem', color: 'var(--low)', lineHeight: '1.5', marginBottom: '1.5rem' }}>
                      {mod.desc}
                    </p>
                  </div>

                  {mod.isReact ? (
                    <button 
                      onClick={() => handleModuleSelect(mod.id)}
                      style={{
                        width: '100%',
                        background: 'var(--accent)',
                        color: 'var(--black)',
                        border: 'none',
                        fontFamily: 'var(--sans)',
                        fontWeight: '600',
                        fontSize: '0.95rem',
                        padding: '0.8rem',
                        borderRadius: '6px',
                        cursor: 'pointer',
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'center',
                        gap: '0.5rem',
                        transition: 'all 0.3s'
                      }}
                      className="widget-btn"
                    >
                      Launch Slider <ChevronRight size={16} />
                    </button>
                  ) : (
                    <a 
                      href={mod.path}
                      target="_blank"
                      rel="noopener noreferrer"
                      style={{
                        width: '100%',
                        background: 'var(--surface2)',
                        border: '1px solid var(--border-hi)',
                        color: 'var(--mid)',
                        fontFamily: 'var(--sans)',
                        fontWeight: '600',
                        fontSize: '0.95rem',
                        padding: '0.8rem',
                        borderRadius: '6px',
                        cursor: 'pointer',
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'center',
                        gap: '0.5rem',
                        textDecoration: 'none',
                        transition: 'all 0.3s'
                      }}
                      className="widget-btn-secondary"
                    >
                      Open Slide Deck <ExternalLink size={16} />
                    </a>
                  )}
                </div>
              ))}
            </div>
          </div>
        </div>
      )}

      {/* SLIDE PORTAL ENGINE VIEWPORT */}
      {currentSubjectId !== null && currentModuleId !== null && (
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
              <span className="bank-title">Slide Directory</span>
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
                    background: `linear-gradient(to bottom, rgba(0,0,0,0.4), rgba(0,0,0,0.8)), url('/${currentSlide.image}')`,
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
                      <div className="console-line text-accent" style={{ marginTop: '0.8rem', borderLeftColor: 'var(--accent)' }}>✔ scanf mapped address &amp;score directly in RAM memory.</div>
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

              {/* RENDER QUIZZES AND PRACTICE TASKS */}
              {currentSlide.type === 'quiz' && (
                <div style={{ animation: 'fadeIn 0.6s' }}>
                  <div className="eyebrow">{currentSlide.eyebrow}</div>
                  <QuizCard slideId={currentSlide.question || slideIdx} question={currentSlide.question} options={currentSlide.options} />
                </div>
              )}

              {currentSlide.type === 'blank' && (
                <div style={{ animation: 'fadeIn 0.6s' }}>
                  <div className="eyebrow">{currentSlide.eyebrow}</div>
                  <h2 className="title" style={{ marginBottom: '1rem' }}>{currentSlide.title}</h2>
                  <p className="lede" style={{ marginBottom: '2rem' }}>{currentSlide.lede}</p>
                  <CodeBlank slideId={currentSlide.title || slideIdx} code={currentSlide.code} blankVal={currentSlide.blankVal} />
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

              {/* PROGRESS BAR WIDGET */}
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
