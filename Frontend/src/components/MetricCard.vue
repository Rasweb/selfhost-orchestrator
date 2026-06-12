<script setup lang="ts">
const props = defineProps<{ label: string; value: string; icon?: string }>()
</script>

<template>
  <article class="metric-card" :aria-label="label">
    <div class="left">
      <div class="icon" v-if="props.icon" v-html="props.icon" aria-hidden="true"></div>
      <div class="label">{{ label }}</div>
    </div>
    <div class="right">
      <div class="value" aria-live="polite">{{ value }}</div>
    </div>
  </article>
</template>

<style scoped>   
.metric-card, 
.left,
.right{
    display: flex;
    flex-direction: column;
}

.metric-card {
  gap: 8px;
  padding: 12px;
  border-radius: 10px;
  background: var(--color-background-soft);
  border: 1px solid var(--color-border)
}

.left {
  gap: 8px;
  align-items: flex-start
}

.icon {
  width: 28px;
  height: 28px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--vt-c-indigo)
}

.label {
  font-size: 0.9rem;
  color: var(--color-text);
  opacity: 0.9
}

.right {
  gap: 2px
}

.value {
  font-weight: 700;
  font-size: 1.5rem
}

.delta {
  font-size: 0.8rem;
  color: var(--color-text);
  opacity: 0.7
}

@media (min-width: 640px) {
  .metric-card,
  .left {
    flex-direction: row;
    align-items: center;
  }

  .metric-card {
    justify-content: space-between;
    gap: 12px
  }

  .value {
    font-size: 1.25rem
  }
}
</style>
