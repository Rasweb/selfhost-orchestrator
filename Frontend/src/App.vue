<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import { ref } from 'vue'

const isOpen = ref(false);

</script>

<template>
    <div class="layout">
      <header>
        <button class="menu-btn" @click="isOpen = !isOpen" :class="{active: isOpen}">
          <span v-if="isOpen">X</span>
          <span v-else>☰</span>
        </button>
        <span class="title">
          Headline
        </span>
      </header>
      <aside class="sidebar" :class="{open: isOpen}">
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
        <RouterLink to="/settings/notifications">Settings</RouterLink>
      </aside>
      <main>
        <RouterView />
      </main>
    </div>
</template>

<style scoped>
.layout {
  display: grid;
  gap: 1rem;
}

header {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  padding: 1rem;
}

.title {
  padding: 1rem;
  font-size: 1.25rem;
  font-weight: 600;
}

.menu-btn {
  border: 1px solid #ccc;
  background: white;
  padding: 0.6rem 0.8rem;
  font-size: 1.2rem;
  border-radius: 0.5rem;
  cursor: pointer;
}

.sidebar {
  display: none;
  width: 100px;
  flex-direction: column;
  gap: 4px;
}

.sidebar.open {
  display: flex;
}

.sidebar a {
  padding: 8px 12px;
  font-size: 0.9rem;
  border-radius: 6px;
}

@media (min-width: 1024px) {
  .sidebar {
    padding: 8px;
    overflow-y: auto;
  }
}

main {
  padding: 1rem;
}

@media (min-width: 1024px) {
  .layout {
    grid-template-columns: 110px 1fr;
    grid-template-areas:
      "header header"
      "sidebar main";
  }

  header {
    grid-area: header;
  }

  .sidebar{
    grid-area: sidebar;
  }
  main {
    grid-area: main;
  }
}
</style>
