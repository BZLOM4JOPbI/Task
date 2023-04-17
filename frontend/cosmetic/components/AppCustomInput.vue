<template>
    <input
    type="checkbox"
    value="input"
    :checked="modelCheck"
    @change="$emit('update:modelCheck', $event.target.checked)"
  />
</template>
<script setup>
defineProps(['modelCheck'])
defineEmits(['update:modelCheck'])
</script>   