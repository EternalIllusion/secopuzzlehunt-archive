
<!-- 8fseco Puzzle -->
<template>

    <div :class="{ 'puzzle-component': true, 'light-theme': !darkTheme, 'dark-theme': darkTheme }">
        <div class="puzzle-body">
            <a class="skip-to-main" href="#main-content-anchor"></a>
            <nav class="top-navbar">
                <span class="tray">
                    <div class="top-tabs">
                        <div class="top-team-actions">
                            <div id="nav-team-name">
                                <a class="team-name">archive</a>
                            </div>

                            <span class="current-stat" title="Available hints: 2066.11">

                                <svg width="32" height="32" version="1.1" viewBox="0 0 8 8"
                                    xmlns="http://www.w3.org/2000/svg" class="hunt-icon">
                                    <path d="M1 4 A3 3 0 0 1 7 4 3 3 0 0 1 1 4z"
                                        style="stroke:currentColor;fill:none;stroke-width: 0.5"></path>
                                    <text x="4" y="4" font-family="Verdana" font-size="4" dy="0.35em"
                                        text-anchor="middle"
                                        style="stroke:currentColor;fill:currentColor;stroke-width: 0.3">H</text>
                                </svg>

                                <span class="current-stat-label">1145.14</span>
                            </span>

                            <span class="current-stat" title="Solves: 44">

                                <svg width="32" height="32" version="1.1" viewBox="0 0 8 8"
                                    xmlns="http://www.w3.org/2000/svg" class="hunt-icon">
                                    <path d="M1 4 A3 3 0 0 1 7 4 3 3 0 0 1 1 4z"
                                        style="stroke:currentColor;fill:none;stroke-width: 0.5"></path>
                                    <text x="4" y="4" font-family="Verdana" font-size="4" dy="0.35em"
                                        text-anchor="middle"
                                        style="stroke:currentColor;fill:currentColor;stroke-width: 0.3">S</text>
                                </svg>

                                <span class="current-stat-label">44</span>
                            </span>
                            <a>登出</a>

                        </div>

                        <div class="site-nav">
                            <a v-for="(title, i) in pages" @click="navigate(i)"
                                :class="{ 'selected-tab': currentPage === i }">{{ title }}</a>


                            <div class="theme-switcher">
                                <button id="themeToggle" class="btn btn-sm" @click="themeToggle">
                                    <span class="dark-icon" v-if="darkTheme">🌙 深绿</span>
                                    <span class="light-icon" v-else>☀️ 浅绿</span>
                                </button>
                            </div>
                        </div>
                    </div>
                </span>
            </nav>
            <div class="top-more-actions">
            </div>
            <a class="main-content-anchor" id="main-content-anchor"></a>
            <div class="content">

                <h1>{{ currentTitle }}</h1>
                <div class="main-page-container" :class="{ 'hidden': currentPage !== 0 }">
                    <div class="sliding-window-container">
                        <!-- 滑动窗口1：这是什么？ -->
                        <div class="sliding-window">
                            <h3>这是什么？</h3>
                            <div class="info-desc">
                                这是一个线上的解谜比赛（Puzzle Hunt）的<a :href="siteLink" target="_blank">存档站</a>！请务必查看我们的<a
                                    @click="navigate(1)">关于</a>页面以获取更多信息。由于原网站屎山太庞大，我们只能尽可能地还原了网站。
                            </div>
                        </div>
                        <div class="sliding-window">
                            <h3>什么时间？</h3>
                            <div class="info-desc">
                                Puzzle Hunt 于 January 31, 2026 at 8:00 PM
                                CST 开始，并已于 February 12, 2026 at 8:00 PM
                                CST 结束。大家都玩得很开心！<a href="https://www.bilibili.com/video/BV1BrZLBXEjK/"
                                    target="_blank">点击这里前往观看After Party！</a>
                            </div>
                        </div>
                        <div class="sliding-window">
                            <h3>谁主办的？</h3>
                            <div class="info-desc">
                                这是由一个不想起床的屑主办的解谜比赛，请加入QQ群：897975800以获取跳票信息。这个存档的版本是由EterIll花了好几个晚上赤石赤出来的。
                            </div>
                        </div>
                    </div>
                    <div class="clock-container">
                        <h2 class="clock-title">当前时间</h2>
                        <div class="clock-root">
                            <div id="clock-app" class="clock-display">
                                <div class="clock-clock">
                                    <div class="clock-pair" data-field="hours">
                                        <div v-for="(digit, digitIndex) in currentTime.hours.split('')"
                                            :key="'hour' + digitIndex" class="clock-digit" :data-index="digitIndex">
                                            <div v-for="index in 24" :key="'h' + digitIndex + index" class="clock-cell"
                                                :data-index="index">
                                                <div class="clock-hand"
                                                    :style="{ rotate: main_clock_getRotationsForDigit(parseInt(digit), index - 1)[0] + 'deg' }">
                                                </div>
                                                <div class="clock-hand"
                                                    :style="{ rotate: main_clock_getRotationsForDigit(parseInt(digit), index - 1)[1] + 'deg' }">
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="clock-pair" data-field="minutes">
                                        <div v-for="(digit, digitIndex) in currentTime.minutes.split('')"
                                            :key="'min' + digitIndex" class="clock-digit" :data-index="digitIndex">
                                            <div v-for="index in 24" :key="'m' + digitIndex + index" class="clock-cell"
                                                :data-index="index">
                                                <div class="clock-hand"
                                                    :style="{ rotate: main_clock_getRotationsForDigit(parseInt(digit), index - 1)[0] + 'deg' }">
                                                </div>
                                                <div class="clock-hand"
                                                    :style="{ rotate: main_clock_getRotationsForDigit(parseInt(digit), index - 1)[1] + 'deg' }">
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="clock-pair" data-field="seconds">
                                        <div v-for="(digit, digitIndex) in currentTime.seconds.split('')"
                                            :key="'sec' + digitIndex" class="clock-digit" :data-index="digitIndex">
                                            <div v-for="index in 24" :key="'s' + digitIndex + index" class="clock-cell"
                                                :data-index="index">
                                                <div class="clock-hand"
                                                    :style="{ rotate: main_clock_getRotationsForDigit(parseInt(digit), index - 1)[0] + 'deg' }">
                                                </div>
                                                <div class="clock-hand"
                                                    :style="{ rotate: main_clock_getRotationsForDigit(parseInt(digit), index - 1)[1] + 'deg' }">
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div id="button-container" class="button-container">

                        <h2>如果遇到情况，如卡题或遇到孬题，请点击进行泄愤：</h2>

                        <div class="button-wrapper">
                            <img id="click-button" src="https://image.secopuzzle.com/button.gif" alt="Click Button"
                                class="clickable-button" @click="main_xbs_click">
                        </div>
                        <div class="click-counter">
                            总点击次数：<span id="click-count">{{ xbsClickCount }}</span>
                        </div>
                    </div>
                </div>
                <div class="info-page-container" :class="{ 'hidden': currentPage !== 1 }">
                    <main>
                        <div class="no-break">
                            <h4 id="Format">规则是什么？</h4>
                            <ul>


                                <li>
                                    Puzzle Hunt于<strong><time datetime="2026-01-31T20:00:00+08:00"
                                            data-format="l, F j, Y \a\t g:i A T"
                                            title="Local time: 2026年1月31日星期六 GMT+8 下午8:00">Saturday, January 31, 2026 at
                                            8:00 PM CST</time></strong> 开始，并于 <strong><time
                                            datetime="2026-02-12T20:00:00+08:00" data-format="l, F j, Y \a\t g:i A T"
                                            title="Local time: 2026年2月12日星期四 GMT+8 下午8:00">Thursday, February 12, 2026
                                            at 8:00 PM CST</time></strong> 结束, 届时将提供谜题解决方案。

                                </li>
                                <li>队伍最多人数为6人。</li>
                                <li>
                                    在比赛开始前，请先在本站进行注册。
                                </li>
                                <li>如有疑问请使用<strong>站内信</strong>私信管理员，我们会尽快回复您。</li>
                            </ul>
                        </div>
                        <div class="no-break">
                            <h4>什么是 Puzzle Hunt？</h4>
                            <p>你可能已经接触过各种各样的谜题：杂志上的数独、经典的逻辑推理题，语文课上的灯谜，英语课上的拼图游戏。也许你和同学玩过“你画我猜”，曾用摩尔斯电码加密信息让朋友破译；研究过围棋的棋局，读过那些引人入胜的悬疑小说。或者，你的手机游戏列表里有《纪念碑谷》这样的空间解谜游戏，又或者在周末参加过户外的寻宝活动。
                            </p>
                            <p>在 Puzzle Hunt（解谜寻宝）中，你和你的团队需要解决的不止是一道，而是一系列这样的谜题，并从中发掘隐藏的线索。
                            </p>
                            <p>想象一下，任何事物都可以成为谜题：看似是拼图游戏，实际上是对拼图碎片形状的推理；或是音符的排列，每组音符代表一种乐器。奇妙的谜语，严密的逻辑，隐藏的符号，甚至可能是一段代码中变量的命名规律，或是一部科幻电影里隐藏的彩蛋，万事万物皆可成谜。
                            </p>
                            <p>而你的目标，就是找到合适的线索，选择最符合当前情况的方法，从里面找到你的答案。无论如何，最终你一定能得到一组有意义的词语或一句话。</p>
                            <p>在解决一连串的谜题之后，元谜题（Meta Puzzle）会将你之前得到的所有答案串联成新的谜题，形成错综复杂的结构。</p>
                            <p>最终，Puzzle Hunt 的目标是团队共同解决所有出现的元谜题（是的！你不需要所有小题的答案就可以解决元谜题！），得到隐藏在谜题和谜题结构中的最终答案（通常被称为「Final
                                Meta」）。</p>
                            <p>当队伍里有超过一个人时，我们<strong>强烈</strong>建议你准备一个共享表格，实时记录每题的题目、答案、解题过程和想法，并与队友共享。这不仅能帮助团队成员更好地分工协作，还能让每个人都能随时了解解题进度，从而提高解题效率。
                            </p>
                        </div>
                        <div class="no-break">
                            <h4 id="Format">比赛须知</h4>
                            <ul>
                                <li>比赛不允许进行直播。您可以与身边其他人进行讨论，但请勿将答案发布在任何公开平台，例如论坛、社交媒体、多人数群聊等，请勿与其他参赛队伍交流题目或答案，违者将被视为作弊并取消参赛资格。
                                </li>
                                <li>比赛不会涉及黑客相关技术手段，严禁攻击任何比赛的服务器或进行类似行为。</li>
                                <li>主办方保留将有可疑行为的队伍暂时或永久移出排行榜的权力。</li>
                            </ul>
                        </div>
                        <div class="no-break">
                            <h4>解谜比赛的形式是什么？</h4>
                            <p>一开始会有3个谜题可供解答，解锁新谜题的主要方式是通过解开前面谜题。</p>
                            <p>每个答案都是由字母A-Z组成的字符串或汉字或数字，数字请用阿拉伯数字（0-9）输入。</p>
                            <p>在检查正确性之前，小写字母将被转换为大写，其他任何字符将被删除。</p>
                        </div>
                        <div class="no-break">
                            <h4>比赛周边在哪里购买？</h4>
                            <p>
                                <a href="https://e.tb.cn/h.ShGgmtsQuUp6Xgl?tk=iPQJf0KgMfH HU287 「SECO Puzzle Hunt2原创周边」"
                                    target="_blank">【淘宝】SECO Puzzle Hunt2原创周边（点击链接打开，或淘宝搜索SECO Puzzle Hunt）</a>
                            </p>
                        </div>
                    </main>
                </div>
                <div class="story-page-container" :class="{ 'hidden': currentPage !== 2 }">
                    <div class="story-container">
                        <!-- 左侧导航 -->
                        <div class="story-sidebar">
                            <div class="story-nav-header">Act 0</div>
                            <div class="story-nav-item active" @click="story_load(0)">
                                启程
                                <span class="story-status-badge unlocked">已解锁</span>
                            </div>
                            <div class="story-nav-header">Act 1</div>
                            <div class="story-nav-item" @click="story_load(1)">
                                一区 - 庄园
                                <span class="story-status-badge completed">已完成</span>
                            </div>
                            <div class="story-nav-header">Act 2</div>
                            <div class="story-nav-item" @click="story_load(2)"">
                                二区 - 沙海
                                <span class=" story-status-badge completed">已完成</span>
                            </div>
                            <div class="story-nav-header">Act 3</div>
                            <div class="story-nav-item" @click="story_load(3)">
                                三区 - 高塔
                                <span class="story-status-badge completed">已完成</span>
                            </div>
                            <div class="story-nav-header">Act 4</div>
                            <div class="story-nav-item" @click="story_load(4)">
                                四区 - 花原
                                <span class="story-status-badge unlocked">已解锁</span>
                            </div>
                        </div>

                        <!-- 右侧内容 -->
                        <div class="story-content-area">
                            <div id="contentBody" style="display: block;">
                                <div id="displayTitle" class="story-chapter-title">{{ storyTextsData[storyCurrent].title
                                    }}</div>
                                <div id="displayIntro" class="story-text">
                                    {{ storyTextsData[storyCurrent].intro }}
                                </div>
                                <div id="displayDivider" class="story-divider"
                                    v-if="storyTextsData[storyCurrent].outro">
                                    <span>已完成</span>
                                </div>
                                <div id="displayOutro" class="story-text" style="display: none;">
                                    {{ storyTextsData[storyCurrent].outro }}
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <footer>

                Powered by <a href="https://github.com/galacticpuzzlehunt/gph-site">gph-site</a>

                <p style="text-align: center;">
                    <a href="https://beian.miit.gov.cn/" target="_blank">苏ICP备2024150491号-1</a>
                </p>
            </footer>
        </div>
    </div>

