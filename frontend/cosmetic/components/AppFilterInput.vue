<template>
    <label>
        <input type="checkbox" :value="inputValue" @input="$emit('update:inputValue', $event.target.value)">{{ label }}
    </label>
</template>
<script setup>
    import { ref } from 'vue'
    defineProps(['label', 'inputValue',]);
    defineEmits(['update:inputValue']);

</script>
<style scoped>
    label {
        margin-bottom: 10px;
        font-size: 18px;
        display: flex;
        align-items: center;
        width: 100%;
    }
    label input[type='checkbox'] {
        margin-right: 10px;
        position: relative;
        width: 20px;
        height: 20px;
        accent-color: var(--color-accent);
    } 
</style>