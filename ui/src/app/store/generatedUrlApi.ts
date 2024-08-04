import { emptySplitApi as api } from "./emptyApi"
const injectedRtkApi = api.injectEndpoints({
  endpoints: build => ({
    getApiV1Companies: build.query<
      GetApiV1CompaniesApiResponse,
      GetApiV1CompaniesApiArg
    >({
      query: queryArg => ({
        url: `/api/v1/companies/`,
        params: {
          search: queryArg.search,
          country: queryArg.country,
          page: queryArg.page,
          size: queryArg.size,
        },
      }),
    }),
  }),
  overrideExisting: false,
})
export { injectedRtkApi as urlApi }
export type GetApiV1CompaniesApiResponse =
  /** status 200 Successful Response */ PageCompanyBase
export type GetApiV1CompaniesApiArg = {
  search?: string | null
  country?: string | null
  /** Page number */
  page?: number
  /** Page size */
  size?: number
}
export type CompanyBase = {
  name: string
  country: string
  meta: object
}
export type PageCompanyBase = {
  items: CompanyBase[]
  total: number | null
  page: number | null
  size: number | null
  pages?: number | null
}
export type ValidationError = {
  loc: (string | number)[]
  msg: string
  type: string
}
export type HttpValidationError = {
  detail?: ValidationError[]
}
export const { useGetApiV1CompaniesQuery } = injectedRtkApi
