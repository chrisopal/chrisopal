WORD_SETS = {
    "junior": [
        {
            "id": "junior-apple",
            "term": "apple",
            "phonetic": "/ˈæp.əl/",
            "meaning": "n. 苹果",
            "scene": "水果与健康饮食",
            "example": "She eats an apple every morning to stay healthy.",
            "image": "https://images.unsplash.com/photo-1570913149827-d2ac84ab3f9a?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "multiple_choice",
                    "prompt": "Which fruit is known for keeping the doctor away?",
                    "options": [
                        {"value": "A", "label": "Apple"},
                        {"value": "B", "label": "Banana"},
                        {"value": "C", "label": "Orange"},
                        {"value": "D", "label": "Grape"},
                    ],
                    "answer": "A",
                }
            ],
        },
        {
            "id": "junior-library",
            "term": "library",
            "phonetic": "/ˈlaɪ.brer.i/",
            "meaning": "n. 图书馆",
            "scene": "校园设施",
            "example": "Our school library opens at eight in the morning.",
            "image": "https://images.unsplash.com/photo-1526243741027-444d633d7365?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "cloze",
                    "prompt": "Fill in the blank: We borrowed books from the school _____.",
                    "answer": "library",
                }
            ],
        },
        {
            "id": "junior-planet",
            "term": "planet",
            "phonetic": "/ˈplæn.ɪt/",
            "meaning": "n. 行星",
            "scene": "太空与科学",
            "example": "Earth is the only planet known to support life.",
            "image": "https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "multiple_choice",
                    "prompt": "Which of the following is a planet?",
                    "options": [
                        {"value": "A", "label": "Earth"},
                        {"value": "B", "label": "Moon"},
                        {"value": "C", "label": "Comet"},
                        {"value": "D", "label": "Meteor"},
                    ],
                    "answer": "A",
                }
            ],
        },
        {
            "id": "junior-teamwork",
            "term": "teamwork",
            "phonetic": "/ˈtiːm.wɜːrk/",
            "meaning": "n. 团队合作",
            "scene": "校园生活",
            "example": "Good teamwork helps us win basketball games.",
            "image": "https://images.unsplash.com/photo-1521737604893-d14cc237f11d?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "reading",
                    "prompt": "Why did the coach praise the team?",
                    "passage": "The coach said the team played well because everyone passed the ball and helped each other score.",
                    "options": [
                        {"value": "A", "label": "They practiced alone."},
                        {"value": "B", "label": "They all wore new shoes."},
                        {"value": "C", "label": "They helped each other score."},
                        {"value": "D", "label": "They arrived late."},
                    ],
                    "answer": "C",
                }
            ],
        },
        {
            "id": "junior-weather",
            "term": "weather",
            "phonetic": "/ˈweð.ər/",
            "meaning": "n. 天气",
            "scene": "日常交流",
            "example": "The weather is sunny today, perfect for a picnic.",
            "image": "https://images.unsplash.com/photo-1501973801540-537f08ccae7b?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "cloze",
                    "prompt": "The _____ forecast says it will rain tomorrow.",
                    "answer": "weather",
                }
            ],
        },
        {
            "id": "junior-science",
            "term": "science",
            "phonetic": "/ˈsaɪ.əns/",
            "meaning": "n. 科学",
            "scene": "学科课程",
            "example": "Science experiments make the class exciting.",
            "image": "https://images.unsplash.com/photo-1559757175-5700dde675cb?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "multiple_choice",
                    "prompt": "Which subject teaches about experiments and discoveries?",
                    "options": [
                        {"value": "A", "label": "History"},
                        {"value": "B", "label": "Science"},
                        {"value": "C", "label": "Art"},
                        {"value": "D", "label": "Music"},
                    ],
                    "answer": "B",
                }
            ],
        },
        {
            "id": "junior-musician",
            "term": "musician",
            "phonetic": "/mjuːˈzɪʃ.ən/",
            "meaning": "n. 音乐家",
            "scene": "职业梦想",
            "example": "He wants to become a musician and play the guitar on stage.",
            "image": "https://images.unsplash.com/photo-1511379938547-c1f69419868d?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "multiple_choice",
                    "prompt": "Who performs music for people?",
                    "options": [
                        {"value": "A", "label": "Engineer"},
                        {"value": "B", "label": "Musician"},
                        {"value": "C", "label": "Doctor"},
                        {"value": "D", "label": "Pilot"},
                    ],
                    "answer": "B",
                }
            ],
        },
        {
            "id": "junior-mountain",
            "term": "mountain",
            "phonetic": "/ˈmaʊn.tən/",
            "meaning": "n. 山",
            "scene": "地理与旅行",
            "example": "We climbed the mountain and enjoyed the fresh air.",
            "image": "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "cloze",
                    "prompt": "They camped on the _____ to see the sunrise.",
                    "answer": "mountain",
                }
            ],
        },
        {
            "id": "junior-artist",
            "term": "artist",
            "phonetic": "/ˈɑːr.tɪst/",
            "meaning": "n. 艺术家",
            "scene": "兴趣与创意",
            "example": "The artist paints colorful pictures of city life.",
            "image": "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "multiple_choice",
                    "prompt": "Who creates paintings and drawings?",
                    "options": [
                        {"value": "A", "label": "Artist"},
                        {"value": "B", "label": "Chef"},
                        {"value": "C", "label": "Teacher"},
                        {"value": "D", "label": "Driver"},
                    ],
                    "answer": "A",
                }
            ],
        },
        {
            "id": "junior-history",
            "term": "history",
            "phonetic": "/ˈhɪs.tɔːr.i/",
            "meaning": "n. 历史",
            "scene": "学科课程",
            "example": "History lessons tell stories about the past.",
            "image": "https://images.unsplash.com/photo-1529158062015-cad636e69505?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "reading",
                    "prompt": "What do students learn in history class?",
                    "passage": "History helps students understand important events that happened many years ago and how they changed our world today.",
                    "options": [
                        {"value": "A", "label": "Future technology"},
                        {"value": "B", "label": "Past events"},
                        {"value": "C", "label": "Sports skills"},
                        {"value": "D", "label": "Cooking"},
                    ],
                    "answer": "B",
                }
            ],
        },
        {
            "id": "junior-forest",
            "term": "forest",
            "phonetic": "/ˈfɔːr.ɪst/",
            "meaning": "n. 森林",
            "scene": "自然探索",
            "example": "Birds sing loudly in the forest every morning.",
            "image": "https://images.unsplash.com/photo-1508780709619-79562169bc64?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "cloze",
                    "prompt": "We walked through the green _____.",
                    "answer": "forest",
                }
            ],
        },
        {
            "id": "junior-lesson",
            "term": "lesson",
            "phonetic": "/ˈles.ən/",
            "meaning": "n. 课；课程",
            "scene": "学校生活",
            "example": "Today's English lesson includes a fun speaking activity.",
            "image": "https://images.unsplash.com/photo-1523580846011-d3a5bc25702b?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "multiple_choice",
                    "prompt": "What do students have with their teacher each day?",
                    "options": [
                        {"value": "A", "label": "Lesson"},
                        {"value": "B", "label": "Holiday"},
                        {"value": "C", "label": "Concert"},
                        {"value": "D", "label": "Journey"},
                    ],
                    "answer": "A",
                }
            ],
        },
    ],
    "senior": [
        {
            "id": "senior-analysis",
            "term": "analysis",
            "phonetic": "/əˈnæl.ə.sɪs/",
            "meaning": "n. 分析",
            "scene": "阅读理解",
            "example": "The teacher asked for a detailed analysis of the poem.",
            "image": "https://images.unsplash.com/photo-1524995997946-a1c2e315a42f?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "multiple_choice",
                    "prompt": "What does the word analysis mean in the passage?",
                    "options": [
                        {"value": "A", "label": "总结"},
                        {"value": "B", "label": "分析"},
                        {"value": "C", "label": "记忆"},
                        {"value": "D", "label": "猜测"},
                    ],
                    "answer": "B",
                }
            ],
        },
        {
            "id": "senior-debate",
            "term": "debate",
            "phonetic": "/dɪˈbeɪt/",
            "meaning": "n./v. 辩论",
            "scene": "校园活动",
            "example": "Our class will debate the advantages of gap years.",
            "image": "https://images.unsplash.com/photo-1521737604893-d14cc237f11d?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "cloze",
                    "prompt": "The students prepared facts to win the _____.",
                    "answer": "debate",
                }
            ],
        },
        {
            "id": "senior-sustainable",
            "term": "sustainable",
            "phonetic": "/səˈsteɪ.nə.bəl/",
            "meaning": "adj. 可持续的",
            "scene": "环境保护",
            "example": "Sustainable energy sources reduce pollution.",
            "image": "https://images.unsplash.com/photo-1509395176047-4a66953fd231?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "reading",
                    "prompt": "Why are sustainable practices encouraged?",
                    "passage": "Schools promote sustainable practices such as recycling and saving electricity because they protect the environment and reduce waste.",
                    "options": [
                        {"value": "A", "label": "They are easy"},
                        {"value": "B", "label": "They save energy and protect nature"},
                        {"value": "C", "label": "They are fashionable"},
                        {"value": "D", "label": "They require no effort"},
                    ],
                    "answer": "B",
                }
            ],
        },
        {
            "id": "senior-thesis",
            "term": "thesis",
            "phonetic": "/ˈθiː.sɪs/",
            "meaning": "n. 论文；论点",
            "scene": "学术写作",
            "example": "Her graduation thesis focuses on renewable cities.",
            "image": "https://images.unsplash.com/photo-1524995997946-a1c2e315a42f?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "multiple_choice",
                    "prompt": "A thesis is best described as?",
                    "options": [
                        {"value": "A", "label": "A research paper"},
                        {"value": "B", "label": "A sports event"},
                        {"value": "C", "label": "A holiday"},
                        {"value": "D", "label": "A recipe"},
                    ],
                    "answer": "A",
                }
            ],
        },
        {
            "id": "senior-laboratory",
            "term": "laboratory",
            "phonetic": "/ləˈbɒr.ə.tɔːr.i/",
            "meaning": "n. 实验室",
            "scene": "科学研究",
            "example": "The chemistry laboratory requires safety goggles at all times.",
            "image": "https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "cloze",
                    "prompt": "Students wore gloves in the chemistry _____.",
                    "answer": "laboratory",
                }
            ],
        },
        {
            "id": "senior-innovation",
            "term": "innovation",
            "phonetic": "/ˌɪn.əˈveɪ.ʃən/",
            "meaning": "n. 创新",
            "scene": "科技竞赛",
            "example": "Innovation drives new apps that improve learning.",
            "image": "https://images.unsplash.com/photo-1545239351-1141bd82e8a6?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "multiple_choice",
                    "prompt": "Innovation most nearly means?",
                    "options": [
                        {"value": "A", "label": "Tradition"},
                        {"value": "B", "label": "Imitation"},
                        {"value": "C", "label": "Creativity"},
                        {"value": "D", "label": "Restriction"},
                    ],
                    "answer": "C",
                }
            ],
        },
        {
            "id": "senior-literary",
            "term": "literary",
            "phonetic": "/ˈlɪt.ər.ər.i/",
            "meaning": "adj. 文学的",
            "scene": "阅读课",
            "example": "The literary club analyzes classic novels each week.",
            "image": "https://images.unsplash.com/photo-1463320726281-696a485928c7?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "cloze",
                    "prompt": "They organized a _____ festival celebrating novels.",
                    "answer": "literary",
                }
            ],
        },
        {
            "id": "senior-mentor",
            "term": "mentor",
            "phonetic": "/ˈmen.tɔːr/",
            "meaning": "n. 导师",
            "scene": "学习支持",
            "example": "A mentor guides new students through campus life.",
            "image": "https://images.unsplash.com/photo-1521737604893-d14cc237f11d?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "multiple_choice",
                    "prompt": "A mentor is someone who?",
                    "options": [
                        {"value": "A", "label": "Needs help"},
                        {"value": "B", "label": "Provides guidance"},
                        {"value": "C", "label": "Organizes parties"},
                        {"value": "D", "label": "Sells products"},
                    ],
                    "answer": "B",
                }
            ],
        },
        {
            "id": "senior-perspective",
            "term": "perspective",
            "phonetic": "/pərˈspek.tɪv/",
            "meaning": "n. 观点；角度",
            "scene": "写作表达",
            "example": "The article presents a global perspective on education.",
            "image": "https://images.unsplash.com/photo-1489515217757-5fd1be406fef?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "reading",
                    "prompt": "What does perspective mean in the passage?",
                    "passage": "When students travel abroad, they gain a new perspective because they see problems from different cultural angles.",
                    "options": [
                        {"value": "A", "label": "Vacation"},
                        {"value": "B", "label": "Point of view"},
                        {"value": "C", "label": "Language"},
                        {"value": "D", "label": "Obstacle"},
                    ],
                    "answer": "B",
                }
            ],
        },
        {
            "id": "senior-research",
            "term": "research",
            "phonetic": "/rɪˈsɝːtʃ/",
            "meaning": "n./v. 研究",
            "scene": "学术任务",
            "example": "Research papers require credible sources.",
            "image": "https://images.unsplash.com/photo-1517433670267-08bbd4be8903?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "cloze",
                    "prompt": "They spent weeks doing market _____.",
                    "answer": "research",
                }
            ],
        },
        {
            "id": "senior-scholarship",
            "term": "scholarship",
            "phonetic": "/ˈskɒl.ə.ʃɪp/",
            "meaning": "n. 奖学金",
            "scene": "升学规划",
            "example": "She received a scholarship for her outstanding grades.",
            "image": "https://images.unsplash.com/photo-1523580846011-d3a5bc25702b?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "multiple_choice",
                    "prompt": "A scholarship is money given to students for?",
                    "options": [
                        {"value": "A", "label": "Travel"},
                        {"value": "B", "label": "Entertainment"},
                        {"value": "C", "label": "Education"},
                        {"value": "D", "label": "Shopping"},
                    ],
                    "answer": "C",
                }
            ],
        },
    ],
    "cet4": [
        {
            "id": "cet4-accelerate",
            "term": "accelerate",
            "phonetic": "/əkˈsel.ə.reɪt/",
            "meaning": "v. 加速",
            "scene": "科技与交通",
            "example": "The government hopes to accelerate the development of green vehicles.",
            "image": "https://images.unsplash.com/photo-1525609004556-c46c7d6cf023?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "multiple_choice",
                    "prompt": "What does accelerate mean?",
                    "options": [
                        {"value": "A", "label": "Slow down"},
                        {"value": "B", "label": "Speed up"},
                        {"value": "C", "label": "Stop"},
                        {"value": "D", "label": "Start"},
                    ],
                    "answer": "B",
                }
            ],
        },
        {
            "id": "cet4-diverse",
            "term": "diverse",
            "phonetic": "/daɪˈvɜːs/",
            "meaning": "adj. 多样的",
            "scene": "社会与文化",
            "example": "The city is known for its diverse cultural festivals.",
            "image": "https://images.unsplash.com/photo-1489515217757-5fd1be406fef?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "cloze",
                    "prompt": "Students from _____ backgrounds joined the project.",
                    "answer": "diverse",
                }
            ],
        },
        {
            "id": "cet4-efficient",
            "term": "efficient",
            "phonetic": "/ɪˈfɪʃ.ənt/",
            "meaning": "adj. 高效的",
            "scene": "工作与生产力",
            "example": "An efficient workflow saves both time and money.",
            "image": "https://images.unsplash.com/photo-1521737604893-d14cc237f11d?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "multiple_choice",
                    "prompt": "An efficient system is one that?",
                    "options": [
                        {"value": "A", "label": "Wastes energy"},
                        {"value": "B", "label": "Saves resources"},
                        {"value": "C", "label": "Creates problems"},
                        {"value": "D", "label": "Stops working"},
                    ],
                    "answer": "B",
                }
            ],
        },
        {
            "id": "cet4-finance",
            "term": "finance",
            "phonetic": "/ˈfaɪ.næns/",
            "meaning": "n./v. 金融；融资",
            "scene": "经济与管理",
            "example": "Small businesses often struggle to finance their expansion.",
            "image": "https://images.unsplash.com/photo-1483478550801-ceba5fe50e8e?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "reading",
                    "prompt": "Why do startups seek finance?",
                    "passage": "Startups seek finance to purchase equipment, hire employees, and bring products to market before they make profits.",
                    "options": [
                        {"value": "A", "label": "To reduce staff"},
                        {"value": "B", "label": "To buy equipment and grow"},
                        {"value": "C", "label": "To increase taxes"},
                        {"value": "D", "label": "To shut down"},
                    ],
                    "answer": "B",
                }
            ],
        },
        {
            "id": "cet4-graduate",
            "term": "graduate",
            "phonetic": "/ˈɡrædʒ.u.ət/",
            "meaning": "n. 毕业生；v. 毕业",
            "scene": "职业规划",
            "example": "Many graduates attend job fairs to explore opportunities.",
            "image": "https://images.unsplash.com/photo-1523580846011-d3a5bc25702b?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "cloze",
                    "prompt": "She will _____ from university next July.",
                    "answer": "graduate",
                }
            ],
        },
        {
            "id": "cet4-innovation",
            "term": "innovation",
            "phonetic": "/ˌɪn.əˈveɪ.ʃən/",
            "meaning": "n. 创新",
            "scene": "科技发展",
            "example": "Innovation keeps the company ahead of competitors.",
            "image": "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "multiple_choice",
                    "prompt": "Innovation refers to?",
                    "options": [
                        {"value": "A", "label": "Doing the same thing"},
                        {"value": "B", "label": "Creating something new"},
                        {"value": "C", "label": "Avoiding change"},
                        {"value": "D", "label": "Stopping growth"},
                    ],
                    "answer": "B",
                }
            ],
        },
        {
            "id": "cet4-logistics",
            "term": "logistics",
            "phonetic": "/ləˈdʒɪs.tɪks/",
            "meaning": "n. 物流；后勤",
            "scene": "供应链",
            "example": "Efficient logistics reduce delivery times dramatically.",
            "image": "https://images.unsplash.com/photo-1517959105821-eaf2591984c2?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "reading",
                    "prompt": "What is the role of logistics in e-commerce?",
                    "passage": "Online stores rely on logistics companies to store, package, and ship products quickly so that customers receive orders on time.",
                    "options": [
                        {"value": "A", "label": "Design websites"},
                        {"value": "B", "label": "Store and deliver goods"},
                        {"value": "C", "label": "Write advertisements"},
                        {"value": "D", "label": "Train employees"},
                    ],
                    "answer": "B",
                }
            ],
        },
        {
            "id": "cet4-neglect",
            "term": "neglect",
            "phonetic": "/nɪˈɡlekt/",
            "meaning": "v./n. 忽视",
            "scene": "社会问题",
            "example": "We should not neglect the needs of rural students.",
            "image": "https://images.unsplash.com/photo-1496307042754-b4aa456c4a2d?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "cloze",
                    "prompt": "The report warns against _____ public health.",
                    "answer": "neglect",
                }
            ],
        },
        {
            "id": "cet4-pollution",
            "term": "pollution",
            "phonetic": "/pəˈluː.ʃən/",
            "meaning": "n. 污染",
            "scene": "环境保护",
            "example": "Air pollution is a serious challenge for big cities.",
            "image": "https://images.unsplash.com/photo-1489515217757-5fd1be406fef?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "multiple_choice",
                    "prompt": "Pollution is caused by?",
                    "options": [
                        {"value": "A", "label": "Clean energy"},
                        {"value": "B", "label": "Natural parks"},
                        {"value": "C", "label": "Harmful substances"},
                        {"value": "D", "label": "Fresh air"},
                    ],
                    "answer": "C",
                }
            ],
        },
        {
            "id": "cet4-reliable",
            "term": "reliable",
            "phonetic": "/rɪˈlaɪ.ə.bəl/",
            "meaning": "adj. 可靠的",
            "scene": "职场素质",
            "example": "Reliable data supports better business decisions.",
            "image": "https://images.unsplash.com/photo-1521791136064-7986c2920216?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "cloze",
                    "prompt": "Choose a _____ source before quoting information.",
                    "answer": "reliable",
                }
            ],
        },
        {
            "id": "cet4-strategy",
            "term": "strategy",
            "phonetic": "/ˈstræt.ə.dʒi/",
            "meaning": "n. 战略；策略",
            "scene": "商业计划",
            "example": "A digital strategy helps companies reach young customers.",
            "image": "https://images.unsplash.com/photo-1521737604893-d14cc237f11d?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "reading",
                    "prompt": "Why is a clear strategy important?",
                    "passage": "Without a clear strategy, a company may waste resources on actions that do not support its goals.",
                    "options": [
                        {"value": "A", "label": "It increases confusion"},
                        {"value": "B", "label": "It helps align actions with goals"},
                        {"value": "C", "label": "It delays progress"},
                        {"value": "D", "label": "It lowers morale"},
                    ],
                    "answer": "B",
                }
            ],
        },
    ],
    "cet6": [
        {
            "id": "cet6-articulate",
            "term": "articulate",
            "phonetic": "/ɑːrˈtɪk.jə.lət/",
            "meaning": "adj./v. 善于表达的；清晰表达",
            "scene": "演讲与表达",
            "example": "She delivered an articulate speech on climate action.",
            "image": "https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "multiple_choice",
                    "prompt": "Someone who is articulate can?",
                    "options": [
                        {"value": "A", "label": "Speak clearly"},
                        {"value": "B", "label": "Run fast"},
                        {"value": "C", "label": "Sing loudly"},
                        {"value": "D", "label": "Draw well"},
                    ],
                    "answer": "A",
                }
            ],
        },
        {
            "id": "cet6-benchmark",
            "term": "benchmark",
            "phonetic": "/ˈbentʃ.mɑːrk/",
            "meaning": "n./v. 基准；对比",
            "scene": "商业分析",
            "example": "Firms benchmark their performance against industry leaders.",
            "image": "https://images.unsplash.com/photo-1556740749-887f6717d7e4?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "cloze",
                    "prompt": "They used last year's sales as a _____.",
                    "answer": "benchmark",
                }
            ],
        },
        {
            "id": "cet6-consolidate",
            "term": "consolidate",
            "phonetic": "/kənˈsɒl.ɪ.deɪt/",
            "meaning": "v. 巩固；合并",
            "scene": "企业战略",
            "example": "The company plans to consolidate its market position through mergers.",
            "image": "https://images.unsplash.com/photo-1520607162513-77705c0f0d4a?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "reading",
                    "prompt": "Why do companies consolidate operations?",
                    "passage": "During economic downturns, firms consolidate operations to reduce costs, share resources, and maintain stability.",
                    "options": [
                        {"value": "A", "label": "To increase expenses"},
                        {"value": "B", "label": "To reduce costs and stay stable"},
                        {"value": "C", "label": "To hire more staff"},
                        {"value": "D", "label": "To expand offices"},
                    ],
                    "answer": "B",
                }
            ],
        },
        {
            "id": "cet6-discrepancy",
            "term": "discrepancy",
            "phonetic": "/dɪˈskrep.ən.si/",
            "meaning": "n. 差异；不一致",
            "scene": "数据分析",
            "example": "Auditors found a discrepancy between the reports.",
            "image": "https://images.unsplash.com/photo-1556740749-887f6717d7e4?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "cloze",
                    "prompt": "The accountant noticed a _____ in the budget.",
                    "answer": "discrepancy",
                }
            ],
        },
        {
            "id": "cet6-elaborate",
            "term": "elaborate",
            "phonetic": "/iˈlæb.ə.reɪt/",
            "meaning": "v. 详尽说明；adj. 精细的",
            "scene": "学术写作",
            "example": "Please elaborate on the methodology section.",
            "image": "https://images.unsplash.com/photo-1520607162513-77705c0f0d4a?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "multiple_choice",
                    "prompt": "To elaborate is to?",
                    "options": [
                        {"value": "A", "label": "Simplify"},
                        {"value": "B", "label": "Repeat"},
                        {"value": "C", "label": "Explain in detail"},
                        {"value": "D", "label": "Ignore"},
                    ],
                    "answer": "C",
                }
            ],
        },
        {
            "id": "cet6-facilitate",
            "term": "facilitate",
            "phonetic": "/fəˈsɪl.ɪ.teɪt/",
            "meaning": "v. 促进；使便利",
            "scene": "会议与合作",
            "example": "Digital tools facilitate collaboration across time zones.",
            "image": "https://images.unsplash.com/photo-1521737604893-d14cc237f11d?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "reading",
                    "prompt": "How do digital tools facilitate teamwork?",
                    "passage": "With shared online workspaces, teams can brainstorm ideas and edit documents simultaneously, facilitating rapid decision-making.",
                    "options": [
                        {"value": "A", "label": "They slow down projects"},
                        {"value": "B", "label": "They help people work together quickly"},
                        {"value": "C", "label": "They reduce communication"},
                        {"value": "D", "label": "They replace meetings"},
                    ],
                    "answer": "B",
                }
            ],
        },
        {
            "id": "cet6-imperative",
            "term": "imperative",
            "phonetic": "/ɪmˈper.ə.tɪv/",
            "meaning": "adj. 至关重要的；n. 命令",
            "scene": "政策与社会",
            "example": "It is imperative that universities address mental health.",
            "image": "https://images.unsplash.com/photo-1475724017904-b712052c192a?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "multiple_choice",
                    "prompt": "Imperative most nearly means?",
                    "options": [
                        {"value": "A", "label": "Optional"},
                        {"value": "B", "label": "Unimportant"},
                        {"value": "C", "label": "Essential"},
                        {"value": "D", "label": "Temporary"},
                    ],
                    "answer": "C",
                }
            ],
        },
        {
            "id": "cet6-mitigate",
            "term": "mitigate",
            "phonetic": "/ˈmɪt.ɪ.ɡeɪt/",
            "meaning": "v. 缓解；减轻",
            "scene": "危机管理",
            "example": "Effective communication mitigates the impact of rumors.",
            "image": "https://images.unsplash.com/photo-1521737604893-d14cc237f11d?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "cloze",
                    "prompt": "The new policy aims to _____ traffic congestion.",
                    "answer": "mitigate",
                }
            ],
        },
        {
            "id": "cet6-resilient",
            "term": "resilient",
            "phonetic": "/rɪˈzɪl.jənt/",
            "meaning": "adj. 有弹性的；有复原力的",
            "scene": "个人品质",
            "example": "Resilient students adapt quickly to challenges.",
            "image": "https://images.unsplash.com/photo-1521791136064-7986c2920216?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "reading",
                    "prompt": "What makes a team resilient?",
                    "passage": "Teams become resilient when they learn from mistakes, support each other emotionally, and keep improving skills despite setbacks.",
                    "options": [
                        {"value": "A", "label": "Ignoring problems"},
                        {"value": "B", "label": "Learning and supporting each other"},
                        {"value": "C", "label": "Working alone"},
                        {"value": "D", "label": "Avoiding feedback"},
                    ],
                    "answer": "B",
                }
            ],
        },
        {
            "id": "cet6-subsidize",
            "term": "subsidize",
            "phonetic": "/ˈsʌb.sɪ.daɪz/",
            "meaning": "v. 补贴；资助",
            "scene": "经济政策",
            "example": "The city subsidizes public transport for students.",
            "image": "https://images.unsplash.com/photo-1521791136064-7986c2920216?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "cloze",
                    "prompt": "The government decided to _____ rural clinics.",
                    "answer": "subsidize",
                }
            ],
        },
        {
            "id": "cet6-transformative",
            "term": "transformative",
            "phonetic": "/trænsˈfɔːr.mə.tɪv/",
            "meaning": "adj. 具有变革性的",
            "scene": "教育创新",
            "example": "Online courses provide transformative learning experiences.",
            "image": "https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "reading",
                    "prompt": "Why are transformative teachers valued?",
                    "passage": "Transformative teachers design activities that change how students see problems, encouraging creativity and empathy.",
                    "options": [
                        {"value": "A", "label": "They keep everything the same"},
                        {"value": "B", "label": "They create meaningful changes"},
                        {"value": "C", "label": "They avoid interaction"},
                        {"value": "D", "label": "They focus on memorization"},
                    ],
                    "answer": "B",
                }
            ],
        },
    ],
    "ielts": [
        {
            "id": "ielts-adjacent",
            "term": "adjacent",
            "phonetic": "/əˈdʒeɪ.sənt/",
            "meaning": "adj. 毗邻的",
            "scene": "学术写作",
            "example": "The diagram shows two adjacent buildings with contrasting heights.",
            "image": "https://images.unsplash.com/photo-1505843513577-22bb7d21e455?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "multiple_choice",
                    "prompt": "If two rooms are adjacent, they are?",
                    "options": [
                        {"value": "A", "label": "Far apart"},
                        {"value": "B", "label": "Next to each other"},
                        {"value": "C", "label": "Different in color"},
                        {"value": "D", "label": "Under renovation"},
                    ],
                    "answer": "B",
                }
            ],
        },
        {
            "id": "ielts-biodiversity",
            "term": "biodiversity",
            "phonetic": "/ˌbaɪ.oʊ.dɪˈvɜːr.sə.t̬i/",
            "meaning": "n. 生物多样性",
            "scene": "环境类作文",
            "example": "Protecting wetlands is crucial for global biodiversity.",
            "image": "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "reading",
                    "prompt": "Why is biodiversity important?",
                    "passage": "Scientists warn that losing biodiversity weakens ecosystems, making them less able to provide food, clean water, and climate regulation.",
                    "options": [
                        {"value": "A", "label": "It increases pollution"},
                        {"value": "B", "label": "It strengthens ecosystems"},
                        {"value": "C", "label": "It reduces habitats"},
                        {"value": "D", "label": "It harms food supply"},
                    ],
                    "answer": "B",
                }
            ],
        },
        {
            "id": "ielts-coherent",
            "term": "coherent",
            "phonetic": "/koʊˈhɪr.ənt/",
            "meaning": "adj. 连贯的",
            "scene": "雅思写作评分标准",
            "example": "A coherent essay uses linking words to connect ideas smoothly.",
            "image": "https://images.unsplash.com/photo-1523240795612-9a054b0db644?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "cloze",
                    "prompt": "Use transition words to make your argument _____.",
                    "answer": "coherent",
                }
            ],
        },
        {
            "id": "ielts-deteriorate",
            "term": "deteriorate",
            "phonetic": "/dɪˈtɪr.i.ə.reɪt/",
            "meaning": "v. 恶化",
            "scene": "图表描述",
            "example": "Air quality deteriorated rapidly according to the chart.",
            "image": "https://images.unsplash.com/photo-1521791136064-7986c2920216?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "multiple_choice",
                    "prompt": "If conditions deteriorate, they?",
                    "options": [
                        {"value": "A", "label": "Improve"},
                        {"value": "B", "label": "Stay the same"},
                        {"value": "C", "label": "Get worse"},
                        {"value": "D", "label": "Disappear"},
                    ],
                    "answer": "C",
                }
            ],
        },
        {
            "id": "ielts-emission",
            "term": "emission",
            "phonetic": "/ɪˈmɪʃ.ən/",
            "meaning": "n. 排放",
            "scene": "环境趋势",
            "example": "The report highlights a sharp decline in carbon emissions.",
            "image": "https://images.unsplash.com/photo-1489515217757-5fd1be406fef?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "reading",
                    "prompt": "How can cities reduce emissions?",
                    "passage": "Cities reduce emissions by expanding public transport, encouraging cycling, and improving building efficiency.",
                    "options": [
                        {"value": "A", "label": "Increasing parking"},
                        {"value": "B", "label": "Expanding public transport"},
                        {"value": "C", "label": "Removing bike lanes"},
                        {"value": "D", "label": "Building larger roads"},
                    ],
                    "answer": "B",
                }
            ],
        },
        {
            "id": "ielts-fluctuate",
            "term": "fluctuate",
            "phonetic": "/ˈflʌk.tʃu.eɪt/",
            "meaning": "v. 波动",
            "scene": "数据描述",
            "example": "The chart shows visitor numbers fluctuating throughout the year.",
            "image": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "cloze",
                    "prompt": "Sales tend to _____ during holiday seasons.",
                    "answer": "fluctuate",
                }
            ],
        },
        {
            "id": "ielts-implement",
            "term": "implement",
            "phonetic": "/ˈɪm.plə.ment/",
            "meaning": "v. 实施",
            "scene": "政策措施",
            "example": "The city implemented strict waste management policies.",
            "image": "https://images.unsplash.com/photo-1483478550801-ceba5fe50e8e?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "multiple_choice",
                    "prompt": "To implement a plan means to?",
                    "options": [
                        {"value": "A", "label": "Discuss it"},
                        {"value": "B", "label": "Ignore it"},
                        {"value": "C", "label": "Put it into action"},
                        {"value": "D", "label": "Cancel it"},
                    ],
                    "answer": "C",
                }
            ],
        },
        {
            "id": "ielts-justify",
            "term": "justify",
            "phonetic": "/ˈdʒʌs.tə.faɪ/",
            "meaning": "v. 证明……正当",
            "scene": "大作文论证",
            "example": "You must justify your opinion with concrete evidence.",
            "image": "https://images.unsplash.com/photo-1524995997946-a1c2e315a42f?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "reading",
                    "prompt": "How can a writer justify an argument?",
                    "passage": "Writers justify arguments by citing data, referencing studies, and explaining logical connections between ideas.",
                    "options": [
                        {"value": "A", "label": "Sharing anecdotes only"},
                        {"value": "B", "label": "Using evidence and logic"},
                        {"value": "C", "label": "Adding unrelated facts"},
                        {"value": "D", "label": "Copying others"},
                    ],
                    "answer": "B",
                }
            ],
        },
        {
            "id": "ielts-notable",
            "term": "notable",
            "phonetic": "/ˈnoʊ.t̬ə.bəl/",
            "meaning": "adj. 显著的",
            "scene": "图表描述",
            "example": "There was a notable increase in renewable energy usage.",
            "image": "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "cloze",
                    "prompt": "The graph shows a _____ rise in exports.",
                    "answer": "notable",
                }
            ],
        },
        {
            "id": "ielts-substantially",
            "term": "substantially",
            "phonetic": "/səbˈstæn.ʃəl.i/",
            "meaning": "adv. 大幅度地",
            "scene": "数据趋势",
            "example": "Employment rates improved substantially after the policy.",
            "image": "https://images.unsplash.com/photo-1520607162513-77705c0f0d4a?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "multiple_choice",
                    "prompt": "Substantially is closest in meaning to?",
                    "options": [
                        {"value": "A", "label": "Slightly"},
                        {"value": "B", "label": "Barely"},
                        {"value": "C", "label": "Greatly"},
                        {"value": "D", "label": "Rarely"},
                    ],
                    "answer": "C",
                }
            ],
        },
    ],
    "toefl": [
        {
            "id": "toefl-aggregation",
            "term": "aggregation",
            "phonetic": "/ˌæɡ.rəˈɡeɪ.ʃən/",
            "meaning": "n. 聚合",
            "scene": "托福听力/阅读",
            "example": "The lecture explained the aggregation of sediments in river deltas.",
            "image": "https://images.unsplash.com/photo-1517959105821-eaf2591984c2?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "reading",
                    "prompt": "What does aggregation describe in geology?",
                    "passage": "Aggregation occurs when mineral particles stick together, forming larger structures that eventually build river deltas.",
                    "options": [
                        {"value": "A", "label": "Particles separating"},
                        {"value": "B", "label": "Particles sticking together"},
                        {"value": "C", "label": "Water evaporating"},
                        {"value": "D", "label": "Plants decaying"},
                    ],
                    "answer": "B",
                }
            ],
        },
        {
            "id": "toefl-catastrophic",
            "term": "catastrophic",
            "phonetic": "/ˌkæt̬.əˈstrɒf.ɪk/",
            "meaning": "adj. 灾难性的",
            "scene": "托福综合写作",
            "example": "The reading passage argued that asteroid impacts can be catastrophic for ecosystems.",
            "image": "https://images.unsplash.com/photo-1476231790875-016a80c274f1?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "multiple_choice",
                    "prompt": "Catastrophic events are?",
                    "options": [
                        {"value": "A", "label": "Harmless"},
                        {"value": "B", "label": "Manageable"},
                        {"value": "C", "label": "Disastrous"},
                        {"value": "D", "label": "Predictable"},
                    ],
                    "answer": "C",
                }
            ],
        },
        {
            "id": "toefl-chronology",
            "term": "chronology",
            "phonetic": "/krəˈnɑː.lə.dʒi/",
            "meaning": "n. 年代学；年代顺序",
            "scene": "托福阅读",
            "example": "Archaeologists reconstructed the chronology of the ancient civilization.",
            "image": "https://images.unsplash.com/photo-1458682625221-3a45f8a844c7?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "cloze",
                    "prompt": "The historian studied the _____ of events in the empire.",
                    "answer": "chronology",
                }
            ],
        },
        {
            "id": "toefl-depict",
            "term": "depict",
            "phonetic": "/dɪˈpɪkt/",
            "meaning": "v. 描述；描绘",
            "scene": "托福写作",
            "example": "The professor depicted the migration patterns of birds using charts.",
            "image": "https://images.unsplash.com/photo-1521737604893-d14cc237f11d?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "multiple_choice",
                    "prompt": "To depict something means to?",
                    "options": [
                        {"value": "A", "label": "Hide it"},
                        {"value": "B", "label": "Describe or show it"},
                        {"value": "C", "label": "Damage it"},
                        {"value": "D", "label": "Forget it"},
                    ],
                    "answer": "B",
                }
            ],
        },
        {
            "id": "toefl-flourish",
            "term": "flourish",
            "phonetic": "/ˈflɝː.ɪʃ/",
            "meaning": "v. 繁荣；茂盛",
            "scene": "托福听力",
            "example": "Early civilizations flourished along river valleys.",
            "image": "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "reading",
                    "prompt": "Why did river valley civilizations flourish?",
                    "passage": "They flourished because rivers provided fertile soil, reliable water, and trade routes.",
                    "options": [
                        {"value": "A", "label": "Because of mountain barriers"},
                        {"value": "B", "label": "Due to fertile soil and water"},
                        {"value": "C", "label": "Because of deserts"},
                        {"value": "D", "label": "Due to cold climates"},
                    ],
                    "answer": "B",
                }
            ],
        },
        {
            "id": "toefl-hypothesis",
            "term": "hypothesis",
            "phonetic": "/haɪˈpɑː.θə.sɪs/",
            "meaning": "n. 假设；假说",
            "scene": "托福综合写作",
            "example": "The lecture challenged the hypothesis presented in the reading.",
            "image": "https://images.unsplash.com/photo-1520607162513-77705c0f0d4a?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "cloze",
                    "prompt": "Scientists tested the _____ through experiments.",
                    "answer": "hypothesis",
                }
            ],
        },
        {
            "id": "toefl-impetus",
            "term": "impetus",
            "phonetic": "/ˈɪm.pɪ.təs/",
            "meaning": "n. 推动力；促进因素",
            "scene": "托福阅读",
            "example": "The new discovery provided impetus for further research.",
            "image": "https://images.unsplash.com/photo-1521737604893-d14cc237f11d?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "multiple_choice",
                    "prompt": "Impetus most nearly means?",
                    "options": [
                        {"value": "A", "label": "Obstacle"},
                        {"value": "B", "label": "Motivation"},
                        {"value": "C", "label": "Conclusion"},
                        {"value": "D", "label": "Prediction"},
                    ],
                    "answer": "B",
                }
            ],
        },
        {
            "id": "toefl-meticulous",
            "term": "meticulous",
            "phonetic": "/məˈtɪk.jə.ləs/",
            "meaning": "adj. 一丝不苟的",
            "scene": "托福口语",
            "example": "He is meticulous about citing sources in research papers.",
            "image": "https://images.unsplash.com/photo-1521737604893-d14cc237f11d?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "cloze",
                    "prompt": "The lab assistant kept _____ records of each experiment.",
                    "answer": "meticulous",
                }
            ],
        },
        {
            "id": "toefl-proponent",
            "term": "proponent",
            "phonetic": "/prəˈpoʊ.nənt/",
            "meaning": "n. 支持者",
            "scene": "托福阅读",
            "example": "Proponents of renewable energy argue it reduces emissions.",
            "image": "https://images.unsplash.com/photo-1521791136064-7986c2920216?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "reading",
                    "prompt": "What does a proponent do?",
                    "passage": "In debates, proponents present evidence supporting a proposal, while opponents critique it.",
                    "options": [
                        {"value": "A", "label": "Opposes an idea"},
                        {"value": "B", "label": "Supports an idea"},
                        {"value": "C", "label": "Ignores an idea"},
                        {"value": "D", "label": "Controls an idea"},
                    ],
                    "answer": "B",
                }
            ],
        },
        {
            "id": "toefl-reservoir",
            "term": "reservoir",
            "phonetic": "/ˈrez.ə.vwɑːr/",
            "meaning": "n. 水库；储备",
            "scene": "托福听力",
            "example": "The lecture described how reservoirs regulate water supply.",
            "image": "https://images.unsplash.com/photo-1517959105821-eaf2591984c2?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "cloze",
                    "prompt": "The city built a new _____ to store drinking water.",
                    "answer": "reservoir",
                }
            ],
        },
        {
            "id": "toefl-synthesize",
            "term": "synthesize",
            "phonetic": "/ˈsɪn.θə.saɪz/",
            "meaning": "v. 综合；合成",
            "scene": "托福写作",
            "example": "Students must synthesize information from the lecture and reading.",
            "image": "https://images.unsplash.com/photo-1520607162513-77705c0f0d4a?auto=format&fit=crop&w=600&q=80",
            "questions": [
                {
                    "type": "multiple_choice",
                    "prompt": "To synthesize information is to?",
                    "options": [
                        {"value": "A", "label": "Separate it"},
                        {"value": "B", "label": "Memorize it"},
                        {"value": "C", "label": "Combine ideas"},
                        {"value": "D", "label": "Forget it"},
                    ],
                    "answer": "C",
                }
            ],
        },
    ],
}
