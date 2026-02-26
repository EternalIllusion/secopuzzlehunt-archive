
<!-- seco2-knot Puzzle -->
<template>

    <div class="knot-game-container">
        <div class="level-selector" id="levelSelector">
            <button v-for="i in TOTAL_LEVELS" :key="i" class="level-btn" :class="{
                'solved': progress.levelStates[i - 1]?.solved,
                'active': currentLevelIndex === i - 1,
            }" :disabled="i - 1 > progress.unlockedLevel" @click="loadLevel(i - 1)">
                {{ i }}
            </button>
            <button class="btn-game" @click="unlockAll">全部解锁</button>
        </div>
        <div class="status-bar">
            <span id="levelTitle">关卡 {{ currentLevelIndex + 1 }}</span>
            <div id="gameStatus" class="status-text"
                :class="{ 'status-success': progress.levelStates[currentLevelIndex]?.solved }">
                {{ statusText }}
            </div>
        </div>
        <div class="knot-canvas-wrapper" id="canvasWrapper" ref="canvasWrapperRef">
            <canvas id="gameCanvas" ref="canvasRef"></canvas>
            <div class="zoom-controls">
                <button class="zoom-btn" @click="zoomIn">+</button>
                <button class="zoom-btn" @click="resetView">⌂</button>
                <button class="zoom-btn" @click="zoomOut">-</button>
            </div>
        </div>
        <div class="controls">
            <button class="btn-game" @click="resetLevelPositions">重置本关布局</button>
            <button class="btn-game" @click="snapLevelPositions" style="display: none;">吸附到grid125px</button>
            <button class="btn-game" @click="pasteLevelPositions">一键完成本关</button>
        </div>
        <div id="final-victory" v-if="isAllLevelsSolved">
            <h2>🎉 恭喜！你已解开所有绳结！</h2>
            <p>所有关卡均已通过，你的耐心令人钦佩。</p>
            <p class="xm">如果你用了一键完成的话当我没说（</p>
        </div>
    </div>

</template>

<style>

/* ================= 容器样式 ================= */
.knot-game-container {
    font-family: var(--text-font);
    background: rgba(var(--accent-bg-rgb), 0.15);
    border: 2px solid var(--border-color);
    border-radius: 12px;
    padding: 20px;
    color: var(--body-text-color);
    text-align: center;
    position: relative;
    min-height: 600px;
    display: flex;
    flex-direction: column;
    user-select: none;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
    backdrop-filter: blur(5px);
}

/* ================= 画布区域 ================= */
.knot-canvas-wrapper {
    position: relative;
    flex: 1;
    width: 100%;
    min-height: 500px;
    overflow: hidden;
    border: 2px solid var(--primary-green);
    border-radius: 10px;

    /* 深色背景，确保白线和彩色节点清晰可见 */
    background: rgba(20, 20, 20, 0.9);
    box-shadow: inset 0 0 20px rgba(0, 0, 0, 0.8);

    cursor: grab;
    touch-action: none;
    transition: border-color 0.3s ease;
}

/* 当关卡完成时，边框变绿以示庆祝 */
.knot-canvas-wrapper.solved-state {
    border-color: var(--mint-green);
    box-shadow: 0 0 20px rgba(var(--mint-green), 0.2);
}

.knot-canvas-wrapper:active {
    cursor: grabbing;
}

canvas {
    display: block;
    width: 100%;
    height: 100%;
}

/* ================= UI 控件 ================= */
.level-selector {
    display: flex;
    justify-content: center;
    gap: 10px;
    margin-bottom: 20px;
    flex-wrap: wrap;
}

.level-btn {
    width: 44px;
    height: 44px;
    border-radius: 50%;
    border: 2px solid var(--border-color);
    background: rgba(var(--accent-bg-rgb), 0.3);
    color: var(--accent-green);
    font-family: var(--input-font);
    font-weight: bold;
    font-size: 1.1rem;
    cursor: pointer;
    transition: all 0.2s;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.level-btn:hover:not(:disabled) {
    transform: translateY(-2px) scale(1.1);
    background: var(--btn-hover-color);
    color: var(--white-color);
    border-color: var(--light-flair-rgb);
}

.level-btn.active {
    background: var(--primary-green);
    color: var(--white-color);
    border-color: var(--white-color);
    transform: scale(1.15);
    box-shadow: 0 0 15px var(--glow-color);
}

.level-btn.solved {
    background: var(--dark-green);
    border-color: var(--secondary-green);
    color: var(--mint-green);
}

.level-btn:disabled {
    opacity: 0.3;
    cursor: not-allowed;
    background: #111;
    border-color: #333;
}

.status-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 12px 24px;
    background: rgba(var(--dark-accent-rgb), 0.6);
    border-left: 4px solid var(--accent-green);
    border-radius: 8px;
    margin-bottom: 15px;
}

#levelTitle {
    font-family: var(--accent-font);
    color: var(--accent-green);
    font-weight: 700;
    font-size: 1.2rem;
}

.status-text {
    font-family: var(--input-font);
    font-size: 1.1rem;
    font-weight: bold;
    color: var(--subtle-text-color);
}

.status-success {
    color: var(--mint-green) !important;
    text-shadow: 0 0 10px var(--glow-color);
}

.controls {
    margin-top: 15px;
    display: flex;
    justify-content: center;
    gap: 15px;
}

.btn-game {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 10px 24px;
    border-radius: 25px;
    background: var(--btn-bg-color);
    color: var(--btn-text-color);
    border: none;
    cursor: pointer;
    font-family: var(--btn-font);
    font-weight: 600;
    transition: all 0.3s ease;
}

.btn-game:hover {
    background: var(--btn-hover-color);
    box-shadow: 0 0 15px var(--glow-color);
}

#final-victory {
    margin-top: 20px;
    padding: 20px;
    background: rgba(var(--secondary-green), 0.3);
    border: 2px solid var(--primary-green);
    border-radius: 10px;
    color: var(--white-color);
}

.zoom-controls {
    position: absolute;
    bottom: 15px;
    right: 15px;
    display: flex;
    flex-direction: column;
    gap: 8px;
}

