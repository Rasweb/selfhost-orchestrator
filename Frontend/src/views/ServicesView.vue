<script setup lang="ts">
import ServiceCard from '@/components/ServiceCard.vue'
import { ref } from 'vue'

const services = ref([
    { id: 1, name: 'Service One', status: 'online', uptime: '4d 12h', version: '0.9.4', url: 'https://example.com' },
    { id: 2, name: 'Service Two', status: 'online', uptime: '1d 2h', version: '1.2.0', url: 'https://example.org' },
    { id: 3, name: 'Database', status: 'offline', uptime: null, version: '12.3', url: '' },
    { id: 4, name: 'Cache', status: 'online', uptime: '12h', version: '3.4.1', url: '' },
    { id: 5, name: 'MQ', status: 'unknown', uptime: null, version: '2.1.0', url: '' },
])

function handleRestart(id: number | string) {
    alert(`Restart requested for ${id}`)
}
</script>

<template>
    <section>
        <header class="section-head">
            <div>
                <h2>All Services</h2>
                <p class="muted">Complete list of registered services.</p>
            </div>
        </header>

        <div class="cards-grid">
            <ServiceCard v-for="s in services" :key="s.id" :service="s" @restart="handleRestart" />
        </div>
    </section>
</template>

<style scoped>
.section-head {
    margin-bottom: 8px
}

.muted {
    color: var(--color-text);
    opacity: 0.8;
    margin: 0
}

.cards-grid {
    display: grid;
    gap: 1rem;
    grid-template-columns: repeat(auto-fit, minmax(240px, 240px));
    justify-content: center;
    max-width: 1200px;
    margin: 0 auto
}
</style>
