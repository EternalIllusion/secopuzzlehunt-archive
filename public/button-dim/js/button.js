document.onreadystatechange=function(){
    loadingGame()
}

let loadingGame = function(){
	calcPlayer()
    Building()
    intervalID()
}

function getByID(id,id2){
	document.getElementById(id).innerHTML = id2;
}

function addedCss(id,id2){
	document.getElementById(id).classList.add(id2)
}

function removeCss(id,id2){
	document.getElementById(id).classList.remove(id2)
}

function n(x){
    return new Decimal(x)
}

function calcPlayer(){
    loader(['data', 'offline'], n(0))
    loader(['data', 'devSpeed'], n(1))

    loader(['button', 'times'], n(0))
    for(let i = 1; i<=8; i++){
        loader(['button', 'buydim'+i], n(0))
        loader(['button', 'dim'+i], n(0))
    }
    for(let i = 1; i<=10; i++){
        loader(['button', 'buytick'+i], n(0))
        loader(['button', 'tick'+i], n(0))
    }
}

function pushButton(){
    player.button.times = player.button.times.add(1)

    getByID('click-count', formatWhole(player.button.times))
}

function costDim(id){
    const BASE_COSTS = [null, 10, 1e2, 1e4, 1e6, 1e9, 1e13, 1e18, 1e24];
    const BASE_COST_MULTIPLIERS = [null, 1e3, 1e4, 1e5, 1e6, 1e8, 1e10, 1e12, 1e15];
    return n(BASE_COSTS[id]).mul(n(BASE_COST_MULTIPLIERS[id]).pow(player.button['buydim'+id])).div(100)
}

function buyDim(id){
    let cost = costDim(id)

    if(player.button.times.gte(cost)){
        player.button['buydim'+id] = player.button['buydim'+id].add(1)
        player.button['dim'+id] = player.button['dim'+id].add(1)

        player.button.times = player.button.times.sub(cost)
    }
}

function costTick(id){
    const BASE_COSTS = [null, 1e4, 1e6, 1e8, 1e10, 1e12, 1e14, 1e16, 1e18, 1e20, 1e22];
    const BASE_COST_MULTIPLIERS = [null, 10, 10, 1e2, 1e2, 1e3, 1e3, 1e4, 1e4, 1e5, 1e5];
    return n(BASE_COSTS[id]).mul(n(BASE_COST_MULTIPLIERS[id]).pow(player.button['buytick'+id]))
}

function buyTick(id){
    let cost = costTick(id)

    if(player.button.times.gte(cost)){
        player.button['buytick'+id] = player.button['buytick'+id].add(1)
        player.button['tick'+id] = player.button['tick'+id].add(1)

        player.button.times = player.button.times.sub(cost)
    }
}

function getTick(){
    let eff = [null, n(1.01), n(1.02), n(1.03), n(1.04), n(1.05), n(1.06), n(1.07), n(1.08), n(1.09), n(1.1)]
    let total = n(1)
    for(let i = 1; i<=10; i++){
        total = total.mul(n(eff[i]).pow(player.button['tick'+i]))
    }
    return total
}

function Building(){
    let tickB = ''
    let eff = [null, n(1.01), n(1.02), n(1.03), n(1.04), n(1.05), n(1.06), n(1.07), n(1.08), n(1.09), n(1.1)]
    let level = [null, 'IV', 'LuV', 'ZPM', 'UV', 'UHV', 'UEV', 'UIV', 'UMV', 'UXV', 'MAX']
    let name = [null, '主机', '纳米主机', '量子主机', '晶体主机', '湿件主机', '生物主机', '光学主机', '异星主机', '寰宇主机', '超时空主机']
    for(let i = 1; i<=10; i++){
        tickB += `<div style="display: inline-flex">
                <dimensionsName>
                    <b><`+level[i]+`>`+level[i]+`</`+level[i]+`></b>`+name[i]+`<small><sub><b style="color: var(--accent-color);">(×`+format(eff[i])+`)</b></sub></small>
                </dimensionsName>
                <dimensionsAmount>
                    你有 <b id="tick`+i+`" style="color: var(--accent-color);">0</b> 个<b><`+level[i]+`>`+level[i]+`</`+level[i]+`></b>`+name[i]+`
                </dimensionsAmount>
                <dimensionsCost>
                    <button id="buyTick`+i+`" class="buyTick" onclick="buyTick(`+i+`)">
                        需求: <b id="costtick`+i+`">0</b> 按钮
                    </button>
                </dimensionsCost>
            </div><br><br>`
    }
    getByID('ticks', tickB)
}

function intervalID(){
    for(let i = 1; i<=8; i++){
        if(i==1){
            player.button.times = player.button.times.add(n(player.button['dim1']).mul(n(2).pow(player.button['buydim'+i])).mul(getTick()).mul(DIFF))
        }else{
            player.button['dim'+Number(i-1)] = player.button['dim'+Number(i-1)].add(n(player.button['dim'+i]).mul(n(2).pow(player.button['buydim'+i])).mul(getTick()).mul(DIFF))
        }

        if(player.button['buydim'+i].gte(1)){
            getByID('dimensions'+i, formatWhole(player.button['dim'+i])+' × '+formatWhole(n(2).pow(player.button['buydim'+i])))
        }else{
            getByID('dimensions'+i, formatWhole(player.button['dim'+i]))
        }
        getByID('costdimensions'+i, formatWhole(costDim(i)))

        if(player.button.times.gte(costDim(i))){
            removeCss('buyDim'+i, 'cantbuy')
        }else{
            addedCss('buyDim'+i, 'cantbuy')
        }
    }
    
    for(let i = 1; i<=10; i++){
        getByID('tick'+i, formatWhole(player.button['tick'+i]))
        getByID('costtick'+i, formatWhole(costTick(i)))

        if(player.button.times.gte(costTick(i))){
            removeCss('buyTick'+i, 'cantbuy')
        }else{
            addedCss('buyTick'+i, 'cantbuy')
        }
    }

    getByID('click-count', formatWhole(player.button.times))
    getByID('tick-count', format(getTick())+'×')

    getByID('displayButton', formatWhole(player.button.times))
    getByID('displayButtonGain', '(+'+formatWhole(n(player.button['dim1']).mul(n(2).pow(player.button['buydim'+i])).mul(getTick()))+'/s)')
    getByID('displayTick', format(getTick())+'×')

    save()
}

var T = new Date()
var TIMESTART = new Date()
var OFFLINETIME = new Date()
var DIFF = 0
setInterval(function(){
	T = new Date()
	var OFFLINETIMEGAIN = n((Number(OFFLINETIME.getTime())-player.data.offline)/1000)
	player.data.offline = n((Number(T.getTime())))
	DIFF = n(Math.min((Number(T.getTime())-TIMESTART)/1000,1e100))
	var OFFLINEBOOST = n(1).mul(player.data.devSpeed)
	DIFF=DIFF.mul(OFFLINEBOOST)
	TIMESTART=T.getTime()

	intervalID()
}, 50)