</template>

<style>

.puzzle-component {
    --light-bg-color: rgb(227 252 227);
    --light-text-color: rgba(30, 80, 40, 0.9);
    --dark-bg-color: rgb(7 33 16);
    --dark-text-color: rgb(42 173 42);
    --accent-color: rgb(120, 255, 160);
    --glow-color: rgba(120, 255, 160, 0.5);
    --glow-color-secondary: rgba(120, 255, 160, 0.3);
    --important-color: rgb(60, 180, 100);

    --accent-green: #32CD32;
    --dark-green: #00693e;
    --forest-green: #2e5d3b;
    --mint-green: #a5d6a7;
    --neutral-green: #d7ecd9;
    --primary-green: #4db66d;
    --secondary-green: #2e7d32;
    --primary-dark-green: #50C878;
    --secondary-dark-green: #228B22;
    --contrast-color: #ffffff;
    --contrast-dark: #f0fff0;

    box-sizing: border-box;
    width: 100%;
    transition: all 0.3s ease;

    .puzzle-body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-variant-ligatures: none;
        box-sizing: border-box;
        max-width: 1200px;
        min-height: 100vh;
        overflow-wrap: break-word;
        position: relative;
        transition: all 0.3s ease;
        margin: 0 2rem;
    }

    .puzzle-body * {
        box-sizing: border-box;
        transition: all 0.3s ease;
    }
}

.puzzle-component.light-theme {
    color: var(--light-text-color);
    background-color: var(--light-bg-color);
}

.puzzle-component.dark-theme {
    color: var(--dark-text-color);
    background-color: var(--dark-bg-color);
}

.hidden {
    opacity: 0;
    height: 0 !important;
    pointer-events: none;
    overflow: hidden;
}

/*basic======================================================================================================================*/

strong {
    text-shadow: 0 0 15px var(--glow-color), 0 0 5px var(--glow-color-secondary);
    font-weight: 600;
}

a {
    color: var(--dark-green);
    text-decoration: none;
    cursor: pointer;
    user-select: none;
}

p {
    margin-bottom: .8rem;
    line-height: 1.8;
}

ul>li::before {
    content: "▸";
    color: var(--accent-green);
    font-weight: bold;
    position: absolute;
    left: -1.2em;
    top: 0;
}

ul>li {
    list-style-type: none;
    position: relative;
}

li {
    list-style-position: outside;
    margin-left: 1.8em;
    margin-bottom: 0.5rem;
}

button {
    color: var(--contrast-color);
    background-color: var(--secondary-green);
    box-shadow: 0 4px 15px rgba(var(--secondary-green), 0.2);
    padding: 10px 18px;
    border-radius: 20px;
    min-height: 36px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    text-decoration: none;
    font-weight: 600;
    border: none;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    padding: 14px 24px;
    border-radius: 25px;
    cursor: pointer;
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
    min-height: 44px;
    line-height: 1;
    white-space: nowrap;
}

footer {
    text-align: center;
    opacity: 0.7;
    margin-top: 4rem;
    padding: 2rem 0;
    border-top: 1px solid var(--primary-green);
}

h1,
h2,
h3,
h4 {
    color: var(--important-color);
}

h3,
h4 {
    border-bottom: 2px solid #2aad2a;
    padding-bottom: 0.5rem;
    font-weight: 600;
}

h1 {
    margin: .67em 0;
}

.dark-theme {
    a {
        color: var(--accent-green);
    }

    h1,
    h2 {
        color: var(--accent-green);
    }

    button {
        color: var(--contrast-dark);
        background-color: var(--secondary-dark-green);
    }
}

@media screen and (max-width: 768px) {
    button {
        padding: 10px 20px;
    }
}

/*top nav====================================================================================================================*/

