<template>
    <form>
        <slot />
    </form>
    {{ model }}
</template>
<style scoped>
    form label:last-child {
        margin-bottom: 20px;
    }
</style>
<script setup>
    defineProps(['model']);
</script>