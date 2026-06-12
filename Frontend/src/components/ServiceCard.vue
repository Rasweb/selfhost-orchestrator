<script setup lang="ts">
import type { Service } from '@/types/types.ts'

const props = defineProps<{ service: Service }>()
const emit = defineEmits(['restart'])

function onRestart() {
  emit('restart', props.service.id)
}
</script>

<template>
  <article
    class="service-card"
    :aria-label="`Service ${service.name}`"
    :id="`svc-${service.id}`"
    :aria-labelledby="`svc-title-${service.id}`"
    tabindex="0"
    role="group"
  >
    <header class="card-head">
      <div class="leading">
        <div class="icon" aria-hidden="true">
          <!-- simple service icon -->
          <svg width="28" height="28" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <rect x="3" y="4" width="18" height="14" rx="2" stroke="currentColor" stroke-width="1.2" />
            <path d="M7 8h10M7 12h10" stroke="currentColor" stroke-width="1" stroke-linecap="round" />
          </svg>
        </div>
        <div class="meta">
          <div class="title" :id="`svc-title-${service.id}`">{{ service.name }}</div>
          <div class="subtitle">{{ service.version ?? '—' }}</div>
        </div>
      </div>
      <div class="status-wrap">
        <span :class="['status-dot', service.status]" aria-hidden="true"></span>
        <div :class="['status', service.status]" role="status" aria-live="polite">{{ service.status }}</div>
      </div>
    </header>

    <div class="card-body">
      <div class="row"><strong>Uptime:</strong> <span>{{ service.uptime ?? 'n/a' }}</span></div>
      <div class="row"><strong>URL:</strong>
        <a v-if="service.url" :href="service.url" target="_blank" rel="noopener">Open</a>
        <span v-else>—</span>
      </div>
    </div>

    <footer class="card-foot">
      <button type="button" class="btn" @click="onRestart" :aria-label="`Restart ${service.name}`">Restart</button>
      <a v-if="service.url" :href="service.url" target="_blank" rel="noopener" class="btn ghost" :aria-label="`Open ${service.name} in new tab`">Open</a>
    </footer>
  </article>
</template>

<style scoped>
.card-head,
.leading {
    display: flex;
    align-items: flex-start;
}

.service-card {
  border: 1px solid var(--color-border);
  background: var(--color-background-soft);
  border-radius: 12px;
  padding: 12px;
  display: flex;
  flex-direction: column;
  gap: 8px
}

.card-head {
  justify-content: space-between;
  gap: 8px
}

.leading {
  gap: 10px;
  flex: 1
}

.icon {
  color: var(--vt-c-indigo);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0
}

.meta .title {
  font-weight: 600;
  word-break: break-word
}

.meta .subtitle {
  font-size: 0.85rem;
  color: var(--color-text);
  opacity: 0.8
}

.status-wrap {
  display: flex;
  align-items: center;
  gap: 6px;
  flex-shrink: 0
}

.status-dot {
  width: 10px;
  height: 10px;
  border-radius: 999px;
  display: inline-block
}

.status {
  padding: 4px 8px;
  border-radius: 999px;
  font-weight: 600;
  text-transform: capitalize;
  font-size: 0.8rem
}

.status.online {
  background: rgba(55, 200, 120, 0.12);
  color: #2a8a4d;
  border: 1px solid rgba(55, 200, 120, 0.22)
}

.status.offline {
  background: rgba(240, 80, 80, 0.08);
  color: #a33;
  border: 1px solid rgba(240, 80, 80, 0.12)
}

.status.unknown {
  background: rgba(160, 160, 160, 0.06);
  color: #666;
  border: 1px solid rgba(160, 160, 160, 0.08)
}

.status-dot.online {
  background: #2a8a4d
}

.status-dot.offline {
  background: #a33
}

.status-dot.unknown {
  background: #888
}

.card-body {
  font-size: 0.9rem;
  color: var(--color-text);
  display: flex;
  flex-direction: column;
  gap: 4px
}

.row {
  display: flex;
  justify-content: space-between;
  gap: 8px
}

.card-foot {
  display: flex;
  flex-direction: column;
  gap: 8px
}

.btn {
  background: var(--vt-c-indigo);
  color: var(--vt-c-white);
  border: none;
  padding: 8px 10px;
  border-radius: 8px;
  cursor: pointer;
  font-size: 0.9rem
}

.btn.ghost {
  background: transparent;
  color: var(--vt-c-indigo);
  border: 1px solid var(--color-border)
}

@media (min-width: 640px) {
  .card-foot {
    flex-direction: row;
    justify-content: flex-end
  }
}
</style>
