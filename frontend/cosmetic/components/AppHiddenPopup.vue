<template>
    <div class="filter" @click="changeOptionsVisible">
        <span><slot name="filter-name" /></span><img class='arrow' v-bind:class='{ top: status, bottom: !status }' src="/img/icons/arrow.svg" alt="">
        <div v-show='status' v-bind:class="{ isVisible: status}">
            <slot name="options" />
        </div>
    </div>
</template>


<script setup>
    import { ref, watch } from 'vue';
    let status = ref(false);
    const changeOptionsVisible = () => {
        status.value = !status.value

    };
</script>

<style scoped>
    .filter {
        width: 100%;
        display: flex;
        align-items: center;
        margin-bottom: 20px;
        cursor: pointer;
        padding-right: 10px;
        position: relative;
    }
    .arrow {
        /* justify-self: flex-end; */
        margin-left: auto;
    }
    .filter span {
        font-size: 18px;
        user-select: none;
        margin-right: 10px;
        -moz-user-select: none;
        -moz-user-select: none;
        -webkit-user-select: none;
    }
    .isVisible {
        animation: increaseOpacity 0.5s;
        position: absolute;
        top: 100%;
        right: 0;
        border: 1px solid var(--color-accent);
        z-index: 1;
        background-color: #fff;
    }
    .top {
        animation: arrowRotateTop 0.5s forwards;
    }
    .bottom {
        animation: arrowRotateBottom 0.5s;
    }
    @keyframes increaseOpacity {
        from {
            opacity: 0;
        }
        to {
            opacity: 1;
        }
    }
    @keyframes arrowRotateTop {
        from {
            -moz-transform: rotate(0deg);
            -webkit-transform: rotate(0deg);
            transform: rotate(0deg);
        }
        to {
            -moz-transform: rotate(180deg);
            -webkit-transform: rotate(180deg);
            transform: rotate(180deg);
        }
    }
    @keyframes arrowRotateBottom {
        from {
            -moz-transform: rotate(180deg);
            -webkit-transform: rotate(180deg);
            transform: rotate(180deg);
        }
        to {
            -moz-transform: rotate(360deg);
            -webkit-transform: rotate(360deg);
            transform: rotate(360deg);
        }
    }
</style>