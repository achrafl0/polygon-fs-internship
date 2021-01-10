/* eslint-disable import/prefer-default-export */
import ApiClient from './client';
import { ServerPerformanceData } from '../types';

export async function getPerformances(): Promise<ServerPerformanceData | void> {
  return ApiClient()
    .get<ServerPerformanceData>('/performances')
    .then((data) => data.data)
    .catch((err) => console.log(`Shit happened ${err}`));
}
