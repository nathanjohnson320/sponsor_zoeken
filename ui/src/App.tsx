import { api } from "./app/store/api"

const App = () => {
  const { isLoading, isError, data } = api.useGetApiV1CompaniesQuery({
    page: 1,
    size: 10,
    search: "",
  })

  return (
    <>
      <header>
        <div className="h-20 flex-col">
          <div
            className="w-full h-1/3"
            style={{ backgroundColor: "#0072CE" }}
          ></div>
          <div className="w-full h-1/3 bg-black"></div>
          <div className="w-full h-1/3 bg-white"></div>
        </div>
      </header>
      <main>
        <div className="w-screen flex justify-cente py-4 border-t-2 border-slate-700">
          <h1 className="text-3xl font-bold">Search</h1>
        </div>

        <div className="pb-8 border-b-2 border-slate-700">
          <div className="rounded-md px-3 pb-1.5 pt-2.5 shadow-sm ring-1 ring-inset ring-gray-300 focus-within:ring-2 focus-within:ring-indigo-600">
            <label
              htmlFor="search"
              className="block text-xs font-medium text-gray-900"
            >
              Company Name
            </label>
            <input
              id="search"
              name="search"
              type="text"
              placeholder="Company name"
              className="block w-full border-0 p-0 text-gray-900 placeholder:text-gray-400 focus:ring-0 sm:text-sm sm:leading-6"
            />
          </div>
        </div>
      </main>
    </>
  )
}

export default App
