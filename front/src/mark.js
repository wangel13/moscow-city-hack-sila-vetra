function Mark({ distance }) {
  let percent = 100 - distance
  if (percent < 0) {
    percent = 0
  }

  let classes = ''
  if (percent <= 100) {
    classes = 'bg-green-100 text-green-800 dark:bg-green-200 dark:text-green-800'
  }
  if (percent < 60) {
    classes = 'bg-yellow-100 text-yellow-800 dark:bg-yellow-200 dark:text-yellow-800'
  }
  if (percent < 30) {
    classes = 'bg-red-100 text-red-800 dark:bg-red-200 dark:text-red-800'
  }

  return (
    <p
      className={`${classes} text-xl font-semibold inline-flex items-center py-1.5 px-3 rounded dark:bg-blue-200 dark:text-blue-800`}
    >
      {percent} / 100
    </p>
  )
}

export default Mark
