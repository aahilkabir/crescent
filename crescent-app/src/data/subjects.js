export const subjects = [
  {
    id: 'pps',
    title: 'Programming for Problem Solving',
    code: 'PPS (C Programming)',
    desc: 'Master C programming logic, variables, loops, arrays, and standard lab manual exercises with visual tracers.',
    icon: 'code',
    modules: [
      { id: 'intro', title: 'Module 1: C Fundamentals', desc: 'Origins, preprocessors, variables, operators, and preprocessor link sections.', isReact: true },
      { id: 'control', title: 'Module 3: Control & Arrays', desc: 'if-else loops, arrays, and string garland NULL check.', isReact: true },
      { id: 'lab', title: 'PPS Lab Manual Activities', desc: '20 practical challenges with live swapping, bank tracing, stack frames.', isReact: true }
    ]
  },
  {
    id: 'dt',
    title: 'Design Thinking',
    code: 'GEE 1102',
    desc: 'Learn empathy mapping, brainstorming, creative prototyping, and design frameworks.',
    icon: 'lightbulb',
    modules: [
      { title: 'Module 1 Activity Deck', path: '/HTML/Design Thinking/GEE 1102 - Design Thinking Module 1 Activity Deck.html', desc: 'Empathy maps, user journeys, and creative brainstorming sessions.' },
      { title: 'Design Thinking CAT 1', path: '/HTML/Design Thinking/GEE 1102 - Design Thinking CAT 1.html', desc: 'Continuous assessment test evaluations and presentation slides.' }
    ]
  },
  {
    id: 'ai',
    title: 'AI Foundations',
    code: 'CSE AI-F',
    desc: 'Explore neural networks, machine learning models, training algorithms, and AI frameworks.',
    icon: 'cpu',
    modules: [
      { title: 'AI Foundations Seminar - Final', path: '/HTML/AI Foundations/AI Foundations Seminar - Final.html', desc: 'Comprehensive final seminar slides for AI and ML architectures.' },
      { title: 'AI Foundations Seminar - Simplified', path: '/HTML/AI Foundations/AI Foundations Seminar - Simplified.html', desc: 'Easy-to-understand slides covering neural net workflows.' },
      { title: 'AI Foundations Seminar', path: '/HTML/AI Foundations/AI Foundations Seminar.html', desc: 'Main presentation covering artificial intelligence fundamentals.' },
      { title: 'The Foundations', path: '/HTML/AI Foundations/The Foundations.html', desc: 'Historical context and essential mathematical concepts.' },
      { title: 'ML Foundations', path: '/HTML/AI Foundations/ml-foundations.html', desc: 'Core machine learning models, weights, and bias adjustments.' }
    ]
  },
  {
    id: 'id',
    title: 'Industry Developer',
    code: 'CSE ID-B',
    desc: 'Think like a professional software engineer, learning git, build tools, and software architecture.',
    icon: 'briefcase',
    modules: [
      { title: 'Think Like an Industry Developer - New Blueprint', path: '/HTML/Industry Developer/Think Like an Industry Developer - New Blueprint.html', desc: 'Modern industry engineering skills blueprint.' },
      { title: 'Think Like an Industry Developer', path: '/HTML/Industry Developer/Think Like an Industry Developer.html', desc: 'Interactive developer training slides.' },
      { title: 'TLID Presentation', path: '/HTML/Industry Developer/TLID.html', desc: 'Think Like an Industry Developer core syllabus.' }
    ]
  }
];
