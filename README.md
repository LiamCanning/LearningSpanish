# Hablemos — Spanish Learning Platform (A2 → B1)

A modern, interactive Spanish learning platform for intermediate learners (A2 → B1 level). Built specifically for learners in Spain seeking conversational fluency, with a focus on past/future tenses, subjunctive mood, essential grammar structures, and everyday Spanish.

## Features

✨ **9 Dedicated Sections**
- **Inicio** — Dashboard with streak tracker and section navigation
- **Hoy** — Daily word + phrase of the day (deterministic 24h refresh)
- **Tiempos Verbales** — Past, present, future, and subjunctive tenses with conjugation tables
- **Chuletas** — Grammar cheat sheets (Ser vs Estar, Por vs Para, Se constructions)
- **Vocabulario por Temas** — Themed word lists (home, food, work, travel, etc.)
- **Conectores y Discurso** — Connecting words organized by function
- **Frases y Modismos** — Situational phrases and Spanish idioms
- **Ejercicios** — Four exercise types: fill-in-the-blank, multiple choice, translation, matching
- **Mi Glosario** — Personal glossary with manual word entry and persistence

📚 **Content Coverage**
- Pretérito indefinido, imperfecto, perfecto, pluscuamperfecto
- Future simple (futuro simple) and near future (ir a + infinitivo)
- Subjunctive mood (present & past) with WEIRDO triggers
- Essential structures: reflexive/pronominal verbs, passive/impersonal se, imperativo
- 40+ connecting words (porque, sin embargo, además, etc.)
- Themed vocabulary (10 categories)
- 30+ Spanish idioms and conversational phrases

🎯 **Learning Features**
- **Word of the Day** — Large-format daily word with example and etymology tip
- **Phrase of the Day** — Daily phrase with usage context and dialogue
- **4 Exercise Types**
  - Rellena el hueco (Fill-in-the-blank conjugation)
  - Opción múltiple (Multiple choice)
  - Traducción (Spanish translation typing)
  - Empareja (Tap-to-match pairs)
- **Progress Tracking** — Streak counter, exercise stats (localStorage)
- **Dark Mode** — Full dark mode support

🎨 **Design**
- Mobile-first responsive layout
- Warm Mediterranean aesthetic (terracotta, burgundy, sand)
- Glassmorphism effects on navigation
- Spanish-first UI with English translations
- Serif font (Fraunces) for Spanish hero words

## Tech Stack

- Single-file HTML/React app (no build step)
- React 18 (CDN)
- Babel Standalone (inline JSX)
- Tailwind CSS (CDN)
- Google Fonts (Inter + Fraunces)
- localStorage for persistence

## Access

**Live App**: https://liamcanning.github.io/LearningSpanish/

Open `index.html` in any modern browser. No installation required.

## Getting Started

1. Open the app
2. Start with **Hoy** to see today's word and phrase
3. Explore each section by tapping the section tiles on **Inicio**
4. Add words to **Mi Glosario** as you learn
5. Practice with **Ejercicios** to reinforce topics

## Data Persistence

All personal glossary entries and progress are saved to your browser's localStorage:
- `hablemos.glossary` — Personal word entries
- `hablemos.dark` — Dark mode preference
- `hablemos.streak` — Learning streak

## Customization

The app is a single `index.html` file. To customize:
- Edit the `WORDS_OF_DAY`, `PHRASES_OF_DAY`, `TENSES`, `VOCAB_THEMES`, etc. arrays at the top
- Modify the color palette in the Tailwind config section
- All changes are applied on page reload

## Level & Context

Designed for A2→B1 learners living in Spain, with emphasis on:
- Castilian Spanish (tú/vosotros forms)
- Colloquial and conversational phrases
- Past tense storytelling (indefinido + imperfecto)
- Subjunctive mood triggers and usage
- Authentic Spanish idioms and fillers

---

**Made for learning Spanish the real way.** 🇪🇸

