import { studyPlan } from './words.js';

const dayNumberEl = document.getElementById('day-number');
const dayThemeEl = document.getElementById('day-theme');
const dayDateEl = document.getElementById('day-date');
const wordListEl = document.getElementById('word-list');
const masteredCountEl = document.getElementById('mastered-count');
const studyMinutesEl = document.getElementById('study-minutes');

const prevDayBtn = document.getElementById('prev-day');
const nextDayBtn = document.getElementById('next-day');
const startQuizBtn = document.getElementById('start-quiz');

const quizModal = document.getElementById('quiz-modal');
const closeQuizBtn = document.getElementById('close-quiz');
const quizBody = document.getElementById('quiz-body');
const quizResult = document.getElementById('quiz-result');
const quizQuestionEl = document.getElementById('quiz-question');
const quizOptionsEl = document.getElementById('quiz-options');
const quizCurrentEl = document.getElementById('quiz-current');
const quizTotalEl = document.getElementById('quiz-total');
const quizCorrectEl = document.getElementById('quiz-correct');
const quizAccuracyEl = document.getElementById('quiz-accuracy');
const restartQuizBtn = document.getElementById('restart-quiz');

const storageKey = 'daily-words-progress-v1';
const progress = JSON.parse(localStorage.getItem(storageKey) ?? '{}');

let currentDayIndex = Number(localStorage.getItem('current-day-index') ?? 0);
if (currentDayIndex >= studyPlan.length) currentDayIndex = 0;

let activeTimer = null;
let sessionStart = Date.now();

function getDayProgress(day) {
  if (!progress[day]) {
    progress[day] = { mastered: [], seconds: 0 };
  } else if (progress[day].minutes !== undefined) {
    progress[day].seconds = progress[day].minutes;
    delete progress[day].minutes;
  }
  return progress[day];
}

function saveProgress() {
  localStorage.setItem(storageKey, JSON.stringify(progress));
}

function updateMasteredUI(day) {
  const dayProgress = getDayProgress(day);
  masteredCountEl.textContent = dayProgress.mastered.length;
  const cards = wordListEl.querySelectorAll('.word-card');
  cards.forEach((card) => {
    const term = card.dataset.term;
    card.classList.toggle('mastered', dayProgress.mastered.includes(term));
    const button = card.querySelector('.mark-btn');
    button.textContent = dayProgress.mastered.includes(term) ? '已掌握 ✅' : '标记已掌握';
  });
}

function updateStudyMinutes(day) {
  const minutes = Math.floor(getDayProgress(day).seconds / 60);
  studyMinutesEl.textContent = minutes;
}

function accumulateSessionTime(day) {
  const now = Date.now();
  const elapsedSeconds = Math.floor((now - sessionStart) / 1000);
  if (elapsedSeconds > 0) {
    getDayProgress(day).seconds += elapsedSeconds;
    sessionStart = now;
    saveProgress();
    updateStudyMinutes(day);
  }
}

function startStudyTimer(day) {
  sessionStart = Date.now();
  if (activeTimer) {
    clearInterval(activeTimer);
  }
  activeTimer = setInterval(() => {
    accumulateSessionTime(day);
  }, 60000);
}

window.addEventListener('beforeunload', () => {
  accumulateSessionTime(studyPlan[currentDayIndex].day);
});

function renderDay(index) {
  const dayData = studyPlan[index];
  if (!dayData) return;

  dayNumberEl.textContent = dayData.day;
  dayThemeEl.textContent = dayData.theme;
  dayDateEl.textContent = dayData.date;

  wordListEl.innerHTML = '';
  const template = document.getElementById('word-card-template');

  dayData.words.forEach((word) => {
    const node = template.content.cloneNode(true);
    const article = node.querySelector('.word-card');
    article.dataset.term = word.term;

    const imgEl = node.querySelector('img');
    imgEl.src = word.image;
    imgEl.alt = `${word.term} illustration`;

    node.querySelector('.word-text').textContent = word.term;
    node.querySelector('.word-phonetic').textContent = word.phonetic;
    node.querySelector('.word-meaning').textContent = word.meaning;
    node.querySelector('.word-sentence').textContent = `${word.sentence} ${word.translation}`;

    const pronounceBtn = node.querySelector('.pronounce-btn');
    pronounceBtn.addEventListener('click', () => pronounce(word.term, word.sentence));

    const markBtn = node.querySelector('.mark-btn');
    markBtn.addEventListener('click', () => toggleMastered(dayData.day, word.term));

    wordListEl.appendChild(node);
  });

  updateMasteredUI(dayData.day);
  updateStudyMinutes(dayData.day);
  startStudyTimer(dayData.day);
  localStorage.setItem('current-day-index', String(index));
}

