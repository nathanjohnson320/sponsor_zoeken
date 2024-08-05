import { useState } from "react"
import { api } from "./app/store/api"
import { useDebounce } from "@uidotdev/usehooks"

const App = () => {
  const [searchTerm, setSearchTerm] = useState("")
  const debouncedSearchTerm = useDebounce(searchTerm, 500)

  const { isLoading, isError, data } = api.useGetApiV1CompaniesQuery({
    page: 1,
    size: 10,
    search: debouncedSearchTerm,
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
          <h1 className="text-3xl font-bold px-2">Search</h1>
        </div>

        <div className="pb-8 px-2 border-b-2 border-slate-700">
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
              onChange={e => setSearchTerm(e.target.value)}
            />
          </div>
        </div>

        <div className="mt-4">
          <div className="sm:flex sm:items-center">
            <div className="px-2 sm:flex-auto">
              <h1 className="text-base font-semibold leading-6 text-gray-900">
                Results
              </h1>
              <p className="mt-2 text-sm text-gray-700">
                Companies that are in government lists that are able to provide
                sponsorship for visas.
              </p>
            </div>
          </div>
          <div className="px-2 flow-root">
            <div className="-mx-4 -my-2 overflow-x-auto sm:-mx-6 lg:-mx-8">
              <div className="inline-block min-w-full py-2 align-middle sm:px-6 lg:px-8">
                <table className="min-w-full divide-y divide-gray-300">
                  <thead>
                    <tr>
                      <th
                        scope="col"
                        className="py-3.5 pl-4 pr-3 text-left text-sm font-semibold text-gray-900 sm:pl-0"
                      >
                        Name
                      </th>

                      <th
                        scope="col"
                        className="py-3.5 pl-4 pr-3 text-left text-sm font-semibold text-gray-900 sm:pl-0"
                      >
                        Country
                      </th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-gray-200">
                    {data?.items?.map(company => (
                      <tr key={company.id}>
                        <td className="whitespace-nowrap py-4 pl-4 pr-3 text-sm  text-gray-900 sm:pl-0">
                          {company.name}
                        </td>

                        <td className="uppercase whitespace-nowrap py-4 pl-4 pr-3 text-sm text-gray-900 sm:pl-0">
                          {company.country}
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </div>
      </main>
    </>
  )
}

export default App
