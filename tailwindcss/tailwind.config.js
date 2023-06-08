/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
      "../templates/**/*.{html,js}",
      "./node_modules/tw-elements/dist/js/**/*.js",

  ],
  theme: {
      colors: {
      'neutral': '#ff6c38',
    },
    extend: {},
  },
  darkMode: "class",
  plugins: [require("tw-elements/dist/plugin.cjs")],
}

