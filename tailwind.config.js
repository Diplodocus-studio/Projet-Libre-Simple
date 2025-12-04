/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [],
  theme: {
    extend: {
       colors: {
        'platinum': '#EFEFEF',
        'jet-black': '#2B303A',
        'frosted-blue': '#92DCE5',
        'lavender-blush': '#EEE5E9',
        'custom-grey': '#7C7C7C',
        'burnt-tangerine': '#D64933',
      },
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
