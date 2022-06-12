import './App.css'
import { useState } from 'react'
import Mark from './mark'

function App() {
  const [text, setText] = useState()
  const [isLoading, setIsLoading] = useState(false)
  const [checkResult, setCheckResult] = useState([])

  const handleInput = (e) => {
    setText(e?.target?.value)
  }
  const handleCheck = async () => {
    setIsLoading(true)
    try {
      let response = await fetch('http://188.166.164.18:5000/check', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json;charset=utf-8',
        },
        body: JSON.stringify({ text }),
      })
      let result = await response.json()
      console.log({ result })
      setCheckResult(result?.news)
      setIsLoading(false)
    } catch (error) {
      console.log({ error })
      setIsLoading(false)
    }
  }

  return (
    <div className="App">
      <div className="mx-auto max-w-3xl px-4 py-4 sm:px-6 xl:max-w-5xl xl:px-0">
        <h1 className="pt-4 pb-6 sm:pr-16 text-2xl font-medium title-font text-gray-900">
          Проверка новостей
        </h1>
        <div className="mb-4 w-full bg-gray-50 rounded-lg border border-gray-200 dark:bg-gray-700 dark:border-gray-600">
          <div className="py-2 px-4 bg-white rounded-t-lg dark:bg-gray-800">
            <label htmlFor="comment" className="sr-only">
              Your comment
            </label>
            <textarea
              disabled={isLoading}
              onChange={handleInput}
              value={text}
              rows="12"
              className="px-0 w-full text-sm text-gray-900 bg-white border-0 dark:bg-gray-800 focus:ring-0 dark:text-white dark:placeholder-gray-400"
              placeholder="Вставьте текст новости"
              required=""
            ></textarea>
          </div>
          <div className="flex justify-between items-center py-2 px-3 border-t dark:border-gray-600">
            <button
              disabled={isLoading}
              onClick={handleCheck}
              className="inline-flex items-center py-2.5 px-4 text-xs font-medium text-center text-white bg-blue-700 rounded-lg focus:ring-4 focus:ring-blue-200 dark:focus:ring-blue-900 hover:bg-blue-800"
            >
              {isLoading ? (
                <>
                  <svg
                    role="status"
                    className="w-4 h-4 mr-2 text-gray-200 animate-spin dark:text-gray-600 fill-blue-600"
                    viewBox="0 0 100 101"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <path
                      d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z"
                      fill="currentColor"
                    />
                    <path
                      d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z"
                      fill="currentFill"
                    />
                  </svg>{' '}
                  Оценка...
                </>
              ) : (
                'Оценить'
              )}
            </button>
          </div>
        </div>
        <p className="ml-auto text-xs text-gray-500 dark:text-gray-400">
          Оценка производится на базе данных с{' '}
          <a href="https://mos.ru" rel="noreferrer" target="_blank">
            mos.ru
          </a>
        </p>

        {checkResult.length ? (
          <div className="mt-6">
            <h2 className="pt-2 pb-6 sm:pr-16 text-xl font-medium title-font text-gray-900">
              Ваша оценка
            </h2>
            <div className="flex items-center mb-5">
              <Mark distance={checkResult[0].distance} />
              <p className="ml-4 font-medium text-gray-900 dark:text-white">
                <a
                  className="underline"
                  rel="noreferrer"
                  target="_blank"
                  href={checkResult[0].link}
                >
                  Ссылка на наиболее похожий источник
                </a>
              </p>
            </div>
            <div>
              <h3 className="pt-4 pb-4 sm:pr-16 text-lg font-medium title-font text-gray-900">
                Похожие новости
              </h3>
              <ul className="pl-5 list-disc">
                {checkResult.map((item, index) => (
                  <li key={index}>
                    <a className="underline" rel="noreferrer" target="_blank" href={item?.link}>
                      Новость {index + 1}
                    </a>
                  </li>
                ))}
              </ul>
            </div>
          </div>
        ) : (
          ''
        )}
      </div>
    </div>
  )
}

export default App
