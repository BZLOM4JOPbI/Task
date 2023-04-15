<template>
    <div class="card">
        <img class='card-img' src="/img/photo.png" alt="">
        <h6 class="card-title">{{  title }}</h6>
        <p class="card-desc">{{ desc }}</p>
        <p class="card-price">{{ price }}&#x20bd;</p>
        <button class="add-to-cart"><img src="/img/icons/cart.svg" alt=""></button>
    </div>
</template>
<script setup>
    defineProps(['title', 'desc', 'price']);
</script>
<style scoped>
    .card {
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        position: relative;
    }
    .card-title {
        margin: 20px 0 5px;
        font-size: 20px;
        line-height: 26px;
        font-weight: 500;
        color: var(--color-accent);
    }
    .card-img {
        max-width: 100%;
        width: 100%;
    }
    .card-price {
        font-size: 20px;
        line-height: 26px;
        font-weight: 500;
        margin: 17px 0 12px;
    }
    .card-desc {
        color: var(--text-opacity);
    }
    .add-to-cart {
        position: absolute;
        right: 0;
        bottom: 0;
        background-color: var(--color-accent);
        padding: 13px 20px;
        cursor: pointer;
    }
    .add-to-cart img {
        filter: invert(1);
    }
    @media screen and (max-width: 1050px) {
    .add-to-cart img {
        width: 20px;
        height: 20px;
    }
    .add-to-cart {
        padding: 8px 15px;
    }
    }
</style>