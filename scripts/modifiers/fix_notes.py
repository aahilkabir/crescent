import os
# Dynamic PROJECT_ROOT resolution
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = SCRIPT_DIR
while os.path.basename(PROJECT_ROOT) in ["generators", "modifiers", "scripts", "utilities", "parts"]:
    PROJECT_ROOT = os.path.dirname(PROJECT_ROOT)

import json
import re

with open(os.path.join(PROJECT_ROOT, "HTML", "AI Foundations", "The Foundations.html"), "r", encoding="utf-8") as f:
    html = f.read()

# Fix overlapping active slide
html = html.replace('<section class="slide center active"><div class="glow g3"></div>', '<section class="slide center"><div class="glow g3"></div>')

notes = [
  "",
  "<b>The Rare Reality:</b> In 2015, a 9.0 CGPA got you the job. Today, an 8.5 or 9.0 just puts you in a pile of 10,000 identical resumes. 85% of Fortune 500 companies now use ATS (Applicant Tracking Systems) powered by LLMs. Your resume isn't being read by a human HR manager; it's being parsed by a machine looking for semantic vector similarity to the job description. If you don't know how to build AI, you don't even know how the machine judging you works.",
  "<b>Speaker Point:</b> People use 'AI' for everything. But basic AI is just rules. If X happens, do Y. A smart washing machine weighs your clothes and adds water. It's 'smart', but it's not learning. It's just following a script.",
  "<b>Deep Insight:</b> In traditional programming, humans write the logic to turn data into answers. In Machine Learning, humans provide the data and the answers, and the machine writes the <i>logic</i>. It flips the paradigm of computing upside down.",
  "<b>Speaker Point:</b> Imagine a massive corporate office. The intern at the bottom just looks at edges of an image. They pass it to the manager who sees shapes. They pass it to the CEO who says 'That's a cat'. That hierarchy of layers is Deep Learning.",
  "<b>The Rare Fact:</b> Generative AI relies on the concept of 'Latent Space.' When it cooks a new Dosa, it's not picking pieces of old Dosas. It is finding a completely empty coordinate in mathematical space that <i>represents</i> Dosa-ness, and pulling it into reality. It creates from the 'in-between' spaces.",
  "<b>Speaker Point:</b> When an interviewer asks you the difference, tell them they are nested. GenAI is inside Deep Learning, which is inside ML, which is inside AI. Draw these dolls on a whiteboard, and you beat 70% of the candidates.",
  "<b>Speaker Point:</b> Take a photo of this slide. This is your mental map. If anyone ever tries to confuse you with buzzwords, bring this up. AI is the behavior, ML is the method, DL is the architecture, and GenAI is the final creative product.",
  "<b>Speaker Point:</b> You have the past 10 years of Anna University question papers <i>and</i> the answer keys. You study both until you spot the pattern. The AI does the exact same thing with labeled data.",
  "<b>Speaker Point:</b> Your mom is out. You have to clean the room. Nobody tells you what the groups are, but you naturally put all the shirts in one pile, and books in another. The AI clusters raw data exactly like this without an answer key.",
  "<b>Speaker Point:</b> You drop into Pochinki. You make a mistake, you die (penalty). You do it right, you get a Chicken Dinner (reward). Over millions of games, the AI learns to survive. This is how self-driving cars learn.",
  "<b>Speaker Point:</b> People think ChatGPT reads English. It doesn't. It shatters your words into numbers called Tokens. 'Hamburger' isn't food to the AI, it's three numbers: Ham, bur, ger. When OpenAI charges you money, they don't charge by the word, they charge by the puzzle piece.",
  "<b>Speaker Point:</b> How does the AI remember facts? Through parameters. Think of them as tiny mathematical knobs. GPT-4 has over a <i>Trillion</i> of these knobs. The reason Nvidia is worth $3 Trillion is because they are the only company on Earth who figured out how to build a silicon chip that can turn a trillion knobs in less than a second.",
  "<b>Speaker Point:</b> You don't always have to pay OpenAI. The future is Open Source. Companies like Meta are releasing models (like Llama-3) that you can download and run on your own laptop for free. If you want to protect your company's private data, you build Open Source.",
  "",
  "<b>The Rare Fact:</b> Pitts was a runaway 15-year-old prodigy. He and Warren McCulloch created the first mathematical model of a neural network in 1943. <br><br><b>The Tragedy:</b> Later in life, after a bitter misunderstanding led to him being fired from MIT, Pitts burned all his research papers, refused his PhD, and drank himself to death. The man who laid the mathematical foundation for every AI today died completely forgotten.",
  "<b>The Rare Fact:</b> The 'Perceptron' wasn't just code. It was a <i>massive physical machine</i> (The Mark I Perceptron). It had 400 photocells for 'eyes' and used physical electric motors to turn dials (potentiometers) to adjust the 'weights.' It literally wired itself.",
  "<b>The Rare Fact:</b> The book that destroyed AI funding was written by Marvin Minsky. Minsky and Frank Rosenblatt went to the exact same high school. They were childhood rivals. Minsky literally destroyed his high school rival's life work.",
  "<b>The Rare Fact:</b> While the US and UK gave up, Ivakhnenko, working behind the Iron Curtain in Soviet Ukraine, figured out how to train networks 8 layers deep by building them up like polynomials. He invented Deep Learning 20 years before the West caught on.",
  "<b>The Rare Fact:</b> Created by Joseph Weizenbaum, ELIZA was the first chatbot. Weizenbaum's own secretary, who <i>knew</i> it was just a dumb program, asked Weizenbaum to leave the room so she could tell the machine her deep personal secrets. Weizenbaum was so horrified that he spent the rest of his life aggressively campaigning <i>against</i> AI.",
  "<b>The Rare Fact:</b> Before 2008, Neural Networks were trained on CPUs and took months. Andrew Ng and his team at Stanford were among the first to realize that GPUs (graphics cards built for video games) were mathematically perfect for Neural Networks. They achieved a 70x speedup. That single realization created the modern AI boom.",
  "<b>The Rare Fact:</b> OpenAI was originally founded as a non-profit to save humanity from Google. Sam Altman realized you couldn't beat Google without billions of dollars for GPUs. He engineered a controversial 'capped-profit' transition, took $10B from Microsoft, and launched ChatGPT.",
  "",
  "<b>Speaker Point:</b> A vector is just a dot in a Kolam. Words, images, audio—AI turns all of it into coordinates. It understands meaning purely by measuring the distance between dots.",
  "<b>The Rare Fact:</b> Word Embeddings (Word2Vec) were invented by Tomas Mikolov at Google in 2013. The crazy part? He wasn't trying to make machines understand language! He was just trying to compress data to save server space. <code>King - Man + Woman = Queen</code> was an <i>accident</i> of compression!",
  "<b>Speaker Point:</b> If the vector is the raw rice, the Matrix is the grinder. It stretches, squashes, and transforms the data.",
  "<b>The Rare Fact:</b> James Joseph Sylvester coined the mathematical term 'Matrix' in 1850. He chose the word 'Matrix' (which comes from the Latin word for <i>womb</i>) because he saw it as a pregnant vessel where numbers grew. <br><br><b>Speaker Point:</b> A 19th-century mathematician looked at numbers in a grid and called it a womb. Today, 175 years later, that exact grid is giving birth to Artificial Intelligence.",
  "<b>Speaker Point:</b> Let's stop talking theory. If I asked you to build a Gemini-style AI to translate ancient Tamil documents contextually, how would you do it?",
  "<b>Speaker Point:</b> 1. The Recipe: We gather the Tamil/English pairs, shatter them into Tokens, plot them as Vector coordinates, and feed them into a Transformer engine.",
  "<b>Speaker Point:</b> 2. The Tools: We don't code from scratch. We go to Hugging Face to download the base, use PyTorch to do the math, and CUDA to talk to the GPU.",
  "<b>Speaker Point:</b> 3. The Execution: The AI guesses the translation, we calculate how wrong it was (Loss), and we Backpropagate to turn the knobs (Parameters) until it gets it right.",
  "<b>Speaker Point:</b> 4. The Skills: You don't need a PhD. You need Python, Math Intuition, and System Design to stop the server from melting.",
  "<b>Speaker Point:</b> Take photos of these. If you want intuition, read Grokking.",
  "<b>Speaker Point:</b> If you want the Bible, read Goodfellow.",
  "<b>Speaker Point:</b> If you want the raw math, read Bishop.",
  "<b>Speaker Point:</b> For blogs, if you aren't watching Andrej Karpathy's 'Zero to Hero' series, you are already falling behind the curve.",
  "<b>Speaker Point:</b> Read Lilian Weng's research for the absolute cutting edge.",
  "<b>Speaker Point:</b> Let's do a reality check. You sit in an interview in 2026. They don't ask you what AI stands for. They ask you why your validation loss is spiking, or how to scale a vector DB to 10 million embeddings. If you just know how to type prompts into ChatGPT, the interview is over in 30 seconds.",
  "<b>Speaker Point:</b> API wrappers are dead. Being a 'prompt engineer' is a temporary job. You need to understand the architecture.",
  "<b>The Deep Insight:</b> AI is currently moving from the 'Discovery' phase to the 'Engineering' phase. We don't need 10,000 more researchers trying to build a better GPT-4. We need 1,000,000 engineers who know how to plug GPT-4 into a bank's database securely (RAG). You need breadth, and you need extreme vertical depth in one area.",
  "<b>Speaker Point:</b> Group A gets automated. Group B builds the automation. Claim your seat in the founding cohort. Talk to me before you leave this room."
]

notes_js = "const NOTES=" + json.dumps(notes) + ";"
html = re.sub(r"const NOTES=\[\];", notes_js, html)

with open(os.path.join(PROJECT_ROOT, "HTML", "AI Foundations", "The Foundations.html"), "w", encoding="utf-8") as f:
    f.write(html)

print("Fixed overlapping slide and injected NOTES array.")
