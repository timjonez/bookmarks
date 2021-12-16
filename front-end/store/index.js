export const state = () => ({
  bookmarks: [
    {
      id: 1,
      name: 'Google',
      url: 'https://google.com',
      icon: 'https://www.google.com/favicon.ico'
    },
    {
      id: 2,
      name: 'Facebook',
      url: 'https://facebook.com',
      icon: 'https://facebook.com/favicon.ico'
    },
    {
      id: 3,
      name: 'Amazon',
      url: 'https://amazon.com',
      icon: 'https://amazon.com/favicon.ico'
    }
  ]
})

export const actions = {
  editBookmark (x, payload) {
    console.log('edit bookmark clicked')
    console.log(x)
    console.log(payload)
  },
  deleteBookmark (x, payload) {
    console.log('delete bookmark clicked')
    console.log(x)
    console.log(payload)
  }
}
