let baseUrl = ''
if (process.env.NODE_ENV === 'production') {
   baseUrl = ''
} else {
   baseUrl = 'http://localhost:8000'
}

export const apiHost = baseUrl