<template>
    <div class="slider-header">
        <h2>Также рекомендуем</h2>
        <a href="">Все товары<img src="/img/icons/arrow.svg" /></a>
    </div>
    <div class="slider">
        <div class="slider-container">
            <div class="slider-wrap">
                <div class="slider-slide" v-for="card in cards">
                    <AppCard :title="card.title_of_product" :desc="card.brief_info_about_product" :price="card.price"></AppCard>
                </div>
            </div>
        </div>
        <button @click="slide('prev')" class="slider-btn-prev"><img src="/img/icons/page-left.svg" /></button>
        <button @click="slide('next')" class="slider-btn-next"><img src="/img/icons/page-left.svg" style="transform: rotate(180deg);" /></button>
    </div>
</template>
<style scoped>
    .slider {
        margin-top: 50px;
        position: relative;
        width: 100%;
    }
    .slider-container {
        position: relative;
        overflow: hidden;
        height: 452px;
    }
    .slider-wrap {
        position: absolute;
        top: 0;
        left: 0;
        display: flex;
        column-gap: 32px;
        height: 100%;
        transition: transform 0.5s ease;
    }
    .slider-slide {
        flex: 0 0 282px;
        /* width: 250px; */
    }
    .slider-controls {
        width: 100%;
        position: relative;
        top: 0;
    }
    .slider-btn-next, .slider-btn-prev {
        position: absolute;
        transform: translate(-50%, 0);
        padding: 13px;
        border: 1px solid var(--color-focus);
        background-color: var(--bg-common);
        cursor: pointer;
    }
    .slider-btn-prev {
        top: 50%;
        left: -40px;
    }
    .slider-btn-next {
        top: 50%;
        right: -87px;
    }
    .slider-header {
        margin-top: 80px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .slider-header h2 {
        font-size: 40px;
        font-weight: 500;
        font-family: 'Montserrat Alternates';
    }
    .slider-header a {
        display: flex;
        align-items: center;
    }
    .slider-header img {
        margin-left: 10px;
        transform: rotate(-90deg);
    }
    @media screen and (max-width: 1350px) {
        .slider {
            width: 910px;
            margin: 50px auto;
        }
    }
    @media screen and (max-width: 1050px) {
        .slider {
            width: 596px;
        }
    }
    @media screen and (max-width: 760px) {
        .slider {
            width: 282px;
        }
    }
    @media screen and (max-width: 760px) {
        .slider {
            width: 282px;
        }
    }
    @media screen and (max-width: 420px) {
        .slider-btn-next {
            top: initial;
            bottom: -60px;
            right: 0;
        }
        .slider-btn-prev {
            top: initial;
            bottom: -60px;
            left: 47px;
        }
    }
</style>
<script setup>
    import { ref, onMounted } from 'vue';

    defineProps(['cards']);
    const currentIndex = ref(0);
    const slideWidth = ref(null);

    onMounted(() => {setTimeout(() => {
        slideWidth.value = document.querySelector('.slider .card').offsetWidth;
    }, 3000)})

    const slide = (direction) => {
        const slider = document.querySelector('.slider').offsetWidth / 282;
        const slides = document.querySelectorAll('.slider-slide');
        const wrap = document.querySelector('.slider-wrap');
        const isSoloCard = Math.ceil(slider) === 1 ? 0 : 1;
        const maxIndex = slides.length - Math.ceil(slider) + isSoloCard;
        let nexIndex;

        if (direction === 'next') {
            nexIndex = currentIndex.value === maxIndex ? 0 : currentIndex.value + 1;
        } else {
            nexIndex = currentIndex.value === 0 ? maxIndex : currentIndex.value - 1;
        }
        wrap.style.transform = `translateX(-${(slideWidth.value + 32) * nexIndex}px)`;
        currentIndex.value = nexIndex;
    }
</script>