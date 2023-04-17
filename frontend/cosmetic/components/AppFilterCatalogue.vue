<template>
    <div class="filter catalogue">
        <img src="/img/icons/grid.svg" alt=""><span>Каталог</span><img class='arrow' src="/img/icons/arrow.svg" alt="">
    </div>
    <!-- <p v-bind:class="{nonDisplay: isVisible}">Camry 3.5</p> -->
    <!-- <p v-if="isVisible">Camry 3.5</p> -->
    <slot name="options" />
</template>


<script setup>

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
        user-select: none;
        -moz-user-select: none;
        -moz-user-select: none;
        -webkit-user-select: none;
    }
    .catalogue {
        background-color: var(--color-focus);
        padding: 20px 10px;
    }
    .catalogue img:first-child {
        margin-right: 10px;
    }
    .nonDisplay {
        display: none !important;
    }
</style>