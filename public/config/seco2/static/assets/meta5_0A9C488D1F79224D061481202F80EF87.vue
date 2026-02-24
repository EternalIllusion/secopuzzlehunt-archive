<!-- seco2-meta5 Puzzle -->
<template>
  <div class="mc-container">
    <div class="mc-sidebar">
      <div 
        class="mc-nav-item" 
        :class="{ active: currentPage === 'tutorial' }"
        @click="changePage('tutorial')"
      >
        游戏教程
      </div>
      <div 
        class="mc-nav-item" 
        v-for="n in 8" 
        :key="n"
        :class="{ active: currentPage === n.toString() }"
        @click="changePage(n.toString())"
      >
        地点 {{ n }}
      </div>
    </div>
    
    <div class="mc-content">
      <!-- 游戏教程页面 -->
      <div 
        class="mc-page" 
        :class="{ active: currentPage === 'tutorial' }"
        data-page="tutorial"
      >
        <h2 class="mc-page-title">Minecraft Puzzle Hunt 游戏教程</h2>
        
        <div class="mc-text-content">
          
          <div class="mc-section">
            <h3>游戏前准备</h3>

            <h4>【存档模式】</h4>
            <p><strong><a href="https://www.123865.com/s/T3OlVv-dCSRA?pwd=seco#">『来自123云盘VIP会员EterIll的分享』SECO2【暗格MC】</a></strong>
