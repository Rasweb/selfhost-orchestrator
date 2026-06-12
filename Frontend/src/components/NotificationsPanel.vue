<script setup lang="ts">
import { ref } from 'vue'
import { RouterLink } from 'vue-router'

type Notification = {
    id: number
    name: string
    enabled: boolean
    lastTriggered?: string
}

const notifications = ref<Notification[]>([
    { id: 1, name: 'Service down alert', enabled: true, lastTriggered: '2026-06-11 09:12' },
    { id: 2, name: 'High CPU', enabled: false, lastTriggered: '2026-06-10 18:03' },
])

function toggle(n: Notification) {
    n.enabled = !n.enabled
}

function clearAll() {
    notifications.value = []
}
</script>

<template>
    <aside class="notifications" role="region" aria-label="Notifications">
        <header class="notif-head">
            <h4>Notifications</h4>
            <div class="actions">
                <RouterLink to="/settings/notifications" class="link">Settings</RouterLink>
                <button type="button" class="clear" @click="clearAll"
                    aria-label="Clear all notifications">Clear</button>
            </div>
        </header>

        <ul class="notif-list">
            <li v-for="n in notifications" :key="n.id" class="notif-item">
                <div class="row">
                    <div class="title">{{ n.name }}</div>
                    <div class="controls">
                        <label>
                            <input type="checkbox" :checked="n.enabled" @change="() => toggle(n)" />
                            <span class="sr">Enable</span>
                        </label>
                    </div>
                </div>
                <div class="meta">{{ n.lastTriggered ?? 'Never' }}</div>
            </li>
            <li v-if="notifications.length === 0" class="empty">No notifications configured</li>
        </ul>
    </aside>
</template>

<style scoped>
.notif-head,
.row {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.notifications {
    padding: 10px;
    border-radius: 8px;
    background: var(--color-background-soft);
    border: 1px solid var(--color-border)
}

.notif-head {
    gap: 8px
}

.notif-head h4 {
    margin: 0
}

.notif-list {
    list-style: none;
    padding: 8px 0;
    margin: 0;
    display: flex;
    flex-direction: column;
    gap: 8px
}

.notif-item {
    padding: 8px;
    border-radius: 6px;
    background: transparent;
    border: 1px solid transparent
}

.notif-item .title {
    font-weight: 600
}

.meta {
    font-size: 0.85rem;
    color: var(--color-text);
    opacity: 0.7
}

.actions {
    display: flex;
    gap: 8px;
    align-items: center
}

.link {
    color: var(--vt-c-indigo);
    text-decoration: none
}

.clear {
    background: transparent;
    border: 1px solid var(--color-border);
    padding: 6px;
    border-radius: 6px;
    cursor: pointer
}

.empty {
    padding: 12px;
    color: var(--color-text);
    opacity: 0.8
}

.sr {
    position: absolute;
    left: -9999px
}
</style>