function pronounce(term, sentence) {
  if (!('speechSynthesis' in window)) {
    alert('当前浏览器暂不支持语音播放，可以尝试在 Chrome 中打开。');
    return;
  }
  const utterance = new SpeechSynthesisUtterance(`${term}. ${sentence}`);
  utterance.lang = 'en-US';
  window.speechSynthesis.cancel();
  window.speechSynthesis.speak(utterance);
}

function toggleMastered(day, term) {
  const dayProgress = getDayProgress(day);
  const idx = dayProgress.mastered.indexOf(term);
  if (idx >= 0) {
    dayProgress.mastered.splice(idx, 1);
  } else {
    dayProgress.mastered.push(term);
  }
  saveProgress();
  updateMasteredUI(day);
}

function changeDay(offset) {
  accumulateSessionTime(studyPlan[currentDayIndex].day);
  currentDayIndex = (currentDayIndex + offset + studyPlan.length) % studyPlan.length;
  renderDay(currentDayIndex);
}

function buildQuiz(dayData) {
  const words = dayData.words;
  const questions = words.map((word) => {
    const distractors = shuffle(
      words
        .filter((other) => other.term !== word.term)
        .map((item) => item.meaning)
    ).slice(0, 3);

    const options = shuffle([word.meaning, ...distractors]);

    return {
      prompt: `“${word.term}” 的中文释义是？`,
      correct: word.meaning,
      options,
    };
  });
  return questions;
}

function shuffle(array) {
  const arr = [...array];
  for (let i = arr.length - 1; i > 0; i -= 1) {
    const j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
}

let quizState = {
  questions: [],
  current: 0,
  correct: 0,
};

function openQuiz() {
  quizState = {
    questions: buildQuiz(studyPlan[currentDayIndex]),
    current: 0,
    correct: 0,
  };
  quizTotalEl.textContent = quizState.questions.length;
  quizResult.hidden = true;
  quizBody.hidden = false;
  quizModal.hidden = false;
  renderQuizQuestion();
}

function closeQuiz() {
  quizModal.hidden = true;
}

function renderQuizQuestion() {
  const { current, questions } = quizState;
  if (current >= questions.length) {
    return showQuizResult();
  }

  const question = questions[current];
  quizCurrentEl.textContent = current + 1;
  quizQuestionEl.textContent = question.prompt;
  quizOptionsEl.innerHTML = '';

  question.options.forEach((option) => {
    const btn = document.createElement('button');
    btn.className = 'quiz-option';
    btn.type = 'button';
    btn.textContent = option;
    btn.addEventListener('click', () => handleQuizAnswer(btn, question.correct));
    quizOptionsEl.appendChild(btn);
  });
}

function handleQuizAnswer(button, correctAnswer) {
  const options = Array.from(quizOptionsEl.children);
  options.forEach((optionBtn) => {
    optionBtn.disabled = true;
    if (optionBtn.textContent === correctAnswer) {
      optionBtn.classList.add('correct');
    }
  });

  if (button.textContent === correctAnswer) {
    button.classList.add('correct');
    quizState.correct += 1;
  } else {
    button.classList.add('wrong');
  }

  setTimeout(() => {
    quizState.current += 1;
    renderQuizQuestion();
  }, 800);
}

function showQuizResult() {
  quizBody.hidden = true;
  quizResult.hidden = false;
  quizCorrectEl.textContent = quizState.correct;
  const accuracy = Math.round((quizState.correct / quizState.questions.length) * 100);
  quizAccuracyEl.textContent = Number.isNaN(accuracy) ? 0 : accuracy;
}

prevDayBtn.addEventListener('click', () => changeDay(-1));
nextDayBtn.addEventListener('click', () => changeDay(1));
startQuizBtn.addEventListener('click', openQuiz);
closeQuizBtn.addEventListener('click', () => {
  quizModal.hidden = true;
});
restartQuizBtn.addEventListener('click', () => {
  openQuiz();
});

quizModal.addEventListener('click', (event) => {
  if (event.target === quizModal) {
    closeQuiz();
  }
});

document.addEventListener('keydown', (event) => {
  if (event.key === 'Escape' && !quizModal.hidden) {
    closeQuiz();
  }
});

renderDay(currentDayIndex);
