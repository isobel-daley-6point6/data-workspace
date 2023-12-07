const dataServicesHelp = 'https://data-services-help.trade.gov.uk';

const URLS = {
  external: {
    dataServices: {
      dataWorkspace: {
        collections: `${dataServicesHelp}/data-workspace/how-to/start-using-data-workspace/collections/`,
        policiesAndStandardsDataTypes: `${dataServicesHelp}/data-workspace/policies-and-standards/standards/data-types/`
      }
    }
  },
  collections: {
    base: '/collections',
    create: '/collections/create',
    filtered: {
      bookmarked: '/datasets/?q=&sort=relevance&my_datasets=bookmarked'
    }
  }
} as const;

export default URLS;
