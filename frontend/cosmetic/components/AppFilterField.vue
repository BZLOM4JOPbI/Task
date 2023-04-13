<template>
    <div class="filter" @click="clickEvent">
        <span><slot name="filter-name" /></span><img class='arrow' src="/img/icons/arrow.svg" alt="">
    </div>
    <div v-if='status' v-bind:class="{ isVisible: status}">
        <slot name="options" />
    </div>
</template>


<script setup>
    import { ref, watch } from 'vue';
    let status = ref(false);
    const clickEvent = () => {
        status.value = !status.value

    };
    watch (status, (cur, old) => console.log(`Значение изменилось с ${old} на ${cur}`))
</script>

<style scoped>
    .filter {
        width: 100%;
        display: flex;
        align-items: center;
        margin-bottom: 20px;
        cursor: pointer;
        padding-right: 10px;
    }
    .arrow {
        /* justify-self: flex-end; */
        margin-left: auto;
    }
    .filter span {
        font-size: 18px;
        font-weight: 600;
    }
    .isVisible {
        animation: increaseOpacity 1s;
    }
    @keyframes increaseOpacity {
        from {
            opacity: 0;
        }
        to {
            opacity: 1;
        }
    }
</style>