提取码：<strong>seco</strong><br />【以下所有文件以及地图均在链接中】</p>
            
            <h4>启动器设置</h4>
            <ul>
              <li>运行提供的启动器文件，解压后获得文件夹</li>
              <li><a>SECO PUZZLE HUNT 懒人包（包含 Mod，无需额外下载）</a></li>
              <li><a>SECO PUZZLE HUNT 下载包（不包含 Mod，需要等待启动器自动下载）</a></li>
              <li>点击文件夹中的 <code>Plain Craft Launcher.exe</code> 运行游戏</li>
              <li>如果无法运行，请从 <a href="https://pcl.ruanmao.net/" target="_blank">PCL2官网</a> 下载启动器并替换原本的启动器</li>
            </ul>
            
            <h4>登录游戏</h4>
            <ul>
              <li>打开启动器后，使用正版账号登录或选择离线模式</li>
              <li>离线模式需创建新角色名，<strong>严禁使用汉字和特殊符号</strong></li>
              <li>点击"启动游戏"按钮，等待游戏加载，加载完成后，点击多人游戏后加入服务器</li>
              <li>若无法启动，请安装 <a>Java 21</a></li>
            </ul>
          </div>
          
          <div class="mc-section">
            <h3>游戏基本操作</h3>
            
            <h4>键位设置</h4>
            <p>首次进入游戏前，请熟悉基本操作键位：</p>
            <ul>
              <li>打开按键设置：<code>选项 → 按键控制 → 按键绑定</code></li>
              <li>移动：<code>W, A, S, D</code></li>
              <li>鼠标控制视角移动，可在设置中调整灵敏度</li>
              <li>跳跃：<code>空格</code></li>
              <li>疾跑：<code>Ctrl</code></li>
              <li>下蹲：<code>Shift</code></li>
              <li>打开物品栏：<code>E</code></li>
              <li>打开聊天栏：<code>T</code></li>
            </ul>
            
            <h4>视频设置</h4>
            <p>根据你的电脑配置调整视频设置：</p>
            <ul>
              <li>打开视频设置：<code>选项 → 视频设置</code></li>
              <li>关闭视角摇晃：<code>视频设置 → 视角摇晃 → 关（如果头晕不适关闭，也可以不使用全屏游玩）</code></li>
              <li>降低渲染距离和模拟距离以提升性能</li>
              <li>调整完需要点击应用</li>
            </ul>
            
            <h4>Mod 特殊键位</h4>
            <p>注意这些由 Mod 添加的特殊功能键,下载包可能需要手动设置：</p>
            <ul>
              <li>打开任务面板：<code>R(由于键位冲突，可以自行修改)</code></li>
              <li>打开语音系统：<code>V</code></li>
              <li>打开小地图路径点：<code>U</code></li>
              <li>放大小地图：<code>Z</code></li>
              <li>设置小地图：<code>Y</code></li>
              <li>新建路径点：<code>B</code></li>
            </ul>
          </div>
          
          <div class="mc-section">
            <h3>服务器内比赛细则</h3>
            
            <h4>初始设置</h4>
            <ul>
              <li>进入游戏后，按 <code>T</code> 呼出聊天栏</li>
              <li>按照指示设置账号密码，请务必牢记！</li>
              <li>游戏模式为冒险模式，无法破坏方块</li>
            </ul>
            
            <h4>队伍系统</h4>
            <p>创建或加入队伍以与队友协作：</p>
            <ul>
              <li>创建队伍：<code>/ftbteams party create &lt;队伍名&gt;</code> （队伍名使用字母拼音或英文，最长15个字符）</li>
              <li>邀请玩家：<code>/ftbteams party invite &lt;玩家名&gt;</code></li>
              <li>队伍成员间发送消息：<code>/ftbteams msg &lt;消息内容&gt;</code></li>
              <li>踢出玩家：<code>/ftbteams party kick &lt;玩家名&gt;</code></li>
              <li>退出队伍：<code>/ftbteams party leave</code></li>
            </ul>
            <p>收到邀请后，点击聊天栏中的 <code>Accept</code> 或 <code>Deny</code> 进行操作</p>
            
            <h4>任务系统</h4>
            <p>完成任务以推进比赛进程：</p>
            <ul>
              <li>按 <code>E</code> 打开物品栏，点击任务书图标或直接按 <code>R</code> 打开任务面板</li>
              <li>共有8个指南针图标代表8个定位任务，根据提供的图片找到对应场景</li>
              <li>到达正确位置后，任务会自动完成</li>
              <li>打开任务书，点击带有 <code>!</code> 角标的任务领取奖励</li>
              <li>领取奖励后会被传送到小题题面处，若位置没变，题目就在附近</li>
            </ul>
            <p><strong>重要提示：</strong>当一个人到达目标地点后，队伍中每个人都会获得一次传送机会。使用后需再次有人到达该地点才能重新获得传送机会。建议完成一个地点的题目后再前往下一个地点。</p>
            
            <h4>辅助功能</h4>
            <ul>
              <li>返回出生点：<code>/spawn</code> （当你被卡在某处时使用）</li>
              <li>传送到队友：<code>/tpa &lt;玩家名&gt;</code> （需要对方在聊天栏点击同意）</li>
              <li>让队友传送到你：<code>/tpahere &lt;玩家名&gt;</code> （同上）</li>
              <li>语音系统：按 <code>V</code> 打开，可设置群组和密码</li>
              <li>小地图功能：<code>U</code> 打开路径点 / <code>Z</code> 放大 / <code>Y</code> 设置 / <code>B</code> 新建路径点</li>
            </ul>
          </div>
          
          <div class="mc-section">
            <h3>比赛规则</h3>
            
            <h4>作弊行为</h4>
            <ul>
              <li>禁止在聊天栏发送任何有关比赛内容的信息</li>
              <li>禁止随意加入他人队伍或拉非同队玩家进入队伍</li>
              <li>语音系统禁止与非同队玩家交流比赛内容</li>
              <li>禁止使用本教程未提及的任何<strong>指令</strong>和<strong>模组</strong>和<strong>材质包</strong>作弊</li>
              <li><strong>违反规则的队伍将被取消比赛资格</strong></li>
            </ul>
            
            <h4>服务器礼仪</h4>
            <ul>
              <li>完成题目后请及时退出服务器，避免占用服务器资源</li>
              <li>遇到问题请通过网站站内信联系管理员</li>
              <li>保持友好的游戏环境，尊重其他参赛队伍</li>
            </ul>
          </div>
          
          <p style="text-align: center; margin-top: 30px; font-size: 18px;">
            <strong>祝各位选手比赛顺利，取得好成绩！</strong><br>
            如有任何问题，请通过站内信联系我们
          </p>
          <p style="text-align: center;"><span class="btn" style="display: inline-block; padding: 10px 30px; background: #4caf50; color: white; text-decoration: none; border: 2px solid #000; box-shadow: 3px 3px 0 #000;">站内信关闭了喵</span></p>
        </div>
      </div>
      
      <!-- 页面 1 -->
      <div 
        class="mc-page" 
        :class="{ active: currentPage === '1' }"
        data-page="1"
      >
        <h2 class="mc-page-title">移动迷宫</h2>
        
        <div class="mc-image-container">
          <img 
            src="/config/seco2/static/assets/meta51_5c01bdeda2571507e647efc6e65deba7.png" 
            alt="地点1图片" 
            style="display:none;" 
            @load="onImageLoad($event)"
          >
          <div class="mc-image-placeholder">图片位置</div>
        </div>
        
        <div class="mc-text-content">
          <p>墙壁在这里不断延伸，每一条通道都通向未知。有些冒险者会在纸上做好标记，但大多数人最终还是走了回头路。</p>
          <p>这里的结构像是有人刻意设计的——复杂、精密，充满了分叉与转折。保持清醒的头脑，否则很容易迷失在相似的景色中。</p>
        </div>
      </div>
      
      <!-- 页面 2 -->
      <div 
        class="mc-page" 
        :class="{ active: currentPage === '2' }"
        data-page="2"
      >
        <h2 class="mc-page-title">简单跑酷</h2>
        
        <div class="mc-image-container">
          <img 
            src="/config/seco2/static/assets/meta52_c2c312756ee0d08a36816b51ff21ac57.png" 
            alt="地点2图片" 
            style="display:none;" 
            @load="onImageLoad($event)"
          >
          <div class="mc-image-placeholder">图片位置</div>
        </div>
        
        <div class="mc-text-content">
          <p>这条路径如此流畅，每一步都恰到好处。跟随着设计者的意图前进，几乎不需要停顿。</p>
          <p>不过，最优解往往不在最显眼的地方。有时候，那些被遗忘的角落，或许才是真正的捷径。</p>
        </div>
      </div>
      
      <!-- 页面 3 -->
      <div 
        class="mc-page" 
        :class="{ active: currentPage === '3' }"
        data-page="3"
      >
        <h2 class="mc-page-title">破损数码管</h2>
        
        <div class="mc-image-container">
          <img 
            src="/config/seco2/static/assets/meta53_b92b1c90241961c6b7af2e52de73ad25.png" 
            alt="地点3图片" 
            style="display:none;" 
            @load="onImageLoad($event)"
          >
          <div class="mc-image-placeholder">图片位置</div>
        </div>
        
        <div class="mc-text-content">
          <p>古老的显示装置因年久失修而变得残缺不全。要理解它曾经想要表达的信息，需要先恢复它原本的样子。</p>
          <p>观察那些破碎的部分，将它们拼合在一起。颜色相同的事物总会自然地聚集在一起，这是一种本能的秩序。</p>
        </div>
      </div>
      
      <!-- 页面 4 -->
      <div 
        class="mc-page" 
        :class="{ active: currentPage === '4' }"
        data-page="4"
      >
        <h2 class="mc-page-title">奇怪音频</h2>
        
        <div class="mc-image-container">
          <img 
            src="/config/seco2/static/assets/meta54_689690683249ea5037fc962246e447e9.png" 
            alt="地点4图片" 
            style="display:none;" 
            @load="onImageLoad($event)"
          >
          <div class="mc-image-placeholder">图片位置</div>
        </div>
        
        <div class="mc-text-content">
          <p>奇特的旋律回荡在空气中，仿佛在诉说着某个故事。单纯聆听或许只能听到表面的信息。</p>
          <p>声音的本质不仅仅是听觉的产物。在这个世界里，每一个声音都有其物理表现形式。</p>
        </div>
      </div>
      
      <!-- 页面 5 -->
      <div 
        class="mc-page" 
        :class="{ active: currentPage === '5' }"
        data-page="5"
      >
        <h2 class="mc-page-title">树林秘密</h2>
        
        <div class="mc-image-container">
          <img 
            src="/config/seco2/static/assets/meta55_b756b13bcb81ef484b5ff593bbdefcfa.png" 
            alt="地点5图片" 
            style="display:none;" 
            @load="onImageLoad($event)"
          >
          <div class="mc-image-placeholder">图片位置</div>
        </div>
        
        <div class="mc-text-content">
          <p>繁茂的植被覆盖着这片土地，生命的色彩在这里绽放。大自然总是追求平衡与和谐。</p>
          <p>但在规律之中，偶尔会出现例外。那些与周围环境不太协调的事物，往往承载着特殊的意义。用心感受这片森林的韵律，你会发现异样。</p>
        </div>
      </div>
      
      <!-- 页面 6 -->
      <div 
        class="mc-page" 
        :class="{ active: currentPage === '6' }"
        data-page="6"
      >
        <h2 class="mc-page-title">见证者洞穴</h2>
        
        <div class="mc-image-container">
          <img 
            src="/config/seco2/static/assets/meta56_7934ec41fd5259326f9e824041a68773.png" 
            alt="地点6图片" 
            style="display:none;" 
            @load="onImageLoad($event)"
          >
          <div class="mc-image-placeholder">图片位置</div>
        </div>
        
        <div class="mc-text-content">
          <p>洞穴墙壁上刻画着规则的线条和图案，这些符号似乎在引导着什么。某位独立游戏设计师曾用类似的方式，创造了一个充满谜题的孤岛。</p>
          <p>观察、推理、验证——这是解开谜题的永恒法则。那些线条不是随意勾画的装饰，而是通往真相的路径。</p>
        </div>
      </div>
      
      <!-- 页面 7 -->
      <div 
        class="mc-page" 
        :class="{ active: currentPage === '7' }"
        data-page="7"
      >
        <h2 class="mc-page-title">黑白视错觉</h2>
        
        <div class="mc-image-container">
          <img 
            src="/config/seco2/static/assets/meta57_979400ce4ffdd926a0898763c22ae629.png" 
            alt="地点7图片" 
            style="display:none;" 
            @load="onImageLoad($event)"
          >
          <div class="mc-image-placeholder">图片位置</div>
        </div>
        
        <div class="mc-text-content">
          <p>光影在这里交织成复杂的图案，明与暗的对比创造出令人困惑的视觉效果。大脑会自动填补缺失的信息，但这种本能有时会误导我们。</p>
          <p>当所有直观的尝试都失败时，或许该质疑一下基本假设。有些问题的答案，需要你放弃惯性思维，去探索那些"不应该存在"的可能性。</p>
        </div>
      </div>
      
      <!-- 页面 8 -->
      <div 
        class="mc-page" 
        :class="{ active: currentPage === '8' }"
        data-page="8"
      >
        <h2 class="mc-page-title">立体峡谷</h2>
        
        <div class="mc-image-container">
          <img 
            src="/config/seco2/static/assets/meta58_c5d126d054fb58ace5397bfcc576ee39.png" 
            alt="地点8图片" 
            style="display:none;" 
            @load="onImageLoad($event)"
          >
          <div class="mc-image-placeholder">图片位置</div>
        </div>
        
        <div class="mc-text-content">
          <p>谜题的轮廓在不同高度呈现出截然不同的形态。从单一视角很难理解整体的构造——每一层都有其独特的意义。</p>
          <p>建筑师在设计三维结构时，常常会在纸面上绘制多个视图。同样的道理，要真正理解这个空间，或许需要从多个维度去审视它。</p>
        </div>
      </div>
    </div>
  </div>

