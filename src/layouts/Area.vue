<template>
    <div class="body">
    </div>

    <div class="area-banner">
        <img :src="banner" alt="区域立绘"></img>
    </div>
    <div class="navi-container">
        <div class="row header-line">
            <ul class="col link-button-wrapper">
                <li class="sp-li">
                    <div class="link sp-title">
                        <div class="link-title">
                            <h2>{{ data.title }}</h2>
                        </div>
                    </div>
                </li>
                <li v-for="link in data.problems" class="link-li" @click="navigate(link.path)">
                    <div class="link-title">
                        {{ link.title }}
                    </div>
                </li>
            </ul>
            <div class="site-info" @click="navigate('/')">Powered by EterIll's PH Archive with CCXCArchiveEvolved</div>
        </div>


        <div :class="{ 'loader': true, 'loading': loading }">
            <div class="loading-tip"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"
                    fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
                    class="">
                    <animateTransform xmlns="http://www.w3.org/2000/svg" attributeName="transform" attributeType="XML"
                        type="rotate" from="360" to="0" dur="1.0s" repeatCount="indefinite" />
                    <path d="M21 12a9 9 0 1 1-6.219-8.56" />
                </svg>
                加载中……请稍后……</div>
        </div>

    </div>
</template>

<script setup lang="ts">
import { onMounted, reactive, ref } from 'vue';
//import { useRoute, useRouter } from 'vue-router'

import { getAreaInfo } from '../api';
import { useTheme } from '../dataschem/theme';
import { Area } from '../dataschem/interfaces';

const route = useRoute();
const router = useRouter();

const data = reactive<Area>({ title: '', problems: [] });
const loading = ref(true);

const theme = useTheme();

const bgImg = ref('data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==');
const banner = ref('data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==');
const bgSnap = ref(0);

onBeforeMount(async () => {
    var hunt = route.params.hunt as string;
    var pgid = route.params.pgid as string;
    if (!hunt || !pgid) return;
    await theme.update(hunt)
    let huntTheme = theme.themes[hunt];
    let areaTheme = huntTheme?.areas[pgid];
    banner.value = areaTheme?.banner ?? huntTheme?.root?.banner ?? bgImg.value;
    bgImg.value = `url("${banner.value}")`;
    bgSnap.value = areaTheme.snapMargin ?? 40;
})

async function loadDetail() {
    console.log("site-render");

    const adata = await getAreaInfo(route.params.hunt as string ?? "", route.params.pgid as string ?? "");

    console.debug(adata);

    Object.assign(data, adata);
}

const navigate = (path: string) => {
    router.push(path);
}

//const route = useRoute();
//const router = useRouter();

onMounted(async () => {
    await loadDetail();
    loading.value = false;
});

</script>

<style lang="scss" scoped>


.area-banner {
    display: flex;
    position: fixed;
    right: 3rem;
    max-height: 800px;
    max-width: 400px;
    top: 50%;
    transform: translateY(-50%);
    background-color: #ffffff66;
    backdrop-filter: blur(10px);
    box-shadow: #fff 0 0 2rem;
    border: #fff 2px solid;
    border-radius: 2rem;
    overflow: hidden;
    width: 30vw;
    height: auto;
    transition: all ease 0.5s;

    img {
        height: 100%;
        width: 100%;
        object-fit: contain;
    }
}

.page-title {
    position: fixed;
    right: 2rem;
    bottom: 2rem;
    pointer-events: none;
    transition: all ease .4s;
}

.body {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    max-height: 100vh;
    overflow-y: scroll;
    overflow-x: hidden;
    filter: blur(15px);
    z-index: -1;
}

.body::before {
    content: "";
    background: v-bind(bgImg) no-repeat right top / cover;
    top: 0;
    left: 0;
    bottom: 0;
    right: 0;
    position: fixed;
    z-index: -3;
    transition: all ease .3s, margin-right ease-in-out .15s;
}


@media (max-width: 800px) {
    .body::before {
        margin-right: calc(-1vh * v-bind(bgSnap));
    }
}


.navi-container {
    background: linear-gradient(to right, #ffffffcc 0%, #ffffff66 85%, #ffffff33 95%, #ffffff00 100%);
    margin: 0;
    margin-right: 40%;
    padding: 1rem;
    min-height: calc(100vh - 2rem);
    top: 0;
}

.navi-container .loader::before {
    content: ' ';
    position: absolute;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    z-index: 800;
    transition: backdrop-filter 1s ease;
    pointer-events: none;
}

.navi-container .loader>.loading-tip {
    z-index: 900;
    position: relative;
    opacity: 0%;
    transition: all .8s ease;
}

.navi-container .loader {
    position: absolute;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: row;
    pointer-events: none;
}

.navi-container .loader.loading>.loading-tip {
    opacity: 100%;
}

.navi-container .loader.loading::before {
    backdrop-filter: blur(15px);
    pointer-events: all;
}

.navi-container .link-li {
    display: flex;
    padding-left: 1rem;
    padding-right: 0;
    cursor: pointer;
    background: linear-gradient(to right, #ffffffdd 0%, #ffffffbb 60%, #ffffff33 85%, #ffffff00 100%);
    border-radius: 12px;
    align-items: center;
    min-height: 5rem;
    transition: all ease .5s;

    .link-title {
        display: flex;
        padding: 0;
        font-size: 1.6rem;
        font-weight: bold;
        align-items: center;
        line-height: 1.8rem;
    }
}

.sp-li {
    .sp-title {
        display: flex;
        flex-direction: row;
        align-items: center;
        flex-wrap: wrap;

        .link-logo {
            max-height: 4rem;
            max-width: 4rem;
            object-fit: cover;
            height: auto;
            width: auto;
        }
    }
}


@media (max-width: 1000px) {
    .navi-container .page-title {
        opacity: 0;
    }
}

.site-info {
    cursor: pointer;
    margin: 1rem;
}
</style>