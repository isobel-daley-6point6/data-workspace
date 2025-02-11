import { DATA_USAGE_KEYS } from './constants';
import type {
  DataUsageKeys,
  DataUsageResponse,
  TransformedDataUsageResponse,
  TransformedYourBookmarksResponse,
  TransformedYourRecentCollectionResponse,
  TransformedYourRecentItemsResponse,
  TransformedYourRecentToolsResponse,
  YourBookmarksResponse,
  YourRecentCollectionResponse,
  YourRecentIemsResponse,
  YourRecentToolsResponse
} from './types/';

export const transformDataUsageResponse = (
  response: DataUsageResponse
): TransformedDataUsageResponse =>
  Object.keys(response).map((key) => ({
    label: DATA_USAGE_KEYS[key as DataUsageKeys],
    value: Math.round(response[key as keyof unknown] * 1000) / 1000
  }));

export const transformRecentCollectionsResponse = (
  response: YourRecentCollectionResponse
): TransformedYourRecentCollectionResponse =>
  response.results.map(({ name, collection_url }) => ({
    name: name,
    url: collection_url
  }));

export const transformRecentItemsResponse = (
  response: YourRecentIemsResponse
): TransformedYourRecentItemsResponse =>
  response.results.map(({ related_object, extra }) => ({
    name: related_object.name,
    url: extra.path
  }));

export const transformYourBookmarksResponse = (
  response: YourBookmarksResponse
): TransformedYourBookmarksResponse =>
  response.results.map(({ name, url }) => ({
    name: name,
    url: url
  }));

export const transformRecentToolsResponse = (
  response: YourRecentToolsResponse
): TransformedYourRecentToolsResponse =>
  response.results.map(({ extra, tool_url }) => ({
    name: extra.tool,
    url: tool_url
  }));