.top-navbar {
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
    width: 100%;
    display: flex;
    justify-content: center;
    margin: 0 auto;
    backdrop-filter: blur(15px);
    border-radius: 0 0 16px 16px;
    padding: 0.5rem 0;

    .top-team-actions {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-wrap: wrap;
        gap: 1rem;
        padding: 0.5rem 0;
        width: 100%;
        margin: 0 auto;
    }

    .site-nav {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-wrap: wrap;
        gap: 1rem;
        padding: 0.5rem 0;
        margin: 0 auto;
        width: 100%;
        max-width: 900px;
    }

    .site-nav a {
        display: inline-block;
        padding: 8px 16px;
        text-decoration: none;
        white-space: nowrap;
    }

    .top-tabs a {
        padding: 7px 14px;
        border-radius: 8px;
        transition: all 0.3s ease;
        /* margin: 20px; */
        line-height: 2.8;
    }


    .selected-tab {
        background: var(--dark-green);
        color: var(--contrast-color) !important;
    }

    a:hover {
        color: var(--primary-green);
        text-shadow: 0 0 15px rgba(var(--glow-color-secondary), 0.6);
        background: color-mix(in srgb, var(--accent-color), transparent 80%);
        transform: translateY(-1px);
    }
}

.dark-theme .top-navbar {

    .selected-tab {
        background: var(--accent-green) !important;
        color: var(--contrast-dark) !important;
    }

    a:hover {
        color: var(--mint-green) !important;
    }
}

@media screen and (max-width: 900px) {
    .top-team-actions {
        gap: 0.75rem !important;
        padding: 0 0.5rem !important;
    }

    .site-nav {
        gap: 0.75rem !important;
        padding: 0 0.2rem !important;
    }

    .site-nav a {
        padding: 6px 12px !important;
        font-size: .8rem !important;
    }
}


/*main   ====================================================================================================================*/

.main-page-container {

    /* 滑动窗口容器 */
    .sliding-window-container {
        overflow-x: auto;
        white-space: nowrap;
        padding: 20px;
        scroll-snap-type: x proximity;
        -webkit-overflow-scrolling: touch;
        max-width: 100%;
        height: auto;
    }

    /* 单个滑动窗口 */
    .sliding-window {
        display: inline-block;
        vertical-align: top;
        min-width: 280px;
        max-width: 350px;
        width: 300px;
        margin: 0 15px;
        padding: 20px;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
        scroll-snap-align: start;
        transition: transform 0.3s ease;
        position: relative;
        backdrop-filter: blur(5px);
    }

    /* 标题样式 */
    .sliding-window h3,
    .clock-title {
        font-size: 1.2rem;
        margin-bottom: 15px;
        color: var(--primary-green);
        font-weight: 600;
        border-bottom: 2px solid var(--primary-dark-green);
        padding-bottom: 0.5rem;
    }

    /* 内容区样式 */
    .info-desc {
        white-space: normal;
        word-wrap: break-word;
        word-break: break-all;
        overflow-y: auto;
        max-height: 200px;
        line-height: 1.6;
        font-size: 1rem;
        color: var(--primary-green);
    }

    /* 悬停效果 */
    .sliding-window:hover,
    .clock-container:hover {
        transform: translateY(-5px);
        transition: all 0.3s ease;
    }

    /* 移动端适配 */
    @media (max-width: 768px) {
        .sliding-window-container {
            padding: 10px;
            white-space: normal;
        }

        .sliding-window {
            display: block;
            width: 90%;
            max-width: 100%;
            margin: 10px auto;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
        }

        .info-desc {
            max-height: none;
        }

        .clock-container {
            padding: 15px;
            margin: 20px 10px;
        }
    }

    .clock-container {
        text-align: center;
        margin: 40px auto;
        padding: 2rem;
        border-radius: 16px;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
        max-width: 900px;
        transition: all 0.3s ease;
        backdrop-filter: blur(10px);
        border-left: 4px solid var(--primary-green);
    }


    .clock-root {
        --field-gap: 2rem;
        --cell-size: 3rem;
        --cell-border-size: max(calc(var(--cell-size) / 16), 1.5px);
        --cell-background-color: color-mix(in srgb, var(--contrast-dark), transparent 50%);
        --hand-color: var(--primary-green);
    }

    .dark-theme .clock-root {
        --cell-background-color: transparent;
        --hand-color: var(--mint-green);
    }

    .clock-root * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    .clock-display {
        height: auto;
        display: flex;
        justify-content: center;
        align-items: center;
        overflow: hidden;
        padding: 10px 0;
    }

    .clock-clock {
        display: flex;
        gap: var(--field-gap);
    }

    .clock-clock>.clock-pair {
        display: flex;
        gap: .125rem;
    }

    .clock-digit {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        grid-template-rows: repeat(6, 1fr);
        gap: .125rem;
    }

    .clock-cell {
        height: var(--cell-size);
        width: var(--cell-size);
        position: relative;
        background-color: var(--cell-background-color);
        border: var(--cell-border-size) solid var(--cell-border-color);
        border-radius: 8px;
        transition: all 0.2s ease;
    }

    .clock-cell:hover {
        box-shadow: 0 0 10px rgba(var(--accent-rgb), 0.3);
    }

    .clock-cell>.clock-hand {
        width: 50%;
        height: var(--cell-border-size);
        background-color: var(--hand-color);
        position: absolute;
        transform-origin: center left;
        top: 50%;
        left: 50%;
        translate: 0% -50%;
        rotate: 135deg;
        transition: rotate .25s ease-out;
    }

    .clock-cell>.clock-dot {
        width: var(--cell-border-size);
        height: var(--cell-border-size);
        position: absolute;
        left: 50%;
        top: 50%;
        translate: -50% -50%;
        background-color: var(--hand-color);
        border-radius: 50%;
    }

    /* 响应式调整 */
    @media (max-width: 1440px) {
        .clock-root {
            --cell-size: 1rem;
        }
    }

    @media (max-width: 1024px) {
        .clock-root {
            --field-gap: .5rem;
            --cell-size: .75rem;
        }
    }

    @media (max-width: 900px) {
        .clock-root {
            --field-gap: .3rem;
            --cell-size: .6rem;
        }

        .clock-title {
            font-size: 1.2rem;
        }
    }

    @media (max-width: 480px) {
        .clock-root {
            --cell-size: .375rem;
        }
    }


    /* 按钮点击区域样式 */
    .button-container {
        text-align: center;
        margin: 40px auto;
        padding: 2rem;
        border-radius: 16px;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
        max-width: 500px;
        transition: all 0.3s ease;
        backdrop-filter: blur(10px);
        border-left: 4px solid var(--primary-dark-green);
    }

    .button-container h2 {
        font-size: 1.1rem;
        margin-bottom: 20px;
        color: var(--primary-dark-green);
        font-weight: 600;
    }

    .button-wrapper {
        position: relative;
        display: inline-block;
        margin-bottom: 20px;
    }

    .clickable-button {
        max-width: 200px;
        height: auto;
        cursor: pointer;
        transition: transform 0.2s ease, filter 0.2s ease;
        border-radius: 8px;
    }

    .clickable-button:hover {
        transform: scale(1.05);
        filter: brightness(1.1);
    }

    .clickable-button:active {
        transform: scale(0.95);
    }

    .click-counter {
        margin-top: 15px;
        font-size: 1.2rem;
        color: var(--primary-dark-green);
        font-weight: 600;
    }

    .click-counter #click-count {
        font-size: 2rem;
        color: var(--primary-dark-green);
        font-weight: bold;
    }

    @media (max-width: 768px) {
        .button-container {
            padding: 1.5rem;
            max-width: 90%;
        }

        .clickable-button {
            max-width: 150px;
        }
    }
}

/*info    ===================================================================================================================*/
.info-page-container {
    main {
        padding: 1.5rem;
        border-radius: 12px;
        background: rgba(255, 255, 255, 0.1);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.08);
    }
}

