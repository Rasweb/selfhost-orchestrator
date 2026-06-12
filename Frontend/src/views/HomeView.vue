<script setup lang="ts">
import ServiceCard from '@/components/ServiceCard.vue'
import MetricCard from '@/components/MetricCard.vue'
import QuickActions from '@/components/QuickActions.vue'
import SystemCard from '@/components/SystemCard.vue'
import { ref } from 'vue'
import { RouterLink } from 'vue-router'
import type { Service } from '@/types/types.ts'

const services = ref<Service[]>([
  { id: 1, name: 'Service One', status: 'online', uptime: '4d 12h', version: '0.9.4', url: 'https://example.com' },
  { id: 2, name: 'Service Two', status: 'online', uptime: '1d 2h', version: '1.2.0', url: 'https://example.org' },
  { id: 3, name: 'Database', status: 'offline', uptime: null, version: '12.3', url: '' },
])

function handleRestart(id: number | string) {
  alert(`Restart requested for ${id}`)
}
</script>

<template>
  <div class="dashboard">
    <main class="main-col">
      <section class="top-row">
        <div class="metrics">
          <MetricCard label="Services Up" value="3"/>
          <MetricCard label="Uptime" value="99.98%"/>
          <MetricCard label="Active Alerts" value="0" />
        </div>

        <div class="actions">
          <QuickActions @add="() => console.log('Add service')" @refresh="() => console.log('Refresh')"
            @runchecks="() => console.log('Run checks')" />
        </div>
      </section>

      <section class="services-preview">
        <header class="section-head">
          <div>
            <h2>Services</h2>
            <p class="muted">Quick overview — press "Show more" to manage services.</p>
          </div>
          <RouterLink to="/services" class="show-more">Show more →</RouterLink>
        </header>

        <div class="cards-grid">
          <ServiceCard v-for="s in services.slice(0, 3)" :key="s.id" :service="s" @restart="handleRestart" />
        </div>
      </section>
    </main>

    <aside class="side-col">
      <SystemCard cpu="12%" ram="1.8 GB / 4 GB" disk="18%" />

      <div style="height:12px"></div>

      <section>
        <h3>Recent events</h3>
        <div class="events">
          <div class="ev">No recent events</div>
        </div>
      </section>
    </aside>
  </div>
</template>

<style scoped>
.dashboard,
.metrics {
  display: grid;
  grid-template-columns: 1fr;
}

.main-col,
.side-col,
.top-row {
  display: flex;
  flex-direction: column;
}

.dashboard,
.main-col,
.top-row,
.cards-grid {
  gap: 1rem;
}

.side-col,
.metrics,
.services-preview,
.section-head {
  gap: 12px
}

.actions {
  display: flex;
  flex-direction: column;
  gap: 8px;
  width: 100%
}

.services-preview .section-head {
  display: flex;
  flex-direction: column;
}

.cards-grid {
  display: grid;
  grid-template-columns: 1fr;
  margin-top: 1rem
}

.muted {
  color: var(--color-text);
  opacity: 0.8;
  margin: 0;
  font-size: 0.95rem
}

.show-more {
  color: var(--vt-c-indigo);
  text-decoration: none;
  padding: 6px;
  border-radius: 8px
}

h2 {
  font-size: 1.25rem;
  margin-bottom: 0.25rem
}

.events {
  padding: 8px;
  border: 1px dashed var(--color-border);
  border-radius: 8px
}

.ev {
  padding: 8px;
  color: var(--color-text);
  opacity: 0.8
}

@media (min-width: 640px) {
  .metrics,
  .cards-grid {
    grid-template-columns: repeat(2, 1fr)
  }

  .actions {
    flex-direction: row;
    flex-wrap: wrap;
    width: auto
  }

}

@media (min-width: 1024px) {
  .dashboard {
    grid-template-columns: 2fr 1fr;
    align-items: start;
  }

  .metrics {
    grid-template-columns: repeat(3, 1fr);
  }

  .services-preview .section-head {
    flex-direction: row;
    justify-content: space-between;
    align-items: flex-end
  }
}

</style>
