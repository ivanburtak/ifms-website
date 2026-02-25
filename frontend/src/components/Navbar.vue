<template>
  <header class="bg-gradient-to-r from-slate-900 to-slate-800 text-white shadow-lg sticky top-0 z-50">
    <div class="container-custom flex items-center justify-between py-4">
      <router-link to="/" class="text-2xl font-bold bg-gradient-to-r from-sky-400 to-blue-500 bg-clip-text text-transparent hover:from-sky-300 hover:to-blue-400 transition">
        IFMS
      </router-link>
      <nav class="flex items-center space-x-1 md:space-x-2">
        <router-link to="/" class="px-3 py-2 rounded-lg text-slate-300 hover:text-white hover:bg-slate-800 transition duration-200 text-sm md:text-base">
          Головна
        </router-link>
        <router-link to="/events" class="px-3 py-2 rounded-lg text-slate-300 hover:text-white hover:bg-slate-800 transition duration-200 text-sm md:text-base">
          Події
        </router-link>
        <router-link to="/members" class="px-3 py-2 rounded-lg text-slate-300 hover:text-white hover:bg-slate-800 transition duration-200 text-sm md:text-base">
          Члени
        </router-link>
        <router-link to="/links" class="px-3 py-2 rounded-lg text-slate-300 hover:text-white hover:bg-slate-800 transition duration-200 text-sm md:text-base">
          Посилання
        </router-link>
        <router-link to="/contact" class="px-3 py-2 rounded-lg text-slate-300 hover:text-white hover:bg-slate-800 transition duration-200 text-sm md:text-base">
          Зв'язок
        </router-link>
      </nav>
    </div>
  </header>
</template>