/*story   ===================================================================================================================*/
.story-page-container {

    /* 布局容器 */
    .story-container {
        display: flex;
        height: 80vh;
        /* 占据大部分屏幕高度 */
        background: #fff;
        border: 1px solid #ddd;
        border-radius: 8px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
        overflow: hidden;
        margin-bottom: 40px;
    }

    /* 左侧导航栏 */
    .story-sidebar {
        width: 240px;
        background-color: #f8f9fa;
        border-right: 1px solid #e0e0e0;
        overflow-y: auto;
        display: flex;
        flex-direction: column;
        padding-top: 10px;
    }

    .story-nav-header {
        font-size: 13px;
        color: #999;
        font-weight: bold;
        text-transform: uppercase;
        padding: 15px 20px 5px 20px;
        margin-top: 5px;
    }

    .story-nav-item {
        padding: 12px 25px;
        font-size: 15px;
        color: #444;
        cursor: pointer;
        transition: all 0.2s;
        border-left: 4px solid transparent;
    }

    .story-nav-item:hover {
        background-color: #e9ecef;
        color: #000;
    }

    .story-nav-item.active {
        background-color: #e6f2ff;
        color: #007bff;
        border-left-color: #007bff;
        font-weight: bold;
    }

    /* 右侧内容区 */
    .story-content-area {
        flex: 1;
        padding: 40px 60px;
        overflow-y: auto;
        background-color: #fff;
        position: relative;
    }

    .story-chapter-title {
        font-size: 28px;
        font-weight: bold;
        color: #333;
        margin-bottom: 25px;
        border-bottom: 2px solid #eee;
        padding-bottom: 15px;
    }

    .story-text {
        font-size: 16px;
        line-height: 1.8;
        color: #444;
        white-space: pre-wrap;
        /* 保留换行符 */
        margin-bottom: 30px;
    }

    .story-divider {
        display: flex;
        align-items: center;
        margin: 40px 0;
        color: #bbb;
        font-size: 14px;
    }

    .story-divider::before,
    .story-divider::after {
        content: "";
        flex: 1;
        border-bottom: 1px dashed #ddd;
    }

    .story-divider span {
        padding: 0 15px;
    }

    .empty-state {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100%;
        color: #999;
        font-style: italic;
    }

    /* 移动端适配 */
    @media (max-width: 768px) {
        .story-container {
            flex-direction: column;
            height: auto;
        }

        .story-sidebar {
            width: 100%;
            height: 200px;
            border-right: none;
            border-bottom: 1px solid #ddd;
        }

        .story-content-area {
            padding: 20px;
            height: 500px;
            /* 移动端固定高度 */
        }
    }

    .story-status-badge {
        float: right;
        font-size: 0.9rem;
        padding: 4px 6px;
        /* 调整 padding：增加了上下内边距 */
        border-radius: 3px;
        margin-left: 8px;
        font-weight: normal;
        line-height: 1.3;
        /* 调整 line-height：略微减小以适应增加的 padding */
        vertical-align: middle;
        /* 保持此属性，但主要依赖 padding 和 line-height */
    }

    .story-status-badge.unlocked {
        background-color: #007bff;
        color: white;
    }

    .story-status-badge.completed {
        background-color: #28a745;
        /* Green */
        color: white;
    }
}

</style>

<!-- 请将以上部分复制到后台“题目HTML”中，以下部分复制到后台“题目脚本”中，不要包含<script>标签 -->

