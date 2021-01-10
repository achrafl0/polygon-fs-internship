export interface PerformanceData {
  min_resp: number;
  max_resp: number;
  avg_resp: number;
}

export interface ServerPerformanceData {
  [key: string]: PerformanceData;
}
