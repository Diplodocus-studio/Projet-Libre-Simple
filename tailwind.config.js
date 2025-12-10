/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./templates/*.html'],
  theme: {
    colors: {
        'platinum': '#efefef',
        'jet-black': '#2b303a',
        'frosted-blue': '#92dce5',
        'lavender-blush': '#eee5e9',
        'custom-grey': '#7c7c7c',
        'burnt-tangerine': '#d64933'
      },
  },
  plugins: [],
  "editor.quickSuggestions": {
  "strings": "on"
  },
  "tailwindCSS.includeLanguages": {
    "plaintext": "html"
  }
}
