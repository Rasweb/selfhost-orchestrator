<script setup lang="ts">
const emit = defineEmits(['add','refresh','runchecks'])
</script>

<template>
  <div class="quick-actions" role="toolbar" aria-label="Quick actions">
    <button type="button" class="qa primary" @click="$emit('add')" aria-label="Add service">+ Add Service</button>
    <button type="button" class="qa primary" @click="$emit('runchecks')" aria-label="Run health checks">Run checks</button>
    <button type="button" class="qa primary" @click="$emit('refresh')" aria-label="Refresh data">Refresh</button>
  </div>
</template>

<style scoped>
.quick-actions {
  display: flex;
  flex-direction: column;
  gap: 8px;
  width: 100%
}

.qa {
  padding: 10px 12px;
  border-radius: 8px;
  border: 1px solid var(--color-border);
  background: transparent;
  cursor: pointer;
  width: 100%
}

.qa.primary {
  background: var(--vt-c-indigo);
  color: var(--vt-c-white);
  border: none
}

@media (min-width: 640px) {
  .quick-actions {
    flex-direction: row;
    width: auto
  }

  .qa {
    width: auto
  }
}
</style>
