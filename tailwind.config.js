module.exports = {
  content: [
      './**/*.html',
      './node_modules/flowbite/**/*.js',
  ],
  theme: {
    extend: {},
    fontFamily: {
      'display': ['ABeeZee']
    }
  },
  plugins: [
    require('flowbite/plugin'),
  ],
}
