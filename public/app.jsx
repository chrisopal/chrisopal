const { useState, useEffect } = React;

const API_BASE = window.__API_BASE__ || 'http://localhost:8000';

const difficultyOptions = [
  { value: 'junior', label: '初中' },
  { value: 'senior', label: '高中' },
  { value: 'cet4', label: '大学 CET-4' },
  { value: 'cet6', label: '大学 CET-6' },
  { value: 'ielts', label: '雅思 IELTS' },
  { value: 'toefl', label: '托福 TOEFL' },
];

const questionTypeLabel = {
  multiple_choice: '选择题',
  cloze: '完形填空',
  reading: '阅读理解',
};

function formatDate(date) {
  return date.toISOString().split('T')[0];
}

async function request(path, options) {
  const resp = await fetch(`${API_BASE}${path}`, {
    headers: { 'Content-Type': 'application/json' },
    credentials: 'same-origin',
    ...options,
  });
  if (!resp.ok) {
    const text = await resp.text();
    throw new Error(text || '请求失败');
  }
  const contentType = resp.headers.get('content-type');
  if (contentType && contentType.includes('application/json')) {
    return resp.json();
  }
  return resp.text();
}

function pronounce(word) {
  if (!window.speechSynthesis) return;
  const utterance = new SpeechSynthesisUtterance(word);
  utterance.lang = 'en-US';
  window.speechSynthesis.speak(utterance);
}

function SettingsPanel({ config, onSave, saving, selectedDate, onChangeDate }) {
  const [draft, setDraft] = useState(() => config || { difficulty: 'junior', words_per_day: 10 });

  useEffect(() => {
    if (config) {
      setDraft(config);
    }
  }, [config]);

  if (!config) return null;

  const workingDraft = draft || config;

  return (
    <div className="controls-grid">
      <div className="control-card">
        <h3>背诵难度</h3>
        <select
          value={workingDraft.difficulty}
          onChange={(event) =>
            setDraft((prev) => ({ ...(prev || config), difficulty: event.target.value }))
          }
        >
          {difficultyOptions.map((option) => (
            <option key={option.value} value={option.value}>
              {option.label}
            </option>
          ))}
        </select>
        <button
          className="primary-btn"
          onClick={() => onSave(draft)}
          disabled={saving}
        >
          {saving ? '保存中…' : '应用难度'}
        </button>
      </div>

      <div className="control-card">
        <h3>每日单词量</h3>
        <input
          type="number"
          min="5"
          max="30"
          value={workingDraft.words_per_day}
          onChange={(event) =>
            setDraft((prev) => ({
              ...(prev || config),
              words_per_day: Number(event.target.value),
            }))
          }
        />
        <button
          className="primary-btn"
          onClick={() => onSave(draft)}
          disabled={saving}
        >
          {saving ? '保存中…' : '更新数量'}
        </button>
      </div>

      <div className="control-card">
        <h3>学习日历</h3>
        <input
          type="date"
          value={selectedDate}
          onChange={(event) => onChangeDate(event.target.value)}
        />
        <p className="word-scene">
          支持自动复习：学习后的下一天会加入上一日未掌握单词。
        </p>
      </div>
    </div>
  );
}

function WordCard({
  word,
  mastered,
  onToggleMastered,
  isFavorite,
  onToggleFavorite,
  showMasterToggle = true,
}) {
  return (
    <article className="word-card">
      <div className="word-header">
        <div className="word-title">
          <h3>{word.term}</h3>
          <span>{word.phonetic}</span>
        </div>
        <button
          className="secondary-btn"
          onClick={() => pronounce(word.term)}
          aria-label={`${word.term} 发音`}
        >
          🔊 发音
        </button>
      </div>
      <img src={word.image} alt={word.term} className="word-image" loading="lazy" />
      <p className="word-scene">场景：{word.scene}</p>
      <p className="word-meaning">释义：{word.meaning}</p>
      <p className="word-example">例句：{word.example}</p>
      <div className="word-actions">
        {showMasterToggle && (
          <button className="secondary-btn" onClick={() => onToggleMastered(word.id)}>
            {mastered ? '✅ 已掌握' : '标记已掌握'}
          </button>
        )}
        <button className="secondary-btn" onClick={() => onToggleFavorite(word)}>
          {isFavorite ? '★ 已收藏' : '☆ 收藏'}
        </button>
      </div>
    </article>
  );
}

