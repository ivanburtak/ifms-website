<template>
  <div>
    <!-- Hero Section -->
    <div class="bg-gradient-to-r from-slate-900 to-slate-800 text-white py-16 mb-8">
      <div class="container-custom">
        <h1 class="text-5xl font-bold mb-4">Івано-Франківське<br/>Математичне Товариство</h1>
        <p class="text-lg text-slate-300 mb-6 max-w-2xl">Об'єднання математиків та любителів точних наук. Ми організуємо конференції, семінари та воркшопи для розвитку математичної науки.</p>
        <div class="flex gap-4">
          <router-link to="/apply" class="px-6 py-3 bg-sky-600 hover:bg-sky-700 !text-white rounded-lg font-semibold transition">Подати заяву</router-link>
          <router-link to="/events" class="px-6 py-3 bg-slate-700 hover:bg-slate-600 !text-white rounded-lg font-semibold transition">Переглянути події</router-link>
        </div>
      </div>
    </div>

    <!-- Quick Stats -->
    <div class="container-custom mb-12">
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-12">
        <div class="bg-slate-50 p-6 rounded-lg border border-slate-200 text-center">
          <div class="text-3xl font-bold text-slate-900 mb-2">24</div>
          <div class="text-slate-600">Активних членів</div>
        </div>
        <div class="bg-slate-50 p-6 rounded-lg border border-slate-200 text-center">
          <div class="text-3xl font-bold text-sky-600 mb-2">15+</div>
          <div class="text-slate-600">Подій щороку</div>
        </div>
        <div class="bg-slate-50 p-6 rounded-lg border border-slate-200 text-center">
          <div class="text-3xl font-bold text-slate-900 mb-2">5 років</div>
          <div class="text-slate-600">Діяльності</div>
        </div>
      </div>
    </div>

    <!-- About Section -->
    <section class="container-custom mb-12">
      <h2 class="text-3xl font-bold mb-6 text-slate-900">Про нас</h2>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
        <div>
          <p class="text-slate-700 mb-4 leading-relaxed">Івано-Франківське математичне товариство - це об'єднання професіоналів та студентів, які займаються математичною наукою та її застосуванням.</p>
          <p class="text-slate-700 leading-relaxed">Ми організуємо різноманітні заходи для обміну знаннями, розвитку наукових компетенцій та побудови спільноти дослідників.</p>
        </div>
        <div class="bg-slate-50 p-6 rounded-lg border border-slate-200">
          <h3 class="font-semibold text-slate-900 mb-4">Установчі документи</h3>
          <ul class="space-y-3">
            <li><a href="#" class="text-sky-600 hover:text-sky-700 hover:underline flex items-center gap-2"><span>📄</span> Статут товариства</a></li>
            <li><a href="#" class="text-sky-600 hover:text-sky-700 hover:underline flex items-center gap-2"><span>📄</span> Положення про діяльність</a></li>
          </ul>
        </div>
      </div>
    </section>
  </div>
</template>