.zoom-btn {
    width: 36px;
    height: 36px;
    background: rgba(255, 255, 255, 0.1);
    color: white;
    border: 1px solid rgba(255, 255, 255, 0.3);
    border-radius: 6px;
    cursor: pointer;
    font-size: 1.2rem;
    transition: all 0.2s;
}

.zoom-btn:hover {
    background: rgba(255, 255, 255, 0.3);
}

.xm {
    text-decoration: line-through;
    color: #eee;
}

</style>

<!-- 请将以上部分复制到后台“题目HTML”中，以下部分复制到后台“题目脚本”中，不要包含<script>标签 -->

<script>
var __vue_puzzle_component__=function(t){"use strict";const e=[{name:"riser的脚好香",nodes:[{x:.6041406567177076,y:.6266155088852988,text:"",textDisplay:"",color:"#666666"},{x:.24084477656789488,y:.3939822294022617,text:"",textDisplay:"",color:"#ff5d5d"},{x:.2420932160185815,y:.5991518578352181,text:"",textDisplay:"",color:"#ff5d5d"},{x:.2445900949199548,y:.29705169628432954,text:"",textDisplay:"",color:"#3eb1ff"},{x:.2383478976665216,y:.500605815831987,text:"",textDisplay:"",color:"#3eb1ff"},{x:.24334165546926814,y:.699313408723748,text:"",textDisplay:"",color:"#3eb1ff"},{x:.6041406567177076,y:.4004442649434572,text:"5",textDisplay:"5",color:"#666666"}],edges:[[3,0],[0,4],[0,1],[4,6],[6,1],[2,6],[6,5]],timestamp:"2025-12-11T14:22:39.105Z",version:"1.3"},{name:"riser好美味",nodes:[{x:.2368220272267935,y:.8113709795858423,text:"",textDisplay:"",color:"#3b8b5a"},{x:.18385792931887537,y:.20269945007424822,text:"",textDisplay:"",color:"#666666"},{x:.7513304069037124,y:.8619576214487361,text:"",textDisplay:"",color:"#ffb000"},{x:.33770602324187565,y:.12763540085834119,text:"",textDisplay:"",color:"#666666"},{x:.3465333728931953,y:.8668531029193387,text:"",textDisplay:"",color:"#f44336"},{x:.8471702031180405,y:.7787344364484914,text:"7",textDisplay:"7",color:"#666666"},{x:.6201812120841056,y:.894594164586087,text:"",textDisplay:"",color:"#3b8b5a"},{x:.9077006007270898,y:.4931646839966711,text:"",textDisplay:"",color:"#f44336"},{x:.12584963161020316,y:.705302214389452,text:"",textDisplay:"",color:"#ffb000"},{x:.11071703220794081,y:.35772302997666494,text:"",textDisplay:"",color:"#666666"},{x:.08549603320417029,y:.5094829555653466,text:"",textDisplay:"",color:"#f44336"},{x:.49407621706525295,y:.8880668559586169,text:"",textDisplay:"",color:"#666666"},{x:.7841177056086142,y:.19617214144677805,text:"",textDisplay:"",color:"#ffb000"},{x:.4814657175633677,y:.121108092230871,text:"",textDisplay:"",color:"#f44336"},{x:.8875238015240734,y:.6351336466441475,text:"",textDisplay:"",color:"#3b8b5a"},{x:.8749133020221881,y:.321822832525579,text:"",textDisplay:"",color:"#3b8b5a"},{x:.6529685107890073,y:.13416270948581135,text:"",textDisplay:"",color:"#ffb000"}],edges:[[0,1],[1,2],[2,3],[3,7],[3,8],[3,4],[4,5],[1,6],[6,5],[5,10],[10,11],[1,12],[12,11],[11,13],[8,9],[9,14],[5,15],[15,9],[11,16],[16,9]],timestamp:"2025-12-07T09:09:15.182Z",version:"1.2"},{name:"我不是神父",nodes:[{x:.26855726894072857,y:.08758243698443866,text:"",textDisplay:"",color:"#ff1f1f"},{x:.6831458999814075,y:.5450259535375547,text:"",textDisplay:"",color:"#666666"},{x:.241264600439618,y:.8796997027804593,text:"",textDisplay:"",color:"#ffcc00"},{x:.6831458999814075,y:.6055699483754671,text:"",textDisplay:"",color:"#666666"},{x:.2932506356798285,y:.5433441759031682,text:"",textDisplay:"",color:"#1aa043"},{x:.34003806739601805,y:.8780179251460729,text:"",textDisplay:"",color:"#ffcc00"},{x:.2932506356798285,y:.46093707181823185,text:"",textDisplay:"",color:"#1aa043"},{x:.458306297567497,y:.08926421461882511,text:"",textDisplay:"",color:"#ff1f1f"},{x:.6831458999814075,y:.4844819586996422,text:"",textDisplay:"",color:"#666666"},{x:.3582331797300917,y:.08926421461882511,text:"",textDisplay:"",color:"#ff1f1f"},{x:.6883445035054286,y:.3095770847234508,text:"",textDisplay:"",color:"#666666"},{x:.40761991320829166,y:.09262776988759802,text:"",textDisplay:"",color:"#ff1f1f"},{x:.6883445035054286,y:.2523966451543113,text:"",textDisplay:"",color:"#666666"},{x:.3127453988949075,y:.08926421461882511,text:"",textDisplay:"",color:"#ff1f1f"},{x:.384226197350197,y:.8830632580492322,text:"",textDisplay:"",color:"#ffcc00"},{x:.6883445035054286,y:.36675752429259034,text:"",textDisplay:"",color:"#666666"},{x:.4310136290663864,y:.8864268133180051,text:"",textDisplay:"",color:"#ffcc00"},{x:.07490928767094425,y:.3903024111740007,text:"",textDisplay:"",color:"#2c6fdb"},{x:.29065133391781806,y:.8830632580492322,text:"",textDisplay:"",color:"#ffcc00"},{x:.6844455508624129,y:.41889263095857043,text:"",textDisplay:"",color:"#666666"},{x:.47780106078257595,y:.8897903685867782,text:"",textDisplay:"",color:"#ffcc00"},{x:.6857452017434181,y:.723294382782519,text:"9",textDisplay:"9",color:"#666666"},{x:.06971068414692319,y:.5298899548280765,text:"",textDisplay:"",color:"#2c6fdb"},{x:.06971068414692319,y:.45420996128068597,text:"",textDisplay:"",color:"#2c6fdb"},{x:.4102192149703022,y:.5483895088063275,text:"",textDisplay:"",color:"#1aa043"},{x:.41281851673231273,y:.4710277376245506,text:"",textDisplay:"",color:"#1aa043"},{x:.35303457620607065,y:.4659824047213912,text:"",textDisplay:"",color:"#1aa043"},{x:.6857452017434181,y:.6677957208477658,text:"",textDisplay:"",color:"#666666"},{x:.35303457620607065,y:.5467077311719412,text:"",textDisplay:"",color:"#1aa043"},{x:.06971068414692319,y:.3331219716048612,text:"",textDisplay:"",color:"#2c6fdb"},{x:.06451208062290213,y:.5971610602035348,text:"",textDisplay:"",color:"#2c6fdb"}],edges:[[0,1],[1,2],[2,3],[3,4],[3,5],[3,6],[1,7],[7,8],[8,9],[9,10],[10,11],[11,12],[12,13],[1,14],[14,15],[15,17],[17,8],[15,16],[16,10],[10,18],[18,19],[19,20],[21,22],[6,21],[8,23],[23,21],[21,24],[24,19],[19,25],[25,12],[12,26],[26,27],[27,28],[15,29],[29,27],[27,30]],timestamp:"2025-12-07T09:34:28.195Z",version:"1.2"},{name:"但是riser真的好香",nodes:[{x:.3712296885401443,y:.6627503879446065,text:"",textDisplay:"",color:"#2fb8f4"},{x:.4752017590205654,y:.6661139432133795,text:"",textDisplay:"",color:"#35bc4e"},{x:.7195361246495551,y:.49120906923718805,text:"",textDisplay:"",color:"#666666"},{x:.5284874451417813,y:.33984908214240706,text:"",textDisplay:"",color:"#666666"},{x:.4765014099015707,y:.5450259535375547,text:"",textDisplay:"",color:"#c14cc5"},{x:.3751286411831601,y:.5517530640751005,text:"",textDisplay:"",color:"#c14cc5"},{x:.6337591665032076,y:.3465761926799528,text:"",textDisplay:"",color:"#666666"},{x:.5882713856680234,y:.5416623982687817,text:"",textDisplay:"",color:"#f44242"},{x:.47910071166358126,y:.5416623982687817,text:"",textDisplay:"",color:"#f44242"},{x:.4297139781853812,y:.32975841633608827,text:"",textDisplay:"",color:"#666666"},{x:.6922434561484444,y:.2557602004230842,text:"",textDisplay:"",color:"#2fb8f4"},{x:.6636511367663286,y:.5786615062252838,text:"",textDisplay:"",color:"#f44242"},{x:.5882713856680234,y:.5416623982687817,text:"",textDisplay:"",color:"#666666"},{x:.4310136290663864,y:.32807663870170184,text:"",textDisplay:"",color:"#35bc4e"},{x:.5856720839060129,y:.6661139432133795,text:"",textDisplay:"",color:"#c14cc5"},{x:.49339687135463917,y:.24566953461676547,text:"1",textDisplay:"1",color:"#666666"},{x:.7117382193635233,y:.3835753006364549,text:"",textDisplay:"",color:"#f44242"},{x:.5843724330250075,y:.4273015191305027,text:"",textDisplay:"",color:"#c14cc5"},{x:.36993003765913907,y:.42393796386172977,text:"",textDisplay:"",color:"#f44242"},{x:.48170001342559177,y:.42393796386172977,text:"",textDisplay:"",color:"#35bc4e"},{x:.6636511367663286,y:.5786615062252838,text:"",textDisplay:"",color:"#666666"},{x:.6454560244322549,y:.46766418235577767,text:"",textDisplay:"",color:"#2fb8f4"},{x:.4323132799473917,y:.32807663870170184,text:"",textDisplay:"",color:"#35bc4e"},{x:.5973689418350602,y:.2507148675199249,text:"",textDisplay:"",color:"#2fb8f4"}],edges:[[7,6],[6,8],[8,9],[5,6],[5,2],[2,10],[10,9],[0,2],[1,3],[3,4],[4,2],[9,11],[11,12],[3,13],[13,12],[3,14],[14,15],[15,16],[15,17],[15,18],[18,12],[12,19],[19,20],[9,21],[21,20],[20,22],[20,23]],timestamp:"2025-12-07T09:47:01.777Z",version:"1.2"},{name:"wwwwwwwwwww",nodes:[{x:.25392098010987624,y:.4377238327330074,text:"",textDisplay:"",color:"#2ca84f"},{x:.6046499316353472,y:.35323025905534805,text:"",textDisplay:"",color:"#666666"},{x:.6979289081048873,y:.39668409694671575,text:"",textDisplay:"",color:"#3366cc"},{x:.2595177186980486,y:.6718917369253778,text:"",textDisplay:"",color:"#666666"},{x:.4386133535195657,y:.7419006979725813,text:"",textDisplay:"",color:"#c4cc23"},{x:.4218684969174579,y:.5749192245557351,text:"",textDisplay:"",color:"#3366cc"},{x:.5117561373668961,y:.6589256865912763,text:"",textDisplay:"",color:"#c4cc23"},{x:.237130764345359,y:.3315033401096642,text:"",textDisplay:"",color:"#666666"},{x:.7165002072795054,y:.6815428109854604,text:"",textDisplay:"",color:"#c4cc23"},{x:.5318923299891058,y:.785354535863949,text:"",textDisplay:"",color:"#666666"},{x:.35466227469697964,y:.505318691675135,text:"",textDisplay:"",color:"#c4cc23"},{x:.19049127611058894,y:.7032750642913655,text:"",textDisplay:"",color:"#3366cc"},{x:.5754265493519148,y:.6944668820678513,text:"",textDisplay:"",color:"#666666"},{x:.32294742269733595,y:.3918558927365638,text:"",textDisplay:"",color:"#3366cc"},{x:.6941977490461058,y:.33633154431981616,text:"",textDisplay:"",color:"#666666"},{x:.27330420228574753,y:.5813812600969306,text:"",textDisplay:"",color:"#3366cc"},{x:.6141281723232007,y:.5135298869143781,text:"",textDisplay:"",color:"#ff3333"},{x:.29123257069769226,y:.23735335801170088,text:"",textDisplay:"",color:"#666666"},{x:.7576274530453931,y:.5825699590375665,text:"",textDisplay:"",color:"#ff3333"},{x:.4640934387319855,y:.19799383729054204,text:"",textDisplay:"",color:"#ff3333"},{x:.7601955880535378,y:.47475767366720517,text:"",textDisplay:"",color:"#666666"},{x:.6195745678704736,y:.5849840611426423,text:"",textDisplay:"",color:"#ff3333"},{x:.4624312073712983,y:.37437296529160347,text:"4",textDisplay:"4",color:"#666666"},{x:.3471999565794164,y:.31460462537413236,text:"",textDisplay:"",color:"#2ca84f"},{x:.6736763742228069,y:.18665721380510525,text:"",textDisplay:"",color:"#ff3333"},{x:.7315093396339217,y:.26390848116753673,text:"",textDisplay:"",color:"#ff3333"},{x:.5057742165776347,y:.5439443253563506,text:"",textDisplay:"",color:"#666666"},{x:.3751836495202785,y:.3990981990517917,text:"",textDisplay:"",color:"#ff3333"},{x:.16623874222850854,y:.5439443253563506,text:"",textDisplay:"",color:"#2ca84f"},{x:.532979608028569,y:.44890953150242324,text:"",textDisplay:"",color:"#2ca84f"},{x:.6083810906941288,y:.2518379706421568,text:"",textDisplay:"",color:"#666666"},{x:.4068985015199221,y:.44738024115331143,text:"",textDisplay:"",color:"#2ca84f"},{x:.6904665899873242,y:.5922263674578703,text:"",textDisplay:"",color:"#9966cc"},{x:.6680796356346345,y:.780526331653797,text:"",textDisplay:"",color:"#9966cc"},{x:.3419683720735128,y:.7510096930533118,text:"",textDisplay:"",color:"#9966cc"},{x:.44234451257834734,y:.3049482169538284,text:"",textDisplay:"",color:"#9966cc"},{x:.18116337846363495,y:.3701289737908799,text:"",textDisplay:"",color:"#9966cc"}],edges:[[0,1],[1,2],[2,3],[3,5],[3,4],[3,6],[6,7],[7,8],[8,9],[9,10],[1,11],[11,12],[12,13],[13,14],[14,15],[16,17],[17,18],[18,12],[12,19],[19,20],[20,21],[21,22],[20,23],[23,22],[22,24],[24,7],[7,25],[25,26],[26,27],[1,28],[28,20],[22,29],[29,30],[30,31],[26,36],[36,9],[9,35],[35,30],[30,34],[34,14],[14,33],[33,17],[17,32]],timestamp:"2025-12-07T10:18:31.518Z",version:"1.2"},{name:"(猛舔riser脚丫子)",nodes:[{x:.9150020799386814,y:.9271001615508885,text:"",textDisplay:"",color:"#d663c9"},{x:.44059508867775754,y:.07088045234248788,text:"",textDisplay:"",color:"#666666"},{x:.7052642522233256,y:.7138529886914378,text:"",textDisplay:"",color:"#d663c9"},{x:.3574421069842233,y:.9616179821627255,text:"",textDisplay:"",color:"#666666"},{x:.38066999504479876,y:.5086833602584814,text:"",textDisplay:"",color:"#d663c9"},{x:.7951518926727638,y:.07411147011308562,text:"",textDisplay:"",color:"#666666"},{x:.6902829788150858,y:.40690630048465265,text:"",textDisplay:"",color:"#d663c9"},{x:.9075114432345616,y:.1742730210016155,text:"",textDisplay:"",color:"#666666"},{x:.3581980849324392,y:.3471324717285945,text:"",textDisplay:"",color:"#27c1b9"},{x:.6003953383656476,y:.10319063004846526,text:"",textDisplay:"",color:"#27c1b9"},{x:.24122876462975665,y:.4532364287049313,text:"",textDisplay:"",color:"#666666"},{x:.0991913462593269,y:.6477771897375048,text:"",textDisplay:"",color:"#27c1b9"},{x:.9362255506003543,y:.7203150242326333,text:"",textDisplay:"",color:"#666666"},{x:.21371994449384618,y:.7814501198445433,text:"",textDisplay:"",color:"#666666"},{x:.6428422796889935,y:.9416397415185783,text:"",textDisplay:"",color:"#2b7ee0"},{x:.5438317864639313,y:.2554761992059788,text:"",textDisplay:"",color:"#2b7ee0"},{x:.37442779779136554,y:.7009289176090469,text:"",textDisplay:"",color:"#2b7ee0"},{x:.8413441523481695,y:.933562197092084,text:"",textDisplay:"",color:"#666666"},{x:.7576987091521645,y:.26635702746365103,text:"",textDisplay:"",color:"#2b7ee0"},{x:.5154706300535069,y:.9631998045433695,text:"",textDisplay:"",color:"#36ba55"},{x:.08978360303481123,y:.8689418416801292,text:"",textDisplay:"",color:"#36ba55"},{x:.17467748568150285,y:.07411147011308562,text:"",textDisplay:"",color:"#36ba55"},{x:.9487099451072207,y:.5296849757673667,text:"",textDisplay:"",color:"#ff0101"},{x:.24833541327201472,y:.600767366720517,text:"",textDisplay:"",color:"#666666"},{x:.05068586146620948,y:.3687957347918583,text:"",textDisplay:"",color:"#ff0101"},{x:.9312317927976077,y:.3810581583198708,text:"",textDisplay:"",color:"#666666"},{x:.3257386592145865,y:.13711631663974153,text:"",textDisplay:"",color:"#ff0101"},{x:.5579483970423018,y:.4844507269789984,text:"9",textDisplay:"9",color:"#666666"},{x:.11849771040060399,y:.22596930533117932,text:"",textDisplay:"",color:"#ff0101"},{x:.24515916753861622,y:.9325586495307606,text:"",textDisplay:"",color:"#ff9900"},{x:.745941077466024,y:.5024805265776803,text:"",textDisplay:"",color:"#ff9900"},{x:.5579483970423018,y:.723546042003231,text:"",textDisplay:"",color:"#ff9900"},{x:.08728672413343794,y:.49091276252019383,text:"",textDisplay:"",color:"#ff9900"},{x:.05357885896489861,y:.11773021001615509,text:"",textDisplay:"",color:"#ff9900"},{x:.39337264760681767,y:.845380651634866,text:"",textDisplay:"",color:"#ff9900"}],edges:[[0,1],[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[12,11],[11,10],[10,9],[9,7],[7,8],[12,14],[14,13],[3,15],[15,12],[3,16],[16,17],[18,17],[19,1],[1,20],[20,17],[17,21],[13,22],[28,27],[27,26],[26,24],[27,29],[29,25],[22,23],[23,30],[30,10],[5,31],[31,10],[17,32],[32,5],[33,17],[23,34],[34,27],[26,25],[23,24]],timestamp:"2025-12-07T10:36:28.867Z",version:"1.2"},{name:"震撼美味！！！！！",nodes:[{x:.5726877798892229,y:.4575602698298456,text:"",textDisplay:"",color:"#666666"},{x:.562712170773381,y:.4675923874167386,text:"",textDisplay:"",color:"#666666"},{x:.5679936275547116,y:.45773373975344994,text:"",textDisplay:"",color:"#666666"},{x:.5654390337464217,y:.46021809369951533,text:"",textDisplay:"",color:"#666666"},{x:.5642308072008682,y:.46303202679541267,text:"",textDisplay:"",color:"#666666"},{x:.5691843520984816,y:.4618336025848142,text:"",textDisplay:"",color:"#666666"},{x:.567935912647795,y:.4731421647819063,text:"",textDisplay:"",color:"#008bd8"},{x:.5754265493519148,y:.45537156704361875,text:"",textDisplay:"",color:"#008bd8"},{x:.5682570072892135,y:.4675923874167386,text:"",textDisplay:"",color:"#f456a6"},{x:.5654845890312973,y:.4675923874167386,text:"",textDisplay:"",color:"#666666"},{x:.5654845890312973,y:.4675923874167386,text:"",textDisplay:"",color:"#f456a6"},{x:.5578881630046069,y:.4551183998165731,text:"",textDisplay:"",color:"#f456a6"},{x:.5700147204647324,y:.4629644196272036,text:"",textDisplay:"",color:"#666666"},{x:.5467124419861221,y:.4618336025848142,text:"",textDisplay:"",color:"#f456a6"},{x:.5705735367171342,y:.46303202679541267,text:"",textDisplay:"",color:"#666666"},{x:.5673591682528809,y:.47284644367670225,text:"",textDisplay:"",color:"#f456a6"},{x:.5642308072008682,y:.4685037837609798,text:"",textDisplay:"",color:"#666666"},{x:.565456349398001,y:.45561040923516577,text:"",textDisplay:"",color:"#f456a6"},{x:.5557738345125135,y:.4685037837609798,text:"",textDisplay:"",color:"#a2c60a"},{x:.5616507116882414,y:.46545957177318664,text:"",textDisplay:"",color:"#a2c60a"},{x:.5760779991947953,y:.4629644196272036,text:"",textDisplay:"",color:"#a2c60a"},{x:.5740569062847743,y:.4603490796903268,text:"",textDisplay:"",color:"#666666"},{x:.5659725346446907,y:.4603490796903268,text:"",textDisplay:"",color:"#a2c60a"},{x:.5700147204647324,y:.45773373975344994,text:"",textDisplay:"",color:"#666666"},{x:.5691843520984816,y:.4682956381260097,text:"",textDisplay:"",color:"#a2c60a"},{x:.5616507116882414,y:.48023331558021787,text:"",textDisplay:"",color:"#666666"},{x:.5597478928333616,y:.48023331558021787,text:"",textDisplay:"",color:"#a2c60a"},{x:.562712170773381,y:.4675923874167386,text:"",textDisplay:"",color:"#666666"},{x:.562712170773381,y:.45324209969724977,text:"",textDisplay:"",color:"#a2c60a"},{x:.5682570072892135,y:.46041724355699415,text:"",textDisplay:"",color:"#ea2f2f"},{x:.5710294255471297,y:.4675923874167386,text:"",textDisplay:"",color:"#666666"},{x:.5659725346446907,y:.45773373975344994,text:"",textDisplay:"",color:"#ea2f2f"},{x:.5619303488246488,y:.4603490796903268,text:"",textDisplay:"",color:"#ea2f2f"},{x:.5726877798892229,y:.4602961483126291,text:"",textDisplay:"",color:"#ea2f2f"},{x:.5654845890312973,y:.4675923874167386,text:"6",textDisplay:"6",color:"#666666"},{x:.5730676248175203,y:.4506858279661554,text:"",textDisplay:"",color:"#ea2f2f"},{x:.5642308072008682,y:.4685037837609798,text:"",textDisplay:"",color:"#666666"},{x:.565456349398001,y:.45561040923516577,text:"",textDisplay:"",color:"#ea2f2f"},{x:.5684592935450455,y:.46303202679541267,text:"",textDisplay:"",color:"#666666"},{x:.5660433674685202,y:.4535496297928702,text:"",textDisplay:"",color:"#ea2f2f"},{x:.5621165640287795,y:.4712396622437634,text:"",textDisplay:"",color:"#2730a0"},{x:.5663450503729569,y:.4575602698298456,text:"",textDisplay:"",color:"#2730a0"},{x:.5705735367171342,y:.47397554072654696,text:"",textDisplay:"",color:"#2730a0"},{x:.5629421548450484,y:.46506462035541196,text:"",textDisplay:"",color:"#666666"},{x:.5616507116882414,y:.46545957177318664,text:"",textDisplay:"",color:"#2730a0"},{x:.5682570072892135,y:.46041724355699415,text:"",textDisplay:"",color:"#2730a0"},{x:.5726877798892229,y:.46303202679541267,text:"",textDisplay:"",color:"#2730a0"},{x:.5599397525154648,y:.46041724355699415,text:"",textDisplay:"",color:"#666666"},{x:.5599397525154648,y:.4675923874167386,text:"",textDisplay:"",color:"#2730a0"},{x:.5673591682528809,y:.46792186240769185,text:"",textDisplay:"",color:"#2730a0"},{x:.5654845890312973,y:.4783551032063552,text:"",textDisplay:"",color:"#666666"},{x:.5660433674685202,y:.4535496297928702,text:"",textDisplay:"",color:"#2730a0"},{x:.5660433674685202,y:.44083842476155755,text:"",textDisplay:"",color:"#875d32"},{x:.5673591682528809,y:.445761246697145,text:"",textDisplay:"",color:"#875d32"},{x:.5543949159996323,y:.46041724355699415,text:"",textDisplay:"",color:"#875d32"},{x:.5654845890312973,y:.4675923874167386,text:"",textDisplay:"",color:"#666666"},{x:.5654845890312973,y:.4783551032063552,text:"",textDisplay:"",color:"#875d32"},{x:.5793466803208783,y:.46041724355699415,text:"",textDisplay:"",color:"#875d32"},{x:.5682570072892135,y:.46041724355699415,text:"",textDisplay:"",color:"#875d32"},{x:.5682570072892135,y:.45324209969724977,text:"",textDisplay:"",color:"#875d32"},{x:.5616507116882414,y:.4506858279661554,text:"",textDisplay:"",color:"#ffa329"},{x:.5571673342575485,y:.46041724355699415,text:"",textDisplay:"",color:"#ffa329"},{x:.5679936275547116,y:.4525030598796962,text:"",textDisplay:"",color:"#ffa329"},{x:.562712170773381,y:.46041724355699415,text:"",textDisplay:"",color:"#ffa329"},{x:.5730676248175203,y:.46053499050417623,text:"",textDisplay:"",color:"#ffa329"},{x:.5659725346446907,y:.45773373975344994,text:"",textDisplay:"",color:"#ffa329"}],edges:[[0,1],[1,2],[2,3],[3,4],[4,5],[5,6],[7,0],[8,9],[9,10],[10,0],[0,11],[11,12],[12,13],[13,14],[14,15],[15,16],[16,17],[18,9],[9,19],[1,20],[20,21],[21,22],[22,23],[23,24],[24,25],[25,26],[26,27],[27,28],[19,1],[29,30],[30,12],[12,31],[31,21],[21,32],[32,2],[2,33],[33,34],[39,38],[38,37],[37,36],[36,35],[35,34],[40,30],[30,41],[41,14],[14,42],[42,43],[43,44],[44,25],[25,45],[45,4],[4,46],[46,47],[47,48],[48,38],[49,38],[50,49],[51,50],[52,50],[50,53],[53,34],[34,54],[54,55],[55,56],[56,47],[47,57],[57,5],[5,58],[58,27],[27,59],[60,16],[16,61],[43,61],[23,62],[62,3],[3,63],[63,55],[55,64],[64,36],[23,65],[65,43]],timestamp:"2025-12-07T12:06:33.184Z",version:"1.3"}],x=[{solved:!0,positions:[{x:250,y:750},{x:500,y:1e3},{x:750,y:500},{x:0,y:750},{x:500,y:750},{x:1e3,y:750},{x:750,y:750}],view:{x:30,y:-100,scale:.25}},{solved:!0,positions:[{x:250,y:750},{x:0,y:750},{x:-250,y:1e3},{x:-500,y:1e3},{x:-500,y:750},{x:-500,y:500},{x:-250,y:750},{x:-500,y:1250},{x:-1e3,y:750},{x:-1e3,y:250},{x:-500,y:250},{x:-250,y:0},{x:0,y:250},{x:0,y:-250},{x:-1e3,y:-250},{x:-750,y:500},{x:-750,y:0}],view:{x:230,y:75,scale:.2}},{solved:!0,positions:[{x:-1e3,y:-500},{x:-750,y:500},{x:-750,y:750},{x:-750,y:1e3},{x:-1e3,y:1e3},{x:-750,y:1250},{x:-500,y:1e3},{x:-500,y:500},{x:-250,y:500},{x:0,y:500},{x:250,y:500},{x:500,y:500},{x:750,y:500},{x:1250,y:500},{x:-750,y:250},{x:0,y:250},{x:250,y:250},{x:-250,y:500},{x:250,y:750},{x:500,y:1e3},{x:1e3,y:1250},{x:-250,y:1e3},{x:-250,y:1250},{x:-250,y:750},{x:250,y:1e3},{x:750,y:750},{x:750,y:250},{x:750,y:0},{x:1250,y:-250},{x:250,y:0},{x:1e3,y:0}],view:{x:180,y:100,scale:.15}},{solved:!0,positions:[{x:875,y:-375},{x:875,y:0},{x:1e3,y:-375},{x:1e3,y:0},{x:1e3,y:-250},{x:1125,y:-625},{x:1250,y:-625},{x:1250,y:-750},{x:1250,y:-500},{x:1250,y:-375},{x:1125,y:-375},{x:1250,y:-250},{x:1250,y:-125},{x:1125,y:-125},{x:1e3,y:125},{x:1250,y:250},{x:1e3,y:375},{x:1375,y:375},{x:1250,y:0},{x:1375,y:-125},{x:1625,y:-125},{x:1375,y:-375},{x:1750,y:-125},{x:1750,y:0}],view:{x:-160,y:180,scale:.2}},{solved:!0,positions:[{x:-1250,y:500},{x:-500,y:500},{x:-500,y:750},{x:-500,y:1250},{x:-750,y:1250},{x:-500,y:1500},{x:0,y:1250},{x:250,y:1250},{x:500,y:1250},{x:750,y:1250},{x:1e3,y:1250},{x:-250,y:250},{x:0,y:250},{x:250,y:250},{x:750,y:250},{x:1e3,y:250},{x:0,y:-500},{x:0,y:-250},{x:0,y:0},{x:0,y:250},{x:0,y:500},{x:0,y:750},{x:250,y:750},{x:250,y:500},{x:250,y:1e3},{x:250,y:1250},{x:750,y:1750},{x:1e3,y:1750},{x:-250,y:500},{x:500,y:750},{x:750,y:750},{x:1250,y:500},{x:-250,y:-250},{x:250,y:-250},{x:750,y:250},{x:750,y:1e3},{x:750,y:1500}],view:{x:220,y:90,scale:.15}},{solved:!0,positions:[{x:-1e3,y:500},{x:-500,y:500},{x:-250,y:500},{x:0,y:500},{x:500,y:500},{x:750,y:250},{x:1e3,y:250},{x:1250,y:250},{x:1500,y:0},{x:1e3,y:750},{x:750,y:750},{x:500,y:750},{x:250,y:750},{x:500,y:1250},{x:250,y:1e3},{x:0,y:750},{x:0,y:250},{x:0,y:0},{x:250,y:-500},{x:-500,y:1500},{x:-250,y:250},{x:500,y:-250},{x:750,y:1250},{x:1e3,y:1250},{x:1250,y:1250},{x:1750,y:1500},{x:1500,y:1250},{x:1250,y:1500},{x:1500,y:1750},{x:1500,y:1500},{x:1e3,y:1e3},{x:750,y:500},{x:500,y:250},{x:-500,y:-250},{x:1e3,y:1500}],view:{x:160,y:90,scale:.15}},{solved:!0,positions:[{x:-500,y:875},{x:-250,y:875},{x:0,y:875},{x:250,y:875},{x:625,y:875},{x:750,y:875},{x:1125,y:625},{x:-1250,y:875},{x:-500,y:500},{x:-500,y:625},{x:-500,y:750},{x:-500,y:1e3},{x:-375,y:1125},{x:-250,y:1250},{x:-125,y:1375},{x:125,y:1625},{x:250,y:1625},{x:375,y:1625},{x:-625,y:625},{x:-375,y:625},{x:-250,y:1e3},{x:-125,y:1e3},{x:0,y:1125},{x:250,y:1125},{x:375,y:1125},{x:500,y:1250},{x:625,y:1375},{x:750,y:1375},{x:875,y:1500},{x:-625,y:1625},{x:-625,y:1375},{x:-250,y:1125},{x:0,y:1e3},{x:0,y:375},{x:0,y:250},{x:250,y:125},{x:375,y:125},{x:500,y:125},{x:625,y:125},{x:875,y:0},{x:-1e3,y:1375},{x:-375,y:1375},{x:125,y:1375},{x:250,y:1375},{x:375,y:1375},{x:625,y:1125},{x:625,y:750},{x:625,y:625},{x:625,y:375},{x:375,y:0},{x:125,y:-125},{x:125,y:-250},{x:250,y:-125},{x:0,y:0},{x:250,y:375},{x:375,y:500},{x:500,y:625},{x:750,y:750},{x:750,y:1250},{x:750,y:1625},{x:250,y:1750},{x:250,y:1500},{x:250,y:1e3},{x:250,y:625},{x:375,y:375},{x:250,y:1250}],view:{x:220,y:60,scale:.15}}],l="knot_game_progress_v4",y="#FFFFFF",o="#FF5252";return{setup(){const a=t.ref(null),s=t.ref(null),i=t.ref(null),c=t.ref([]),r=t.ref([]),p=t.ref(.5),n=t.ref(0),v=t.ref(0),u=t.ref(!1),D=t.ref(null),f=t.ref(!1),d=t.ref({x:0,y:0}),m=t.ref(0),w=t.ref({unlockedLevel:0,levelStates:Array(7).fill(null).map(()=>({solved:!1,positions:null}))}),h=t.computed(()=>{var t;if(null==(t=w.value.levelStates[m.value])?void 0:t.solved)return"✨ 关卡完成！";const{count:e}=E();return`剩余交叉: ${e}`}),b=t.computed(()=>w.value.levelStates.every(t=>t.solved));function g(){c.value.length>0&&(w.value.levelStates[m.value].positions=c.value.map(t=>({x:t.x,y:t.y})),w.value.levelStates[m.value].view={x:n.value,y:v.value,scale:p.value}),localStorage.setItem(l,JSON.stringify(w.value))}function L(t,e,x,l){const y=(e.x-t.x)*(l.y-x.y)-(l.x-x.x)*(e.y-t.y);if(0===y)return!1;const o=((l.y-x.y)*(l.x-t.x)+(x.x-l.x)*(l.y-t.y))/y,a=((t.y-e.y)*(l.x-t.x)+(e.x-t.x)*(l.y-t.y))/y;return 0<o&&o<1&&0<a&&a<1}function E(){let t=0;const e=new Set;for(let x=0;x<r.value.length;x++)for(let l=x+1;l<r.value.length;l++){const y=r.value[x],o=r.value[l];y[0]!==o[0]&&y[0]!==o[1]&&y[1]!==o[0]&&y[1]!==o[1]&&(L(c.value[y[0]],c.value[y[1]],c.value[o[0]],c.value[o[1]])&&(t++,e.add(x),e.add(l)))}return{count:t,badEdges:e}}async function S(t){var x,l,y;if(t>w.value.unlockedLevel)return;m.value=t,_(),c.value=[],r.value=[];const o=e[t],a=w.value.levelStates[t],s=a.positions&&a.positions.length===o.nodes.length;o.nodes.forEach((t,e)=>{let x,l;s?(x=a.positions[e].x,l=a.positions[e].y):(x=1080*t.x,l=720*t.y),c.value.push({id:e,x:x,y:l,radius:12,color:t.color||"#2196f3",text:t.text?t.text.substring(0,1):""})}),s&&(n.value=(null==(x=a.view)?void 0:x.x)??n.value,v.value=(null==(l=a.view)?void 0:l.y)??v.value,p.value=(null==(y=a.view)?void 0:y.scale)??p.value),r.value=o.edges,M(),T(!0)}function k(t,e,x){const l=function(t,e){const x=a.value.getBoundingClientRect();return{x:(t-x.left-n.value)/p.value,y:(e-x.top-v.value)/p.value}}(t,e);if("start"===x){const x=c.value.find(t=>{const e=l.x-t.x,x=l.y-t.y;return Math.sqrt(e*e+x*x)<=t.radius+10});x?(u.value=!0,D.value=x):(f.value=!0,d.value={x:t-n.value,y:e-v.value},s.value.style.cursor="grabbing")}else"move"===x?u.value&&D.value?(D.value.x=l.x,D.value.y=l.y,M()):f.value&&(n.value=t-d.value.x,v.value=e-d.value.y,M()):"end"===x&&(u.value&&(T(),g()),u.value=!1,D.value=null,f.value=!1,s.value.style.cursor="grab")}function T(t=!1){const{count:e}=E(),x=w.value.levelStates[m.value];0!==e||x.solved||(x.solved=!0,m.value<6&&m.value===w.value.unlockedLevel&&w.value.unlockedLevel++,g()),M()}function M(){const t=window.devicePixelRatio||1,e=s.value.getBoundingClientRect();a.value.width===e.width*t&&a.value.height===e.height*t||(a.value.width=e.width*t,a.value.height=e.height*t,i.value.scale(t,t)),i.value.clearRect(0,0,a.value.width,a.value.height),i.value.save(),i.value.translate(n.value,v.value),i.value.scale(p.value,p.value);const{badEdges:x}=E();i.value.lineCap="round",r.value.forEach((t,e)=>{const l=c.value[t[0]],a=c.value[t[1]];i.value.beginPath(),i.value.moveTo(l.x,l.y),i.value.lineTo(a.x,a.y),x.has(e)?(i.value.strokeStyle=o,i.value.lineWidth=4):(i.value.strokeStyle=y,i.value.lineWidth=3),i.value.stroke()}),c.value.forEach(t=>{i.value.beginPath(),i.value.arc(t.x,t.y,t.radius,0,2*Math.PI),i.value.fillStyle=t.color,i.value.fill(),i.value.strokeStyle="white",i.value.lineWidth=2,i.value.stroke(),t.text&&(i.value.fillStyle="white",i.value.font='bold 12px "Cascadia Code", monospace',i.value.textAlign="center",i.value.textBaseline="middle",i.value.fillText(t.text,t.x,t.y))}),i.value.restore()}function _(){p.value=.5,n.value=0,v.value=0,M()}return t.onMounted(()=>{i.value=a.value.getContext("2d"),w.value=function(){const t=localStorage.getItem(l);return t?JSON.parse(t):{unlockedLevel:0,levelStates:Array(7).fill(null).map(()=>({solved:!1,positions:null}))}}();const e=function(){const t=s.value,e=t=>k(t.clientX,t.clientY,"start"),x=t=>k(t.clientX,t.clientY,"move"),l=t=>k(t.clientX,t.clientY,"end");t.addEventListener("mousedown",e),window.addEventListener("mousemove",x),window.addEventListener("mouseup",l);const y=t=>{t.preventDefault(),k(t.touches[0].clientX,t.touches[0].clientY,"start")},o=t=>{(u.value||f.value)&&t.preventDefault(),k(t.touches[0].clientX,t.touches[0].clientY,"move")},a=()=>k(0,0,"end");t.addEventListener("touchstart",y,{passive:!1}),window.addEventListener("touchmove",o,{passive:!1}),window.addEventListener("touchend",a);const i=t=>{t.preventDefault();const e=t.deltaY>0?.9:1.1;p.value=Math.max(.2,Math.min(3,p.value*e)),M()},c=()=>M();return t.addEventListener("wheel",i),window.addEventListener("resize",c),()=>{t.removeEventListener("mousedown",e),window.removeEventListener("mousemove",x),window.removeEventListener("mouseup",l),t.removeEventListener("touchstart",y),window.removeEventListener("touchmove",o),window.removeEventListener("touchend",a),t.removeEventListener("wheel",i),window.removeEventListener("resize",c)}}();S(Math.min(w.value.unlockedLevel,6)),t.onUnmounted(e)}),{canvasRef:a,canvasWrapperRef:s,nodes:c,edges:r,scale:p,translateX:n,translateY:v,isDraggingNode:u,draggedNode:D,isPanning:f,panStart:d,currentLevelIndex:m,progress:w,statusText:h,isAllLevelsSolved:b,loadLevel:S,resetLevelPositions:function(){confirm("确定重置本关布局吗？")&&(w.value.levelStates[m.value].positions=null,localStorage.setItem(l,JSON.stringify(w.value)),S(m.value))},zoomIn:function(){p.value=Math.min(1.2*p.value,3),M()},zoomOut:function(){p.value=Math.max(p.value/1.2,.5),M()},resetView:_,snapLevelPositions:function(){c.value.map(t=>(t.x=125*Math.round(t.x/125),t.y=125*Math.round(t.y/125),t)),M(),g()},pasteLevelPositions:async function(){var t,l,y;const o=m.value;_(),c.value=[],r.value=[];const a=e[o],s=x[o];a.nodes.forEach((t,e)=>{let x,l;x=s.positions[e].x,l=s.positions[e].y,c.value.push({id:e,x:x,y:l,radius:12,color:t.color||"#2196f3",text:t.text?t.text.substring(0,1):""})}),n.value=(null==(t=s.view)?void 0:t.x)??n.value,v.value=(null==(l=s.view)?void 0:l.y)??v.value,p.value=(null==(y=s.view)?void 0:y.scale)??p.value,r.value=a.edges,M(),T(!0),g()},TOTAL_LEVELS:7,unlockAll:()=>{w.value.unlockedLevel=6}}}}}(Vue);


// 确保导出名称正确
export default __vue_puzzle_component__;
</script>
