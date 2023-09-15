/** @type {import('tailwindcss').Config} */

const defaultTheme = require('tailwindcss/defaultTheme')

module.exports = {
  content: [
    "./assets/**/*.{py,html,js}",
    "./components/**/*.{py,html,js}",
    "./data/**/*.{py,html,js}",
    "./pages/**/*.{py,html,js}",
    "./utils/**/*.{py,html,js}",
    "./app.py"
  ],
  theme: {
    screens: {
      'xs': '475px',
      ...defaultTheme.screens,
    },
  },
  plugins: [
    require('@tailwindcss/typography')
  ],
}
