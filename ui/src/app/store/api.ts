import { urlApi as generatedUrlApi } from "./generatedUrlApi"

export const TAG_TYPES = ["Companies"]

export const api = generatedUrlApi.enhanceEndpoints({
  addTagTypes: TAG_TYPES,
  endpoints: {
    getApiV1Companies: {
      providesTags: ["Companies"],
    },
  },
})
