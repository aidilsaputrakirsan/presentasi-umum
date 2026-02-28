<template>
  <div class="network-container absolute inset-0 z-[-1] pointer-events-none overflow-hidden transition-colors duration-500" :class="isDark ? 'bg-slate-900' : 'bg-blue-50'">
    <canvas ref="canvasEl" class="w-full h-full pointer-events-auto"></canvas>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, watch } from 'vue'

const canvasEl = ref(null)
let animationFrameId = null
let particles = []
let mouse = { x: null, y: null, radius: 150 }

// Tweak styling relative to theme
const isDark = ref(false)
const checkDark = () => {
  isDark.value = document.documentElement.classList.contains('dark')
}

onMounted(() => {
  const canvas = canvasEl.value
  const ctx = canvas.getContext('2d')
  
  canvas.width = window.innerWidth
  canvas.height = window.innerHeight

  checkDark()
  const observer = new MutationObserver(checkDark)
  observer.observe(document.documentElement, { attributes: true, attributeFilter: ['class'] })

  class Particle {
    constructor(x, y, dx, dy, size, color) {
      this.x = x
      this.y = y
      this.dx = dx
      this.dy = dy
      this.size = size
      this.color = color
      this.baseX = x
      this.baseY = y
    }

    draw() {
      ctx.beginPath()
      ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2, false)
      ctx.fillStyle = isDark.value ? 'rgba(96, 165, 250, 0.8)' : 'rgba(59, 130, 246, 0.6)'
      ctx.fill()
    }

    update() {
      if (this.x > canvas.width || this.x < 0) this.dx = -this.dx
      if (this.y > canvas.height || this.y < 0) this.dy = -this.dy

      // Interactivity
      let dx = mouse.x - this.x
      let dy = mouse.y - this.y
      let distance = Math.sqrt(dx * dx + dy * dy)
      
      if (distance < mouse.radius) {
        const force = (mouse.radius - distance) / mouse.radius
        const forceX = dx * force * 0.05
        const forceY = dy * force * 0.05
        this.x -= forceX
        this.y -= forceY
      } else {
        if (this.x !== this.baseX) { this.x -= (this.x - this.baseX) * 0.05 }
        if (this.y !== this.baseY) { this.y -= (this.y - this.baseY) * 0.05 }
      }

      this.baseX += this.dx
      this.baseY += this.dy
      this.x += this.dx
      this.y += this.dy

      this.draw()
    }
  }

  function init() {
    particles = []
    let numberOfParticles = (canvas.width * canvas.height) / 15000
    for (let i = 0; i < numberOfParticles; i++) {
        let size = (Math.random() * 2) + 1
        let x = (Math.random() * ((innerWidth - size * 2) - (size * 2)) + size * 2)
        let y = (Math.random() * ((innerHeight - size * 2) - (size * 2)) + size * 2)
        let dx = (Math.random() * 0.5) - 0.25
        let dy = (Math.random() * 0.5) - 0.25
        let color = '#3b82f6'
        particles.push(new Particle(x, y, dx, dy, size, color))
    }
  }

  function connect() {
    let maxDistance = 120
    let opacityValue = 1
    for (let a = 0; a < particles.length; a++) {
        for (let b = a; b < particles.length; b++) {
            let distance = ((particles[a].x - particles[b].x) * (particles[a].x - particles[b].x))
                + ((particles[a].y - particles[b].y) * (particles[a].y - particles[b].y))
            if (distance < (maxDistance * maxDistance)) {
                opacityValue = 1 - (distance / 15000)
                ctx.strokeStyle = isDark.value ? `rgba(96, 165, 250, ${opacityValue})` : `rgba(59, 130, 246, ${opacityValue})`
                ctx.lineWidth = 1
                ctx.beginPath()
                ctx.moveTo(particles[a].x, particles[a].y)
                ctx.lineTo(particles[b].x, particles[b].y)
                ctx.stroke()
            }
        }
    }
  }

  function animate() {
      animationFrameId = requestAnimationFrame(animate)
      ctx.clearRect(0, 0, innerWidth, innerHeight)
      
      for (let i = 0; i < particles.length; i++) {
          particles[i].update()
      }
      connect()
  }

  // Event Listeners
  window.addEventListener('resize', () => {
      canvas.width = window.innerWidth
      canvas.height = window.innerHeight
      init()
  })
  
  window.addEventListener('mousemove', (e) => {
      mouse.x = e.x
      mouse.y = e.y
  })
  
  window.addEventListener('mouseout', () => {
      mouse.x = undefined
      mouse.y = undefined
  })

  init()
  animate()

  onUnmounted(() => {
    cancelAnimationFrame(animationFrameId)
    observer.disconnect()
    window.removeEventListener('resize', init)
  })
})
</script>

<style scoped>
.network-container {
  /* Ensure it sits behind slides but over the slidev background */
  z-index: -1;
  pointer-events: auto; /* allows interaction with canvas */
}
</style>

<style>
/* CSS Global untuk menimpa warna dasar background theme 'seriph' agar tidak menjadi pink saat di Export ke PDF */
:root {
  --slidev-theme-background: #eff6ff !important; /* Tailwind bg-blue-50 */
}
.dark {
  --slidev-theme-background: #0f172a !important; /* Tailwind bg-slate-900 */
}
@media print {
  .slidev-layout {
    background-color: #eff6ff !important;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }
}
</style>