function WordSection({ title, words, masteredSet, onToggleMastered, favorites, onToggleFavorite }) {
  if (!words.length) return null;
  return (
    <section>
      <h2 className="section-heading">{title}</h2>
      <div className="word-grid">
        {words.map((word) => (
          <WordCard
            key={word.id}
            word={word}
            mastered={masteredSet.has(word.id)}
            onToggleMastered={onToggleMastered}
            isFavorite={favorites.has(word.id)}
            onToggleFavorite={onToggleFavorite}
          />
        ))}
      </div>
    </section>
  );
}

function FavoritesPanel({ favoriteWords, onToggleFavorite }) {
  if (!favoriteWords.length) return null;
  return (
    <section className="favorites-panel">
      <h2 className="section-heading">我的收藏</h2>
      <div className="word-grid">
        {favoriteWords.map((word) => (
          <WordCard
            key={`fav-${word.id}`}
            word={word}
            mastered={false}
            onToggleMastered={() => {}}
            isFavorite={true}
            onToggleFavorite={onToggleFavorite}
            showMasterToggle={false}
          />
        ))}
      </div>
    </section>
  );
}

function QuizModal({
  open,
  onClose,
  quizState,
  setQuizState,
  onSubmitResults,
}) {
  const [inputValue, setInputValue] = useState('');

  useEffect(() => {
    if (!open) {
      setInputValue('');
    }
  }, [open, quizState.index]);

  if (!open) return null;

  const { questions, index, finished, correctCount, answers } = quizState;
  const current = questions[index];
  const total = questions.length;
  const currentType = current ? current.type : null;
  const currentTypeLabel =
    currentType && questionTypeLabel[currentType]
      ? questionTypeLabel[currentType]
      : '巩固练习';

  const handleAnswer = (value) => {
    if (!current) return;
    const isCorrect =
      current.type === 'cloze'
        ? value.trim().toLowerCase() === current.answer.toLowerCase()
        : value === current.answer;

    const nextAnswers = [
      ...answers,
      {
        questionId: current.id,
        wordId: current.wordId,
        selected: value,
        correct: isCorrect,
        type: current.type,
      },
    ];

    const nextState = {
      questions,
      index: index + 1,
      finished: index + 1 >= total,
      correctCount: correctCount + (isCorrect ? 1 : 0),
      answers: nextAnswers,
    };

    setInputValue('');
    setQuizState(nextState);

    if (nextState.finished) {
      onSubmitResults(nextState);
    }
  };

  return (
    <div className="quiz-modal" role="dialog" aria-modal="true">
      <div className="quiz-dialog">
        <div className="quiz-header">
          <h3>今日测验 · {currentTypeLabel}</h3>
          <button className="close-btn" onClick={onClose} aria-label="关闭测验">
            ×
          </button>
        </div>
        {!finished && current && (
          <div className="quiz-body">
            <p className="quiz-progress">
              题目 {index + 1} / {total} · 单词 {current.term}
            </p>
            {current.type === 'reading' && (
              <div className="quiz-feedback">
                <strong>阅读材料：</strong>
                <p>{current.passage}</p>
              </div>
            )}
            <p className="quiz-question">{current.prompt}</p>
            {current.type === 'multiple_choice' && (
              <div className="quiz-options">
                {current.options.map((option) => (
                  <button
                    key={option.value}
                    className="quiz-option"
                    onClick={() => handleAnswer(option.value)}
                  >
                    <strong>{option.value}</strong> · {option.label}
                  </button>
                ))}
              </div>
            )}
            {current.type === 'reading' && (
              <div className="quiz-options">
                {current.options.map((option) => (
                  <button
                    key={option.value}
                    className="quiz-option"
                    onClick={() => handleAnswer(option.value)}
                  >
                    <strong>{option.value}</strong> · {option.label}
                  </button>
                ))}
              </div>
            )}
            {current.type === 'cloze' && (
              <div className="quiz-options">
                <input
                  className="quiz-input"
                  value={inputValue}
                  onChange={(event) => setInputValue(event.target.value)}
                  placeholder="输入答案"
                />
                <button
                  className="primary-btn"
                  onClick={() => inputValue && handleAnswer(inputValue)}
                >
                  提交
                </button>
              </div>
            )}
          </div>
        )}
        {finished && (
          <div className="quiz-body">
            <h3>测验完成 ✅</h3>
            <p className="quiz-feedback">
              正确 {correctCount} / {total}，正确率 {Math.round((correctCount / total) * 100)}%
            </p>
            <button className="primary-btn" onClick={onClose}>
              关闭
            </button>
          </div>
        )}
      </div>
    </div>
  );
}