</template>

<style>

    @font-face {
        font-family: 'Minecraft';
        src: url("/config/seco2/static/pix_6ABD64EE724768C863D2969484B89E65.ttf") format('truetype');
    }
    
    body {
        background: #2d2d2d;
    }
    
    .mc-container {
        display: flex;
        max-width: 1400px;
        margin: 20px auto;
        gap: 20px;
        min-height: 600px;
        font-family: 'Minecraft', monospace;
    }
    
    .mc-sidebar {
        width: 220px;
        background: linear-gradient(to bottom, #3c3c3c, #2d2d2d);
        border: 4px solid #000;
        box-shadow: inset 0 0 0 2px #5a5a5a;
        padding: 10px 0;
        position: sticky;
        top: 20px;
        height: fit-content;
    }
    
    .mc-nav-item {
        padding: 12px 15px;
        cursor: pointer;
        background: linear-gradient(to bottom, #555, #333);
        border: 2px solid #000;
        border-left: none;
        border-right: none;
        margin: 2px 0;
        color: #fff;
        text-shadow: 2px 2px 0 #000;
        font-size: 14px;
        transition: all 0.1s;
        position: relative;
    }
    
    .mc-nav-item:hover {
        background: linear-gradient(to bottom, #6a6a6a, #4a4a4a);
        transform: scale(1.02);
    }
    
    .mc-nav-item.active {
        background: linear-gradient(to bottom, #4caf50, #2e7d32);
        border-color: #1b5e20;
        box-shadow: inset 0 0 10px rgba(0,0,0,0.5);
    }
    
    .mc-nav-item.active::before {
        content: '▶';
        position: absolute;
        left: 5px;
        animation: blink 1s infinite;
    }
    
    @keyframes blink {
        0%, 50% { opacity: 1; }
        51%, 100% { opacity: 0; }
    }
    
    .mc-content {
        flex: 1;
        background: linear-gradient(to bottom, #c6c6c6, #8b8b8b);
        border: 4px solid #000;
        box-shadow: inset 0 0 0 2px #fff, 0 8px 0 #000;
        padding: 30px;
        color: #3e3e3e;
    }
    
    .mc-page {
        display: none;
    }
    
    .mc-page.active {
        display: block;
        animation: fadeIn 0.3s;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    
    .mc-page-title {
        font-size: 32px;
        font-weight: normal;
        color: #3e3e3e;
        text-shadow: 2px 2px 0 #fff;
        margin-bottom: 20px;
        padding-bottom: 10px;
        border-bottom: 4px solid #5a5a5a;
    }
    
    .mc-image-container {
        margin: 20px 0;
        text-align: center;
        background: #3e3e3e;
        border: 4px solid #000;
        padding: 10px;
        box-shadow: inset 0 0 20px rgba(0,0,0,0.5);
    }
    
    .mc-image-container img {
        max-width: 100%;
        height: auto;
        border: 2px solid #000;
        image-rendering: pixelated;
    }
    
    .mc-image-placeholder {
        background: repeating-linear-gradient(
            45deg,
            #4a4a4a,
            #4a4a4a 10px,
            #3a3a3a 10px,
            #3a3a3a 20px
        );
        border: 2px dashed #777;
        padding: 40px 20px;
        color: #aaa;
        font-size: 18px;
        text-shadow: 1px 1px 0 #000;
    }
    
    .mc-text-content {
        font-size: 16px;
        line-height: 1.8;
        color: #fff;
        text-shadow: 2px 2px 0 #000;
    }
    
    .mc-text-content p {
        margin-bottom: 15px;
    }
    
    .mc-text-content h3, .mc-text-content h4 {
        color: #2e2e2e;
        text-shadow: 2px 2px 0 #fff;
        margin: 20px 0 10px;
    }
    
    .mc-text-content ul {
        list-style: none;
        padding-left: 0;
    }
    
    .mc-text-content li {
        padding: 5px 0 5px 25px;
        position: relative;
    }
    
    .mc-text-content li::before {
        content: '■';
        position: absolute;
        left: 5px;
        color: #5a5a5a;
    }
    
    .mc-text-content code {
        background: #3e3e3e;
        color: #fff;
        padding: 2px 6px;
        border: 2px solid #000;
        font-family: 'Minecraft', monospace;
        text-shadow: 1px 1px 0 #000;
    }
    
    .mc-text-content a {
        color: #1976d2;
        text-decoration: underline;
        text-shadow: 1px 1px 0 rgba(255,255,255,0.5);
    }
    
    .mc-text-content strong {
        color: #d32f2f;
        text-shadow: 1px 1px 0 rgba(255,255,255,0.8);
    }
    
    .mc-section {
        background: rgba(255,255,255,0.3);
        border: 2px solid #5a5a5a;
        padding: 15px;
        margin: 15px 0;
        box-shadow: inset 0 0 10px rgba(255,255,255,0.5);
    }
    
    @media (max-width: 768px) {
        .mc-container {
            flex-direction: column;
        }
        
        .mc-sidebar {
            width: 100%;
            position: static;
            display: flex;
            overflow-x: auto;
            padding: 5px 0;
        }
        
        .mc-nav-item {
            white-space: nowrap;
            min-width: 120px;
            margin: 0 2px;
        }
        
        .mc-content {
            padding: 15px;
        }
        
        .mc-page-title {
            font-size: 24px;
        }
    }

</style>

<!-- 请将以上部分复制到后台“题目HTML”中，以下部分复制到后台“题目脚本”中，不要包含<script>标签 -->

<script>
var __vue_puzzle_component__=function(){"use strict";return{name:"MinecraftTutorial",data:()=>({currentPage:"tutorial"}),methods:{changePage(e){this.currentPage=e},onImageLoad(e){e.target.style.display="block",e.target.nextElementSibling&&(e.target.nextElementSibling.style.display="none")}}}}();


// 确保导出名称正确
export default __vue_puzzle_component__;
</script>
