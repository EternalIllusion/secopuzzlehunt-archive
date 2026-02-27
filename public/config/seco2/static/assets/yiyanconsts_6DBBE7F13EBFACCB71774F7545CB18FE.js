const yiyan_data = [
    {type: "normal", text: "「对我来说这是这片沙海的浴火重生……」"},
    {type: "normal", text: "她的笔触很轻，像湖面一触即散的水汽。"},
    {
        type: "normal",
        text: "「在每一个半年的终末，北来或南来的日光总会在此略微逗留。」",
    },
    {
        type: "normal",
        text: "「但这个周期比沙海的周期长一点，惯性让最后几十天的生命力运转并渐渐耗散。」",
    },
    {
        type: "normal",
        text: "她抬眼看向窗外，像在问自己，也像在问这本快写满的本子，「记录的句子也会随着惯性一起冲淡吗？」",
    },
    {
        type: "bold",
        text: "\n记录本角落潦草的涂鸦像是隐语，将其意义深锁在纷乱线条里。",
    },
    {
        type: "normal",
        text: "\n可……这些符号明明是风干的文字，以澜夜凝望了八年的眼睛也未能读懂任何一个弯折。",
    },
    {type: "normal", text: "「真希望它能够被我理解，即便将信息全然倾出也好。」"},
    {
        type: "hint",
        text: "\n记录的文字有部分飘落下来了。只要把「隐语」的「█」归还给「日光」，澜夜就有可能读懂这些符号了！",
    },
    {type: "bracket", text: "【二画】"},
    {
        type: "input",
        stage: 1,
        answer: "阝",
        replacements: [
            {from: "日", to: "阳", glow:1},
            {from: "隐", to: "急", glow:1},
        ],
        removes: [
            "「真希望它能够被我理解，即便将信息全然倾出也好。」",
            "也未能读懂任何一个弯折。",
        ],
        adds: "却足以读懂任何一个弯折。\n",
    },
    {
        type: "normal",
        text: "弯折的线条里，藏着沙漏倒转的轨迹，像是时间在角落低语。",
    },
    {
        type: "normal",
        text: "「角落的符号警告着沙海的毁灭，破碎的记忆现实无法佐证。」",
    },
    {
        type: "normal",
        text: "就像没有接口的电话，她的思绪悬在半空。「下次切换之前必须做的到底是什么？」",
    },
    {
        type: "normal",
        text: "「忽然想起当年第一次发现异常时还不相信它的存在，似乎只是经历了一次无形的诱导。」",
    },
    {
        type: "normal",
        text: "似乎只是顺从了这次诱导，回过神来，便已踏入一处被遗忘的土穴。",
    },
    {type: "normal", text: "「直到记录第三百二十次落日……」"},
    {
        type: "bold",
        text: "\n这段记录似乎是澜夜新摹写的,看上去在以陌生的方式仿效着前文。",
    },
    {
        type: "normal",
        text: "\n但细看内容，却像是在有意迎合某个对象，连落款的弧度都显得刻意。",
    },
    {type: "normal", text: "「真希望它本就是我出自我心底的笔迹。」"},
    {type: "hint", text: "\n描写的文字有部分飘落下来了。……"},
    {type: "bracket", text: "【四画】【十画】（不成词）"},
    {
        type: "input",
        stage: 2,
        answer: "斤莫",
        replacements: [
            {from: "口", to: "听", glow:1},
            {from: "土", to: "墓", glow:1},
            {from: "新", to: "亲", glow:1},
            {from: "摹", to: "手", glow:1},
        ],
        removes: ["「真希望它本就是我出自我心底的笔迹。」", "刻意。"],
        adds: "温柔。\n",
    },
    {type: "normal", text: "「线性时间里只有一个线性的自我。」"},
    {
        type: "normal",
        text: "她原以为非她一人能理解这份孤独。她的目光垂向脚边，一小片湿痕不知何时晕开在沙里。",
    },
    {
        type: "normal",
        text: "「可看到凭空出现的文字就在身旁，心里总有些微妙的反应。」",
    },
    {
        type: "normal",
        text: "「它们与沙海是那样的和谐与统一，亲切啊。我仿佛感觉到广远的沙海中地底的水正悄声呼吸……」",
    },
    {type: "normal", text: "她心中回荡起一段壮丽的旋律，像是为月出而谱写的。"},
    {
        type: "normal",
        text: '「不知醒来之后这段终焉的音乐能否让"她"也体会到亲切呢？」',
    },
    {
        type: "bold",
        text: "\n落日将沙海染成画布的底色，　　在另一端的晨光里添上了最后一片未干的湖。",
    },
    {type: "normal", text: "\n她总觉得画布上少了那抹来自星空的凝望……"},
    {
        type: "normal",
        text: "「皓星从未离开，她的目光正从那墨迹未干的字里行间望出来。」",
    },
    {type: "hint", text: "\n文字有部分飘落下来了。然后……消失了？……"},
    {type: "bracket", text: "【五画】【七画】【四画】【五画】→【十二画】【九画】"},
    {
        type: "input",
        stage: 3,
        answer: "皓星",
        replacements: [
            {from: "非", to: "靠", glow:1},
            {from: "广远", to: "旷远", glow:1},
            {from: "水", to: "泉", glow:1},
            {from: "月出", to: "胜出", glow:1},
            {from: "　　", to: "皓星", glow:2},
        ],
        removes: [
            "「皓星从未离开，她的目光正从那墨迹未干的字里行间望出来。」",
            "少了那抹来自星空的凝望……",
        ],
        adds: "有了一抹来自星空的凝望……",
    },
    {
        type: "final_hint",
        text: "不过，她记录的内容似乎也暗藏玄机……\n「对我……」\n「角落……」\n「线性……」",
    },
    {type: "final"},
]