function StatsPanel({ stats, loading }) {
  if (!stats) return null;
  return (
    <section className="stats-panel">
      <h2 className="section-heading">学习统计</h2>
      {loading ? (
        <p>统计加载中…</p>
      ) : (
        <React.Fragment>
          <div className="stats-grid">
            <div className="stat-row">
              <span>学习单词数</span>
              <strong>{stats.learned_words}</strong>
            </div>
            <div className="stat-row">
              <span>错误单词数</span>
              <strong>{stats.mistake_words}</strong>
            </div>
            <div className="stat-row">
              <span>重点复习</span>
              <strong>{stats.review_words}</strong>
            </div>
          </div>
          <div className="analysis-box">
            <strong>AI 学情分析：</strong>
            <p>{stats.ai_analysis}</p>
          </div>
        </React.Fragment>
      )}
    </section>
  );
}

function App() {
  const [config, setConfig] = useState(null);
  const [selectedDate, setSelectedDate] = useState(() => formatDate(new Date()));
  const [wordsData, setWordsData] = useState({ new_words: [], review_words: [], quiz_items: [] });
  const [loadingWords, setLoadingWords] = useState(false);
  const [savingConfig, setSavingConfig] = useState(false);
  const [mastered, setMastered] = useState(new Set());
  const [quizOpen, setQuizOpen] = useState(false);
  const [quizState, setQuizState] = useState({
    questions: [],
    index: 0,
    finished: false,
    correctCount: 0,
    answers: [],
  });
  const [stats, setStats] = useState(null);
  const [statsLoading, setStatsLoading] = useState(false);
  const [favorites, setFavorites] = useState(new Set());
  const [favoriteWords, setFavoriteWords] = useState([]);

  const refreshStats = async (date) => {
    try {
      setStatsLoading(true);
      const data = await request(`/api/stats?date=${date}`);
      setStats(data);
    } catch (error) {
      console.error(error);
    } finally {
      setStatsLoading(false);
    }
  };

  const refreshWords = async (date) => {
    try {
      setLoadingWords(true);
      const data = await request(`/api/words?date=${date}`);
      setWordsData(data);
      setMastered(new Set(data.default_mastered || []));
      setFavorites(new Set(data.favorites || []));
      setFavoriteWords(data.favorite_words || []);
    } catch (error) {
      console.error(error);
    } finally {
      setLoadingWords(false);
    }
  };

  useEffect(() => {
    request('/api/config')
      .then((data) => {
        setConfig(data.config);
        if (data.today) {
          setSelectedDate(data.today);
        }
        if (data.favorites) {
          setFavorites(new Set(data.favorites.map((item) => item.id)));
          setFavoriteWords(data.favorites);
        }
      })
      .catch((error) => console.error(error));
  }, []);

  useEffect(() => {
    if (config) {
      refreshWords(selectedDate);
      refreshStats(selectedDate);
    }
  }, [config, selectedDate]);

  const masteredCount = mastered.size;
  const newWordCount = wordsData && Array.isArray(wordsData.new_words) ? wordsData.new_words.length : 0;
  const reviewWordCount = wordsData && Array.isArray(wordsData.review_words) ? wordsData.review_words.length : 0;
  const totalWords = newWordCount + reviewWordCount;
  const quizItems = wordsData && Array.isArray(wordsData.quiz_items) ? wordsData.quiz_items : [];
  const quizItemCount = quizItems.length;
  const selectedDifficulty = config ? config.difficulty : null;
  const selectedDifficultyOption = difficultyOptions.find((item) => item.value === selectedDifficulty);
  const selectedDifficultyLabel = selectedDifficultyOption ? selectedDifficultyOption.label : '—';

  const handleToggleMastered = (wordId) => {
    setMastered((prev) => {
      const next = new Set(prev);
      if (next.has(wordId)) {
        next.delete(wordId);
      } else {
        next.add(wordId);
      }
      return next;
    });
  };

  const handleToggleFavorite = async (word) => {
    try {
      const fav = !favorites.has(word.id);
      const body = JSON.stringify({ word_id: word.id, favorite: fav });
      await request('/api/favorite', { method: 'POST', body });
      setFavorites((prev) => {
        const next = new Set(prev);
        if (fav) {
          next.add(word.id);
        } else {
          next.delete(word.id);
        }
        return next;
      });
      setFavoriteWords((prev) => {
        if (fav) {
          return [...prev.filter((item) => item.id !== word.id), word];
        }
        return prev.filter((item) => item.id !== word.id);
      });
    } catch (error) {
      console.error(error);
    }
  };

  const handleSaveConfig = async (nextConfig) => {
    setSavingConfig(true);
    try {
      const body = JSON.stringify(nextConfig);
      const data = await request('/api/config', { method: 'POST', body });
      setConfig(data.config);
      await refreshWords(selectedDate);
    } catch (error) {
      console.error(error);
    } finally {
      setSavingConfig(false);
    }
  };

  const buildQuiz = () => {
    const items = quizItems;
    setQuizState({ questions: items, index: 0, finished: false, correctCount: 0, answers: [] });
    setQuizOpen(true);
  };

  const handleCloseQuiz = () => {
    setQuizOpen(false);
    setQuizState({ questions: [], index: 0, finished: false, correctCount: 0, answers: [] });
  };

  const handleSubmitResults = async (state) => {
    try {
      const payload = {
        date: selectedDate,
        answers: state.answers,
        total: state.questions.length,
      };
      const data = await request('/api/progress', {
        method: 'POST',
        body: JSON.stringify(payload),
      });
      setStats(data.stats);
      if (data.review_words) {
        setWordsData((prev) => ({ ...prev, review_words: data.review_words }));
      }
      if (data.favorites) {
        setFavoriteWords(data.favorites);
        setFavorites(new Set(data.favorites.map((item) => item.id)));
      }
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="app-shell">
      <header className="app-header">
        <h1 className="app-title">词海日程 · 智能背词平台</h1>
        <p className="app-subtitle">
          React 前端 × Python 后端 —— 支持多种考试难度、每日单词量自定义、智能复习、收藏、以及 AI 学情分析。兼容移动端、网页与小程序视图。
        </p>
      </header>

      <SettingsPanel
        config={config}
        onSave={handleSaveConfig}
        saving={savingConfig}
        selectedDate={selectedDate}
        onChangeDate={setSelectedDate}
      />

      <section className="summary-bar">
        <div className="items">
          <div className="summary-chip">
            <span>今日掌握</span>
            <strong>
              {masteredCount} / {totalWords}
            </strong>
          </div>
          <div className="summary-chip">
            <span>学习日期</span>
            <strong>{selectedDate}</strong>
          </div>
          <div className="summary-chip">
            <span>当前难度</span>
            <strong>{selectedDifficultyLabel}</strong>
          </div>
          <div className="summary-chip">
            <span>测验题量</span>
            <strong>{quizItemCount}</strong>
          </div>
        </div>
        <div>
          <button className="primary-btn" onClick={buildQuiz} disabled={loadingWords || !quizItemCount}>
            发起今日测验
          </button>
        </div>
      </section>

      {loadingWords ? (
        <p>单词加载中…</p>
      ) : (
        <React.Fragment>
          <WordSection
            title="今日新词"
            words={wordsData.new_words || []}
            masteredSet={mastered}
            onToggleMastered={handleToggleMastered}
            favorites={favorites}
            onToggleFavorite={handleToggleFavorite}
          />
          <WordSection
            title="回顾复习"
            words={wordsData.review_words || []}
            masteredSet={mastered}
            onToggleMastered={handleToggleMastered}
            favorites={favorites}
            onToggleFavorite={handleToggleFavorite}
          />
        </React.Fragment>
      )}

      <FavoritesPanel favoriteWords={favoriteWords} onToggleFavorite={handleToggleFavorite} />

      <StatsPanel stats={stats} loading={statsLoading} />

      <QuizModal
        open={quizOpen}
        onClose={handleCloseQuiz}
        quizState={quizState}
        setQuizState={setQuizState}
        onSubmitResults={handleSubmitResults}
      />
    </div>
  );
}

ReactDOM.createRoot(document.getElementById('root')).render(<App />);
