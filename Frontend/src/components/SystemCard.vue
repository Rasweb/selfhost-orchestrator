<script setup lang="ts">
const props = defineProps<{ cpu?: string; ram?: string; disk?: string }>()
</script>

<template>
    <article class="system-card" role="region" aria-label="System metrics">
        <h3>System</h3>
        <ul>
            <li><strong>CPU:</strong> <span>{{ cpu ?? '—' }}</span></li>
            <li><strong>RAM:</strong> <span>{{ ram ?? '—' }}</span></li>
            <li><strong>Disk:</strong> <span>{{ disk ?? '—' }}</span></li>
        </ul>
    </article>
</template>

<style scoped>
.system-card {
    padding: 12px;
    border-radius: 10px;
    background: var(--color-background-soft);
    border: 1px solid var(--color-border)
}

.system-card h3 {
    margin: 0 0 8px 0
}

.system-card ul {
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
    flex-direction: column;
    gap: 6px
}

.system-card li {
    display: flex;
    justify-content: space-between
}
</style>
