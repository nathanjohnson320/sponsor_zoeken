import "./App.css"
import { api } from "./app/store/api"

const App = () => {
  const { isLoading, isError, data } = api.useGetApiV1CompaniesQuery({
    page: 1,
    size: 10,
    search: "",
  })

  return (
    <div className="App">
      <header className="App-header"></header>
    </div>
  )
}

export default App
