<script setup lang="ts">
import { ref, watchEffect } from 'vue'

const settingsKey = 'notifications.settings'

const defaults = {
    cpuThreshold: 90,
    diskThreshold: 90,
    channels: { email: true, webhook: false },
    webhookUrl: '',
}

const settings = ref(JSON.parse(localStorage.getItem(settingsKey) || 'null') || defaults)

function save() {
    localStorage.setItem(settingsKey, JSON.stringify(settings.value))
    alert('Settings saved (local only)')
}

watchEffect(() => {
    // keep simple reactive persistence during editing (optional)
})
</script>

<template>
    <section>
        <h2>Notifications settings</h2>
        <p class="muted">Configure thresholds and channels for alerts.</p>

        <form class="settings" @submit.prevent="save" aria-label="Notifications settings form">
            <label class="row">
                <span>CPU threshold (%)</span>
                <input type="number" v-model.number="settings.cpuThreshold" min="1" max="100" />
            </label>

            <label class="row">
                <span>Disk threshold (%)</span>
                <input type="number" v-model.number="settings.diskThreshold" min="1" max="100" />
            </label>

            <fieldset class="channels">
                <legend>Channels</legend>
                <label><input type="checkbox" v-model="settings.channels.email" /> Email</label>
                <label><input type="checkbox" v-model="settings.channels.webhook" /> Webhook</label>
            </fieldset>

            <label class="row">
                <span>Webhook URL</span>
                <input type="url" v-model="settings.webhookUrl" :disabled="!settings.channels.webhook"
                    placeholder="https://example.com/webhook" />
            </label>

            <div class="form-actions">
                <button type="submit" class="btn">Save</button>
            </div>
        </form>
    </section>
</template>

<style scoped>
.muted {
    color: var(--color-text);
    opacity: 0.8
}

.settings {
    display: flex;
    flex-direction: column;
    gap: 12px;
    margin-top: 12px;
    max-width: 640px
}

.row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 12px
}

input[type="number"],
input[type="url"] {
    padding: 8px;
    border-radius: 6px;
    border: 1px solid var(--color-border);
    min-width: 180px
}

.channels {
    border: 1px solid var(--color-border);
    padding: 8px;
    border-radius: 6px
}

.form-actions {
    display: flex;
    justify-content: flex-end
}
</style>