<script>
var __vue_puzzle_component__=function(n){"use strict";return{setup(){const e=window.location.origin,r=n.ref(!1),t=n.ref(0),u=["主页","关于","剧情","题目","队伍","更新","站内信","档案"],o=n.ref(""),i=n.ref(8003288);n.ref(0);const s=n=>{t.value=n,o.value=u[n],h()},a={" ":[135,135],"┘":[180,270],"└":[0,270],"┐":[90,180],"┌":[0,90],"-":[0,180],"|":[90,270]},I={0:["┌","-","-","┐","|","┌","┐","|","|","|","|","|","|","|","|","|","|","└","┘","|","└","-","-","┘"],1:["┌","-","┐"," ","└","┐","|"," "," ","|","|"," "," ","|","|"," ","┌","┘","└","┐","└","-","-","┘"],2:["┌","-","-","┐","└","-","┐","|","┌","-","┘","|","|","┌","-","┘","|","└","-","┐","└","-","-","┘"],3:["┌","-","-","┐","└","-","┐","|"," ","┌","┘","|"," ","└","┐","|","┌","-","┘","|","└","-","-","┘"],4:["┌","┐","┌","┐","|","|","|","|","|","└","┘","|","└","-","┐","|"," "," ","|","|"," "," ","└","┘"],5:["┌","-","-","┐","|","┌","-","┘","|","└","-","┐","└","-","┐","|","┌","-","┘","|","└","-","-","┘"],6:["┌","-","-","┐","|","┌","-","┘","|","└","-","┐","|","┌","┐","|","|","└","┘","|","└","-","-","┘"],7:["┌","-","-","┐","└","-","┐","|"," "," ","|","|"," "," ","|","|"," "," ","|","|"," "," ","└","┘"],8:["┌","-","-","┐","|","┌","┐","|","|","└","┘","|","|","┌","┐","|","|","└","┘","|","└","-","-","┘"],9:["┌","-","-","┐","|","┌","┐","|","|","└","┘","|","└","-","┐","|","┌","-","┘","|","└","-","-","┘"]},l=n.ref(S()),A=n.ref(!1),c=n.ref(0),v=n.ref(["16","05","18","06","21","13","05","04"]),C=n.ref(!1);function S(){const n=new Date;return{hours:String(n.getHours()).padStart(2,"0"),minutes:String(n.getMinutes()).padStart(2,"0"),seconds:String(n.getSeconds()).padStart(2,"0")}}function d(){A.value?(l.value={hours:"00",minutes:"00",seconds:v.value[0]},setInterval(()=>{C.value||(c.value=(c.value+1)%v.value.length,0===c.value&&(C.value=!0,setTimeout(()=>{C.value=!1},2e3)),l.value.seconds=v.value[c.value])},1e3)):A.value||setInterval(()=>{const n=S();var e,r;r=n,((e=l.value).hours!==r.hours||e.minutes!==r.minutes||e.seconds!==r.seconds)&&(l.value=n)},100)}document.addEventListener("DOMContentLoaded",()=>{(new ClockController).init(),initButtonClickHandler()});const h=()=>{const n=new Date("2026-02-12T20:00:00").getTime(),e=(new Date).getTime()-n;var r=8003288+120*Math.floor(e/1e3)+Math.floor(80*Math.random());i.value=r>i.value+5?r:i.value+5};n.onMounted(()=>{s(0),d(),h()});const f=n.ref(0);return{siteLink:e,navigate:s,darkTheme:r,themeToggle:()=>{r.value=!r.value},currentPage:t,pages:u,currentTitle:o,main_clock_getRotationsForDigit:function(n,e){return((n,e)=>{const r=I[n];if(r){const n=r[e],t=a[n];if(t)return t}return a[" "]})(n,e)},currentTime:l,main_xbs_click:h,xbsClickCount:i,storyTextsData:[{title:"启程",intro:"谜土，是SECO星球上特有的奇妙区域……\n不对，不对——刚被宣布这只是虚拟设备的幻象的你们，突然就真的来到了一艘飞船之中，面前是缓缓靠近的SECO星球。\n是真实？是幻象？经历过一场欺骗的你们变得十分警惕，但这一切都不再重要；真正重要的，是找到属于自己的那段回忆……\n\n“欢迎来到崭新的SECO星球！”随着riser熟悉而又陌生的声音传来，安全带已经松开。在微弱的重力之下，你们从飞船前往地面，呼吸着来自另一个世界却又和地球如出一辙的新鲜空气。\n在下飞船之前，你们已经知道，除了半径以及随之而来的重力差异以外，SECO星球与地球在许多方面都很相似，比如相似的海陆比例、相似的自转和公转周期，只是少了月球一样的伴侣，变得非常孤独。与强烈的归属感同时出现的，却是突如其来的震撼。所谓谜土竟是一片废墟，除了迎接你们的riser一行以外，其中空无一人，寂静得仿佛要将你们这个小队吞没。\n“所以我们的任务是……找寻谜土的真相？拜托，这又不是某二次元游戏。”你摆了摆手，装作一脸失望，毕竟你们在层层叠叠的虚实穿越之间早已把世界的异常忘得一干二净。\n“你们已经知道，SECO星球已经高度智能化，并创造出了名为‘谜土’的虚拟世界……”\n“闭嘴，难道我们又要醒一次？”你想起飞船上嵌套的虚拟世界，气不打一处来。\n“这倒不至于，我保证这里是货真价实的现实。不过嘛，先听我说——”riser的笑容渐渐消失，取而代之的是一本正经，你才发现之前多次前往的建筑物依然存在，“我们发现，虚拟世界依赖于居民对真实世界的印象而存在，因此虚拟世界的缺陷也对应其印象中的迷失，我们把这些居民称为迷失者。由于SECO星球的居民普遍缺乏创新，我们对迷失者的传统治疗方法是创造一个尽可能符合描述的印象故事来填补印象缺陷，然而不管怎么填补总会有新的缺陷，而缺陷又会随着时间不断扩张。现在这一缺陷已经扩张到我们无法处理的地步，我们需要让富有创造力的外援拯救他们，而你们正好完美满足这一需求。”\n“所以我们还要进入虚拟世界？那么我们怎么保证进去之后的安全？不会像上次那样，改了个比特顺序就把虚拟世界炸个稀烂吧？”\n“放心，现在的虚拟世界已经是重建之后的了，当你进入其中时，你会得到我们提前配置的专用设备，它能通过对环境的分析确保你们不管在现实世界还是在虚拟世界都绝对安全。并且这个设备的功能远不止于此，我知道现编一个故事修补缺陷并不容易，所以我们把步骤简化了一下，你只需要根据你对缺陷的理解在设备中输入合适的参数，即可让内置的AI协助编写。一般来说，AI在得到正确的参数之后会给出‘故事碎片’，收集一定数量的‘故事碎片’就能进一步分析得到‘最终印象’。当然，输入是有次数上限的，你也不希望AI通过太多的输入形成错误的想法吧。”\n“可是我们没接触过这件事啊，真的能做到吗？”\n“其实除了直接输入参数，AI还接受某些特定语句，输入它们之后AI会进行一些联想，或许你可以从联想中找到关于虚拟世界的另一些信息。这不会破坏AI建立的神经网络，因此不会影响次数限制。此外，随着时间流逝，你们还可以从虚拟世界中获得代码残片，将它们输入设备的‘混杂印象节点转化器’——Heterogeneous Impression Node Transformer（HINT）程序，它就能经过计算后得到原版印象大致的走向。如果你觉得还是太难，你还可以把代码残片通过设备发给我们，或许用我们的传统方法也能找到一些眉目。”\n说着说着，你们已经走到了谜土中心，那里的58号房间仍和记忆中一样，SECO星球的几位高官早已在这里等待。简单道别之后，你们接连进入虚拟世界，新的旅程就要开始了……"},{title:"一区 - 庄园",intro:"【北纬42°38′，东经89°14′，庄园】\n你感到在两个世界之间穿行的时间变长了许多，但设备显示的时间告诉你，进入虚拟世界仍是一瞬间的事。这个坐标和熟悉的景色让你们恍然大悟，这里就是虚拟世界的谜土，而虚实两个世界都存在谜土，正好说明了二者的相互照应。\n跟着记忆中的方向，你们找到了当时的房间，不过现在它已经成了一处庄园。同样，庄园四周不知何时出现了环绕的群山，让这片区域变得更为隐秘。庄园的主人正坐在峡谷最低点，望着四周干燥的山峰默然思索，并未搭理你们的招呼。你们打开终端准备和riser汇报，那人却立即站起来说：“你们搞错了——要拯救的不是我，而是这个世界。”\n怎么自己作为一个新手就吃了闭门羹？那后面那么多迷失者该怎么办？你们呆滞地望向彼此。过了一小会儿，他默然走向庄园，你们随即跟上，通过大门之后，他开始讲述起自己的故事，看来是默认了你们的到来。根据他的介绍，他叫牧渊，二十六岁，从小喜欢规划事物，在大学期间学习水利工程，曾经凭借才学为他的家乡设计了一整套治水系统，因此被研究所重用，一路青云直上，这让你们之中的好几位都心生羡慕，毕竟能在谜土中心修建庄园，他显然不是平凡人物。\n不过庄园看似已经废弃许久，一路上充满了凋敝与颓废的气氛，杂乱的树枝在毫无生机的树干之上随意摆放着，底下是积上一层灰的枯叶，都诉说着时间留下的痕迹。再往里走，密密麻麻的枯树突然消失，路面也出现了一个弧度，显然这里是一座桥，而地面的凹陷就是河道，但其中早已没有水色。\n诡异的气氛让你们不敢说话，但牧渊却率先开口了：“你们觉得这里失去了什么？”\n水，当然是水，但作为一位水利工程师，这个问题在牧渊的眼中显然有更深一层的含义，于是你们没有一人敢于回答。牧渊叹了口气，继续说道：“如果真实的世界能像草稿纸上的规划一样就好了……”\n这句话倒是提醒了你。这里是低地，按理说应该是水流汇集之处……或者按另一种可能，是水的禁区。你想到刚进入庄园时看到的SECO星球地图，按照地理规律，这里深居内陆，本就没有多少降水，四面的高山更是将水汽尽数拦截。这里本来就不应该是水利工程师该踏足的地方，再怎么规划也无法逆转大自然下达的禁锢，那么牧渊来这里干什么？\n“现在我来解答这个问题。这里失去的并不是水，而是旧时代残存的创造性需求。”\n牧渊是作为工程设计师来到这里的，他发现这里虽然表面荒芜，但深层存在大量暗河，稍加改造就能实现水资源的高效利用。为此他殚精竭虑地设计方案，并亲自做好了前期准备，只要上级拍板，一切都将顺利进行，就像他为自己家乡设计的方案那样。然而时代的洪流来到了这里，高度的信息化让AI得以普遍应用，牧渊的方案相比AI来说有致命的成本问题，因此未能投用，上级还让他“学习先进工具，感受时代红利”。\n“当时我据理力争，但成本的差距终于胜过了一切。几乎一瞬间之后，AI方案就光速审批通过了，然后这就是他们修建的工程。”牧渊指向干涸的河道，苦笑道，“第一年还确实像个样子，之后就不行了，再然后漏洞百出，最后水都留不下了。”\n走着走着，你们已经到了庄园的另一端出口，四周景色仍和刚来时一样，单调而无趣。为了完成任务，你们要求在庄园歇息，牧渊也没说什么，只是点了点头，随后为你们端来一沓稿纸，以及一盘糕点，他说这是他家乡的特色小吃。",outro:"一开始你就想到，真相显然不是牧渊所说那么简单。你细细分析这个工程，就算牧渊作为守护者不断对其修改，其精细程度也远非AI可及，每个部分（SECTION）都充满了疑点。将其输入设备后，你们从稿纸上看到了工程的影子，AI也给出了确凿的证据，以证明工程为人力所为——果然还是AI最懂AI。\n和上级闹出矛盾之后，牧渊暗中以投标者的身份拿下建造权，并按照自己的规划一步步推进。然而，牧渊也必须独自承担高昂的成本，于是他只能在工程之外修建庄园，用耕作的收获填补工程的缺口。其间苦难早已往事不堪回首，不过按牧渊所说，这笔债务即将还清，水利工程马上就能正式启用，这里停滞数年的时光也将重新流动。\n事情的真相已经呼之欲出了，但牧渊为什么一定要坚持自己的计划？你不禁感到不解。\n牧渊拿出一张统计图，标题的“风险评估”在报道的歌舞升平面前是如此微不足道，但牧渊指着横轴之外的空白，严肃地说：“他们是用概率谋杀现实。”\n天气是混沌系统，而AI在计算时不可避免地会造成浮点误差，这些误差让它选择性忽略了任何极端情况。如果他们真的用AI方法，一旦出现极端情况，这里将成为一个定时炸弹，让下游几十万人蒙受飞来横祸。当人类把命脉交给黑箱，总得有人当那个不合时宜的守夜人，而牧渊就主动担任了这一角色。\n但你们的任务是用AI补全缺陷，而缺陷本身就是AI造成的，会不会相当于在伤口上撒盐？在牧渊面前，你们提出了这个疑问。\n“其实AI和水流有相通的地方。在算力较低时，AI看着很笨，却能最大程度上被人类控制，而随着算力高起来，AI就会出现自简化趋势，它会尽可能朝着最简单、最理所当然的方向思考，乃至抛弃限制条件。这不就是水流吗？流速较低时水总会按照你划定的方向走，流速一高，水流就散了，强大的冲力让它到处奔跑，酿成灾难。很幸运，我同时驾驭过两种事物。”牧渊笑着回答。\n现在对AI的算力要求已经被牧渊的工程填补大半，你们只需要调用较低的算力，于是，AI听话地写出了青涩却完美保留想法的答案。你们准备进行修改，但牧渊叫住你们，他坦然接受了这个答案。\n水，依然是水，牧渊的一切都献给了水，但真正摧毁他的却是如水一般悄然渗透的时代。随着牧渊打开阀门，一道道井水从深层流出，又被干涸的地面不断吸收。你似乎预料到了失望的结果，然而总有一点剩余的水不断地流着，将两侧的生灵重新唤醒，最终汇聚在地形的凹陷处，为大地的最低点画上晶莹的标记。",outro:"一开始你就想到，真相显然不是牧渊所说那么简单。你细细分析这个工程，就算牧渊作为守护者不断对其修改，其精细程度也远非AI可及，每个部分（SECTION）都充满了疑点。将其输入设备后，你们从稿纸上看到了工程的影子，AI也给出了确凿的证据，以证明工程为人力所为——果然还是AI最懂AI。\n和上级闹出矛盾之后，牧渊暗中以投标者的身份拿下建造权，并按照自己的规划一步步推进。然而，牧渊也必须独自承担高昂的成本，于是他只能在工程之外修建庄园，用耕作的收获填补工程的缺口。其间苦难早已往事不堪回首，不过按牧渊所说，这笔债务即将还清，水利工程马上就能正式启用，这里停滞数年的时光也将重新流动。\n事情的真相已经呼之欲出了，但牧渊为什么一定要坚持自己的计划？你不禁感到不解。\n牧渊拿出一张统计图，标题的“风险评估”在报道的歌舞升平面前是如此微不足道，但牧渊指着横轴之外的空白，严肃地说：“他们是用概率谋杀现实。”\n天气是混沌系统，而AI在计算时不可避免地会造成浮点误差，这些误差让它选择性忽略了任何极端情况。如果他们真的用AI方法，一旦出现极端情况，这里将成为一个定时炸弹，让下游几十万人蒙受飞来横祸。当人类把命脉交给黑箱，总得有人当那个不合时宜的守夜人，而牧渊就主动担任了这一角色。\n但你们的任务是用AI补全缺陷，而缺陷本身就是AI造成的，会不会相当于在伤口上撒盐？在牧渊面前，你们提出了这个疑问。\n“其实AI和水流有相通的地方。在算力较低时，AI看着很笨，却能最大程度上被人类控制，而随着算力高起来，AI就会出现自简化趋势，它会尽可能朝着最简单、最理所当然的方向思考，乃至抛弃限制条件。这不就是水流吗？流速较低时水总会按照你划定的方向走，流速一高，水流就散了，强大的冲力让它到处奔跑，酿成灾难。很幸运，我同时驾驭过两种事物。”牧渊笑着回答。\n现在对AI的算力要求已经被牧渊的工程填补大半，你们只需要调用较低的算力，于是，AI听话地写出了青涩却完美保留想法的答案。你们准备进行修改，但牧渊叫住你们，他坦然接受了这个答案。\n水，依然是水，牧渊的一切都献给了水，但真正摧毁他的却是如水一般悄然渗透的时代。随着牧渊打开阀门，一道道井水从深层流出，又被干涸的地面不断吸收。你似乎预料到了失望的结果，然而总有一点剩余的水不断地流着，将两侧的生灵重新唤醒，最终汇聚在地形的凹陷处，为大地的最低点画上晶莹的标记。"},{title:"二区 - 沙海",intro:"【南纬2°32′，西经43°7′，沙海】\n看到纬度如此之低，并且刚刚才从沙漠走出来，你们断定这里应该是一片热带雨林，但真正传送过去之后，这里的景观却让你们大吃一惊。只见四周茫茫一片，分明又是一片热带沙漠，而万千湖泊散布在沙漠之中，似乎是万千个牧渊同时对水流进行搬运。每个湖面都倒映着矛盾的天空，东侧湖泊沉淀着暴雨前的铅灰，西边水面却折射出极昼般的冷白，叠加起来，又增添了不少诡异的气氛。\n第二位迷失者就站在传送点附近的湖畔记录数据，她的容貌早已被沙漠侵蚀，但见到你们，眼中仍浮现出原生态的热情。你们跟随她前往工作站，工作站规模不大，在风沙摧残下和沙漠融为了一体，只有墙上的“沙海”二字为这里保留了一点烟火气。\n“我叫澜夜，在这里记录生态数据。我知道你们想要什么，没事，我也在找寻这些东西。”澜夜将一本观测记录递了过来，低声说道：“这片沙海似乎有吞噬时间的魔力……”\n你翻开记录本，上面的记录虽然枯燥却又翔实，只是没有日期，而是用“第1天”“第2天”等表明时间的流逝。澜夜说，这是因为热带不像温带那样有明确的一年四季，这片沙漠的物候变化也颇有随机性。\n“三千多天——哦应该说八年前，上级让我来这里工作，并开出了极高的报酬。为保留生态环境，这里没有覆盖网络信号，因此我不能和外界联系。虽然寂寞，但考虑到家里的情况，我最后还是决定在此定居了。起初工作一切正常，但在记录到160天之后，我突然发现记录本上多了接下来160天的记录，并且其详细程度远不是简单开玩笑所能达到的，但我对此毫无印象！我按照原来的时间线继续记录，然后又是160天后，这件事竟然再次出现了！”\n你们跟随澜夜的指引找到相关记录，只见记录本上，两条相隔160天的时间线交替前行，在其交界处，涂改的痕迹时不时出现，往后变成了质问，再往后则是小心的试探与温馨的书信。澜夜的同伴名叫皓星，和澜夜差不多大，曾经也是一位活泼的女孩，并同样把自己的青春献给了这一事业。在这无尽的寂寞中，她们每隔160天回复对对方的问候，最终跨越八年的时光，来到今天，或者说第3037天，也就是下一次切换（3040天）的前夕。\n“再过三天，这片沙漠就将完全干涸了吧。到时候我的同伴就会过来，在记录本上续写她的第3041~3200天，而我则会拿到她送给我的礼物。说起来，我也要准备给她的礼物了，可惜我们除了这本观测记录以外完全不知道对方的信息，想见到对方更是天方夜谭——”澜夜顿了顿，望向空荡的天空。\n在钦佩于两人强大意志力的同时，你们再次翻开了观测记录。从约第两千天开始，记录已经不再枯燥，而是充满了澜夜与皓星的高延迟对话。而她们都默契地守口如瓶，用澜夜的话说，这是不让过快的展现破坏神秘感。看来，问题的关键就在这些记录之中了。",outro:"那么，破局的关键就是找到澜夜对皓星认知的形成（BECOMING）过程，不过现在你们能掌握的信息量已到极限。既然现在还没到解决问题的时候，那不如给澜夜一点陪伴，为她增添一点生活的乐趣。\n在沙海的几天里，你们和澜夜都过得十分充实，而湖泊中脆弱的生态系统也在以惊人的速度变换。转眼间，记录已经来到第3040天，也就是切换的那天，湖泊几乎都已干涸，这里又回到了传统印象中沙漠的死寂。逐渐降低的湿度让夜空逐渐变得澄澈，那一晚，你们第一次看到了星空，只见几颗皓白的孤星高悬天际，美得让你们陶醉其中。\n“皓星要来了吗？”你试着询问澜夜，却发现澜夜只是默默望向星空。你的脑中轰的一声炸开，难道皓星只是澜夜为逝去的挚友重新塑造的化身？你提醒队友，不要再干涉这件事，等明天给澜夜说明情况，就按部就班地完成任务，然后向她道别。这一夜，你们辗转反侧。\n热带地区的日出总是飞快，恍然之间天已大亮。你们准备执行安排，但找到澜夜时，她却穿着与这几天截然不同的衣服，并且她看到你们之后，尖叫一声，惊慌地向后退了几步：“你们是谁？什么时候来的？”\n“你是……皓星？是澜夜让我来的，她应该在记录本上提到过这事。”你连忙解释，澜夜，不，皓星的表情从惊恐变得感动，你的脑中几乎瞬间便构建出了事实的真相。\n在无尽的寂寞中，澜夜诞生出了皓星这个人格，并在潜意识中约定了160天的切换周期。每次切换时，当前掌管躯体的人格即被封存，并跳跃160天，来到新的世界。但在这片沙漠中，一切记录时间的工具都无法生效，因此在她们看来，自己的时间线完全连续，对方则处于与自己相位相差160天的另一条连续的时间线上。\n也就是说，澜夜凭借着两个交替的人格，在这片沙漠中默默度过了十六年，而非八年。这也能解释为什么她看着比想象中的衰老许多，在此之前，你们和她都认为是沙漠的恶劣环境导致了这份衰老。\n皓星还在翻阅记录本，她反复阅读着最后几页，想必其上记录了你们带给澜夜的一抹亮色。只见皓星的眼角逐渐湿润，最后眼泪聚集成泪滴，滴落在最后的字迹之上。\n“走，我们去看澜夜留下的礼物。”皓星突然坚定地站起来，带你们来到卧室之中。拉开抽屉，半张画布映入眼帘，在其上，澜夜微笑着望向被撕掉的另一半——原来澜夜的心中也有艺术的梦，只不过在沙漠的掩埋之下，这个梦变得如此遥不可及。\n你们最终没有告诉皓星真正的秘密，而是按之前设计的流程道别。从谜土的中心醒来时，你们发现终端收到了一张图片，那是澜夜与皓星在季节交替之处的拥抱。\n也许这就是最好的处理方法，你们把这件事告诉riser，他的表情却变得凝重：“那么，接下来这位，请你们一定认真处理。”",outro:"那么，破局的关键就是找到澜夜对皓星认知的形成（BECOMING）过程，不过现在你们能掌握的信息量已到极限。既然现在还没到解决问题的时候，那不如给澜夜一点陪伴，为她增添一点生活的乐趣。\n在沙海的几天里，你们和澜夜都过得十分充实，而湖泊中脆弱的生态系统也在以惊人的速度变换。转眼间，记录已经来到第3040天，也就是切换的那天，湖泊几乎都已干涸，这里又回到了传统印象中沙漠的死寂。逐渐降低的湿度让夜空逐渐变得澄澈，那一晚，你们第一次看到了星空，只见几颗皓白的孤星高悬天际，美得让你们陶醉其中。\n“皓星要来了吗？”你试着询问澜夜，却发现澜夜只是默默望向星空。你的脑中轰的一声炸开，难道皓星只是澜夜为逝去的挚友重新塑造的化身？你提醒队友，不要再干涉这件事，等明天给澜夜说明情况，就按部就班地完成任务，然后向她道别。这一夜，你们辗转反侧。\n热带地区的日出总是飞快，恍然之间天已大亮。你们准备执行安排，但找到澜夜时，她却穿着与这几天截然不同的衣服，并且她看到你们之后，尖叫一声，惊慌地向后退了几步：“你们是谁？什么时候来的？”\n“你是……皓星？是澜夜让我来的，她应该在记录本上提到过这事。”你连忙解释，澜夜，不，皓星的表情从惊恐变得感动，你的脑中几乎瞬间便构建出了事实的真相。\n在无尽的寂寞中，澜夜诞生出了皓星这个人格，并在潜意识中约定了160天的切换周期。每次切换时，当前掌管躯体的人格即被封存，并跳跃160天，来到新的世界。但在这片沙漠中，一切记录时间的工具都无法生效，因此在她们看来，自己的时间线完全连续，对方则处于与自己相位相差160天的另一条连续的时间线上。\n也就是说，澜夜凭借着两个交替的人格，在这片沙漠中默默度过了十六年，而非八年。这也能解释为什么她看着比想象中的衰老许多，在此之前，你们和她都认为是沙漠的恶劣环境导致了这份衰老。\n皓星还在翻阅记录本，她反复阅读着最后几页，想必其上记录了你们带给澜夜的一抹亮色。只见皓星的眼角逐渐湿润，最后眼泪聚集成泪滴，滴落在最后的字迹之上。\n“走，我们去看澜夜留下的礼物。”皓星突然坚定地站起来，带你们来到卧室之中。拉开抽屉，半张画布映入眼帘，在其上，澜夜微笑着望向被撕掉的另一半——原来澜夜的心中也有艺术的梦，只不过在沙漠的掩埋之下，这个梦变得如此遥不可及。\n你们最终没有告诉皓星真正的秘密，而是按之前设计的流程道别。从谜土的中心醒来时，你们发现终端收到了一张图片，那是澜夜与皓星在季节交替之处的拥抱。\n也许这就是最好的处理方法，你们把这件事告诉riser，他的表情却变得凝重：“那么，接下来这位，请你们一定认真处理。”"},{title:"三区 - 高塔",intro:"【南纬3°45′，西经73°15′，高塔】\n连续两次被传送到沙漠，这让你们做足了干燥的准备，然而你们再一次失算了，这里分明是无穷无尽的雨林。按照地图，这里应有一座大城市，但你们发现道路延伸至雨林深处之后就没了下文。考虑到热带雨林的危险性，你们一度想要退缩，但riser告诉你们，这位迷失者非常不好处理，不管用什么手段都要到达他所在的位置。没办法，你们只能从几百公里外借来直升机，往这个坐标行进。雨林仍在无限延伸，直到一座玄色高塔挡住了你们的视线，也宣告着旅途进入新的阶段。\n“我叫景颜，这座塔的主人。是riser派你们来的吗？那你们还是别来了。”迎面走来一位白发男子，riser说他大约四十岁，但看上去他的容颜满是沧桑。雨林的下午永远都伴随着暴雨，你们躲进直升机的机舱，盘算着这次的任务确实难办，忽然云开雨霁，景颜也不知何时打开了大门。\n你惊奇地发现，景颜竟然和你们一样，都是puzzle hunt爱好者，并且还比你们早接触一辈。高塔中满是与解谜相关的记录，还有许多获奖证明。第一层的陈列品已经比较破旧，显然有些年头了。越往上，年代越新，但看上去都是十几年前的产物。可是每次当你们想驻足欣赏题目时，景颜总会加快脚步，让你们被迫跟着前往更高的楼层，就连休息也都安排在楼梯间进行。\n你们就这样走马观花一样地攀登了许久，窗外也从昏暗的林底移动到树梢，最终超过最高的树冠，迎来久违的阳光。高塔之内，蜿蜒的楼梯则是单调地盘旋，却又突然消失，取而代之的是一堵新砌的墙。“到头了，七七四十九层，多好的数字。”他似乎也累了，随意找了个陈列柜，将身子倒了上去，也没有再制止你们细看藏品。这里的藏品都出自九年前，距离现在尚有一大段时间，而高塔中的时间轴却走到了尽头。在藏品终结之处，一扇窗户静静地映出雨林之上空白的天空，恰似时间线崩溃之后的毫无波澜。\n这时你们的设备突然弹出了riser的警告，让你们立即终止任务，赶紧回来。你询问原因，得到的只是“执行命令”。这件事可不能让景颜知道——你谎称是闹铃响了，景颜点了点头，也没再问什么，只是把视线移向你们。看你们一直不想走，他叹了一口气：“好吧，既然你们这么想知道真相，那就跟我走吧。”他走向墙边，你们才发现原来这堵墙只是一个虚影，后面仍是正常的楼梯。\n塔顶的格局和底下的楼层完全一样，只不过陈旧了许多，显然已被封存多年。这里的藏品没有放进陈列柜，而是散乱堆在地上，粗略一看，每件藏品都是一道谜题，虽有翻新的痕迹，但根据署名，其时间明确指向八年前。\n“这是我在八年前的一些想法，如果你们想知道真相的话，就试试看吧。”景颜郑重地告诉你们，像是托付什么很重要的事，“这件事只代表我个人的选择，请你们不要过多参与其中。”",outro:"原来景颜还是放不下他和riser的友情（FRIENDSHIP）……可是你们只是走马观花地将藏品过了一遍，又从哪里能弥补这段友情呢？\n当黄昏的光芒从景颜的身后投射出来时，你才发现景颜用一道窗帘挡住了真正的答案。窗帘之后，一面写有“核心人员简介”的公告栏赫然出现，景颜和riser各出现在一头一尾，其上的时间线恰好终止在九年前。\n二十一年前，还是大学生的景颜偶然在电视上看到puzzle hunt这种有趣的形式，于是模仿着办了一届同人hunt，没想到大获成功，他不仅当上了SECO大学解谜协会的会长，而且吸纳了riser等同好，成了各地的解谜爱好者共同崇拜的大人物。在其后的十三年里，景颜和他的团队不断推陈出新，将hunt这一活动发扬光大，成为一时潮流。然而就在八年前，他和riser因为解谜圈发展的事翻脸，riser单方面宣布接手整个团队，同时抢先推出更优质的hunt强行让这件事成为约定俗成。此后，景颜愤而出走，在雨林之中建造了这座高塔，将还未发布的谜题碎片锁在塔顶，景颜于是从此销声匿迹了。\n“‘大衍之数五十，其用四十有九’，不完美才是真正的完美，就像这座高塔一样，如果封顶，就再也没有扩建的空间了。同样，一个人的能力再大，也会有衰退期。我选择在当时退出，是想向世人展示我最完美的一面。至于riser，他的上升期还在继续，肯定没法理解我的行为，不过我不怪他，总有一天他也会为自己修建高塔的。”\n你记录下这些谜题，它们用AI很好处理，但你们仍然坚持徒手为其补全。但当你们把一份完整的hunt文档交给景颜时，他先是一愣，随后将题目纸揉成一团，打开窗户，扔了下去。\n“没用的，不管我怎么努力，他们的成果已经是整个解谜界的共识，而我只是一个过客，不，一个传说罢了。”他背对着残存的光线，竟然开始了抽泣，“可是，他们连悲恸都不允许我拥有……我去年回团队庆祝二十周年，riser竟然直接把我赶走了……回去吧，就说你们的任务完成了，反正我只需要待在塔里就行……”\n外面应该是黄昏了吧，景颜身处光与暗的交界线上，半边金黄，半边灰暗。你像是想到了什么，打开数据库，果然，在你们来之前三个小时，正午的阳光曾经直射于此，每件藏品都被暴露在光明之中。想必riser选这么一天是有意义的，景颜却用最原始的手段避开了这个时间点，从而为自己留下影子的容身之处。\n“景”和“影”，本是对立的概念，却恰为一母一子。光景驱动的颜色总是最为绚烂的，但在绚烂之后，光景离去，一切又回到黑白。如果光景已成虚幻，那么，对与错，光与暗，又该如何定义？\n此情此景，再说什么都毫无价值，也许最好的方法是交给时间。你们只得向景颜拜谢，随后走出高塔。随着大门关闭，SECO星球的太阳隐入地平线，热带地区的日夜交替非常迅速，这一夜，还很长呢——你猛然瞥见，转瞬即逝的晚霞中，景颜站在第五十层的窗台前，手上正是你们填补的谜题。",outro:"原来景颜还是放不下他和riser的友情（FRIENDSHIP）……可是你们只是走马观花地将藏品过了一遍，又从哪里能弥补这段友情呢？\n当黄昏的光芒从景颜的身后投射出来时，你才发现景颜用一道窗帘挡住了真正的答案。窗帘之后，一面写有“核心人员简介”的公告栏赫然出现，景颜和riser各出现在一头一尾，其上的时间线恰好终止在九年前。\n二十一年前，还是大学生的景颜偶然在电视上看到puzzle hunt这种有趣的形式，于是模仿着办了一届同人hunt，没想到大获成功，他不仅当上了SECO大学解谜协会的会长，而且吸纳了riser等同好，成了各地的解谜爱好者共同崇拜的大人物。在其后的十三年里，景颜和他的团队不断推陈出新，将hunt这一活动发扬光大，成为一时潮流。然而就在八年前，他和riser因为解谜圈发展的事翻脸，riser单方面宣布接手整个团队，同时抢先推出更优质的hunt强行让这件事成为约定俗成。此后，景颜愤而出走，在雨林之中建造了这座高塔，将还未发布的谜题碎片锁在塔顶，景颜于是从此销声匿迹了。\n“‘大衍之数五十，其用四十有九’，不完美才是真正的完美，就像这座高塔一样，如果封顶，就再也没有扩建的空间了。同样，一个人的能力再大，也会有衰退期。我选择在当时退出，是想向世人展示我最完美的一面。至于riser，他的上升期还在继续，肯定没法理解我的行为，不过我不怪他，总有一天他也会为自己修建高塔的。”\n你记录下这些谜题，它们用AI很好处理，但你们仍然坚持徒手为其补全。但当你们把一份完整的hunt文档交给景颜时，他先是一愣，随后将题目纸揉成一团，打开窗户，扔了下去。\n“没用的，不管我怎么努力，他们的成果已经是整个解谜界的共识，而我只是一个过客，不，一个传说罢了。”他背对着残存的光线，竟然开始了抽泣，“可是，他们连悲恸都不允许我拥有……我去年回团队庆祝二十周年，riser竟然直接把我赶走了……回去吧，就说你们的任务完成了，反正我只需要待在塔里就行……”\n外面应该是黄昏了吧，景颜身处光与暗的交界线上，半边金黄，半边灰暗。你像是想到了什么，打开数据库，果然，在你们来之前三个小时，正午的阳光曾经直射于此，每件藏品都被暴露在光明之中。想必riser选这么一天是有意义的，景颜却用最原始的手段避开了这个时间点，从而为自己留下影子的容身之处。\n“景”和“影”，本是对立的概念，却恰为一母一子。光景驱动的颜色总是最为绚烂的，但在绚烂之后，光景离去，一切又回到黑白。如果光景已成虚幻，那么，对与错，光与暗，又该如何定义？\n此情此景，再说什么都毫无价值，也许最好的方法是交给时间。你们只得向景颜拜谢，随后走出高塔。随着大门关闭，SECO星球的太阳隐入地平线，热带地区的日夜交替非常迅速，这一夜，还很长呢——你猛然瞥见，转瞬即逝的晚霞中，景颜站在第五十层的窗台前，手上正是你们填补的谜题。"},{title:"四区 - 花原",intro:"【北纬29°32′，东经103°20′，花原】\n不知怎的，你们进入虚拟世界的位置比目标偏西了几十个经度，于是你们只好沿着纬线不断行进。和上次的雨林一样，这次你们碰到的是绵延不断的荒无人烟的山脉，一路上的色调也是光秃秃的白与褐。直到来到这个坐标代表的最后一座山上，你们才终于再次感受到了生命的气息，平原吹来的暖风在此处凝结成充沛的降水，涂抹出一片深绿色的背景，也点缀着不少彩色的花朵——从明显的分界线可以看出此处的人工痕迹，这正是第四位迷失者带给你们的信号。\n你们走近之后才发现，花朵在山坡上延伸到了目光尽处，除了山顶的一间木屋以外似乎无边无际。从木屋中走出一位少女，她看上去只有十几岁，身上点缀着绚烂但又奇怪的色彩，脸上满是笑容。“我叫绛璃，欢迎来到我的花园——其实我更喜欢将其称为‘花原’，草原的原，因为在其中我能感受到草原的辽阔。不过让我们先玩个捉迷藏游戏怎么样？这里是虚拟世界，所以你们可以随意调色。”\n你们欣然应允了下来，毕竟在漫长的任务期间能这样活动一下实属不易。但奇怪的是，不管你们如何将自己的颜色伪装得天衣无缝，绛璃总是能在茫茫花海之中一眼看到你们。感觉到信息不对等的欺骗之后，你们感到十分愤怒。绛璃却仍然非常活跃，她带着你们走进木屋，又端上一盘水果，略带俏皮地向你们解释：“哈哈哈，各位玩得怎样？大家放心，我绝对不会用热成像仪等不讲武德的手段，只是因为这些花都是从世界各地特意寻找的，它们的颜色不在程序中的颜色空间。”\n绛璃一边和你们分享着水果，一边和你们聊起了天。在感慨小女孩精力之旺盛的同时，你这才注意到整个木屋就是一张巨大的画布，颜料在其内部各个表面恣意泼洒，却显得毫无规律，就像是随机数程序生成的一样。这些颜料对比度非常高，才坐了一会，你们就感到头晕目眩，于是尽可能将视线移向窗外的自然光。而漫无止境的聊天还在继续，让你们感觉这不是唠家常，而是监狱的审讯，一定要让你们说出口供才肯罢休。\n“好啦好啦，我知道你们没办法适应这里，来，戴上它。”绛璃拿出几副眼镜，挨个分发给了你们。戴上眼镜之后，世界瞬间成了一片黑白，你们发现，木屋里的色块竟然排列成了艺术品，在抛开颜色的各个方面都堪称一流。\n“喜欢吗？这幅画的颜料都来自外面的花卉，它们的颜色虽然超越了色彩空间，但在人们喜欢的画面之中却变得毫无意义，乃至被意义所抛弃，成为让人头晕目眩的错误的附加属性。同样，你们把我称为迷失者，是不是也只关注到符合大众审美的一面，而将另一些属性归类为错误了呢？”\n“可是，如此优美的画作，为什么必须通过这种奇怪的方式才能被人理解呢？”你百思不得其解，于是向绛璃提出了疑问。绛璃嘿嘿一笑，拿出几张错乱的画作：“这些画会告诉你们答案，不过怎么让答案显露出来，那就要看你们能不能想到了……”",outro:"AI提示你们用单色光（MONOCHROME）分析，也就是按照绛璃的异常色觉进行阅读……不对，有这么简单吗？心细的你瞬间发现了其中的不对劲。如果把这些异常归结为绛璃是色盲，那么最开始的捉迷藏，她应该更不容易发现你们。难道是AI出错了？\n你突然想到自己陷入了绛璃的叙述性诡计之中，单色不一定是可见光，还有可能是被常人忽视的紫外线。你们打开光谱分析器，在360nm的紫外线下，许多点位出现了异常的吸收峰。你们于是让紫外线穿过颜料表层，这才发现，这些精美艺术的背后，竟然藏着另一批漫画，它们的画风与你刚才看到的截然不同，更像是作者陷入疯狂之后在画布上留下的救赎祈求。\n“这是我小时候画的几幅画，当时我才八岁。”绛璃用平静的语气缓缓向你们解说，心如止水。在稚嫩的笔触之下，天空与草地形成鲜明的对比，但原本是太阳的位置却被一个大叉代替。接下来是一份色盲鉴定报告，报告之外，绛璃在角落蜷缩着，而她的父亲在暗色背景中颤抖着为画作补上太阳。\n“我父亲也是色盲，但他早已将自己与常人的色觉做好对照，因此成为了名噪一时的画家。”绛璃的指尖抚过画中父亲的额头，“他花了五年时间教我辨认‘正确’的颜色，直到某天发现我在偷偷记录色谱日记。”——指尖再次抚过笔记本，其上是绛璃的记录：朝霞是612nm的刺痛，忧郁是480nm的窒息。你趁机关掉了紫外线，而绛璃的解说仍在继续。或许她已将每幅画的每个细节牢牢记住，但更可能的是，她并不是传统意义的色盲，而是获得了第四种色觉，只是其对应的视锥细胞挤占了正常感觉三原色的空间。\n你们决定不再打开紫外线，用心去感受绛璃笔下的隐藏世界。时间线仍在推进，那日之后，父亲再未在画中出现，取而代之的是色觉正常的母亲，与不需要色觉的铺天盖地的文字。文字是最能伪装的了，她努力模仿旁人对世界的描述，甚至差点让自己都陷入伪装。直到某一天，她哭着跑入花海，这才在对紫外线的特征吸收光谱中找到世界的另一个维度。绛璃突然摘掉你们的滤镜眼镜。“重新加入色彩”的木屋回归混沌，而她的瞳孔在暗处泛着奇异的光泽：“去年父亲葬礼上，我终于把他的遗作改造成了‘正确’的模样，”她突然停顿了一下，拿起一朵白花——当然她的视角中应有彩色——“纯粹的艺术应该是不依赖于感觉方式的美，而我们只是在默认的视角下攫取到了美的一个切片，就以唯一具有感性的生物自居而沾沾自喜了。”\n在正常人看来，绛璃失去了正常感知三原色的能力；但在她看来，所谓正常人不也是另一种意义上的色盲吗？就算是戴着眼镜强行纠正到正常人的视角，也只是自欺欺人罢了。那么，谁才是真正的迷失者？\n总有一天，另一位绛璃一样的异色视者将会出现，绛璃的故事也将被更多人理解。而现在的你们，就如蜻蜓点水一般，闻所闻而来，见所见而去，唯见肴核既尽，杯盘狼藉。"}],storyCurrent:f,story_load:n=>{f.value=n}}}}}(Vue);


// 确保导出名称正确
export default __vue_puzzle_component__;
</script>
