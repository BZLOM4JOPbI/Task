<template>
        <div class="price-range">
            <p>{{ min }} - {{ max }}</p>
            <input @change="displayMinValue" type="range" value="350" min="350" max="5000" step="50">
            <input @change="displayMaxValue" type="range" value="3700" min="350" max="5000" step="50">
        </div>
</template>
<script setup>
    import { ref } from 'vue'

    let min = ref(100);
    let max = ref(250);

    const validatePrice = (low, high) => {
        if (low > high) {
            min.value = high;
            max.value = low;
            return
        }
        min.value = low;
        max.value = high;
    }
    const displayMinValue = (e) => {
        let low = parseInt(e.target.value);
        let high = parseInt(e.target.nextSibling.value);
        console.log(low, high);
        validatePrice(low, high);
    }
    const displayMaxValue = (e) => {
        let low = parseInt(e.target.previousSibling.value);
        let high = parseInt(e.target.value);
        console.log(low, high);
        validatePrice(low, high);
    }
</script>
<style scoped>
    .price-range {
        width: 100%;
        position: relative;
        margin: 22px 0 40px;
    }
    input[type='range'] {
        width: 100%;
        -webkit-appearance: none;
        -moz-appearance:none;
        background: transparent; 
        position: absolute;
        left: 0;
    }
    input[type='range']::-webkit-slider-thumb {
        -webkit-appearance:none;
        height: 14px;
        width: 14px;
        border-radius: 0;
        background: var(--color-accent);
        cursor: pointer;
        margin-top: -6px;
        position: relative;
        z-index: 1;
    }
    input[type='range']::-moz-range-thumb {
        -moz-appearance:none;
        height: 14px;
        width: 14px;
        background: var(--color-accent);
        cursor: pointer;
        border-radius: 0;
        margin-top: -6px;
        position: relative;
        z-index: 1;
        border: none;
    }
    input[type=range]::-webkit-slider-runnable-track {
        width: 100%;
        height: 2px;
        background: var(--text-opacity);
        border: none;
    }
    input[type=range]::-moz-range-track {
        width: 100%;
        height: 2px;
        background: var(--text-opacity);
        border: none;
    }
    p {
        text-align: center;
        font-size: 18px;
        margin-bottom: 10px;
    }
</style>